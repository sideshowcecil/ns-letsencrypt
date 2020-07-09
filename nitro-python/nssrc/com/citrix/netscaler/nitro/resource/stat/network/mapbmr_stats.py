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

class mapbmr_stats(base_resource) :
	r""" Statistics for MAP-T Basic Mapping rule resource.
	"""
	def __init__(self) :
		self._name = None
		self._clearstats = None
		self._bmrtotv6rxpkts = 0
		self._bmrv6rxpktsrate = 0
		self._bmrtotv6txpkts = 0
		self._bmrv6txpktsrate = 0
		self._bmrtotv4rxpkts = 0
		self._bmrv4rxpktsrate = 0
		self._bmrtotv4txpkts = 0
		self._bmrv4txpktsrate = 0
		self._bmrtotv6rxpktstcp = 0
		self._bmrv6rxpktstcprate = 0
		self._bmrtotv6txpktstcp = 0
		self._bmrv6txpktstcprate = 0
		self._bmrtotv4rxpktstcp = 0
		self._bmrv4rxpktstcprate = 0
		self._bmrtotv4txpktstcp = 0
		self._bmrv4txpktstcprate = 0
		self._bmrtotv6rxpktsudp = 0
		self._bmrv6rxpktsudprate = 0
		self._bmrtotv6txpktsudp = 0
		self._bmrv6txpktsudprate = 0
		self._bmrtotv4rxpktsudp = 0
		self._bmrv4rxpktsudprate = 0
		self._bmrtotv4txpktsudp = 0
		self._bmrv4txpktsudprate = 0
		self._bmrtotv6rxpktsicmp = 0
		self._bmrv6rxpktsicmprate = 0
		self._bmrtotv6txpktsicmp = 0
		self._bmrv6txpktsicmprate = 0
		self._bmrtotv4rxpktsicmp = 0
		self._bmrv4rxpktsicmprate = 0
		self._bmrtotv4txpktsicmp = 0
		self._bmrv4txpktsicmprate = 0

	@property
	def name(self) :
		r"""Basic Mapping Rule name.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Basic Mapping Rule name.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def clearstats(self) :
		r"""Clear the statsistics / counters.<br/>Possible values = basic, full.
		"""
		try :
			return self._clearstats
		except Exception as e:
			raise e

	@clearstats.setter
	def clearstats(self, clearstats) :
		r"""Clear the statsistics / counters
		"""
		try :
			self._clearstats = clearstats
		except Exception as e:
			raise e

	@property
	def bmrv6rxpktsrate(self) :
		r"""Rate (/s) counter for bmrtotv6rxpkts.
		"""
		try :
			return self._bmrv6rxpktsrate
		except Exception as e:
			raise e

	@property
	def bmrv4rxpktsudprate(self) :
		r"""Rate (/s) counter for bmrtotv4rxpktsudp.
		"""
		try :
			return self._bmrv4rxpktsudprate
		except Exception as e:
			raise e

	@property
	def bmrtotv6txpkts(self) :
		r"""Total number of MAP-T BMR V6 Transmitted packets.
		"""
		try :
			return self._bmrtotv6txpkts
		except Exception as e:
			raise e

	@property
	def bmrv6rxpktsudprate(self) :
		r"""Rate (/s) counter for bmrtotv6rxpktsudp.
		"""
		try :
			return self._bmrv6rxpktsudprate
		except Exception as e:
			raise e

	@property
	def bmrtotv6txpktsicmp(self) :
		r"""Total number of MAP-T BMR V6 ICMP Transmitted packets.
		"""
		try :
			return self._bmrtotv6txpktsicmp
		except Exception as e:
			raise e

	@property
	def bmrtotv4rxpktsudp(self) :
		r"""Total number of MAP-T BMR V4 UDP Recieved packets.
		"""
		try :
			return self._bmrtotv4rxpktsudp
		except Exception as e:
			raise e

	@property
	def bmrv6txpktsudprate(self) :
		r"""Rate (/s) counter for bmrtotv6txpktsudp.
		"""
		try :
			return self._bmrv6txpktsudprate
		except Exception as e:
			raise e

	@property
	def bmrv4txpktsicmprate(self) :
		r"""Rate (/s) counter for bmrtotv4txpktsicmp.
		"""
		try :
			return self._bmrv4txpktsicmprate
		except Exception as e:
			raise e

	@property
	def bmrtotv6rxpkts(self) :
		r"""Total number of MAP-T BMR V6 Recieved packets.
		"""
		try :
			return self._bmrtotv6rxpkts
		except Exception as e:
			raise e

	@property
	def bmrv4txpktsrate(self) :
		r"""Rate (/s) counter for bmrtotv4txpkts.
		"""
		try :
			return self._bmrv4txpktsrate
		except Exception as e:
			raise e

	@property
	def bmrtotv4rxpkts(self) :
		r"""Total number of MAP-T BMR V4 Recieved packets.
		"""
		try :
			return self._bmrtotv4rxpkts
		except Exception as e:
			raise e

	@property
	def bmrv4txpktstcprate(self) :
		r"""Rate (/s) counter for bmrtotv4txpktstcp.
		"""
		try :
			return self._bmrv4txpktstcprate
		except Exception as e:
			raise e

	@property
	def bmrv4rxpktsicmprate(self) :
		r"""Rate (/s) counter for bmrtotv4rxpktsicmp.
		"""
		try :
			return self._bmrv4rxpktsicmprate
		except Exception as e:
			raise e

	@property
	def bmrv4rxpktstcprate(self) :
		r"""Rate (/s) counter for bmrtotv4rxpktstcp.
		"""
		try :
			return self._bmrv4rxpktstcprate
		except Exception as e:
			raise e

	@property
	def bmrv6txpktsicmprate(self) :
		r"""Rate (/s) counter for bmrtotv6txpktsicmp.
		"""
		try :
			return self._bmrv6txpktsicmprate
		except Exception as e:
			raise e

	@property
	def bmrv6txpktstcprate(self) :
		r"""Rate (/s) counter for bmrtotv6txpktstcp.
		"""
		try :
			return self._bmrv6txpktstcprate
		except Exception as e:
			raise e

	@property
	def bmrtotv6rxpktsicmp(self) :
		r"""Total number of MAP-T BMR V6 ICMP Recieved packets.
		"""
		try :
			return self._bmrtotv6rxpktsicmp
		except Exception as e:
			raise e

	@property
	def bmrtotv6txpktsudp(self) :
		r"""Total number of MAP-T BMR V6 UDP Transmitted packets.
		"""
		try :
			return self._bmrtotv6txpktsudp
		except Exception as e:
			raise e

	@property
	def bmrv6rxpktstcprate(self) :
		r"""Rate (/s) counter for bmrtotv6rxpktstcp.
		"""
		try :
			return self._bmrv6rxpktstcprate
		except Exception as e:
			raise e

	@property
	def bmrtotv4txpktsicmp(self) :
		r"""Total number of MAP-T BMR V4 ICMP Transmitted packets.
		"""
		try :
			return self._bmrtotv4txpktsicmp
		except Exception as e:
			raise e

	@property
	def bmrtotv4txpktstcp(self) :
		r"""Total number of MAP-T BMR V4 TCP Transmitted packets.
		"""
		try :
			return self._bmrtotv4txpktstcp
		except Exception as e:
			raise e

	@property
	def bmrtotv4rxpktsicmp(self) :
		r"""Total number of MAP-T BMR V4 ICMP Recieved packets.
		"""
		try :
			return self._bmrtotv4rxpktsicmp
		except Exception as e:
			raise e

	@property
	def bmrv6txpktsrate(self) :
		r"""Rate (/s) counter for bmrtotv6txpkts.
		"""
		try :
			return self._bmrv6txpktsrate
		except Exception as e:
			raise e

	@property
	def bmrtotv4txpktsudp(self) :
		r"""Total number of MAP-T BMR V4 UDP Transmitted packets.
		"""
		try :
			return self._bmrtotv4txpktsudp
		except Exception as e:
			raise e

	@property
	def bmrtotv4rxpktstcp(self) :
		r"""Total number of MAP-T BMR V4 TCP Recieved packets.
		"""
		try :
			return self._bmrtotv4rxpktstcp
		except Exception as e:
			raise e

	@property
	def bmrtotv4txpkts(self) :
		r"""Total number of MAP-T BMR V4 Transmitted packets.
		"""
		try :
			return self._bmrtotv4txpkts
		except Exception as e:
			raise e

	@property
	def bmrv4txpktsudprate(self) :
		r"""Rate (/s) counter for bmrtotv4txpktsudp.
		"""
		try :
			return self._bmrv4txpktsudprate
		except Exception as e:
			raise e

	@property
	def bmrtotv6rxpktsudp(self) :
		r"""Total number of MAP-T BMR V6 UDP Recieved packets.
		"""
		try :
			return self._bmrtotv6rxpktsudp
		except Exception as e:
			raise e

	@property
	def bmrtotv6txpktstcp(self) :
		r"""Total number of MAP-T BMR V6 TCP Transmitted packets.
		"""
		try :
			return self._bmrtotv6txpktstcp
		except Exception as e:
			raise e

	@property
	def bmrtotv6rxpktstcp(self) :
		r"""Total number of MAP-T BMR V6 TCP Recieved packets.
		"""
		try :
			return self._bmrtotv6rxpktstcp
		except Exception as e:
			raise e

	@property
	def bmrv4rxpktsrate(self) :
		r"""Rate (/s) counter for bmrtotv4rxpkts.
		"""
		try :
			return self._bmrv4rxpktsrate
		except Exception as e:
			raise e

	@property
	def bmrv6rxpktsicmprate(self) :
		r"""Rate (/s) counter for bmrtotv6rxpktsicmp.
		"""
		try :
			return self._bmrv6rxpktsicmprate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(mapbmr_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.mapbmr
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
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all mapbmr_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = mapbmr_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.name = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class mapbmr_response(base_response) :
	def __init__(self, length=1) :
		self.mapbmr = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.mapbmr = [mapbmr_stats() for _ in range(length)]

