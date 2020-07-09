#!/usr/bin/env python3

import logging
import os
import sys

from nitro import Nitro, DomainNotFound

# config
import nsconfig


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit('Usage: ' + sys.argv[0] + ' <domain> [<domain> ...]')

    log_level = os.environ.get('LOGLEVEL', 'INFO').upper()
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=log_level, format=log_format)

    nitro = Nitro(config=nsconfig.nitro_config)

    # create certs directory if it does not exist
    if not os.path.exists('certs'):
        os.mkdir('certs')

    # fetch domain certs
    for domain in sys.argv[1:]:
        try:
            cert = nitro.get_certificate(domain)

            cert_path = 'certs/%s' % domain
            if not os.path.exists(cert_path):
                os.mkdir(cert_path)

            with open(cert_path + '/cert.pem', 'w') as file:
                file.write(cert.cert)
            with open(cert_path + '/chain.pem', 'w') as file:
                file.write(cert.chain)
            with open(cert_path + '/fullchain.pem', 'w') as file:
                file.write(cert.fullchain)
            with open(cert_path + '/privkey.pem', 'w') as file:
                file.write(cert.key)

            logging.info('Certificate for %s fetched' % domain)
        except DomainNotFound as e:
            logging.error('Domain not found %s' % e.domain)
