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

class aaaglobal_aaapreauthenticationpolicy_binding(base_resource) :
	""" Binding class showing the aaapreauthenticationpolicy that can be bound to aaaglobal.
	"""
	def __init__(self) :
		self._policy = None
		self._priority = None
		self._bindpolicytype = None
		self._builtin = None
		self.___count = None

	@property
	def priority(self) :
		r"""Priority of the bound policy.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		r"""Priority of the bound policy.
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def policy(self) :
		r"""Name of the policy to be unbound.<br/>Minimum length =  1.
		"""
		try :
			return self._policy
		except Exception as e:
			raise e

	@policy.setter
	def policy(self, policy) :
		r"""Name of the policy to be unbound.<br/>Minimum length =  1
		"""
		try :
			self._policy = policy
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r"""Indicates that a variable is a built-in (SYSTEM INTERNAL) type.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	@builtin.setter
	def builtin(self, builtin) :
		r"""Indicates that a variable is a built-in (SYSTEM INTERNAL) type.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL
		"""
		try :
			self._builtin = builtin
		except Exception as e:
			raise e

	@property
	def bindpolicytype(self) :
		r"""Bound policy type.
		"""
		try :
			return self._bindpolicytype
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(aaaglobal_aaapreauthenticationpolicy_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aaaglobal_aaapreauthenticationpolicy_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = aaaglobal_aaapreauthenticationpolicy_binding()
		addresource.policy = resource.policy
		addresource.priority = resource.priority
		return addresource

	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = cls.filter_add_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [aaaglobal_aaapreauthenticationpolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_add_parameters(resource[i])
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = aaaglobal_aaapreauthenticationpolicy_binding()
		deleteresource.policy = resource.policy
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [aaaglobal_aaapreauthenticationpolicy_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i] = cls.filter_delete_parameters(resource[i])
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service) :
		r""" Use this API to fetch a aaaglobal_aaapreauthenticationpolicy_binding resources.
		"""
		try :
			obj = aaaglobal_aaapreauthenticationpolicy_binding()
			response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, filter_) :
		r""" Use this API to fetch filtered set of aaaglobal_aaapreauthenticationpolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaaglobal_aaapreauthenticationpolicy_binding()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service) :
		r""" Use this API to count aaaglobal_aaapreauthenticationpolicy_binding resources configued on NetScaler.
		"""
		try :
			obj = aaaglobal_aaapreauthenticationpolicy_binding()
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, filter_) :
		r""" Use this API to count the filtered set of aaaglobal_aaapreauthenticationpolicy_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = aaaglobal_aaapreauthenticationpolicy_binding()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

class aaaglobal_aaapreauthenticationpolicy_binding_response(base_response) :
	def __init__(self, length=1) :
		self.aaaglobal_aaapreauthenticationpolicy_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.aaaglobal_aaapreauthenticationpolicy_binding = [aaaglobal_aaapreauthenticationpolicy_binding() for _ in range(length)]

