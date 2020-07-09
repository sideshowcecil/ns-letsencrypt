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

class cloudcredential(base_resource) :
	""" Configuration for cloud credentials resource. """
	def __init__(self) :
		self._tenantidentifier = None
		self._applicationid = None
		self._applicationsecret = None
		self._isset = None

	@property
	def tenantidentifier(self) :
		r"""Tenant ID of the Credentials.<br/>Minimum length =  1.
		"""
		try :
			return self._tenantidentifier
		except Exception as e:
			raise e

	@tenantidentifier.setter
	def tenantidentifier(self, tenantidentifier) :
		r"""Tenant ID of the Credentials.<br/>Minimum length =  1
		"""
		try :
			self._tenantidentifier = tenantidentifier
		except Exception as e:
			raise e

	@property
	def applicationid(self) :
		r"""Application ID of the Credentials.<br/>Minimum length =  1.
		"""
		try :
			return self._applicationid
		except Exception as e:
			raise e

	@applicationid.setter
	def applicationid(self, applicationid) :
		r"""Application ID of the Credentials.<br/>Minimum length =  1
		"""
		try :
			self._applicationid = applicationid
		except Exception as e:
			raise e

	@property
	def applicationsecret(self) :
		r"""Application Secret of the Credentials.<br/>Minimum length =  1.
		"""
		try :
			return self._applicationsecret
		except Exception as e:
			raise e

	@applicationsecret.setter
	def applicationsecret(self, applicationsecret) :
		r"""Application Secret of the Credentials.<br/>Minimum length =  1
		"""
		try :
			self._applicationsecret = applicationsecret
		except Exception as e:
			raise e

	@property
	def isset(self) :
		r"""Are the credentials set?.
		"""
		try :
			return self._isset
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cloudcredential_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cloudcredential
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
		updateresource = cloudcredential()
		updateresource.tenantidentifier = resource.tenantidentifier
		updateresource.applicationid = resource.applicationid
		updateresource.applicationsecret = resource.applicationsecret
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update cloudcredential.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the cloudcredential resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = cloudcredential()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class cloudcredential_response(base_response) :
	def __init__(self, length=1) :
		self.cloudcredential = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cloudcredential = [cloudcredential() for _ in range(length)]

