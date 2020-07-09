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

class azurekeyvault(base_resource) :
	""" Configuration for Azure Key Vault entity resource. """
	def __init__(self) :
		self._name = None
		self._azurevaultname = None
		self._azureapplication = None
		self._state = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the Key Vault. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the Key Vault is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my keyvault" or 'my keyvault').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the Key Vault. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the Key Vault is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my keyvault" or 'my keyvault').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def azurevaultname(self) :
		r"""Name of the Key Vault configured in Azure cloud using either the Azure CLI or the Azure portal (GUI).<br/>Minimum length =  3<br/>Maximum length =  25.
		"""
		try :
			return self._azurevaultname
		except Exception as e:
			raise e

	@azurevaultname.setter
	def azurevaultname(self, azurevaultname) :
		r"""Name of the Key Vault configured in Azure cloud using either the Azure CLI or the Azure portal (GUI).<br/>Minimum length =  3<br/>Maximum length =  25
		"""
		try :
			self._azurevaultname = azurevaultname
		except Exception as e:
			raise e

	@property
	def azureapplication(self) :
		r"""Name of the Azure Application object created on the ADC appliance. This object will be used for authentication with Azure Active Directory.<br/>Minimum length =  1<br/>Maximum length =  63.
		"""
		try :
			return self._azureapplication
		except Exception as e:
			raise e

	@azureapplication.setter
	def azureapplication(self, azureapplication) :
		r"""Name of the Azure Application object created on the ADC appliance. This object will be used for authentication with Azure Active Directory.<br/>Minimum length =  1<br/>Maximum length =  63
		"""
		try :
			self._azureapplication = azureapplication
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Current state of keyvault.<br/>Possible values = Created, Could not reach token endpoint, Authorization failed, Token parse error, Access token obtained, Keyvault host is reachable, Keyvault operation succeeded, Keyvault operation failed, Ops failed. Keyvault marked down.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(azurekeyvault_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.azurekeyvault
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
		addresource = azurekeyvault()
		addresource.name = resource.name
		addresource.azurevaultname = resource.azurevaultname
		addresource.azureapplication = resource.azureapplication
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add azurekeyvault.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ azurekeyvault() for _ in range(len(resource))]
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
		deleteresource = azurekeyvault()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete azurekeyvault.
		"""
		try :
			if type(resource) is not list :
				deleteresource = azurekeyvault()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ azurekeyvault() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ azurekeyvault() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i] = cls.filter_delete_parameters(resource)
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the azurekeyvault resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = azurekeyvault()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = azurekeyvault()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [azurekeyvault() for _ in range(len(name))]
						obj = [azurekeyvault() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = azurekeyvault()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of azurekeyvault resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = azurekeyvault()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the azurekeyvault resources configured on NetScaler.
		"""
		try :
			obj = azurekeyvault()
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
		r""" Use this API to count filtered the set of azurekeyvault resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = azurekeyvault()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class State:
		Created = "Created"
		Could_not_reach_token_endpoint = "Could not reach token endpoint"
		Authorization_failed = "Authorization failed"
		Token_parse_error = "Token parse error"
		Access_token_obtained = "Access token obtained"
		Keyvault_host_is_reachable = "Keyvault host is reachable"
		Keyvault_operation_succeeded = "Keyvault operation succeeded"
		Keyvault_operation_failed = "Keyvault operation failed"
		Ops_failed__Keyvault_marked_down = "Ops failed. Keyvault marked down"

class azurekeyvault_response(base_response) :
	def __init__(self, length=1) :
		self.azurekeyvault = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.azurekeyvault = [azurekeyvault() for _ in range(length)]

