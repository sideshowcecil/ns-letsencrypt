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

class videooptimizationpacingpolicy_binding(base_resource):
	""" Binding class showing the resources that can be bound to videooptimizationpacingpolicy_binding. 
	"""
	def __init__(self) :
		self._name = None
		self.videooptimizationpacingpolicy_videooptimizationglobalpacing_binding = []
		self.videooptimizationpacingpolicy_lbvserver_binding = []

	@property
	def name(self) :
		r"""Name of the videooptimization pacing policy for which to display settings.Must provide policy name.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the videooptimization pacing policy for which to display settings.Must provide policy name.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def videooptimizationpacingpolicy_lbvserver_bindings(self) :
		r"""lbvserver that can be bound to videooptimizationpacingpolicy.
		"""
		try :
			return self._videooptimizationpacingpolicy_lbvserver_binding
		except Exception as e:
			raise e

	@property
	def videooptimizationpacingpolicy_videooptimizationglobalpacing_bindings(self) :
		r"""videooptimizationglobalpacing that can be bound to videooptimizationpacingpolicy.
		"""
		try :
			return self._videooptimizationpacingpolicy_videooptimizationglobalpacing_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(videooptimizationpacingpolicy_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.videooptimizationpacingpolicy_binding
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
	def get(self, service, name="", option_="") :
		r""" Use this API to fetch videooptimizationpacingpolicy_binding resource.
		"""
		try :
			if not name :
				obj = videooptimizationpacingpolicy_binding()
				response = obj.get_resources(service, option_)
			elif type(name) is not list :
				obj = videooptimizationpacingpolicy_binding()
				obj.name = name
				response = obj.get_resource(service)
			else :
				if name and len(name) > 0 :
					obj = [videooptimizationpacingpolicy_binding() for _ in range(len(name))]
					for i in range(len(name)) :
						obj[i].name = name[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class videooptimizationpacingpolicy_binding_response(base_response) :
	def __init__(self, length=1) :
		self.videooptimizationpacingpolicy_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.videooptimizationpacingpolicy_binding = [videooptimizationpacingpolicy_binding() for _ in range(length)]

