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

class bot_stats(base_resource) :
	def __init__(self) :
		self._clearstats = None
		self._botrequests = 0
		self._botrequestsrate = 0
		self._botreqbytes = 0
		self._botreqbytesrate = 0
		self._botresponses = 0
		self._botresponsesrate = 0
		self._botresbytes = 0
		self._botresbytesrate = 0
		self._botvioldevicefingerprint = 0
		self._botvioldevicefingerprintrate = 0
		self._botvioldevicefingerprintlog = 0
		self._botvioldevicefingerprintlograte = 0
		self._botvioldevicefingerprintdrop = 0
		self._botvioldevicefingerprintdroprate = 0
		self._botvioldevicefingerprintredirect = 0
		self._botvioldevicefingerprintredirectrate = 0
		self._botviolipreputation = 0
		self._botviolipreputationrate = 0
		self._botviolipreputationlog = 0
		self._botviolipreputationlograte = 0
		self._botviolipreputationdrop = 0
		self._botviolipreputationdroprate = 0
		self._botviolipreputationredirect = 0
		self._botviolipreputationredirectrate = 0
		self._botviolwhitelist = 0
		self._botviolwhitelistrate = 0
		self._botviolwhitelistlog = 0
		self._botviolwhitelistlograte = 0
		self._botviolblacklist = 0
		self._botviolblacklistrate = 0
		self._botviolblacklistlog = 0
		self._botviolblacklistlograte = 0
		self._botviolblacklistdrop = 0
		self._botviolblacklistdroprate = 0
		self._botviolblacklistredirect = 0
		self._botviolblacklistredirectrate = 0
		self._botviolratelimit = 0
		self._botviolratelimitrate = 0
		self._botviolratelimitlog = 0
		self._botviolratelimitlograte = 0
		self._botviolratelimitdrop = 0
		self._botviolratelimitdroprate = 0
		self._botviolratelimitredirect = 0
		self._botviolratelimitredirectrate = 0
		self._botviolstaticsignature = 0
		self._botviolstaticsignaturerate = 0
		self._botviolstaticsignaturelog = 0
		self._botviolstaticsignaturelograte = 0
		self._botviolstaticsignaturedrop = 0
		self._botviolstaticsignaturedroprate = 0
		self._botviolstaticsignatureredirect = 0
		self._botviolstaticsignatureredirectrate = 0

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
	def botviolstaticsignaturedrop(self) :
		r"""Number of static signature violations dropped by the Bot Management.
		"""
		try :
			return self._botviolstaticsignaturedrop
		except Exception as e:
			raise e

	@property
	def botviolblacklistrate(self) :
		r"""Rate (/s) counter for botviolblacklist.
		"""
		try :
			return self._botviolblacklistrate
		except Exception as e:
			raise e

	@property
	def botviolratelimitlog(self) :
		r"""Number of rate limiting violations logged by the Bot Management.
		"""
		try :
			return self._botviolratelimitlog
		except Exception as e:
			raise e

	@property
	def botviolblacklist(self) :
		r"""Number of black list violations seen by the Bot Management.
		"""
		try :
			return self._botviolblacklist
		except Exception as e:
			raise e

	@property
	def botrequestsrate(self) :
		r"""Rate (/s) counter for botrequests.
		"""
		try :
			return self._botrequestsrate
		except Exception as e:
			raise e

	@property
	def botresponsesrate(self) :
		r"""Rate (/s) counter for botresponses.
		"""
		try :
			return self._botresponsesrate
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintlog(self) :
		r"""Number of device fingerprint violations logged by the Bot Management.
		"""
		try :
			return self._botvioldevicefingerprintlog
		except Exception as e:
			raise e

	@property
	def botviolstaticsignatureredirectrate(self) :
		r"""Rate (/s) counter for botviolstaticsignatureredirect.
		"""
		try :
			return self._botviolstaticsignatureredirectrate
		except Exception as e:
			raise e

	@property
	def botviolipreputationlograte(self) :
		r"""Rate (/s) counter for botviolipreputationlog.
		"""
		try :
			return self._botviolipreputationlograte
		except Exception as e:
			raise e

	@property
	def botviolipreputationredirectrate(self) :
		r"""Rate (/s) counter for botviolipreputationredirect.
		"""
		try :
			return self._botviolipreputationredirectrate
		except Exception as e:
			raise e

	@property
	def botviolratelimitredirectrate(self) :
		r"""Rate (/s) counter for botviolratelimitredirect.
		"""
		try :
			return self._botviolratelimitredirectrate
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintdroprate(self) :
		r"""Rate (/s) counter for botvioldevicefingerprintdrop.
		"""
		try :
			return self._botvioldevicefingerprintdroprate
		except Exception as e:
			raise e

	@property
	def botviolwhitelistlograte(self) :
		r"""Rate (/s) counter for botviolwhitelistlog.
		"""
		try :
			return self._botviolwhitelistlograte
		except Exception as e:
			raise e

	@property
	def botviolipreputationdroprate(self) :
		r"""Rate (/s) counter for botviolipreputationdrop.
		"""
		try :
			return self._botviolipreputationdroprate
		except Exception as e:
			raise e

	@property
	def botviolratelimitdroprate(self) :
		r"""Rate (/s) counter for botviolratelimitdrop.
		"""
		try :
			return self._botviolratelimitdroprate
		except Exception as e:
			raise e

	@property
	def botresbytesrate(self) :
		r"""Rate (/s) counter for botresbytes.
		"""
		try :
			return self._botresbytesrate
		except Exception as e:
			raise e

	@property
	def botviolratelimitrate(self) :
		r"""Rate (/s) counter for botviolratelimit.
		"""
		try :
			return self._botviolratelimitrate
		except Exception as e:
			raise e

	@property
	def botviolblacklistdrop(self) :
		r"""Number of black list violations dropped by the Bot Management.
		"""
		try :
			return self._botviolblacklistdrop
		except Exception as e:
			raise e

	@property
	def botreqbytesrate(self) :
		r"""Rate (/s) counter for botreqbytes.
		"""
		try :
			return self._botreqbytesrate
		except Exception as e:
			raise e

	@property
	def botviolipreputationlog(self) :
		r"""Number of ip reputation violations logged by the Bot Management.
		"""
		try :
			return self._botviolipreputationlog
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintdrop(self) :
		r"""Number of device fingerprint violations dropped by the Bot Management.
		"""
		try :
			return self._botvioldevicefingerprintdrop
		except Exception as e:
			raise e

	@property
	def botresbytes(self) :
		r"""Number of bytes transfered for responses.
		"""
		try :
			return self._botresbytes
		except Exception as e:
			raise e

	@property
	def botviolipreputationredirect(self) :
		r"""Number of ip reputation violations requests redirected by the Bot Management to a different Web page or web server.
		"""
		try :
			return self._botviolipreputationredirect
		except Exception as e:
			raise e

	@property
	def botviolratelimit(self) :
		r"""Number of rate limiting violations seen by the Bot Management.
		"""
		try :
			return self._botviolratelimit
		except Exception as e:
			raise e

	@property
	def botreqbytes(self) :
		r"""Number of bytes transfered for requests.
		"""
		try :
			return self._botreqbytes
		except Exception as e:
			raise e

	@property
	def botviolblacklistdroprate(self) :
		r"""Rate (/s) counter for botviolblacklistdrop.
		"""
		try :
			return self._botviolblacklistdroprate
		except Exception as e:
			raise e

	@property
	def botviolwhitelistrate(self) :
		r"""Rate (/s) counter for botviolwhitelist.
		"""
		try :
			return self._botviolwhitelistrate
		except Exception as e:
			raise e

	@property
	def botviolstaticsignaturelograte(self) :
		r"""Rate (/s) counter for botviolstaticsignaturelog.
		"""
		try :
			return self._botviolstaticsignaturelograte
		except Exception as e:
			raise e

	@property
	def botviolstaticsignaturerate(self) :
		r"""Rate (/s) counter for botviolstaticsignature.
		"""
		try :
			return self._botviolstaticsignaturerate
		except Exception as e:
			raise e

	@property
	def botviolipreputation(self) :
		r"""Number of ip reputation violations seen by the Bot Management.
		"""
		try :
			return self._botviolipreputation
		except Exception as e:
			raise e

	@property
	def botviolwhitelist(self) :
		r"""Number of white list violations seen by the Bot Management.
		"""
		try :
			return self._botviolwhitelist
		except Exception as e:
			raise e

	@property
	def botviolblacklistlograte(self) :
		r"""Rate (/s) counter for botviolblacklistlog.
		"""
		try :
			return self._botviolblacklistlograte
		except Exception as e:
			raise e

	@property
	def botviolipreputationdrop(self) :
		r"""Number of ip reputation violations dropped by the Bot Management.
		"""
		try :
			return self._botviolipreputationdrop
		except Exception as e:
			raise e

	@property
	def botviolratelimitdrop(self) :
		r"""Number of rate limiting violations dropped by the Bot Management.
		"""
		try :
			return self._botviolratelimitdrop
		except Exception as e:
			raise e

	@property
	def botviolblacklistredirect(self) :
		r"""Number of black list violations redirected by the Bot Management to a different Web page or web server.
		"""
		try :
			return self._botviolblacklistredirect
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprint(self) :
		r"""Number of device fingerprint violations seen by the Bot Management.
		"""
		try :
			return self._botvioldevicefingerprint
		except Exception as e:
			raise e

	@property
	def botviolratelimitredirect(self) :
		r"""Number of rate limiting violations requests redirected by the Bot Management to a different Web page or web server.
		"""
		try :
			return self._botviolratelimitredirect
		except Exception as e:
			raise e

	@property
	def botviolblacklistredirectrate(self) :
		r"""Rate (/s) counter for botviolblacklistredirect.
		"""
		try :
			return self._botviolblacklistredirectrate
		except Exception as e:
			raise e

	@property
	def botviolstaticsignaturedroprate(self) :
		r"""Rate (/s) counter for botviolstaticsignaturedrop.
		"""
		try :
			return self._botviolstaticsignaturedroprate
		except Exception as e:
			raise e

	@property
	def botviolipreputationrate(self) :
		r"""Rate (/s) counter for botviolipreputation.
		"""
		try :
			return self._botviolipreputationrate
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintredirect(self) :
		r"""Number of device fingerprint violations requests redirected by the Bot Management to a different Web page or web server.
		"""
		try :
			return self._botvioldevicefingerprintredirect
		except Exception as e:
			raise e

	@property
	def botviolstaticsignatureredirect(self) :
		r"""Number of static signature violations requests redirected by the Bot Management to a different Web page or web server.
		"""
		try :
			return self._botviolstaticsignatureredirect
		except Exception as e:
			raise e

	@property
	def botviolwhitelistlog(self) :
		r"""Number of white list violations logged by the Bot Management.
		"""
		try :
			return self._botviolwhitelistlog
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintrate(self) :
		r"""Rate (/s) counter for botvioldevicefingerprint.
		"""
		try :
			return self._botvioldevicefingerprintrate
		except Exception as e:
			raise e

	@property
	def botrequests(self) :
		r"""HTTP/HTTPS requests sent to your protected web servers via the Bot Management.
		"""
		try :
			return self._botrequests
		except Exception as e:
			raise e

	@property
	def botviolstaticsignaturelog(self) :
		r"""Number of static signature violations logged by the Bot Management.
		"""
		try :
			return self._botviolstaticsignaturelog
		except Exception as e:
			raise e

	@property
	def botviolstaticsignature(self) :
		r"""Number of static signature violations seen by the Bot Management.
		"""
		try :
			return self._botviolstaticsignature
		except Exception as e:
			raise e

	@property
	def botviolblacklistlog(self) :
		r"""Number of black list violations logged by the Bot Management.
		"""
		try :
			return self._botviolblacklistlog
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintredirectrate(self) :
		r"""Rate (/s) counter for botvioldevicefingerprintredirect.
		"""
		try :
			return self._botvioldevicefingerprintredirectrate
		except Exception as e:
			raise e

	@property
	def botvioldevicefingerprintlograte(self) :
		r"""Rate (/s) counter for botvioldevicefingerprintlog.
		"""
		try :
			return self._botvioldevicefingerprintlograte
		except Exception as e:
			raise e

	@property
	def botresponses(self) :
		r"""HTTP/HTTPS responses sent by your protected web servers via the Bot Management.
		"""
		try :
			return self._botresponses
		except Exception as e:
			raise e

	@property
	def botviolratelimitlograte(self) :
		r"""Rate (/s) counter for botviolratelimitlog.
		"""
		try :
			return self._botviolratelimitlograte
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(bot_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.bot
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
		r""" Use this API to fetch the statistics of all bot_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = bot_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class bot_response(base_response) :
	def __init__(self, length=1) :
		self.bot = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.bot = [bot_stats() for _ in range(length)]

