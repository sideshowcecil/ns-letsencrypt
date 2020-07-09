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

class sslcacertgroup_binding(base_resource):
	""" Binding class showing the resources that can be bound to sslcacertgroup_binding. 
	"""
	def __init__(self) :
		self._cacertgroupname = None
		self.sslcacertgroup_sslcertkey_binding = []

	@property
	def cacertgroupname(self) :
		r"""Name of the CA certificate group for which to show detailed information.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._cacertgroupname
		except Exception as e:
			raise e

	@cacertgroupname.setter
	def cacertgroupname(self, cacertgroupname) :
		r"""Name of the CA certificate group for which to show detailed information.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._cacertgroupname = cacertgroupname
		except Exception as e:
			raise e

	@property
	def sslcacertgroup_sslcertkey_bindings(self) :
		r"""sslcertkey that can be bound to sslcacertgroup.
		"""
		try :
			return self._sslcacertgroup_sslcertkey_binding
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslcacertgroup_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslcacertgroup_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.cacertgroupname is not None :
				return str(self.cacertgroupname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(self, service, cacertgroupname="", option_="") :
		r""" Use this API to fetch sslcacertgroup_binding resource.
		"""
		try :
			if not cacertgroupname :
				obj = sslcacertgroup_binding()
				response = obj.get_resources(service, option_)
			elif type(cacertgroupname) is not list :
				obj = sslcacertgroup_binding()
				obj.cacertgroupname = cacertgroupname
				response = obj.get_resource(service)
			else :
				if cacertgroupname and len(cacertgroupname) > 0 :
					obj = [sslcacertgroup_binding() for _ in range(len(cacertgroupname))]
					for i in range(len(cacertgroupname)) :
						obj[i].cacertgroupname = cacertgroupname[i];
						response[i] = obj[i].get_resource(service)
			return response
		except Exception as e:
			raise e

class sslcacertgroup_binding_response(base_response) :
	def __init__(self, length=1) :
		self.sslcacertgroup_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslcacertgroup_binding = [sslcacertgroup_binding() for _ in range(length)]

