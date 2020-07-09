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

class aaaotpparameter(base_resource) :
	""" Configuration for AAA otpparameter resource. """
	def __init__(self) :
		self._encryption = None
		self._maxotpdevices = None

	@property
	def encryption(self) :
		r"""To encrypt otp secret in AD or not. Default value is OFF.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._encryption
		except Exception as e:
			raise e

	@encryption.setter
	def encryption(self, encryption) :
		r"""To encrypt otp secret in AD or not. Default value is OFF.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._encryption = encryption
		except Exception as e:
			raise e

	@property
	def maxotpdevices(self) :
		r"""Maximum number of otp devices user can register. Default value is 4. Max value is 255.<br/>Default value: 4<br/>Maximum length =  255.
		"""
		try :
			return self._maxotpdevices
		except Exception as e:
			raise e

	@maxotpdevices.setter
	def maxotpdevices(self, maxotpdevices) :
		r"""Maximum number of otp devices user can register. Default value is 4. Max value is 255.<br/>Default value: 4<br/>Maximum length =  255
		"""
		try :
			self._maxotpdevices = maxotpdevices
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(aaaotpparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.aaaotpparameter
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
		updateresource = aaaotpparameter()
		updateresource.encryption = resource.encryption
		updateresource.maxotpdevices = resource.maxotpdevices
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update aaaotpparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of aaaotpparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = aaaotpparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the aaaotpparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = aaaotpparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Encryption:
		ON = "ON"
		OFF = "OFF"

class aaaotpparameter_response(base_response) :
	def __init__(self, length=1) :
		self.aaaotpparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.aaaotpparameter = [aaaotpparameter() for _ in range(length)]

