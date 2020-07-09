#
# Copyright (c) 2008-2019 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License")
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_resource
from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_response
from nssrc.com.citrix.netscaler.nitro.service.options import options
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception

from nssrc.com.citrix.netscaler.nitro.util.nitro_util import nitro_util

class sslcertkey(base_resource) :
	""" Configuration for certificate key resource. """
	def __init__(self) :
		self._certkey = None
		self._cert = None
		self._key = None
		self._password = None
		self._fipskey = None
		self._hsmkey = None
		self._inform = None
		self._passplain = None
		self._expirymonitor = None
		self._notificationperiod = None
		self._bundle = None
		self._deletefromdevice = None
		self._linkcertkeyname = None
		self._nodomaincheck = None
		self._ocspstaplingcache = None
		self._signaturealg = None
		self._certificatetype = None
		self._serial = None
		self._issuer = None
		self._clientcertnotbefore = None
		self._clientcertnotafter = None
		self._daystoexpiration = None
		self._subject = None
		self._publickey = None
		self._publickeysize = None
		self._version = None
		self._priority = None
		self._status = None
		self._passcrypt = None
		self._data = None
		self._servicename = None
		self._ocspresponsestatus = None
		self._builtin = None
		self._feature = None
		self.___count = None

	@property
	def certkey(self) :
		r"""Name for the certificate and private-key pair. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the certificate-key pair is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cert" or 'my cert').<br/>Minimum length =  1.
		"""
		try :
			return self._certkey
		except Exception as e:
			raise e

	@certkey.setter
	def certkey(self, certkey) :
		r"""Name for the certificate and private-key pair. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the certificate-key pair is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cert" or 'my cert').<br/>Minimum length =  1
		"""
		try :
			self._certkey = certkey
		except Exception as e:
			raise e

	@property
	def cert(self) :
		r"""Name of and, optionally, path to the X509 certificate file that is used to form the certificate-key pair. The certificate file should be present on the appliance's hard-disk drive or solid-state drive. Storing a certificate in any location other than the default might cause inconsistency in a high availability setup. /nsconfig/ssl/ is the default path.<br/>Minimum length =  1.
		"""
		try :
			return self._cert
		except Exception as e:
			raise e

	@cert.setter
	def cert(self, cert) :
		r"""Name of and, optionally, path to the X509 certificate file that is used to form the certificate-key pair. The certificate file should be present on the appliance's hard-disk drive or solid-state drive. Storing a certificate in any location other than the default might cause inconsistency in a high availability setup. /nsconfig/ssl/ is the default path.<br/>Minimum length =  1
		"""
		try :
			self._cert = cert
		except Exception as e:
			raise e

	@property
	def key(self) :
		r"""Name of and, optionally, path to the private-key file that is used to form the certificate-key pair. The certificate file should be present on the appliance's hard-disk drive or solid-state drive. Storing a certificate in any location other than the default might cause inconsistency in a high availability setup. /nsconfig/ssl/ is the default path.<br/>Minimum length =  1.
		"""
		try :
			return self._key
		except Exception as e:
			raise e

	@key.setter
	def key(self, key) :
		r"""Name of and, optionally, path to the private-key file that is used to form the certificate-key pair. The certificate file should be present on the appliance's hard-disk drive or solid-state drive. Storing a certificate in any location other than the default might cause inconsistency in a high availability setup. /nsconfig/ssl/ is the default path.<br/>Minimum length =  1
		"""
		try :
			self._key = key
		except Exception as e:
			raise e

	@property
	def password(self) :
		r"""Passphrase that was used to encrypt the private-key. Use this option to load encrypted private-keys in PEM format.
		"""
		try :
			return self._password
		except Exception as e:
			raise e

	@password.setter
	def password(self, password) :
		r"""Passphrase that was used to encrypt the private-key. Use this option to load encrypted private-keys in PEM format.
		"""
		try :
			self._password = password
		except Exception as e:
			raise e

	@property
	def fipskey(self) :
		r"""Name of the FIPS key that was created inside the Hardware Security Module (HSM) of a FIPS appliance, or a key that was imported into the HSM.<br/>Minimum length =  1.
		"""
		try :
			return self._fipskey
		except Exception as e:
			raise e

	@fipskey.setter
	def fipskey(self, fipskey) :
		r"""Name of the FIPS key that was created inside the Hardware Security Module (HSM) of a FIPS appliance, or a key that was imported into the HSM.<br/>Minimum length =  1
		"""
		try :
			self._fipskey = fipskey
		except Exception as e:
			raise e

	@property
	def hsmkey(self) :
		r"""Name of the HSM key that was created in the External Hardware Security Module (HSM) of a FIPS appliance.<br/>Minimum length =  1.
		"""
		try :
			return self._hsmkey
		except Exception as e:
			raise e

	@hsmkey.setter
	def hsmkey(self, hsmkey) :
		r"""Name of the HSM key that was created in the External Hardware Security Module (HSM) of a FIPS appliance.<br/>Minimum length =  1
		"""
		try :
			self._hsmkey = hsmkey
		except Exception as e:
			raise e

	@property
	def inform(self) :
		r"""Input format of the certificate and the private-key files. The three formats supported by the appliance are:
		PEM - Privacy Enhanced Mail
		DER - Distinguished Encoding Rule
		PFX - Personal Information Exchange.<br/>Default value: PEM<br/>Possible values = DER, PEM, PFX.
		"""
		try :
			return self._inform
		except Exception as e:
			raise e

	@inform.setter
	def inform(self, inform) :
		r"""Input format of the certificate and the private-key files. The three formats supported by the appliance are:
		PEM - Privacy Enhanced Mail
		DER - Distinguished Encoding Rule
		PFX - Personal Information Exchange.<br/>Default value: PEM<br/>Possible values = DER, PEM, PFX
		"""
		try :
			self._inform = inform
		except Exception as e:
			raise e

	@property
	def passplain(self) :
		r"""Pass phrase used to encrypt the private-key. Required when adding an encrypted private-key in PEM format.<br/>Minimum length =  1.
		"""
		try :
			return self._passplain
		except Exception as e:
			raise e

	@passplain.setter
	def passplain(self, passplain) :
		r"""Pass phrase used to encrypt the private-key. Required when adding an encrypted private-key in PEM format.<br/>Minimum length =  1
		"""
		try :
			self._passplain = passplain
		except Exception as e:
			raise e

	@property
	def expirymonitor(self) :
		r"""Issue an alert when the certificate is about to expire.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._expirymonitor
		except Exception as e:
			raise e

	@expirymonitor.setter
	def expirymonitor(self, expirymonitor) :
		r"""Issue an alert when the certificate is about to expire.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._expirymonitor = expirymonitor
		except Exception as e:
			raise e

	@property
	def notificationperiod(self) :
		r"""Time, in number of days, before certificate expiration, at which to generate an alert that the certificate is about to expire.<br/>Minimum length =  10<br/>Maximum length =  100.
		"""
		try :
			return self._notificationperiod
		except Exception as e:
			raise e

	@notificationperiod.setter
	def notificationperiod(self, notificationperiod) :
		r"""Time, in number of days, before certificate expiration, at which to generate an alert that the certificate is about to expire.<br/>Minimum length =  10<br/>Maximum length =  100
		"""
		try :
			self._notificationperiod = notificationperiod
		except Exception as e:
			raise e

	@property
	def bundle(self) :
		r"""Parse the certificate chain as a single file after linking the server certificate to its issuer's certificate within the file.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._bundle
		except Exception as e:
			raise e

	@bundle.setter
	def bundle(self, bundle) :
		r"""Parse the certificate chain as a single file after linking the server certificate to its issuer's certificate within the file.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._bundle = bundle
		except Exception as e:
			raise e

	@property
	def deletefromdevice(self) :
		r"""Delete cert/key file from file system.
		"""
		try :
			return self._deletefromdevice
		except Exception as e:
			raise e

	@deletefromdevice.setter
	def deletefromdevice(self, deletefromdevice) :
		r"""Delete cert/key file from file system.
		"""
		try :
			self._deletefromdevice = deletefromdevice
		except Exception as e:
			raise e

	@property
	def linkcertkeyname(self) :
		r"""Name of the Certificate Authority certificate-key pair to which to link a certificate-key pair.<br/>Minimum length =  1.
		"""
		try :
			return self._linkcertkeyname
		except Exception as e:
			raise e

	@linkcertkeyname.setter
	def linkcertkeyname(self, linkcertkeyname) :
		r"""Name of the Certificate Authority certificate-key pair to which to link a certificate-key pair.<br/>Minimum length =  1
		"""
		try :
			self._linkcertkeyname = linkcertkeyname
		except Exception as e:
			raise e

	@property
	def nodomaincheck(self) :
		r"""Override the check for matching domain names during a certificate update operation.
		"""
		try :
			return self._nodomaincheck
		except Exception as e:
			raise e

	@nodomaincheck.setter
	def nodomaincheck(self, nodomaincheck) :
		r"""Override the check for matching domain names during a certificate update operation.
		"""
		try :
			self._nodomaincheck = nodomaincheck
		except Exception as e:
			raise e

	@property
	def ocspstaplingcache(self) :
		r"""Clear cached ocspStapling response in certkey.
		"""
		try :
			return self._ocspstaplingcache
		except Exception as e:
			raise e

	@ocspstaplingcache.setter
	def ocspstaplingcache(self, ocspstaplingcache) :
		r"""Clear cached ocspStapling response in certkey.
		"""
		try :
			self._ocspstaplingcache = ocspstaplingcache
		except Exception as e:
			raise e

	@property
	def signaturealg(self) :
		r"""Signature algorithm.
		"""
		try :
			return self._signaturealg
		except Exception as e:
			raise e

	@property
	def certificatetype(self) :
		r"""Specifies whether the certificate is of type root-CA, intermediate-CA, server, client, or client and server.<br/>Possible values = ROOT_CERT, INTM_CERT, CLNT_CERT, SRVR_CERT, UNKNOWN_CERT.
		"""
		try :
			return self._certificatetype
		except Exception as e:
			raise e

	@property
	def serial(self) :
		r"""Serial number.
		"""
		try :
			return self._serial
		except Exception as e:
			raise e

	@property
	def issuer(self) :
		r"""Issuer name.
		"""
		try :
			return self._issuer
		except Exception as e:
			raise e

	@property
	def clientcertnotbefore(self) :
		r"""Not-Before date.
		"""
		try :
			return self._clientcertnotbefore
		except Exception as e:
			raise e

	@property
	def clientcertnotafter(self) :
		r"""Not-After date.
		"""
		try :
			return self._clientcertnotafter
		except Exception as e:
			raise e

	@property
	def daystoexpiration(self) :
		r"""Days remaining for the certificate to expire.
		"""
		try :
			return self._daystoexpiration
		except Exception as e:
			raise e

	@property
	def subject(self) :
		r"""Subject name.
		"""
		try :
			return self._subject
		except Exception as e:
			raise e

	@property
	def publickey(self) :
		r"""Public key algorithm.
		"""
		try :
			return self._publickey
		except Exception as e:
			raise e

	@property
	def publickeysize(self) :
		r"""Size of the public key.
		"""
		try :
			return self._publickeysize
		except Exception as e:
			raise e

	@property
	def version(self) :
		r"""Version.
		"""
		try :
			return self._version
		except Exception as e:
			raise e

	@property
	def priority(self) :
		r"""ocsp priority.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@property
	def status(self) :
		r"""Status of the certificate.<br/>Possible values = Valid, Not yet valid, Expired.
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	@property
	def passcrypt(self) :
		r"""Passcrypt.<br/>Minimum length =  1.
		"""
		try :
			return self._passcrypt
		except Exception as e:
			raise e

	@property
	def data(self) :
		r"""Vserver Id.
		"""
		try :
			return self._data
		except Exception as e:
			raise e

	@property
	def servicename(self) :
		r"""Service name to which the certificate key pair is bound.
		"""
		try :
			return self._servicename
		except Exception as e:
			raise e

	@property
	def ocspresponsestatus(self) :
		r"""Ocsp response status of the certificate.<br/>Possible values = NONE, EXPIRED, VALID.
		"""
		try :
			return self._ocspresponsestatus
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r"""Flag to determine if Cert key is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	@property
	def feature(self) :
		r"""The feature to be checked while applying this config.
		"""
		try :
			return self._feature
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslcertkey_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslcertkey
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.certkey is not None :
				return str(self.certkey)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = sslcertkey()
		addresource.certkey = resource.certkey
		addresource.cert = resource.cert
		addresource.key = resource.key
		addresource.password = resource.password
		addresource.fipskey = resource.fipskey
		addresource.hsmkey = resource.hsmkey
		addresource.inform = resource.inform
		addresource.passplain = resource.passplain
		addresource.expirymonitor = resource.expirymonitor
		addresource.notificationperiod = resource.notificationperiod
		addresource.bundle = resource.bundle
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add sslcertkey.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ sslcertkey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i] = cls.filter_add_parameters(resource[i])
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = sslcertkey()
		deleteresource.certkey = resource.certkey
		deleteresource.deletefromdevice = resource.deletefromdevice
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete sslcertkey.
		"""
		try :
			if type(resource) is not list :
				deleteresource = sslcertkey()
				if type(resource) !=  type(deleteresource):
					deleteresource.certkey = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ sslcertkey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].certkey = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ sslcertkey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i] = cls.filter_delete_parameters(resource)
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = sslcertkey()
		updateresource.certkey = resource.certkey
		updateresource.expirymonitor = resource.expirymonitor
		updateresource.notificationperiod = resource.notificationperiod
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update sslcertkey.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ sslcertkey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of sslcertkey resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = sslcertkey()
				if type(resource) !=  type(unsetresource):
					unsetresource.certkey = resource
				else :
					unsetresource.certkey = resource.certkey
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ sslcertkey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].certkey = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ sslcertkey() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].certkey = resource[i].certkey
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def link(cls, client, resource) :
		r""" Use this API to link sslcertkey.
		"""
		try :
			if type(resource) is not list :
				linkresource = sslcertkey()
				linkresource.certkey = resource.certkey
				linkresource.linkcertkeyname = resource.linkcertkeyname
				return linkresource.perform_operation(client,"link")
			else :
				if (resource and len(resource) > 0) :
					linkresources = [ sslcertkey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						linkresources[i].certkey = resource[i].certkey
						linkresources[i].linkcertkeyname = resource[i].linkcertkeyname
				result = cls.perform_operation_bulk_request(client, linkresources,"link")
			return result
		except Exception as e :
			raise e

	@classmethod
	def unlink(cls, client, resource) :
		r""" Use this API to unlink sslcertkey.
		"""
		try :
			if type(resource) is not list :
				unlinkresource = sslcertkey()
				unlinkresource.certkey = resource.certkey
				return unlinkresource.perform_operation(client,"unlink")
			else :
				if (resource and len(resource) > 0) :
					unlinkresources = [ sslcertkey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						unlinkresources[i].certkey = resource[i].certkey
				result = cls.perform_operation_bulk_request(client, unlinkresources,"unlink")
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		changeresource = sslcertkey()
		changeresource.certkey = resource.certkey
		changeresource.cert = resource.cert
		changeresource.key = resource.key
		changeresource.password = resource.password
		changeresource.fipskey = resource.fipskey
		changeresource.inform = resource.inform
		changeresource.passplain = resource.passplain
		changeresource.nodomaincheck = resource.nodomaincheck
		return changeresource

	@classmethod
	def change(cls, client, resource) :
		r""" Use this API to change sslcertkey.
		"""
		try :
			if type(resource) is not list :
				changeresource = cls.filter_update_parameters(resource)
				return changeresource.perform_operation(client,"update")
			else :
				if (resource and len(resource) > 0) :
					changeresources = [ sslcertkey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						changeresources[i] = cls.filter_change_parameters(resource[i])
				result = cls.perform_operation_bulk_request(client, changeresources,"update")
			return result
		except Exception as e :
			raise e

	@classmethod
	def clear(cls, client, resource) :
		r""" Use this API to clear sslcertkey.
		"""
		try :
			if type(resource) is not list :
				clearresource = sslcertkey()
				clearresource.certkey = resource.certkey
				clearresource.ocspstaplingcache = resource.ocspstaplingcache
				return clearresource.perform_operation(client,"clear")
			else :
				if (resource and len(resource) > 0) :
					clearresources = [ sslcertkey() for _ in range(len(resource))]
					for i in range(len(resource)) :
						clearresources[i].certkey = resource[i].certkey
						clearresources[i].ocspstaplingcache = resource[i].ocspstaplingcache
				result = cls.perform_operation_bulk_request(client, clearresources,"clear")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the sslcertkey resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = sslcertkey()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = sslcertkey()
					obj.certkey = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [sslcertkey() for _ in range(len(name))]
						obj = [sslcertkey() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = sslcertkey()
							obj[i].certkey = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of sslcertkey resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslcertkey()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the sslcertkey resources configured on NetScaler.
		"""
		try :
			obj = sslcertkey()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		r""" Use this API to count filtered the set of sslcertkey resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslcertkey()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Bundle:
		YES = "YES"
		NO = "NO"

	class Status:
		Valid = "Valid"
		Not_yet_valid = "Not yet valid"
		Expired = "Expired"

	class Ocspresponsestatus:
		NONE = "NONE"
		EXPIRED = "EXPIRED"
		VALID = "VALID"

	class Feature:
		WL = "WL"
		WebLogging = "WebLogging"
		SP = "SP"
		SurgeProtection = "SurgeProtection"
		LB = "LB"
		LoadBalancing = "LoadBalancing"
		CS = "CS"
		ContentSwitching = "ContentSwitching"
		CR = "CR"
		CacheRedirection = "CacheRedirection"
		SC = "SC"
		SureConnect = "SureConnect"
		CMP = "CMP"
		CMPcntl = "CMPcntl"
		CompressionControl = "CompressionControl"
		PQ = "PQ"
		PriorityQueuing = "PriorityQueuing"
		HDOSP = "HDOSP"
		HttpDoSProtection = "HttpDoSProtection"
		SSLVPN = "SSLVPN"
		AAA = "AAA"
		GSLB = "GSLB"
		GlobalServerLoadBalancing = "GlobalServerLoadBalancing"
		SSL = "SSL"
		SSLOffload = "SSLOffload"
		SSLOffloading = "SSLOffloading"
		CF = "CF"
		ContentFiltering = "ContentFiltering"
		IC = "IC"
		IntegratedCaching = "IntegratedCaching"
		OSPF = "OSPF"
		OSPFRouting = "OSPFRouting"
		RIP = "RIP"
		RIPRouting = "RIPRouting"
		BGP = "BGP"
		BGPRouting = "BGPRouting"
		REWRITE = "REWRITE"
		IPv6PT = "IPv6PT"
		IPv6protocoltranslation = "IPv6protocoltranslation"
		AppFw = "AppFw"
		ApplicationFirewall = "ApplicationFirewall"
		RESPONDER = "RESPONDER"
		HTMLInjection = "HTMLInjection"
		push = "push"
		NSPush = "NSPush"
		NetScalerPush = "NetScalerPush"
		AppFlow = "AppFlow"
		CloudBridge = "CloudBridge"
		ISIS = "ISIS"
		ISISRouting = "ISISRouting"
		CH = "CH"
		CallHome = "CallHome"
		AppQoE = "AppQoE"
		ContentAccelerator = "ContentAccelerator"
		SYSTEM = "SYSTEM"
		RISE = "RISE"
		FEO = "FEO"
		LSN = "LSN"
		LargeScaleNAT = "LargeScaleNAT"
		RDPProxy = "RDPProxy"
		Rep = "Rep"
		Reputation = "Reputation"
		URLFiltering = "URLFiltering"
		VideoOptimization = "VideoOptimization"
		ForwardProxy = "ForwardProxy"
		SSLInterception = "SSLInterception"
		AdaptiveTCP = "AdaptiveTCP"
		CQA = "CQA"
		CI = "CI"
		ContentInspection = "ContentInspection"
		Bot = "Bot"

	class Certificatetype:
		ROOT_CERT = "ROOT_CERT"
		INTM_CERT = "INTM_CERT"
		CLNT_CERT = "CLNT_CERT"
		SRVR_CERT = "SRVR_CERT"
		UNKNOWN_CERT = "UNKNOWN_CERT"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

	class Inform:
		DER = "DER"
		PEM = "PEM"
		PFX = "PFX"

	class Expirymonitor:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class sslcertkey_response(base_response) :
	def __init__(self, length=1) :
		self.sslcertkey = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslcertkey = [sslcertkey() for _ in range(length)]

