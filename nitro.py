import logging
import re
import socket
import urllib3

from base64 import b64decode
from dataclasses import dataclass
from typing import List, Union

from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csvserver import csvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csvserver_responderpolicy_binding import csvserver_responderpolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver import lbvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver_responderpolicy_binding import lbvserver_responderpolicy_binding
from nssrc.com.citrix.netscaler.nitro.resource.config.responder.responderaction import responderaction
from nssrc.com.citrix.netscaler.nitro.resource.config.responder.responderpolicy  import responderpolicy
from nssrc.com.citrix.netscaler.nitro.resource.config.ssl.sslcertkey import sslcertkey
from nssrc.com.citrix.netscaler.nitro.resource.config.system.systemfile import systemfile
from nssrc.com.citrix.netscaler.nitro.resource.config.system.systemfile_args import systemfile_args
from nssrc.com.citrix.netscaler.nitro.service.nitro_service import nitro_service

# disable invalid cert warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class DomainNotFound(Exception):
    """Exception raised if the domain could not be found"""
    domain: str

    def __init__(self, domain: str):
        self.domain = domain


class NitroError(Exception):
    """General exception raised when there is an error with the Nitro API"""
    inner_exception: nitro_exception

    def __init__(self, inner_exception: nitro_exception):
        self.inner_exception = inner_exception


@dataclass(frozen=True)
class NitroConfig:
    """NS Nitro Configuration"""
    host: str
    protocol: str
    username: str
    password: str
    cert_validation: bool = True


@dataclass(frozen=True)
class NitroLB:
    """CS/LB and Client response"""
    client: nitro_service
    lb: Union[csvserver, lbvserver]


@dataclass(frozen=True)
class NitroCert:
    """Certificate information"""
    name: str
    cert: str
    key: str
    chain: str = ''

    @property
    def fullchain(self):
        return self.cert + self.chain


