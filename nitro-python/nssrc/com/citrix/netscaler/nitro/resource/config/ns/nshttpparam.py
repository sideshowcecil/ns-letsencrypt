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

class nshttpparam(base_resource) :
	""" Configuration for HTTP parameter resource. """
	def __init__(self) :
		self._dropinvalreqs = None
		self._markhttp09inval = None
		self._markconnreqinval = None
		self._insnssrvrhdr = None
		self._nssrvrhdr = None
		self._logerrresp = None
		self._conmultiplex = None
		self._maxreusepool = None
		self._http2serverside = None
		self._ignoreconnectcodingscheme = None
		self._builtin = None
		self._feature = None

	@property
	def dropinvalreqs(self) :
		r"""Drop invalid HTTP requests or responses.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._dropinvalreqs
		except Exception as e:
			raise e

	@dropinvalreqs.setter
	def dropinvalreqs(self, dropinvalreqs) :
		r"""Drop invalid HTTP requests or responses.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._dropinvalreqs = dropinvalreqs
		except Exception as e:
			raise e

	@property
	def markhttp09inval(self) :
		r"""Mark HTTP/0.9 requests as invalid.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._markhttp09inval
		except Exception as e:
			raise e

	@markhttp09inval.setter
	def markhttp09inval(self, markhttp09inval) :
		r"""Mark HTTP/0.9 requests as invalid.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._markhttp09inval = markhttp09inval
		except Exception as e:
			raise e

	@property
	def markconnreqinval(self) :
		r"""Mark CONNECT requests as invalid.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._markconnreqinval
		except Exception as e:
			raise e

	@markconnreqinval.setter
	def markconnreqinval(self, markconnreqinval) :
		r"""Mark CONNECT requests as invalid.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._markconnreqinval = markconnreqinval
		except Exception as e:
			raise e

	@property
	def insnssrvrhdr(self) :
		r"""Enable or disable Citrix ADC server header insertion for Citrix ADC generated HTTP responses.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._insnssrvrhdr
		except Exception as e:
			raise e

	@insnssrvrhdr.setter
	def insnssrvrhdr(self, insnssrvrhdr) :
		r"""Enable or disable Citrix ADC server header insertion for Citrix ADC generated HTTP responses.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._insnssrvrhdr = insnssrvrhdr
		except Exception as e:
			raise e

	@property
	def nssrvrhdr(self) :
		r"""The server header value to be inserted. If no explicit header is specified then NSBUILD.RELEASE is used as default server header.<br/>Minimum length =  1.
		"""
		try :
			return self._nssrvrhdr
		except Exception as e:
			raise e

	@nssrvrhdr.setter
	def nssrvrhdr(self, nssrvrhdr) :
		r"""The server header value to be inserted. If no explicit header is specified then NSBUILD.RELEASE is used as default server header.<br/>Minimum length =  1
		"""
		try :
			self._nssrvrhdr = nssrvrhdr
		except Exception as e:
			raise e

	@property
	def logerrresp(self) :
		r"""Server header value to be inserted.<br/>Default value: ON<br/>Possible values = ON, OFF.
		"""
		try :
			return self._logerrresp
		except Exception as e:
			raise e

	@logerrresp.setter
	def logerrresp(self, logerrresp) :
		r"""Server header value to be inserted.<br/>Default value: ON<br/>Possible values = ON, OFF
		"""
		try :
			self._logerrresp = logerrresp
		except Exception as e:
			raise e

	@property
	def conmultiplex(self) :
		r"""Reuse server connections for requests from more than one client connections.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._conmultiplex
		except Exception as e:
			raise e

	@conmultiplex.setter
	def conmultiplex(self, conmultiplex) :
		r"""Reuse server connections for requests from more than one client connections.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._conmultiplex = conmultiplex
		except Exception as e:
			raise e

	@property
	def maxreusepool(self) :
		r"""Maximum limit on the number of connections, from the Citrix ADC to a particular server that are kept in the reuse pool. This setting is helpful for optimal memory utilization and for reducing the idle connections to the server just after the peak time.<br/>Default value: 0<br/>Maximum length =  360000.
		"""
		try :
			return self._maxreusepool
		except Exception as e:
			raise e

	@maxreusepool.setter
	def maxreusepool(self, maxreusepool) :
		r"""Maximum limit on the number of connections, from the Citrix ADC to a particular server that are kept in the reuse pool. This setting is helpful for optimal memory utilization and for reducing the idle connections to the server just after the peak time.<br/>Default value: 0<br/>Maximum length =  360000
		"""
		try :
			self._maxreusepool = maxreusepool
		except Exception as e:
			raise e

	@property
	def http2serverside(self) :
		r"""Enable/Disable HTTP/2 on server side.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._http2serverside
		except Exception as e:
			raise e

	@http2serverside.setter
	def http2serverside(self, http2serverside) :
		r"""Enable/Disable HTTP/2 on server side.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._http2serverside = http2serverside
		except Exception as e:
			raise e

	@property
	def ignoreconnectcodingscheme(self) :
		r"""Ignore Coding scheme in CONNECT request.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ignoreconnectcodingscheme
		except Exception as e:
			raise e

	@ignoreconnectcodingscheme.setter
	def ignoreconnectcodingscheme(self, ignoreconnectcodingscheme) :
		r"""Ignore Coding scheme in CONNECT request.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ignoreconnectcodingscheme = ignoreconnectcodingscheme
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r"""Flag to determine if the http param is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	@property
	def feature(self) :
		r"""The feature to be checked while applying this config.
		"""
		try :
			return self._feature
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nshttpparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nshttpparam
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
		updateresource = nshttpparam()
		updateresource.dropinvalreqs = resource.dropinvalreqs
		updateresource.markhttp09inval = resource.markhttp09inval
		updateresource.markconnreqinval = resource.markconnreqinval
		updateresource.insnssrvrhdr = resource.insnssrvrhdr
		updateresource.nssrvrhdr = resource.nssrvrhdr
		updateresource.logerrresp = resource.logerrresp
		updateresource.conmultiplex = resource.conmultiplex
		updateresource.maxreusepool = resource.maxreusepool
		updateresource.http2serverside = resource.http2serverside
		updateresource.ignoreconnectcodingscheme = resource.ignoreconnectcodingscheme
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nshttpparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nshttpparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nshttpparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nshttpparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nshttpparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Conmultiplex:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Markhttp09inval:
		ON = "ON"
		OFF = "OFF"

	class Insnssrvrhdr:
		ON = "ON"
		OFF = "OFF"

	class Feature:
		WL = "WL"
		WebLogging = "WebLogging"
		SP = "SP"
		SurgeProtection = "SurgeProtection"
		LB = "LB"
		LoadBalancing = "LoadBalancing"
		CS = "CS"
		ContentSwitching = "ContentSwitching"
		CR = "CR"
		CacheRedirection = "CacheRedirection"
		SC = "SC"
		SureConnect = "SureConnect"
		CMP = "CMP"
		CMPcntl = "CMPcntl"
		CompressionControl = "CompressionControl"
		PQ = "PQ"
		PriorityQueuing = "PriorityQueuing"
		HDOSP = "HDOSP"
		HttpDoSProtection = "HttpDoSProtection"
		SSLVPN = "SSLVPN"
		AAA = "AAA"
		GSLB = "GSLB"
		GlobalServerLoadBalancing = "GlobalServerLoadBalancing"
		SSL = "SSL"
		SSLOffload = "SSLOffload"
		SSLOffloading = "SSLOffloading"
		CF = "CF"
		ContentFiltering = "ContentFiltering"
		IC = "IC"
		IntegratedCaching = "IntegratedCaching"
		OSPF = "OSPF"
		OSPFRouting = "OSPFRouting"
		RIP = "RIP"
		RIPRouting = "RIPRouting"
		BGP = "BGP"
		BGPRouting = "BGPRouting"
		REWRITE = "REWRITE"
		IPv6PT = "IPv6PT"
		IPv6protocoltranslation = "IPv6protocoltranslation"
		AppFw = "AppFw"
		ApplicationFirewall = "ApplicationFirewall"
		RESPONDER = "RESPONDER"
		HTMLInjection = "HTMLInjection"
		push = "push"
		NSPush = "NSPush"
		NetScalerPush = "NetScalerPush"
		AppFlow = "AppFlow"
		CloudBridge = "CloudBridge"
		ISIS = "ISIS"
		ISISRouting = "ISISRouting"
		CH = "CH"
		CallHome = "CallHome"
		AppQoE = "AppQoE"
		ContentAccelerator = "ContentAccelerator"
		SYSTEM = "SYSTEM"
		RISE = "RISE"
		FEO = "FEO"
		LSN = "LSN"
		LargeScaleNAT = "LargeScaleNAT"
		RDPProxy = "RDPProxy"
		Rep = "Rep"
		Reputation = "Reputation"
		URLFiltering = "URLFiltering"
		VideoOptimization = "VideoOptimization"
		ForwardProxy = "ForwardProxy"
		SSLInterception = "SSLInterception"
		AdaptiveTCP = "AdaptiveTCP"
		CQA = "CQA"
		CI = "CI"
		ContentInspection = "ContentInspection"
		Bot = "Bot"

	class Ignoreconnectcodingscheme:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

	class Markconnreqinval:
		ON = "ON"
		OFF = "OFF"

	class Http2serverside:
		ON = "ON"
		OFF = "OFF"

	class Logerrresp:
		ON = "ON"
		OFF = "OFF"

	class Dropinvalreqs:
		ON = "ON"
		OFF = "OFF"

class nshttpparam_response(base_response) :
	def __init__(self, length=1) :
		self.nshttpparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nshttpparam = [nshttpparam() for _ in range(length)]

