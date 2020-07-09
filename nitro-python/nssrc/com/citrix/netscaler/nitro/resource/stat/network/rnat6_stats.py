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

class rnat6_stats(base_resource) :
	r""" Statistics for IPv6 RNAT configured route resource.
	"""
	def __init__(self) :
		self._clearstats = None
		self._rnat6totrxbytes = 0
		self._rnat6rxbytesrate = 0
		self._rnat6tottxbytes = 0
		self._rnat6txbytesrate = 0
		self._rnat6totrxpkts = 0
		self._rnat6rxpktsrate = 0
		self._rnat6tottxpkts = 0
		self._rnat6txpktsrate = 0
		self._rnat6tottxsyn = 0
		self._rnat6txsynrate = 0
		self._rnat6cursessions = 0

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
	def rnat6cursessions(self) :
		r"""Currently active RNAT6 sessions.
		"""
		try :
			return self._rnat6cursessions
		except Exception as e:
			raise e

	@property
	def rnat6txpktsrate(self) :
		r"""Rate (/s) counter for rnat6tottxpkts.
		"""
		try :
			return self._rnat6txpktsrate
		except Exception as e:
			raise e

	@property
	def rnat6tottxsyn(self) :
		r"""Requests for connections sent during RNAT6 sessions.
		"""
		try :
			return self._rnat6tottxsyn
		except Exception as e:
			raise e

	@property
	def rnat6tottxbytes(self) :
		r"""Bytes sent during RNAT6 sessions.
		"""
		try :
			return self._rnat6tottxbytes
		except Exception as e:
			raise e

	@property
	def rnat6txsynrate(self) :
		r"""Rate (/s) counter for rnat6tottxsyn.
		"""
		try :
			return self._rnat6txsynrate
		except Exception as e:
			raise e

	@property
	def rnat6rxpktsrate(self) :
		r"""Rate (/s) counter for rnat6totrxpkts.
		"""
		try :
			return self._rnat6rxpktsrate
		except Exception as e:
			raise e

	@property
	def rnat6rxbytesrate(self) :
		r"""Rate (/s) counter for rnat6totrxbytes.
		"""
		try :
			return self._rnat6rxbytesrate
		except Exception as e:
			raise e

	@property
	def rnat6txbytesrate(self) :
		r"""Rate (/s) counter for rnat6tottxbytes.
		"""
		try :
			return self._rnat6txbytesrate
		except Exception as e:
			raise e

	@property
	def rnat6totrxbytes(self) :
		r"""Bytes received during RNAT6 sessions.
		"""
		try :
			return self._rnat6totrxbytes
		except Exception as e:
			raise e

	@property
	def rnat6totrxpkts(self) :
		r"""Packets received during RNAT6 sessions.
		"""
		try :
			return self._rnat6totrxpkts
		except Exception as e:
			raise e

	@property
	def rnat6tottxpkts(self) :
		r"""Packets sent during RNAT6 sessions.
		"""
		try :
			return self._rnat6tottxpkts
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(rnat6_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.rnat6
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
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all rnat6_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = rnat6_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class rnat6_response(base_response) :
	def __init__(self, length=1) :
		self.rnat6 = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.rnat6 = [rnat6_stats() for _ in range(length)]

