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

class icaparameter(base_resource) :
	""" Configuration for Config Parameters for NS ICA resource. """
	def __init__(self) :
		self._enablesronhafailover = None
		self._hdxinsightnonnsap = None
		self._builtin = None

	@property
	def enablesronhafailover(self) :
		r"""Enable/Disable Session Reliability on HA failover. The default value is No.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._enablesronhafailover
		except Exception as e:
			raise e

	@enablesronhafailover.setter
	def enablesronhafailover(self, enablesronhafailover) :
		r"""Enable/Disable Session Reliability on HA failover. The default value is No.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._enablesronhafailover = enablesronhafailover
		except Exception as e:
			raise e

	@property
	def hdxinsightnonnsap(self) :
		r"""Enable/Disable HDXInsight for Non NSAP ICA Sessions. The default value is Yes.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._hdxinsightnonnsap
		except Exception as e:
			raise e

	@hdxinsightnonnsap.setter
	def hdxinsightnonnsap(self, hdxinsightnonnsap) :
		r"""Enable/Disable HDXInsight for Non NSAP ICA Sessions. The default value is Yes.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._hdxinsightnonnsap = hdxinsightnonnsap
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r"""Indicates that the ICA parameter is a built-in (SYSTEM INTERNAL) type.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(icaparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.icaparameter
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
		updateresource = icaparameter()
		updateresource.enablesronhafailover = resource.enablesronhafailover
		updateresource.hdxinsightnonnsap = resource.hdxinsightnonnsap
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update icaparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of icaparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = icaparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the icaparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = icaparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Enablesronhafailover:
		YES = "YES"
		NO = "NO"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

	class Hdxinsightnonnsap:
		YES = "YES"
		NO = "NO"

class icaparameter_response(base_response) :
	def __init__(self, length=1) :
		self.icaparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.icaparameter = [icaparameter() for _ in range(length)]