class Nitro:
    """Nitro"""

    clients: List[nitro_service]

    def __init__(self, config: List[NitroConfig]):
        self.__connect(config)

    def __del__(self):
        self.__disconnect()

    def __connect(self, config: List[NitroConfig]):
        """Connect to all the clients"""
        clients = []
        for c in config:
            try:
                logging.info('Connecting to nitro client %s://%s' % (c.protocol, c.host))
                client = nitro_service(c.host, c.protocol)
                client.certvalidation = c.cert_validation
                client.login(c.username, c.password)
                clients.append(client)
            except nitro_exception as e:
                logging.warning('Could not connect to nitro client: %s (%s)' % (e.message, e.errorcode))
        self.clients = clients

    def __disconnect(self):
        """Disconnect from all clients"""
        try:
            for client in self.clients:
                try:
                    client.logout()
                except nitro_exception:
                    pass
        except AttributeError:
            pass

    def save(self):
        """Save the config of all configured clients"""
        for client in self.clients:
            logging.info('Saving nsconfig for %s' % client.ipaddress)
            client.save_config()

    def get_lb(self, domain: str):
        """Get an CS/LB based on a domain"""
        try:
            # lookup ip of domain
            ip = socket.gethostbyname(domain)

            for client in self.clients:
                # lookup lb
                for lb in lbvserver.get(client):
                    if lb.ipv46 == ip:
                        # lb found
                        return NitroLB(client, lb)
                for lb in csvserver.get(client):
                    if lb.ipv46 == ip:
                        # lb found
                        return NitroLB(client, lb)
        except socket.gaierror as e:
            raise DomainNotFound(domain)
        raise DomainNotFound(domain)

    def get_client(self, domain: str):
        """Get a nitro client based on a domain"""
        return self.get_lb(domain).client

    def get_certificate(self, domain: str):
        """Get a certifivate incl private key and chain"""
        client = self.get_client(domain)
        try:
            for cert in sslcertkey.get(client):
                if 'CN=' + domain in cert.subject:
                    # found matching cert
                    args = systemfile_args()
                    args.filelocation = '/nsconfig/ssl/'

                    # get cert file
                    args.filename = cert.cert
                    certfile = systemfile.get_args(client, args)[0]

                    # get key file
                    args.filename = cert.key
                    keyfile = systemfile.get_args(client, args)[0]

                    # get ca file
                    if cert.linkcertkeyname:
                        cacert = sslcertkey.get(client, cert.linkcertkeyname)
                        args.filename = cert.cert
                        cafile = systemfile.get_args(client, args)[0]

                    return NitroCert(
                        name=domain,
                        cert=b64decode(certfile.filecontent).decode(encoding="utf-8"),
                        key=b64decode(keyfile.filecontent).decode(encoding="utf-8"),
                        chain=b64decode(cafile.filecontent).decode(encoding="utf-8") if cafile else '',
                    )
        except nitro_exception as e:
            raise NitroError(e)
        return None

    def deploy_challenge(self, domain: str, challenge_filename: str, challenge_value: str):
        """Deploy and ACME challenge"""
        logging.info('Deploying challenge for %s: %s' % (domain, challenge_filename))

        lb = self.get_lb(domain)
        client = lb.client
        lb = lb.lb

        action_name = 'ns-letencrypt-responder-action-' + domain
        policy_name = 'ns-letencrypt-responder-policy-' + domain

        # create responder action
        action = responderaction()
        action.name = action_name
        action.type = 'respondwith'
        action.target = "\"HTTP/1.0 200 OK\" +\"\\r\\n\\r\\n\" + \"%s\"" % challenge_value
        logging.info('Creating responder action %s' % action.name)
        responderaction.add(client, action)
        # create responder policy
        policy = responderpolicy()
        policy.name = policy_name
        policy.rule = 'HTTP.REQ.URL.CONTAINS(\"well-known/acme-challenge/%s\")' % challenge_filename
        policy.action = action.name
        logging.info('Creating responder policy %s' % policy.name)
        responderpolicy.add(client, policy)
        # get priorities of existing bindings
        bindings = csvserver_responderpolicy_binding.get(client, lb.name) if lb is csvserver else lbvserver_responderpolicy_binding.get(client, lb.name)
        priorities = list(map(lambda b: int(b.priority), bindings))
        priorities.sort()
        # get next priority
        priority = 10  # TODO: make this configurable?
        for p in priorities:
            if priority == p:
                priority += 1
        # bind responder policy to lb/cs
        if lb is csvserver:
            binding = csvserver_responderpolicy_binding()
            binding.name = lb.name
            binding.policyname = policy.name
            binding.priority = priority
            logging.info('Binding responder policy %s to csvserver %s' % (policy.name, lb.name))
            csvserver_responderpolicy_binding.add(client, binding)
        else:
            binding = lbvserver_responderpolicy_binding()
            binding.name = lb.name
            binding.policyname = policy.name
            binding.priority = priority
            logging.info('Binding responder policy %s to lbvserver %s' % (policy.name, lb.name))
            lbvserver_responderpolicy_binding.add(client, binding)

    def clean_challenge(self, domain: str, challenge_filename: str):
        """Cleanup ACME challenge"""
        logging.info('Cleaning up challenge for %s: %s' % (domain, challenge_filename))

        lb = self.get_lb(domain)
        client = lb.client
        lb = lb.lb

        action_name = 'ns-letencrypt-responder-action-' + domain
        policy_name = 'ns-letencrypt-responder-policy-' + domain

        # unbind responder policy from lb/cs
        if lb is csvserver:
            binding = csvserver_responderpolicy_binding()
            binding.name = lb.name
            binding.policyname = policy_name
            logging.info('Unbinding responder policy %s to csvserver %s' % (policy_name, lb.name))
            csvserver_responderpolicy_binding.delete(client, binding)
        else:
            binding = lbvserver_responderpolicy_binding()
            binding.name = lb.name
            binding.policyname = policy_name
            logging.info('Unbinding responder policy %s to lbvserver %s' % (policy_name, lb.name))
            lbvserver_responderpolicy_binding.delete(client, binding)
        # remove responder policy
        policy = responderpolicy()
        policy.name = policy_name
        logging.info('Removing responder policy %s' % policy.name)
        responderpolicy.delete(client, policy)
        # remove responder action
        action = responderaction()
        action.name = action_name
        logging.info('Removing responder action %s' % action.name)
        responderaction.delete(client, action)

    def deploy_cert(self, domain: str, key_file: str, cert_file: str, full_chain_file: str, chain_file: str, timestamp: str):
        """Deploy a certificate"""
        logging.info('Deploying cert for %s' % domain)
        pass
