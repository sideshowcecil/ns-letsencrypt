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

class urlfilteringcategorization(base_resource) :
	""" Configuration for Categorization resource. """
	def __init__(self) :
		self._url = None
		self._categorization = None

	@property
	def url(self) :
		r"""Url given for categorization.<br/>Minimum length =  1.
		"""
		try :
			return self._url
		except Exception as e:
			raise e

	@url.setter
	def url(self, url) :
		r"""Url given for categorization.<br/>Minimum length =  1
		"""
		try :
			self._url = url
		except Exception as e:
			raise e

	@property
	def categorization(self) :
		r"""NetStar SDK URL Categorization result for a specific url.<br/>Minimum length =  1.
		"""
		try :
			return self._categorization
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(urlfilteringcategorization_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.urlfilteringcategorization
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
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = urlfilteringcategorization()
		addresource.url = resource.url
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add urlfilteringcategorization.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def clear(cls, client, resource="") :
		r""" Use this API to clear urlfilteringcategorization.
		"""
		try :
			if type(resource) is not list :
				clearresource = urlfilteringcategorization()
				return clearresource.perform_operation(client,"clear")
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the urlfilteringcategorization resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = urlfilteringcategorization()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class urlfilteringcategorization_response(base_response) :
	def __init__(self, length=1) :
		self.urlfilteringcategorization = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.urlfilteringcategorization = [urlfilteringcategorization() for _ in range(length)]

