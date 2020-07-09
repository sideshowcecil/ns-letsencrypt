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

class urlfilteringparameter(base_resource) :
	""" Configuration for URLFILTERING paramter resource. """
	def __init__(self) :
		self._hoursbetweendbupdates = None
		self._timeofdaytoupdatedb = None
		self._localdatabasethreads = None
		self._cloudhost = None
		self._seeddbpath = None
		self._maxnumberofcloudthreads = None
		self._cloudkeepalivetimeout = None
		self._cloudserverconnecttimeout = None
		self._clouddblookuptimeout = None
		self._proxyhostip = None
		self._proxyport = None
		self._proxyusername = None
		self._proxypassword = None
		self._seeddbsizelevel = None

	@property
	def hoursbetweendbupdates(self) :
		r"""URL Filtering hours between DB updates.<br/>Maximum length =  720.
		"""
		try :
			return self._hoursbetweendbupdates
		except Exception as e:
			raise e

	@hoursbetweendbupdates.setter
	def hoursbetweendbupdates(self, hoursbetweendbupdates) :
		r"""URL Filtering hours between DB updates.<br/>Maximum length =  720
		"""
		try :
			self._hoursbetweendbupdates = hoursbetweendbupdates
		except Exception as e:
			raise e

	@property
	def timeofdaytoupdatedb(self) :
		r"""URL Filtering time of day to update DB.
		"""
		try :
			return self._timeofdaytoupdatedb
		except Exception as e:
			raise e

	@timeofdaytoupdatedb.setter
	def timeofdaytoupdatedb(self, timeofdaytoupdatedb) :
		r"""URL Filtering time of day to update DB.
		"""
		try :
			self._timeofdaytoupdatedb = timeofdaytoupdatedb
		except Exception as e:
			raise e

	@property
	def localdatabasethreads(self) :
		r"""URL Filtering Local DB number of threads.<br/>Minimum length =  1<br/>Maximum length =  4.
		"""
		try :
			return self._localdatabasethreads
		except Exception as e:
			raise e

	@localdatabasethreads.setter
	def localdatabasethreads(self, localdatabasethreads) :
		r"""URL Filtering Local DB number of threads.<br/>Minimum length =  1<br/>Maximum length =  4
		"""
		try :
			self._localdatabasethreads = localdatabasethreads
		except Exception as e:
			raise e

	@property
	def cloudhost(self) :
		r"""URL Filtering Cloud host.
		"""
		try :
			return self._cloudhost
		except Exception as e:
			raise e

	@cloudhost.setter
	def cloudhost(self, cloudhost) :
		r"""URL Filtering Cloud host.
		"""
		try :
			self._cloudhost = cloudhost
		except Exception as e:
			raise e

	@property
	def seeddbpath(self) :
		r"""URL Filtering Seed DB path.
		"""
		try :
			return self._seeddbpath
		except Exception as e:
			raise e

	@seeddbpath.setter
	def seeddbpath(self, seeddbpath) :
		r"""URL Filtering Seed DB path.
		"""
		try :
			self._seeddbpath = seeddbpath
		except Exception as e:
			raise e

	@property
	def maxnumberofcloudthreads(self) :
		r"""URL Filtering hours between DB updates.<br/>Minimum value =  1<br/>Maximum value =  128.
		"""
		try :
			return self._maxnumberofcloudthreads
		except Exception as e:
			raise e

	@property
	def cloudkeepalivetimeout(self) :
		r"""URL Filtering Cloud keep alive timeout in msec.<br/>Minimum value =  1000<br/>Maximum value =  600000.
		"""
		try :
			return self._cloudkeepalivetimeout
		except Exception as e:
			raise e

	@property
	def cloudserverconnecttimeout(self) :
		r"""URL Filtering Cloud server connect timeout in msec.<br/>Minimum value =  1000<br/>Maximum value =  600000.
		"""
		try :
			return self._cloudserverconnecttimeout
		except Exception as e:
			raise e

	@property
	def clouddblookuptimeout(self) :
		r"""URL Filtering CloudDB send/receive timeout in msec.<br/>Minimum value =  1000<br/>Maximum value =  600000.
		"""
		try :
			return self._clouddblookuptimeout
		except Exception as e:
			raise e

	@property
	def proxyhostip(self) :
		r"""URL Filtering Cloud Proxy HostIp.<br/>Minimum length =  1.
		"""
		try :
			return self._proxyhostip
		except Exception as e:
			raise e

	@property
	def proxyport(self) :
		r"""URL Filtering Cloud Proxy Port.
		"""
		try :
			return self._proxyport
		except Exception as e:
			raise e

	@property
	def proxyusername(self) :
		r"""URL Filtering Cloud Proxy Username.<br/>Minimum length =  1.
		"""
		try :
			return self._proxyusername
		except Exception as e:
			raise e

	@property
	def proxypassword(self) :
		r"""URL Filtering Cloud Proxy Password.<br/>Minimum length =  1.
		"""
		try :
			return self._proxypassword
		except Exception as e:
			raise e

	@property
	def seeddbsizelevel(self) :
		r"""URL Filtering Seed DB Size Level to get downloaded.<br/>Minimum value =  1<br/>Maximum value =  5.
		"""
		try :
			return self._seeddbsizelevel
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(urlfilteringparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.urlfilteringparameter
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
		updateresource = urlfilteringparameter()
		updateresource.hoursbetweendbupdates = resource.hoursbetweendbupdates
		updateresource.timeofdaytoupdatedb = resource.timeofdaytoupdatedb
		updateresource.localdatabasethreads = resource.localdatabasethreads
		updateresource.cloudhost = resource.cloudhost
		updateresource.seeddbpath = resource.seeddbpath
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update urlfilteringparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of urlfilteringparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = urlfilteringparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the urlfilteringparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = urlfilteringparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class urlfilteringparameter_response(base_response) :
	def __init__(self, length=1) :
		self.urlfilteringparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.urlfilteringparameter = [urlfilteringparameter() for _ in range(length)]

