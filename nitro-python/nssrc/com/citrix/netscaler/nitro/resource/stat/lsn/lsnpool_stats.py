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

class lsnpool_stats(base_resource) :
	r""" Statistics for LSN pool resource.
	"""
	def __init__(self) :
		self._poolname = None
		self._clearstats = None
		self._lsnpoolotherportusagepercen = 0
		self._lsnpooltcpportusagepercen = 0
		self._lsnpoolcurportalloctcp = 0
		self._lsnpoolcurportalloctcprate = 0
		self._lsnpoolcurportallocother = 0
		self._lsnpoolcurportallocotherrate = 0
		self._lsnpooltotips = 0

	@property
	def poolname(self) :
		r"""Name of the LSN Pool.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._poolname
		except Exception as e:
			raise e

	@poolname.setter
	def poolname(self, poolname) :
		r"""Name of the LSN Pool.
		"""
		try :
			self._poolname = poolname
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
	def lsnpooltotips(self) :
		r"""Total IPs in this pool.
		"""
		try :
			return self._lsnpooltotips
		except Exception as e:
			raise e

	@property
	def lsnpoolcurportallocother(self) :
		r"""Current port allocation for other protocols in this pool.
		"""
		try :
			return self._lsnpoolcurportallocother
		except Exception as e:
			raise e

	@property
	def lsnpoolcurportalloctcp(self) :
		r"""Current port allocation for tcp in this pool.
		"""
		try :
			return self._lsnpoolcurportalloctcp
		except Exception as e:
			raise e

	@property
	def lsnpooltcpportusagepercen(self) :
		r"""TCP ports usage percentage in this pool.
		"""
		try :
			return self._lsnpooltcpportusagepercen
		except Exception as e:
			raise e

	@property
	def lsnpoolcurportalloctcprate(self) :
		r"""Rate (/s) counter for lsnpoolcurportalloctcp.
		"""
		try :
			return self._lsnpoolcurportalloctcprate
		except Exception as e:
			raise e

	@property
	def lsnpoolotherportusagepercen(self) :
		r"""Other protocols ports usage percentage in this pool.
		"""
		try :
			return self._lsnpoolotherportusagepercen
		except Exception as e:
			raise e

	@property
	def lsnpoolcurportallocotherrate(self) :
		r"""Rate (/s) counter for lsnpoolcurportallocother.
		"""
		try :
			return self._lsnpoolcurportallocotherrate
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsnpool_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsnpool
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.poolname is not None :
				return str(self.poolname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all lsnpool_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = lsnpool_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			else :
				obj.poolname = name
				response = obj.stat_resource(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class lsnpool_response(base_response) :
	def __init__(self, length=1) :
		self.lsnpool = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsnpool = [lsnpool_stats() for _ in range(length)]

