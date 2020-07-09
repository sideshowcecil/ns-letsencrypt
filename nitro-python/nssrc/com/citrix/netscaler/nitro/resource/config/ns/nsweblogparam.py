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

class nsweblogparam(base_resource) :
	""" Configuration for Web log parameters resource. """
	def __init__(self) :
		self._buffersizemb = None
		self._customreqhdrs = None
		self._customrsphdrs = None
		self._builtin = None
		self._feature = None

	@property
	def buffersizemb(self) :
		r"""Buffer size, in MB, allocated for log transaction data on the system. The maximum value is limited to the memory available on the system.<br/>Default value: 16<br/>Minimum length =  1<br/>Maximum length =  4294967294LU.
		"""
		try :
			return self._buffersizemb
		except Exception as e:
			raise e

	@buffersizemb.setter
	def buffersizemb(self, buffersizemb) :
		r"""Buffer size, in MB, allocated for log transaction data on the system. The maximum value is limited to the memory available on the system.<br/>Default value: 16<br/>Minimum length =  1<br/>Maximum length =  4294967294LU
		"""
		try :
			self._buffersizemb = buffersizemb
		except Exception as e:
			raise e

	@property
	def customreqhdrs(self) :
		r"""Name(s) of HTTP request headers whose values should be exported by the Web Logging feature.<br/>Minimum length =  1.
		"""
		try :
			return self._customreqhdrs
		except Exception as e:
			raise e

	@customreqhdrs.setter
	def customreqhdrs(self, customreqhdrs) :
		r"""Name(s) of HTTP request headers whose values should be exported by the Web Logging feature.<br/>Minimum length =  1
		"""
		try :
			self._customreqhdrs = customreqhdrs
		except Exception as e:
			raise e

	@property
	def customrsphdrs(self) :
		r"""Name(s) of HTTP response headers whose values should be exported by the Web Logging feature.<br/>Minimum length =  1.
		"""
		try :
			return self._customrsphdrs
		except Exception as e:
			raise e

	@customrsphdrs.setter
	def customrsphdrs(self, customrsphdrs) :
		r"""Name(s) of HTTP response headers whose values should be exported by the Web Logging feature.<br/>Minimum length =  1
		"""
		try :
			self._customrsphdrs = customrsphdrs
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r"""Flag to determine if log bufs is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
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
			result = service.payload_formatter.string_to_resource(nsweblogparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsweblogparam
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
		updateresource = nsweblogparam()
		updateresource.buffersizemb = resource.buffersizemb
		updateresource.customreqhdrs = resource.customreqhdrs
		updateresource.customrsphdrs = resource.customrsphdrs
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nsweblogparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nsweblogparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nsweblogparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nsweblogparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsweblogparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


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

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

class nsweblogparam_response(base_response) :
	def __init__(self, length=1) :
		self.nsweblogparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsweblogparam = [nsweblogparam() for _ in range(length)]

