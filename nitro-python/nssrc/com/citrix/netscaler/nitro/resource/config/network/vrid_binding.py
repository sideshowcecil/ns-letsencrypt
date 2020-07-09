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

class vrid_binding(base_resource):
	""" Binding class showing the resources that can be bound to vrid_binding. 
	"""
	def __init__(self) :
		self._id = None
		self.vrid_trackinterface_binding = []
		self.vrid_nsip6_binding = []
		self.vrid_interface_binding = []
		self.vrid_channel_binding = []
		self.vrid_nsip_binding = []

	@property
	def id(self) :
		r"""Integer value that uniquely identifies the VMAC address.<br/>Minimum value =  1<br/>Maximum value =  255.
		"""
		try :
			return self._id
		except Exception as e:
			raise e

	@id.setter
	def id(self, id) :
		r"""Integer value that uniquely identifies the VMAC address.<br/>Minimum value =  1<br/>Maximum value =  255
		"""
		try :
			self._id = id
		except Exception as e:
			raise e

	@property
	def vrid_nsip6_bindings(self) :
		r"""nsip6 that can be bound to vrid.
		"""
		try :
			return self._vrid_nsip6_binding
		except Exception as e:
			raise e

	@property
	def vrid_nsip_bindings(self) :
		r"""nsip that can be bound to vrid.
		"""
		try :
			return self._vrid_nsip_binding
		except Exception as e:
			raise e

	@property
	def vrid_interface_bindings(self) :
		r"""interface that can be bound to vrid.
		"""
		try :
			return self._vrid_interface_binding
		except Exception as e:
			raise e

	@property
	def vrid_channel_bindings(self) :
		r"""channel that can be bound to vrid.
		"""
		try :
			return self._vrid_channel_binding
		except Exception as e:
			raise e

	@property
	def vrid_trackinterface_bindings(self) :
		r"""trackinterface that can be bound to vrid.
		"""
		try :
			return self._vrid_trackinterface_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vrid_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vrid_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.id is not None :
				return str(self.id)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, id="", option_="") :
		r""" Use this API to fetch vrid_binding resource.
		"""
		try :
			if not id :
				obj = vrid_binding()
				response = obj.get_resources(service, option_)
			elif type(id) is not list :
				obj = vrid_binding()
				obj.id = id
				response = obj.get_resource(service)
			else :
				if id and len(id) > 0 :
					obj = [vrid_binding() for _ in range(len(id))]
					for i in range(len(id)) :
						obj[i].id = id[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class vrid_binding_response(base_response) :
	def __init__(self, length=1) :
		self.vrid_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vrid_binding = [vrid_binding() for _ in range(length)]

