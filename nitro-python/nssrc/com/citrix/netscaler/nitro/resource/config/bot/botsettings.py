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

class botsettings(base_resource) :
	""" Configuration for Bot engine settings resource. """
	def __init__(self) :
		self._defaultprofile = None
		self._javascriptname = None
		self._sessiontimeout = None
		self._sessioncookiename = None
		self._dfprequestlimit = None

	@property
	def defaultprofile(self) :
		r"""Profile to use when a connection does not match any policy. Default setting is " ", which sends unmatched connections back to the Citrix ADC without attempting to filter them further.<br/>Minimum length =  1.
		"""
		try :
			return self._defaultprofile
		except Exception as e:
			raise e

	@defaultprofile.setter
	def defaultprofile(self, defaultprofile) :
		r"""Profile to use when a connection does not match any policy. Default setting is " ", which sends unmatched connections back to the Citrix ADC without attempting to filter them further.<br/>Minimum length =  1
		"""
		try :
			self._defaultprofile = defaultprofile
		except Exception as e:
			raise e

	@property
	def javascriptname(self) :
		r"""Name of the JavaScript that the BotNet feature  uses in response. 
		Must begin with a letter or number, and can consist of from 1 to 31 letters, numbers, and the hyphen (-) and underscore (_) symbols.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cookie name" or 'my cookie name').<br/>Minimum length =  1.
		"""
		try :
			return self._javascriptname
		except Exception as e:
			raise e

	@javascriptname.setter
	def javascriptname(self, javascriptname) :
		r"""Name of the JavaScript that the BotNet feature  uses in response. 
		Must begin with a letter or number, and can consist of from 1 to 31 letters, numbers, and the hyphen (-) and underscore (_) symbols.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cookie name" or 'my cookie name').<br/>Minimum length =  1
		"""
		try :
			self._javascriptname = javascriptname
		except Exception as e:
			raise e

	@property
	def sessiontimeout(self) :
		r"""Timeout, in seconds, after which a user session is terminated.<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._sessiontimeout
		except Exception as e:
			raise e

	@sessiontimeout.setter
	def sessiontimeout(self, sessiontimeout) :
		r"""Timeout, in seconds, after which a user session is terminated.<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._sessiontimeout = sessiontimeout
		except Exception as e:
			raise e

	@property
	def sessioncookiename(self) :
		r"""Name of the SessionCookie that the BotNet feature use it for tracking. 
		Must begin with a letter or number, and can consist of from 1 to 31 letters, numbers, and the hyphen (-) and underscore (_) symbols.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cookie name" or 'my cookie name').<br/>Minimum length =  1.
		"""
		try :
			return self._sessioncookiename
		except Exception as e:
			raise e

	@sessioncookiename.setter
	def sessioncookiename(self, sessioncookiename) :
		r"""Name of the SessionCookie that the BotNet feature use it for tracking. 
		Must begin with a letter or number, and can consist of from 1 to 31 letters, numbers, and the hyphen (-) and underscore (_) symbols.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cookie name" or 'my cookie name').<br/>Minimum length =  1
		"""
		try :
			self._sessioncookiename = sessioncookiename
		except Exception as e:
			raise e

	@property
	def dfprequestlimit(self) :
		r"""Number of requests to allow without bot session cookie if device fingerprint is enabled.<br/>Minimum length =  1.
		"""
		try :
			return self._dfprequestlimit
		except Exception as e:
			raise e

	@dfprequestlimit.setter
	def dfprequestlimit(self, dfprequestlimit) :
		r"""Number of requests to allow without bot session cookie if device fingerprint is enabled.<br/>Minimum length =  1
		"""
		try :
			self._dfprequestlimit = dfprequestlimit
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(botsettings_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.botsettings
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
		updateresource = botsettings()
		updateresource.defaultprofile = resource.defaultprofile
		updateresource.javascriptname = resource.javascriptname
		updateresource.sessiontimeout = resource.sessiontimeout
		updateresource.sessioncookiename = resource.sessioncookiename
		updateresource.dfprequestlimit = resource.dfprequestlimit
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update botsettings.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of botsettings resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = botsettings()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the botsettings resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = botsettings()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class botsettings_response(base_response) :
	def __init__(self, length=1) :
		self.botsettings = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.botsettings = [botsettings() for _ in range(length)]

