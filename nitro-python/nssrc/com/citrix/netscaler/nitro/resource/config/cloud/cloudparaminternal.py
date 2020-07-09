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

class cloudparaminternal(base_resource) :
	""" Configuration for cloud paramInternal resource. """
	def __init__(self) :
		self._nonftumode = None
		self._iamperm = None
		self.___count = None

	@property
	def nonftumode(self) :
		r"""Indicates if GUI in in FTU mode or not.<br/>Possible values = YES, NO.
		"""
		try :
			return self._nonftumode
		except Exception as e:
			raise e

	@nonftumode.setter
	def nonftumode(self, nonftumode) :
		r"""Indicates if GUI in in FTU mode or not.<br/>Possible values = YES, NO
		"""
		try :
			self._nonftumode = nonftumode
		except Exception as e:
			raise e

	@property
	def iamperm(self) :
		r"""Indicates if user has sufficient IAM previliges.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._iamperm
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cloudparaminternal_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cloudparaminternal
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
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = cloudparaminternal()
		updateresource.nonftumode = resource.nonftumode
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update cloudparaminternal.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ cloudparaminternal() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the cloudparaminternal resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = cloudparaminternal()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of cloudparaminternal resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cloudparaminternal()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the cloudparaminternal resources configured on NetScaler.
		"""
		try :
			obj = cloudparaminternal()
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
		r""" Use this API to count filtered the set of cloudparaminternal resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = cloudparaminternal()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Nonftumode:
		YES = "YES"
		NO = "NO"

	class Iamperm:
		YES = "YES"
		NO = "NO"

class cloudparaminternal_response(base_response) :
	def __init__(self, length=1) :
		self.cloudparaminternal = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cloudparaminternal = [cloudparaminternal() for _ in range(length)]

