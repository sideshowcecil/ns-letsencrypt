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

class nsdiameter(base_resource) :
	""" Configuration for Diameter Parameters resource. """
	def __init__(self) :
		self._identity = None
		self._realm = None
		self._serverclosepropagation = None
		self._ownernode = None
		self.___count = None

	@property
	def identity(self) :
		r"""DiameterIdentity to be used by NS. DiameterIdentity is used to identify a Diameter node uniquely. Before setting up diameter configuration, Citrix ADC (as a Diameter node) MUST be assigned a unique DiameterIdentity.
		example =>
		set ns diameter -identity netscaler.com
		Now whenever Citrix ADC needs to use identity in diameter messages. It will use 'netscaler.com' as Origin-Host AVP as defined in RFC3588
		.<br/>Minimum length =  1.
		"""
		try :
			return self._identity
		except Exception as e:
			raise e

	@identity.setter
	def identity(self, identity) :
		r"""DiameterIdentity to be used by NS. DiameterIdentity is used to identify a Diameter node uniquely. Before setting up diameter configuration, Citrix ADC (as a Diameter node) MUST be assigned a unique DiameterIdentity.
		example =>
		set ns diameter -identity netscaler.com
		Now whenever Citrix ADC needs to use identity in diameter messages. It will use 'netscaler.com' as Origin-Host AVP as defined in RFC3588
		.<br/>Minimum length =  1
		"""
		try :
			self._identity = identity
		except Exception as e:
			raise e

	@property
	def realm(self) :
		r"""Diameter Realm to be used by NS.
		example =>
		set ns diameter -realm com
		Now whenever Citrix ADC system needs to use realm in diameter messages. It will use 'com' as Origin-Realm AVP as defined in RFC3588
		.<br/>Minimum length =  1.
		"""
		try :
			return self._realm
		except Exception as e:
			raise e

	@realm.setter
	def realm(self, realm) :
		r"""Diameter Realm to be used by NS.
		example =>
		set ns diameter -realm com
		Now whenever Citrix ADC system needs to use realm in diameter messages. It will use 'com' as Origin-Realm AVP as defined in RFC3588
		.<br/>Minimum length =  1
		"""
		try :
			self._realm = realm
		except Exception as e:
			raise e

	@property
	def serverclosepropagation(self) :
		r"""when a Server connection goes down, whether to close the corresponding client connection if there were requests pending on the server.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._serverclosepropagation
		except Exception as e:
			raise e

	@serverclosepropagation.setter
	def serverclosepropagation(self, serverclosepropagation) :
		r"""when a Server connection goes down, whether to close the corresponding client connection if there were requests pending on the server.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._serverclosepropagation = serverclosepropagation
		except Exception as e:
			raise e

	@property
	def ownernode(self) :
		r"""ID of the cluster node for which the diameter id is set, can be configured only through CLIP.<br/>Default value: -1<br/>Maximum length =  31.
		"""
		try :
			return self._ownernode
		except Exception as e:
			raise e

	@ownernode.setter
	def ownernode(self, ownernode) :
		r"""ID of the cluster node for which the diameter id is set, can be configured only through CLIP.<br/>Default value: -1<br/>Maximum length =  31
		"""
		try :
			self._ownernode = ownernode
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsdiameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsdiameter
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.ownernode is not None :
				return str(self.ownernode)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = nsdiameter()
		updateresource.identity = resource.identity
		updateresource.realm = resource.realm
		updateresource.serverclosepropagation = resource.serverclosepropagation
		updateresource.ownernode = resource.ownernode
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nsdiameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nsdiameter() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nsdiameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nsdiameter()
				if type(resource) !=  type(unsetresource):
					unsetresource.ownernode = resource
				else :
					unsetresource.ownernode = resource.ownernode
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ nsdiameter() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].ownernode = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ nsdiameter() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].ownernode = resource[i].ownernode
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nsdiameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsdiameter()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = nsdiameter()
					obj.ownernode = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [nsdiameter() for _ in range(len(name))]
						obj = [nsdiameter() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = nsdiameter()
							obj[i].ownernode = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of nsdiameter resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsdiameter()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the nsdiameter resources configured on NetScaler.
		"""
		try :
			obj = nsdiameter()
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
		r""" Use this API to count filtered the set of nsdiameter resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsdiameter()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Serverclosepropagation:
		YES = "YES"
		NO = "NO"

class nsdiameter_response(base_response) :
	def __init__(self, length=1) :
		self.nsdiameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsdiameter = [nsdiameter() for _ in range(length)]

