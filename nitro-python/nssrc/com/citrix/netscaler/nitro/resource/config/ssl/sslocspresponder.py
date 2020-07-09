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

class sslocspresponder(base_resource) :
	""" Configuration for OCSP responser resource. """
	def __init__(self) :
		self._name = None
		self._url = None
		self._cache = None
		self._cachetimeout = None
		self._batchingdepth = None
		self._batchingdelay = None
		self._resptimeout = None
		self._ocspurlresolvetimeout = None
		self._respondercert = None
		self._trustresponder = None
		self._producedattimeskew = None
		self._signingcert = None
		self._usenonce = None
		self._insertclientcert = None
		self._httpmethod = None
		self._ocspaiarefcount = None
		self._ocspipaddrstr = None
		self._port = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the OCSP responder. Cannot begin with a hash (#) or space character and must contain only ASCII alphanumeric, underscore (_), hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the responder is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my responder" or 'my responder').<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the OCSP responder. Cannot begin with a hash (#) or space character and must contain only ASCII alphanumeric, underscore (_), hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the responder is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my responder" or 'my responder').<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def url(self) :
		r"""URL of the OCSP responder.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._url
		except Exception as e:
			raise e

	@url.setter
	def url(self, url) :
		r"""URL of the OCSP responder.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._url = url
		except Exception as e:
			raise e

	@property
	def cache(self) :
		r"""Enable caching of responses. Caching of responses received from the OCSP responder enables faster responses to the clients and reduces the load on the OCSP responder.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cache
		except Exception as e:
			raise e

	@cache.setter
	def cache(self, cache) :
		r"""Enable caching of responses. Caching of responses received from the OCSP responder enables faster responses to the clients and reduces the load on the OCSP responder.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cache = cache
		except Exception as e:
			raise e

	@property
	def cachetimeout(self) :
		r"""Timeout for caching the OCSP response. After the timeout, the Citrix ADC sends a fresh request to the OCSP responder for the certificate status. If a timeout is not specified, the timeout provided in the OCSP response applies.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  43200.
		"""
		try :
			return self._cachetimeout
		except Exception as e:
			raise e

	@cachetimeout.setter
	def cachetimeout(self, cachetimeout) :
		r"""Timeout for caching the OCSP response. After the timeout, the Citrix ADC sends a fresh request to the OCSP responder for the certificate status. If a timeout is not specified, the timeout provided in the OCSP response applies.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  43200
		"""
		try :
			self._cachetimeout = cachetimeout
		except Exception as e:
			raise e

	@property
	def batchingdepth(self) :
		r"""Number of client certificates to batch together into one OCSP request. Batching avoids overloading the OCSP responder. A value of 1 signifies that each request is queried independently. For a value greater than 1, specify a timeout (batching delay) to avoid inordinately delaying the processing of a single certificate.<br/>Minimum length =  1<br/>Maximum length =  8.
		"""
		try :
			return self._batchingdepth
		except Exception as e:
			raise e

	@batchingdepth.setter
	def batchingdepth(self, batchingdepth) :
		r"""Number of client certificates to batch together into one OCSP request. Batching avoids overloading the OCSP responder. A value of 1 signifies that each request is queried independently. For a value greater than 1, specify a timeout (batching delay) to avoid inordinately delaying the processing of a single certificate.<br/>Minimum length =  1<br/>Maximum length =  8
		"""
		try :
			self._batchingdepth = batchingdepth
		except Exception as e:
			raise e

	@property
	def batchingdelay(self) :
		r"""Maximum time, in milliseconds, to wait to accumulate OCSP requests to batch.  Does not apply if the Batching Depth is 1.<br/>Minimum length =  1<br/>Maximum length =  10000.
		"""
		try :
			return self._batchingdelay
		except Exception as e:
			raise e

	@batchingdelay.setter
	def batchingdelay(self, batchingdelay) :
		r"""Maximum time, in milliseconds, to wait to accumulate OCSP requests to batch.  Does not apply if the Batching Depth is 1.<br/>Minimum length =  1<br/>Maximum length =  10000
		"""
		try :
			self._batchingdelay = batchingdelay
		except Exception as e:
			raise e

	@property
	def resptimeout(self) :
		r"""Time, in milliseconds, to wait for an OCSP response. When this time elapses, an error message appears or the transaction is forwarded, depending on the settings on the virtual server. Includes Batching Delay time.<br/>Minimum length =  100<br/>Maximum length =  120000.
		"""
		try :
			return self._resptimeout
		except Exception as e:
			raise e

	@resptimeout.setter
	def resptimeout(self, resptimeout) :
		r"""Time, in milliseconds, to wait for an OCSP response. When this time elapses, an error message appears or the transaction is forwarded, depending on the settings on the virtual server. Includes Batching Delay time.<br/>Minimum length =  100<br/>Maximum length =  120000
		"""
		try :
			self._resptimeout = resptimeout
		except Exception as e:
			raise e

	@property
	def ocspurlresolvetimeout(self) :
		r"""Time, in milliseconds, to wait for an OCSP URL Resolution. When this time elapses, an error message appears or the transaction is forwarded, depending on the settings on the virtual server.<br/>Minimum length =  100<br/>Maximum length =  2000.
		"""
		try :
			return self._ocspurlresolvetimeout
		except Exception as e:
			raise e

	@ocspurlresolvetimeout.setter
	def ocspurlresolvetimeout(self, ocspurlresolvetimeout) :
		r"""Time, in milliseconds, to wait for an OCSP URL Resolution. When this time elapses, an error message appears or the transaction is forwarded, depending on the settings on the virtual server.<br/>Minimum length =  100<br/>Maximum length =  2000
		"""
		try :
			self._ocspurlresolvetimeout = ocspurlresolvetimeout
		except Exception as e:
			raise e

	@property
	def respondercert(self) :
		r""".<br/>Minimum length =  1.
		"""
		try :
			return self._respondercert
		except Exception as e:
			raise e

	@respondercert.setter
	def respondercert(self, respondercert) :
		r""".<br/>Minimum length =  1
		"""
		try :
			self._respondercert = respondercert
		except Exception as e:
			raise e

	@property
	def trustresponder(self) :
		r"""A certificate to use to validate OCSP responses.  Alternatively, if -trustResponder is specified, no verification will be done on the reponse.  If both are omitted, only the response times (producedAt, lastUpdate, nextUpdate) will be verified.
		"""
		try :
			return self._trustresponder
		except Exception as e:
			raise e

	@trustresponder.setter
	def trustresponder(self, trustresponder) :
		r"""A certificate to use to validate OCSP responses.  Alternatively, if -trustResponder is specified, no verification will be done on the reponse.  If both are omitted, only the response times (producedAt, lastUpdate, nextUpdate) will be verified.
		"""
		try :
			self._trustresponder = trustresponder
		except Exception as e:
			raise e

	@property
	def producedattimeskew(self) :
		r"""Time, in seconds, for which the Citrix ADC waits before considering the response as invalid. The response is considered invalid if the Produced At time stamp in the OCSP response exceeds or precedes the current Citrix ADC clock time by the amount of time specified.<br/>Default value: 300<br/>Maximum length =  86400.
		"""
		try :
			return self._producedattimeskew
		except Exception as e:
			raise e

	@producedattimeskew.setter
	def producedattimeskew(self, producedattimeskew) :
		r"""Time, in seconds, for which the Citrix ADC waits before considering the response as invalid. The response is considered invalid if the Produced At time stamp in the OCSP response exceeds or precedes the current Citrix ADC clock time by the amount of time specified.<br/>Default value: 300<br/>Maximum length =  86400
		"""
		try :
			self._producedattimeskew = producedattimeskew
		except Exception as e:
			raise e

	@property
	def signingcert(self) :
		r"""Certificate-key pair that is used to sign OCSP requests. If this parameter is not set, the requests are not signed.<br/>Minimum length =  1.
		"""
		try :
			return self._signingcert
		except Exception as e:
			raise e

	@signingcert.setter
	def signingcert(self, signingcert) :
		r"""Certificate-key pair that is used to sign OCSP requests. If this parameter is not set, the requests are not signed.<br/>Minimum length =  1
		"""
		try :
			self._signingcert = signingcert
		except Exception as e:
			raise e

	@property
	def usenonce(self) :
		r"""Enable the OCSP nonce extension, which is designed to prevent replay attacks.<br/>Possible values = YES, NO.
		"""
		try :
			return self._usenonce
		except Exception as e:
			raise e

	@usenonce.setter
	def usenonce(self, usenonce) :
		r"""Enable the OCSP nonce extension, which is designed to prevent replay attacks.<br/>Possible values = YES, NO
		"""
		try :
			self._usenonce = usenonce
		except Exception as e:
			raise e

	@property
	def insertclientcert(self) :
		r"""Include the complete client certificate in the OCSP request.<br/>Possible values = YES, NO.
		"""
		try :
			return self._insertclientcert
		except Exception as e:
			raise e

	@insertclientcert.setter
	def insertclientcert(self, insertclientcert) :
		r"""Include the complete client certificate in the OCSP request.<br/>Possible values = YES, NO
		"""
		try :
			self._insertclientcert = insertclientcert
		except Exception as e:
			raise e

	@property
	def httpmethod(self) :
		r"""HTTP method used to send ocsp request. POST is the default httpmethod. If request length is > 255, POST wil be used even if GET is set as httpMethod.<br/>Default value: POST<br/>Possible values = GET, POST.
		"""
		try :
			return self._httpmethod
		except Exception as e:
			raise e

	@httpmethod.setter
	def httpmethod(self, httpmethod) :
		r"""HTTP method used to send ocsp request. POST is the default httpmethod. If request length is > 255, POST wil be used even if GET is set as httpMethod.<br/>Default value: POST<br/>Possible values = GET, POST
		"""
		try :
			self._httpmethod = httpmethod
		except Exception as e:
			raise e

	@property
	def ocspaiarefcount(self) :
		r"""No of CA certs referencing this AIA responder.
		"""
		try :
			return self._ocspaiarefcount
		except Exception as e:
			raise e

	@property
	def ocspipaddrstr(self) :
		r"""DNS resolved IP address.
		"""
		try :
			return self._ocspipaddrstr
		except Exception as e:
			raise e

	@property
	def port(self) :
		r"""Port number on which OCSP Server listens.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslocspresponder_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslocspresponder
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
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = sslocspresponder()
		addresource.name = resource.name
		addresource.url = resource.url
		addresource.cache = resource.cache
		addresource.cachetimeout = resource.cachetimeout
		addresource.batchingdepth = resource.batchingdepth
		addresource.batchingdelay = resource.batchingdelay
		addresource.resptimeout = resource.resptimeout
		addresource.ocspurlresolvetimeout = resource.ocspurlresolvetimeout
		addresource.respondercert = resource.respondercert
		addresource.trustresponder = resource.trustresponder
		addresource.producedattimeskew = resource.producedattimeskew
		addresource.signingcert = resource.signingcert
		addresource.usenonce = resource.usenonce
		addresource.insertclientcert = resource.insertclientcert
		addresource.httpmethod = resource.httpmethod
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add sslocspresponder.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ sslocspresponder() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i] = cls.filter_add_parameters(resource[i])
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = sslocspresponder()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete sslocspresponder.
		"""
		try :
			if type(resource) is not list :
				deleteresource = sslocspresponder()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ sslocspresponder() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ sslocspresponder() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i] = cls.filter_delete_parameters(resource)
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = sslocspresponder()
		updateresource.name = resource.name
		updateresource.url = resource.url
		updateresource.cache = resource.cache
		updateresource.cachetimeout = resource.cachetimeout
		updateresource.batchingdepth = resource.batchingdepth
		updateresource.batchingdelay = resource.batchingdelay
		updateresource.resptimeout = resource.resptimeout
		updateresource.ocspurlresolvetimeout = resource.ocspurlresolvetimeout
		updateresource.respondercert = resource.respondercert
		updateresource.trustresponder = resource.trustresponder
		updateresource.producedattimeskew = resource.producedattimeskew
		updateresource.signingcert = resource.signingcert
		updateresource.usenonce = resource.usenonce
		updateresource.insertclientcert = resource.insertclientcert
		updateresource.httpmethod = resource.httpmethod
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update sslocspresponder.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ sslocspresponder() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of sslocspresponder resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = sslocspresponder()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
					unsetresource.insertclientcert = resource.insertclientcert
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ sslocspresponder() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ sslocspresponder() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
							unsetresources[i].insertclientcert = resource[i].insertclientcert
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the sslocspresponder resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = sslocspresponder()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = sslocspresponder()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [sslocspresponder() for _ in range(len(name))]
						obj = [sslocspresponder() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = sslocspresponder()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of sslocspresponder resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslocspresponder()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the sslocspresponder resources configured on NetScaler.
		"""
		try :
			obj = sslocspresponder()
			option_ = options()
			option_.count = True
			response = obj.get_resources(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e

	@classmethod
	def count_filtered(cls, client, filter_) :
		r""" Use this API to count filtered the set of sslocspresponder resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslocspresponder()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Insertclientcert:
		YES = "YES"
		NO = "NO"

	class Usenonce:
		YES = "YES"
		NO = "NO"

	class Cache:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Httpmethod:
		GET = "GET"
		POST = "POST"

class sslocspresponder_response(base_response) :
	def __init__(self, length=1) :
		self.sslocspresponder = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslocspresponder = [sslocspresponder() for _ in range(length)]

