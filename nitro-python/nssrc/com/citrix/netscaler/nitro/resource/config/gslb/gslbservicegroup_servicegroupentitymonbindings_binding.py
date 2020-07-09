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

class gslbservicegroup_servicegroupentitymonbindings_binding(base_resource) :
	""" Binding class showing the servicegroupentitymonbindings that can be bound to gslbservicegroup.
	"""
	def __init__(self) :
		self._servicegroupentname2 = None
		self._monitor_name = None
		self._monitor_state = None
		self._passive = None
		self._monitortotalprobes = None
		self._monitortotalfailedprobes = None
		self._monitorcurrentfailedprobes = None
		self._lastresponse = None
		self._servicegroupname = None
		self._port = None
		self._weight = None
		self._state = None
		self._hashid = None
		self._publicip = None
		self._publicport = None
		self._siteprefix = None
		self.___count = None

	@property
	def servicegroupentname2(self) :
		try :
			return self._servicegroupentname2
		except Exception as e:
			raise e

	@servicegroupentname2.setter
	def servicegroupentname2(self, servicegroupentname2) :
		try :
			self._servicegroupentname2 = servicegroupentname2
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Initial state of the service after binding.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""Initial state of the service after binding.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def publicport(self) :
		r"""The public port associated with the GSLB service's public IP address. The port is mapped to the service's private port number. Applicable to the local GSLB service. Optional.
		"""
		try :
			return self._publicport
		except Exception as e:
			raise e

	@publicport.setter
	def publicport(self, publicport) :
		r"""The public port associated with the GSLB service's public IP address. The port is mapped to the service's private port number. Applicable to the local GSLB service. Optional.
		"""
		try :
			self._publicport = publicport
		except Exception as e:
			raise e

	@property
	def weight(self) :
		r"""When used along with monitor name, it specifies the weight of the monitor binding. When used along with servername & port pair, it specifies the weight of this GSLB service .<br/>Default value: 1<br/>Minimum value =  1<br/>Maximum value =  100.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@weight.setter
	def weight(self, weight) :
		r"""When used along with monitor name, it specifies the weight of the monitor binding. When used along with servername & port pair, it specifies the weight of this GSLB service .<br/>Default value: 1<br/>Minimum value =  1<br/>Maximum value =  100
		"""
		try :
			self._weight = weight
		except Exception as e:
			raise e

	@property
	def port(self) :
		r"""Port number of the GSLB service. Each service must have a unique port number.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		r"""Port number of the GSLB service. Each service must have a unique port number.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	@property
	def siteprefix(self) :
		r"""The site's prefix string. When the GSLB service group is bound to a GSLB virtual server, a GSLB site domain is generated internally for each bound serviceitem-domain pair by concatenating the site prefix of the service item and the name of the domain. If the special string NONE is specified, the site-prefix string is unset. When implementing HTTP redirect site persistence, the Citrix ADC redirects GSLB requests to GSLB services by using their site domains.
		"""
		try :
			return self._siteprefix
		except Exception as e:
			raise e

	@siteprefix.setter
	def siteprefix(self, siteprefix) :
		r"""The site's prefix string. When the GSLB service group is bound to a GSLB virtual server, a GSLB site domain is generated internally for each bound serviceitem-domain pair by concatenating the site prefix of the service item and the name of the domain. If the special string NONE is specified, the site-prefix string is unset. When implementing HTTP redirect site persistence, the Citrix ADC redirects GSLB requests to GSLB services by using their site domains.
		"""
		try :
			self._siteprefix = siteprefix
		except Exception as e:
			raise e

	@property
	def passive(self) :
		r"""Indicates if load monitor is passive. A passive load monitor does not remove service from LB decision when threshold is breached.
		"""
		try :
			return self._passive
		except Exception as e:
			raise e

	@passive.setter
	def passive(self, passive) :
		r"""Indicates if load monitor is passive. A passive load monitor does not remove service from LB decision when threshold is breached.
		"""
		try :
			self._passive = passive
		except Exception as e:
			raise e

	@property
	def monitor_name(self) :
		r"""Monitor name.
		"""
		try :
			return self._monitor_name
		except Exception as e:
			raise e

	@monitor_name.setter
	def monitor_name(self, monitor_name) :
		r"""Monitor name.
		"""
		try :
			self._monitor_name = monitor_name
		except Exception as e:
			raise e

	@property
	def servicegroupname(self) :
		r"""Name of the GSLB service group.<br/>Minimum length =  1.
		"""
		try :
			return self._servicegroupname
		except Exception as e:
			raise e

	@servicegroupname.setter
	def servicegroupname(self, servicegroupname) :
		r"""Name of the GSLB service group.<br/>Minimum length =  1
		"""
		try :
			self._servicegroupname = servicegroupname
		except Exception as e:
			raise e

	@property
	def hashid(self) :
		r"""Unique numerical identifier used by hash based load balancing methods to identify a service.<br/>Minimum value =  1.
		"""
		try :
			return self._hashid
		except Exception as e:
			raise e

	@hashid.setter
	def hashid(self, hashid) :
		r"""Unique numerical identifier used by hash based load balancing methods to identify a service.<br/>Minimum value =  1
		"""
		try :
			self._hashid = hashid
		except Exception as e:
			raise e

	@property
	def publicip(self) :
		r"""The public IP address that a NAT device translates to the GSLB service's private IP address. Optional.
		"""
		try :
			return self._publicip
		except Exception as e:
			raise e

	@publicip.setter
	def publicip(self, publicip) :
		r"""The public IP address that a NAT device translates to the GSLB service's private IP address. Optional.
		"""
		try :
			self._publicip = publicip
		except Exception as e:
			raise e

	@property
	def lastresponse(self) :
		r"""The string form of monstatcode.
		"""
		try :
			return self._lastresponse
		except Exception as e:
			raise e

	@property
	def monitor_state(self) :
		r"""The running state of the monitor on this service.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._monitor_state
		except Exception as e:
			raise e

	@property
	def monitortotalprobes(self) :
		r"""Total number of probes sent to monitor this service.
		"""
		try :
			return self._monitortotalprobes
		except Exception as e:
			raise e

	@property
	def monitortotalfailedprobes(self) :
		r"""Total number of failed probes.
		"""
		try :
			return self._monitortotalfailedprobes
		except Exception as e:
			raise e

	@property
	def monitorcurrentfailedprobes(self) :
		r"""Total number of currently failed probes.
		"""
		try :
			return self._monitorcurrentfailedprobes
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(gslbservicegroup_servicegroupentitymonbindings_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gslbservicegroup_servicegroupentitymonbindings_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.servicegroupname is not None :
				return str(self.servicegroupname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def get(cls, service, servicegroupname="", option_="") :
		r""" Use this API to fetch gslbservicegroup_servicegroupentitymonbindings_binding resources.
		"""
		try :
			if not servicegroupname :
				obj = gslbservicegroup_servicegroupentitymonbindings_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = gslbservicegroup_servicegroupentitymonbindings_binding()
				obj.servicegroupname = servicegroupname
				response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, servicegroupname, filter_) :
		r""" Use this API to fetch filtered set of gslbservicegroup_servicegroupentitymonbindings_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbservicegroup_servicegroupentitymonbindings_binding()
			obj.servicegroupname = servicegroupname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, servicegroupname) :
		r""" Use this API to count gslbservicegroup_servicegroupentitymonbindings_binding resources configued on NetScaler.
		"""
		try :
			obj = gslbservicegroup_servicegroupentitymonbindings_binding()
			obj.servicegroupname = servicegroupname
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, servicegroupname, filter_) :
		r""" Use this API to count the filtered set of gslbservicegroup_servicegroupentitymonbindings_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbservicegroup_servicegroupentitymonbindings_binding()
			obj.servicegroupname = servicegroupname
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Monitor_state:
		UP = "UP"
		DOWN = "DOWN"
		UNKNOWN = "UNKNOWN"
		BUSY = "BUSY"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
		DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
		NS_EMPTY_STR = "NS_EMPTY_STR"
		Unknown = "Unknown"
		DISABLED = "DISABLED"

	class Monstate:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class gslbservicegroup_servicegroupentitymonbindings_binding_response(base_response) :
	def __init__(self, length=1) :
		self.gslbservicegroup_servicegroupentitymonbindings_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.gslbservicegroup_servicegroupentitymonbindings_binding = [gslbservicegroup_servicegroupentitymonbindings_binding() for _ in range(length)]

