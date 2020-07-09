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

class authenticationazurekeyvault(base_resource) :
	""" Configuration for Azure Key Vault entity resource. """
	def __init__(self) :
		self._name = None
		self._vaultname = None
		self._clientid = None
		self._clientsecret = None
		self._servicekeyname = None
		self._signaturealg = None
		self._tokenendpoint = None
		self._pushservice = None
		self._defaultauthenticationgroup = None
		self._refreshinterval = None
		self._tenantid = None
		self._authentication = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the new Azure Key Vault profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after an action is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the new Azure Key Vault profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after an action is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def vaultname(self) :
		r"""Name of the Azure vault account as configured in azure portal.<br/>Minimum length =  1<br/>Maximum length =  63.
		"""
		try :
			return self._vaultname
		except Exception as e:
			raise e

	@vaultname.setter
	def vaultname(self, vaultname) :
		r"""Name of the Azure vault account as configured in azure portal.<br/>Minimum length =  1<br/>Maximum length =  63
		"""
		try :
			self._vaultname = vaultname
		except Exception as e:
			raise e

	@property
	def clientid(self) :
		r"""Unique identity of the relying party requesting for authentication.<br/>Minimum length =  1.
		"""
		try :
			return self._clientid
		except Exception as e:
			raise e

	@clientid.setter
	def clientid(self, clientid) :
		r"""Unique identity of the relying party requesting for authentication.<br/>Minimum length =  1
		"""
		try :
			self._clientid = clientid
		except Exception as e:
			raise e

	@property
	def clientsecret(self) :
		r"""Unique secret string to authorize relying party at authorization server.<br/>Minimum length =  1.
		"""
		try :
			return self._clientsecret
		except Exception as e:
			raise e

	@clientsecret.setter
	def clientsecret(self, clientsecret) :
		r"""Unique secret string to authorize relying party at authorization server.<br/>Minimum length =  1
		"""
		try :
			self._clientsecret = clientsecret
		except Exception as e:
			raise e

	@property
	def servicekeyname(self) :
		r"""Friendly name of the Key to be used to compute signature.<br/>Minimum length =  1.
		"""
		try :
			return self._servicekeyname
		except Exception as e:
			raise e

	@servicekeyname.setter
	def servicekeyname(self, servicekeyname) :
		r"""Friendly name of the Key to be used to compute signature.<br/>Minimum length =  1
		"""
		try :
			self._servicekeyname = servicekeyname
		except Exception as e:
			raise e

	@property
	def signaturealg(self) :
		r"""Algorithm to be used to sign/verify transactions.<br/>Default value: RS256<br/>Possible values = RS256.
		"""
		try :
			return self._signaturealg
		except Exception as e:
			raise e

	@signaturealg.setter
	def signaturealg(self, signaturealg) :
		r"""Algorithm to be used to sign/verify transactions.<br/>Default value: RS256<br/>Possible values = RS256
		"""
		try :
			self._signaturealg = signaturealg
		except Exception as e:
			raise e

	@property
	def tokenendpoint(self) :
		r"""URL endpoint on relying party to which the OAuth token is to be sent.<br/>Minimum length =  1.
		"""
		try :
			return self._tokenendpoint
		except Exception as e:
			raise e

	@tokenendpoint.setter
	def tokenendpoint(self, tokenendpoint) :
		r"""URL endpoint on relying party to which the OAuth token is to be sent.<br/>Minimum length =  1
		"""
		try :
			self._tokenendpoint = tokenendpoint
		except Exception as e:
			raise e

	@property
	def pushservice(self) :
		r"""Name of the service used to send push notifications.<br/>Minimum length =  1.
		"""
		try :
			return self._pushservice
		except Exception as e:
			raise e

	@pushservice.setter
	def pushservice(self, pushservice) :
		r"""Name of the service used to send push notifications.<br/>Minimum length =  1
		"""
		try :
			self._pushservice = pushservice
		except Exception as e:
			raise e

	@property
	def defaultauthenticationgroup(self) :
		r"""This is the group that is added to user sessions that match current IdP policy. It can be used in policies to identify relying party trust.
		"""
		try :
			return self._defaultauthenticationgroup
		except Exception as e:
			raise e

	@defaultauthenticationgroup.setter
	def defaultauthenticationgroup(self, defaultauthenticationgroup) :
		r"""This is the group that is added to user sessions that match current IdP policy. It can be used in policies to identify relying party trust.
		"""
		try :
			self._defaultauthenticationgroup = defaultauthenticationgroup
		except Exception as e:
			raise e

	@property
	def refreshinterval(self) :
		r"""Interval at which access token in obtained.<br/>Default value: 50.
		"""
		try :
			return self._refreshinterval
		except Exception as e:
			raise e

	@refreshinterval.setter
	def refreshinterval(self, refreshinterval) :
		r"""Interval at which access token in obtained.<br/>Default value: 50
		"""
		try :
			self._refreshinterval = refreshinterval
		except Exception as e:
			raise e

	@property
	def tenantid(self) :
		r"""TenantID of the application. This is usually specific to providers such as Microsoft and usually refers to the deployment identifier.
		"""
		try :
			return self._tenantid
		except Exception as e:
			raise e

	@tenantid.setter
	def tenantid(self, tenantid) :
		r"""TenantID of the application. This is usually specific to providers such as Microsoft and usually refers to the deployment identifier.
		"""
		try :
			self._tenantid = tenantid
		except Exception as e:
			raise e

	@property
	def authentication(self) :
		r"""If authentication is disabled, otp checks are not performed after azure vault keys are obtained. This is useful to distinguish whether user has registered devices. .<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._authentication
		except Exception as e:
			raise e

	@authentication.setter
	def authentication(self, authentication) :
		r"""If authentication is disabled, otp checks are not performed after azure vault keys are obtained. This is useful to distinguish whether user has registered devices. .<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._authentication = authentication
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(authenticationazurekeyvault_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationazurekeyvault
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.name is not None :
				return str(self.name)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = authenticationazurekeyvault()
		addresource.name = resource.name
		addresource.vaultname = resource.vaultname
		addresource.clientid = resource.clientid
		addresource.clientsecret = resource.clientsecret
		addresource.servicekeyname = resource.servicekeyname
		addresource.signaturealg = resource.signaturealg
		addresource.tokenendpoint = resource.tokenendpoint
		addresource.pushservice = resource.pushservice
		addresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
		addresource.refreshinterval = resource.refreshinterval
		addresource.tenantid = resource.tenantid
		addresource.authentication = resource.authentication
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add authenticationazurekeyvault.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ authenticationazurekeyvault() for _ in range(len(resource))]
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
		deleteresource = authenticationazurekeyvault()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete authenticationazurekeyvault.
		"""
		try :
			if type(resource) is not list :
				deleteresource = authenticationazurekeyvault()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationazurekeyvault() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationazurekeyvault() for _ in range(len(resource))]
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
		updateresource = authenticationazurekeyvault()
		updateresource.name = resource.name
		updateresource.vaultname = resource.vaultname
		updateresource.clientid = resource.clientid
		updateresource.clientsecret = resource.clientsecret
		updateresource.servicekeyname = resource.servicekeyname
		updateresource.signaturealg = resource.signaturealg
		updateresource.tokenendpoint = resource.tokenendpoint
		updateresource.pushservice = resource.pushservice
		updateresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
		updateresource.refreshinterval = resource.refreshinterval
		updateresource.tenantid = resource.tenantid
		updateresource.authentication = resource.authentication
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update authenticationazurekeyvault.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ authenticationazurekeyvault() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of authenticationazurekeyvault resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = authenticationazurekeyvault()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationazurekeyvault() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationazurekeyvault() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the authenticationazurekeyvault resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = authenticationazurekeyvault()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = authenticationazurekeyvault()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [authenticationazurekeyvault() for _ in range(len(name))]
						obj = [authenticationazurekeyvault() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = authenticationazurekeyvault()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of authenticationazurekeyvault resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationazurekeyvault()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the authenticationazurekeyvault resources configured on NetScaler.
		"""
		try :
			obj = authenticationazurekeyvault()
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
		r""" Use this API to count filtered the set of authenticationazurekeyvault resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationazurekeyvault()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Authentication:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Signaturealg:
		RS256 = "RS256"

class authenticationazurekeyvault_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationazurekeyvault = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationazurekeyvault = [authenticationazurekeyvault() for _ in range(length)]

