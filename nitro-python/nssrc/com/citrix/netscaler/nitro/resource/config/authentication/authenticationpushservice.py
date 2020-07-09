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

class authenticationpushservice(base_resource) :
	""" Configuration for Service details for sending push notifications resource. """
	def __init__(self) :
		self._name = None
		self._clientid = None
		self._clientsecret = None
		self._customerid = None
		self._refreshinterval = None
		self._Namespace = None
		self._hubname = None
		self._servicekey = None
		self._servicekeyname = None
		self._certendpoint = None
		self._pushservicestatus = None
		self._trustservice = None
		self._pushcloudserverstatus = None
		self._signingkeyname = None
		self._signingkey = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the push service. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Cannot be changed after the profile is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my push service" or 'my push service'). .<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the push service. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Cannot be changed after the profile is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my push service" or 'my push service'). .<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def clientid(self) :
		r"""Unique identity for communicating with Citrix Push server in cloud.<br/>Minimum length =  1.
		"""
		try :
			return self._clientid
		except Exception as e:
			raise e

	@clientid.setter
	def clientid(self, clientid) :
		r"""Unique identity for communicating with Citrix Push server in cloud.<br/>Minimum length =  1
		"""
		try :
			self._clientid = clientid
		except Exception as e:
			raise e

	@property
	def clientsecret(self) :
		r"""Unique secret for communicating with Citrix Push server in cloud.<br/>Minimum length =  1.
		"""
		try :
			return self._clientsecret
		except Exception as e:
			raise e

	@clientsecret.setter
	def clientsecret(self, clientsecret) :
		r"""Unique secret for communicating with Citrix Push server in cloud.<br/>Minimum length =  1
		"""
		try :
			self._clientsecret = clientsecret
		except Exception as e:
			raise e

	@property
	def customerid(self) :
		r"""Customer id/name of the account in cloud that is used to create clientid/secret pair.<br/>Minimum length =  1.
		"""
		try :
			return self._customerid
		except Exception as e:
			raise e

	@customerid.setter
	def customerid(self, customerid) :
		r"""Customer id/name of the account in cloud that is used to create clientid/secret pair.<br/>Minimum length =  1
		"""
		try :
			self._customerid = customerid
		except Exception as e:
			raise e

	@property
	def refreshinterval(self) :
		r"""Interval at which certificates or idtoken is refreshed.<br/>Default value: 50.
		"""
		try :
			return self._refreshinterval
		except Exception as e:
			raise e

	@refreshinterval.setter
	def refreshinterval(self, refreshinterval) :
		r"""Interval at which certificates or idtoken is refreshed.<br/>Default value: 50
		"""
		try :
			self._refreshinterval = refreshinterval
		except Exception as e:
			raise e

	@property
	def Namespace(self) :
		r"""This is fully qualified domain name of the notification service in the cloud. If omitted, namespace defaults to https://mfa.cloud.com/.<br/>Minimum length =  1<br/>Maximum length =  63.
		"""
		try :
			return self._Namespace
		except Exception as e:
			raise e

	@property
	def hubname(self) :
		r"""Name of the hub within a namespace. This is used to classify different identities within a namespace.<br/>Minimum length =  1.
		"""
		try :
			return self._hubname
		except Exception as e:
			raise e

	@property
	def servicekey(self) :
		r"""Key to be used to compute signature necessary for registering to notification service.<br/>Minimum length =  1.
		"""
		try :
			return self._servicekey
		except Exception as e:
			raise e

	@property
	def servicekeyname(self) :
		r"""Friendly name of the Key to be used to compute signature necessary for registering to notification service.<br/>Minimum length =  1.
		"""
		try :
			return self._servicekeyname
		except Exception as e:
			raise e

	@property
	def certendpoint(self) :
		r"""URL of the endpoint that contains JWKs (Json Web Key) for JWT (Json Web Token) verification. This is used at cloud instance that offers push service.
		"""
		try :
			return self._certendpoint
		except Exception as e:
			raise e

	@property
	def pushservicestatus(self) :
		r"""Describes status of push service.<br/>Default value: INIT<br/>Possible values = INIT, CERTFETCH, CCTOKEN, COMPLETE.
		"""
		try :
			return self._pushservicestatus
		except Exception as e:
			raise e

	@property
	def trustservice(self) :
		r"""URL of the service that generates tokens for cloud access.<br/>Minimum length =  1.
		"""
		try :
			return self._trustservice
		except Exception as e:
			raise e

	@property
	def pushcloudserverstatus(self) :
		r"""Describes status of the cloud service that does push.<br/>Possible values = UP, DOWN.
		"""
		try :
			return self._pushcloudserverstatus
		except Exception as e:
			raise e

	@property
	def signingkeyname(self) :
		r"""Friendly name of the Key to be used to compute signature necessary for accessing notification service.<br/>Minimum length =  1.
		"""
		try :
			return self._signingkeyname
		except Exception as e:
			raise e

	@property
	def signingkey(self) :
		r"""Key to be used to compute signature necessary for accessing notification service.<br/>Minimum length =  1.
		"""
		try :
			return self._signingkey
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(authenticationpushservice_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationpushservice
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
		addresource = authenticationpushservice()
		addresource.name = resource.name
		addresource.clientid = resource.clientid
		addresource.clientsecret = resource.clientsecret
		addresource.customerid = resource.customerid
		addresource.refreshinterval = resource.refreshinterval
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add authenticationpushservice.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ authenticationpushservice() for _ in range(len(resource))]
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
		deleteresource = authenticationpushservice()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete authenticationpushservice.
		"""
		try :
			if type(resource) is not list :
				deleteresource = authenticationpushservice()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationpushservice() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationpushservice() for _ in range(len(resource))]
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
		updateresource = authenticationpushservice()
		updateresource.name = resource.name
		updateresource.clientid = resource.clientid
		updateresource.clientsecret = resource.clientsecret
		updateresource.customerid = resource.customerid
		updateresource.refreshinterval = resource.refreshinterval
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update authenticationpushservice.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ authenticationpushservice() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of authenticationpushservice resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = authenticationpushservice()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationpushservice() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationpushservice() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the authenticationpushservice resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = authenticationpushservice()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = authenticationpushservice()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [authenticationpushservice() for _ in range(len(name))]
						obj = [authenticationpushservice() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = authenticationpushservice()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of authenticationpushservice resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationpushservice()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the authenticationpushservice resources configured on NetScaler.
		"""
		try :
			obj = authenticationpushservice()
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
		r""" Use this API to count filtered the set of authenticationpushservice resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationpushservice()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Pushcloudserverstatus:
		UP = "UP"
		DOWN = "DOWN"

	class Pushservicestatus:
		INIT = "INIT"
		CERTFETCH = "CERTFETCH"
		CCTOKEN = "CCTOKEN"
		COMPLETE = "COMPLETE"

class authenticationpushservice_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationpushservice = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationpushservice = [authenticationpushservice() for _ in range(length)]

