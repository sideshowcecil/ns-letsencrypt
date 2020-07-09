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

class appfwprofile_jsondosurl_binding(base_resource) :
	""" Binding class showing the jsondosurl that can be bound to appfwprofile.
	"""
	def __init__(self) :
		self._jsondosurl = None
		self._jsonmaxdocumentlengthcheck = None
		self._jsonmaxdocumentlength = None
		self._jsonmaxcontainerdepthcheck = None
		self._jsonmaxcontainerdepth = None
		self._jsonmaxobjectkeycountcheck = None
		self._jsonmaxobjectkeycount = None
		self._jsonmaxobjectkeylengthcheck = None
		self._jsonmaxobjectkeylength = None
		self._jsonmaxarraylengthcheck = None
		self._jsonmaxarraylength = None
		self._jsonmaxstringlengthcheck = None
		self._jsonmaxstringlength = None
		self._state = None
		self._comment = None
		self._isautodeployed = None
		self._name = None
		self.___count = None

	@property
	def jsonmaxarraylengthcheck(self) :
		r"""State if JSON Max array value count check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._jsonmaxarraylengthcheck
		except Exception as e:
			raise e

	@jsonmaxarraylengthcheck.setter
	def jsonmaxarraylengthcheck(self, jsonmaxarraylengthcheck) :
		r"""State if JSON Max array value count check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._jsonmaxarraylengthcheck = jsonmaxarraylengthcheck
		except Exception as e:
			raise e

	@property
	def jsonmaxdocumentlengthcheck(self) :
		r"""State if JSON Max document length check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._jsonmaxdocumentlengthcheck
		except Exception as e:
			raise e

	@jsonmaxdocumentlengthcheck.setter
	def jsonmaxdocumentlengthcheck(self, jsonmaxdocumentlengthcheck) :
		r"""State if JSON Max document length check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._jsonmaxdocumentlengthcheck = jsonmaxdocumentlengthcheck
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Enabled.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""Enabled.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def name(self) :
		r"""Name of the profile to which to bind an exemption or rule.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the profile to which to bind an exemption or rule.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def jsonmaxcontainerdepth(self) :
		r"""Maximum allowed nesting depth  of JSON document. JSON allows one to nest the containers (object and array) in any order to any depth. This check protects against documents that have excessive depth of hierarchy.<br/>Default value: 5<br/>Minimum value =  0<br/>Maximum value =  127.
		"""
		try :
			return self._jsonmaxcontainerdepth
		except Exception as e:
			raise e

	@jsonmaxcontainerdepth.setter
	def jsonmaxcontainerdepth(self, jsonmaxcontainerdepth) :
		r"""Maximum allowed nesting depth  of JSON document. JSON allows one to nest the containers (object and array) in any order to any depth. This check protects against documents that have excessive depth of hierarchy.<br/>Default value: 5<br/>Minimum value =  0<br/>Maximum value =  127
		"""
		try :
			self._jsonmaxcontainerdepth = jsonmaxcontainerdepth
		except Exception as e:
			raise e

	@property
	def jsonmaxobjectkeylengthcheck(self) :
		r"""State if JSON Max object key length check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._jsonmaxobjectkeylengthcheck
		except Exception as e:
			raise e

	@jsonmaxobjectkeylengthcheck.setter
	def jsonmaxobjectkeylengthcheck(self, jsonmaxobjectkeylengthcheck) :
		r"""State if JSON Max object key length check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._jsonmaxobjectkeylengthcheck = jsonmaxobjectkeylengthcheck
		except Exception as e:
			raise e

	@property
	def jsondosurl(self) :
		r"""The URL on which we need to enforce the specified JSON denial-of-service (JSONDoS) attack protections.
		An JSON DoS configuration consists of the following items:
		* URL. PCRE-format regular expression for the URL.
		* Maximum-document-length-check toggle.  ON to enable this check, OFF to disable it.
		* Maximum document length. Positive integer representing the maximum length of the JSON document.
		* Maximum-container-depth-check toggle. ON to enable, OFF to disable.
		* Maximum container depth. Positive integer representing the maximum container depth of the JSON document.
		* Maximum-object-key-count-check toggle. ON to enable, OFF to disable.
		* Maximum object key count. Positive integer representing the maximum allowed number of keys in any of the  JSON object.
		* Maximum-object-key-length-check toggle. ON to enable, OFF to disable.
		* Maximum object key length. Positive integer representing the maximum allowed length of key in any of the  JSON object.
		* Maximum-array-value-count-check toggle. ON to enable, OFF to disable.
		* Maximum array value count. Positive integer representing the maximum allowed number of values in any of the JSON array.
		* Maximum-string-length-check toggle. ON to enable, OFF to disable.
		* Maximum string length. Positive integer representing the maximum length of string in JSON.
		<br/>Minimum length =  1<br/>Maximum length =  2047.
		"""
		try :
			return self._jsondosurl
		except Exception as e:
			raise e

	@jsondosurl.setter
	def jsondosurl(self, jsondosurl) :
		r"""The URL on which we need to enforce the specified JSON denial-of-service (JSONDoS) attack protections.
		An JSON DoS configuration consists of the following items:
		* URL. PCRE-format regular expression for the URL.
		* Maximum-document-length-check toggle.  ON to enable this check, OFF to disable it.
		* Maximum document length. Positive integer representing the maximum length of the JSON document.
		* Maximum-container-depth-check toggle. ON to enable, OFF to disable.
		* Maximum container depth. Positive integer representing the maximum container depth of the JSON document.
		* Maximum-object-key-count-check toggle. ON to enable, OFF to disable.
		* Maximum object key count. Positive integer representing the maximum allowed number of keys in any of the  JSON object.
		* Maximum-object-key-length-check toggle. ON to enable, OFF to disable.
		* Maximum object key length. Positive integer representing the maximum allowed length of key in any of the  JSON object.
		* Maximum-array-value-count-check toggle. ON to enable, OFF to disable.
		* Maximum array value count. Positive integer representing the maximum allowed number of values in any of the JSON array.
		* Maximum-string-length-check toggle. ON to enable, OFF to disable.
		* Maximum string length. Positive integer representing the maximum length of string in JSON.
		<br/>Minimum length =  1<br/>Maximum length =  2047
		"""
		try :
			self._jsondosurl = jsondosurl
		except Exception as e:
			raise e

	@property
	def jsonmaxarraylength(self) :
		r"""Maximum array length in the any of JSON object. This check protects against arrays having large lengths.<br/>Default value: 10000<br/>Minimum value =  0<br/>Maximum value =  2147483647.
		"""
		try :
			return self._jsonmaxarraylength
		except Exception as e:
			raise e

	@jsonmaxarraylength.setter
	def jsonmaxarraylength(self, jsonmaxarraylength) :
		r"""Maximum array length in the any of JSON object. This check protects against arrays having large lengths.<br/>Default value: 10000<br/>Minimum value =  0<br/>Maximum value =  2147483647
		"""
		try :
			self._jsonmaxarraylength = jsonmaxarraylength
		except Exception as e:
			raise e

	@property
	def jsonmaxdocumentlength(self) :
		r"""Maximum document length of JSON document, in bytes.<br/>Default value: 20000000<br/>Minimum value =  0<br/>Maximum value =  2147483647.
		"""
		try :
			return self._jsonmaxdocumentlength
		except Exception as e:
			raise e

	@jsonmaxdocumentlength.setter
	def jsonmaxdocumentlength(self, jsonmaxdocumentlength) :
		r"""Maximum document length of JSON document, in bytes.<br/>Default value: 20000000<br/>Minimum value =  0<br/>Maximum value =  2147483647
		"""
		try :
			self._jsonmaxdocumentlength = jsonmaxdocumentlength
		except Exception as e:
			raise e

	@property
	def jsonmaxobjectkeycountcheck(self) :
		r"""State if JSON Max object key count check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._jsonmaxobjectkeycountcheck
		except Exception as e:
			raise e

	@jsonmaxobjectkeycountcheck.setter
	def jsonmaxobjectkeycountcheck(self, jsonmaxobjectkeycountcheck) :
		r"""State if JSON Max object key count check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._jsonmaxobjectkeycountcheck = jsonmaxobjectkeycountcheck
		except Exception as e:
			raise e

	@property
	def jsonmaxobjectkeylength(self) :
		r"""Maximum key length in the any of JSON object. This check protects against objects that have large keys.<br/>Default value: 128<br/>Minimum value =  0<br/>Maximum value =  2147483647.
		"""
		try :
			return self._jsonmaxobjectkeylength
		except Exception as e:
			raise e

	@jsonmaxobjectkeylength.setter
	def jsonmaxobjectkeylength(self, jsonmaxobjectkeylength) :
		r"""Maximum key length in the any of JSON object. This check protects against objects that have large keys.<br/>Default value: 128<br/>Minimum value =  0<br/>Maximum value =  2147483647
		"""
		try :
			self._jsonmaxobjectkeylength = jsonmaxobjectkeylength
		except Exception as e:
			raise e

	@property
	def jsonmaxobjectkeycount(self) :
		r"""Maximum key count in the any of JSON object. This check protects against objects that have large number of keys.<br/>Default value: 10000<br/>Minimum value =  0<br/>Maximum value =  2147483647.
		"""
		try :
			return self._jsonmaxobjectkeycount
		except Exception as e:
			raise e

	@jsonmaxobjectkeycount.setter
	def jsonmaxobjectkeycount(self, jsonmaxobjectkeycount) :
		r"""Maximum key count in the any of JSON object. This check protects against objects that have large number of keys.<br/>Default value: 10000<br/>Minimum value =  0<br/>Maximum value =  2147483647
		"""
		try :
			self._jsonmaxobjectkeycount = jsonmaxobjectkeycount
		except Exception as e:
			raise e

	@property
	def jsonmaxstringlengthcheck(self) :
		r"""State if JSON Max string value count check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._jsonmaxstringlengthcheck
		except Exception as e:
			raise e

	@jsonmaxstringlengthcheck.setter
	def jsonmaxstringlengthcheck(self, jsonmaxstringlengthcheck) :
		r"""State if JSON Max string value count check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._jsonmaxstringlengthcheck = jsonmaxstringlengthcheck
		except Exception as e:
			raise e

	@property
	def isautodeployed(self) :
		r"""Is the rule auto deployed by dynamic profile ?.<br/>Possible values = AUTODEPLOYED, NOTAUTODEPLOYED.
		"""
		try :
			return self._isautodeployed
		except Exception as e:
			raise e

	@isautodeployed.setter
	def isautodeployed(self, isautodeployed) :
		r"""Is the rule auto deployed by dynamic profile ?.<br/>Possible values = AUTODEPLOYED, NOTAUTODEPLOYED
		"""
		try :
			self._isautodeployed = isautodeployed
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Any comments about the purpose of profile, or other useful information about the profile.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Any comments about the purpose of profile, or other useful information about the profile.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def jsonmaxcontainerdepthcheck(self) :
		r"""State if JSON Max depth check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._jsonmaxcontainerdepthcheck
		except Exception as e:
			raise e

	@jsonmaxcontainerdepthcheck.setter
	def jsonmaxcontainerdepthcheck(self, jsonmaxcontainerdepthcheck) :
		r"""State if JSON Max depth check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._jsonmaxcontainerdepthcheck = jsonmaxcontainerdepthcheck
		except Exception as e:
			raise e

	@property
	def jsonmaxstringlength(self) :
		r"""Maximum string length in the JSON. This check protects against strings that have large length.<br/>Default value: 1000000<br/>Minimum value =  0<br/>Maximum value =  2147483647.
		"""
		try :
			return self._jsonmaxstringlength
		except Exception as e:
			raise e

	@jsonmaxstringlength.setter
	def jsonmaxstringlength(self, jsonmaxstringlength) :
		r"""Maximum string length in the JSON. This check protects against strings that have large length.<br/>Default value: 1000000<br/>Minimum value =  0<br/>Maximum value =  2147483647
		"""
		try :
			self._jsonmaxstringlength = jsonmaxstringlength
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appfwprofile_jsondosurl_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfwprofile_jsondosurl_binding
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
		addresource = appfwprofile_jsondosurl_binding()
		addresource.name = resource.name
		addresource.comment = resource.comment
		addresource.state = resource.state
		addresource.jsondosurl = resource.jsondosurl
		addresource.jsonmaxcontainerdepthcheck = resource.jsonmaxcontainerdepthcheck
		addresource.jsonmaxcontainerdepth = resource.jsonmaxcontainerdepth
		addresource.jsonmaxdocumentlengthcheck = resource.jsonmaxdocumentlengthcheck
		addresource.jsonmaxdocumentlength = resource.jsonmaxdocumentlength
		addresource.jsonmaxobjectkeycountcheck = resource.jsonmaxobjectkeycountcheck
		addresource.jsonmaxobjectkeycount = resource.jsonmaxobjectkeycount
		addresource.jsonmaxobjectkeylengthcheck = resource.jsonmaxobjectkeylengthcheck
		addresource.jsonmaxobjectkeylength = resource.jsonmaxobjectkeylength
		addresource.jsonmaxarraylengthcheck = resource.jsonmaxarraylengthcheck
		addresource.jsonmaxarraylength = resource.jsonmaxarraylength
		addresource.jsonmaxstringlengthcheck = resource.jsonmaxstringlengthcheck
		addresource.jsonmaxstringlength = resource.jsonmaxstringlength
		addresource.isautodeployed = resource.isautodeployed
		return addresource

	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = cls.filter_add_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [appfwprofile_jsondosurl_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_add_parameters(resource[i])
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = appfwprofile_jsondosurl_binding()
		deleteresource.name = resource.name
		deleteresource.jsondosurl = resource.jsondosurl
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [appfwprofile_jsondosurl_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i] = cls.filter_delete_parameters(resource[i])
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name="", option_="") :
		r""" Use this API to fetch appfwprofile_jsondosurl_binding resources.
		"""
		try :
			if not name :
				obj = appfwprofile_jsondosurl_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = appfwprofile_jsondosurl_binding()
				obj.name = name
				response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		r""" Use this API to fetch filtered set of appfwprofile_jsondosurl_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwprofile_jsondosurl_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		r""" Use this API to count appfwprofile_jsondosurl_binding resources configued on NetScaler.
		"""
		try :
			obj = appfwprofile_jsondosurl_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, name, filter_) :
		r""" Use this API to count the filtered set of appfwprofile_jsondosurl_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwprofile_jsondosurl_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class As_scan_location_xmlsql:
		ELEMENT = "ELEMENT"
		ATTRIBUTE = "ATTRIBUTE"

	class Jsonmaxarraylengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxelementdepthcheck:
		ON = "ON"
		OFF = "OFF"

	class Jsonmaxdocumentlengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxattachmentsizecheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlsoaparraycheck:
		ON = "ON"
		OFF = "OFF"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Xmlmaxelementnamelengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex_ff:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlmaxelementscheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlendpointcheck:
		ABSOLUTE = "ABSOLUTE"
		RELATIVE = "RELATIVE"

	class Xmlmaxnamespacescheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxfilesizecheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxattributenamelengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Isvalueregex_xss:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlblockdtd:
		ON = "ON"
		OFF = "OFF"

	class Xmlblockpi:
		ON = "ON"
		OFF = "OFF"

	class Isregex_sql:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlvalidateresponse:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxelementchildrencheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Jsonmaxobjectkeylengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxentityexpansionscheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxnamespaceurilengthcheck:
		ON = "ON"
		OFF = "OFF"

	class As_scan_location_xss:
		FORMFIELD = "FORMFIELD"
		HEADER = "HEADER"
		COOKIE = "COOKIE"

	class Xmlmaxentityexpansiondepthcheck:
		ON = "ON"
		OFF = "OFF"

	class As_scan_location_xmlxss:
		ELEMENT = "ELEMENT"
		ATTRIBUTE = "ATTRIBUTE"

	class Xmlmaxattributevaluelengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Isvalueregex_sql:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class As_scan_location_sql:
		FORMFIELD = "FORMFIELD"
		HEADER = "HEADER"
		COOKIE = "COOKIE"

	class Isregex_ffc:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Filetype:
		pdf = "pdf"
		msdoc = "msdoc"
		text = "text"
		image = "image"
		any = "any"

	class Jsonmaxobjectkeycountcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlattachmentcontenttypecheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex_xmlsql:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlvalidatesoapenvelope:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxchardatalengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlminfilesizecheck:
		ON = "ON"
		OFF = "OFF"

	class Jsonmaxstringlengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex_xss:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class As_value_type_sql:
		Keyword = "Keyword"
		SpecialString = "SpecialString"
		Wildchar = "Wildchar"

	class Isregex_fileuploadtypes_url:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Isregex_xmlxss:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmladditionalsoapheaders:
		ON = "ON"
		OFF = "OFF"

	class Isautodeployed:
		AUTODEPLOYED = "AUTODEPLOYED"
		NOTAUTODEPLOYED = "NOTAUTODEPLOYED"

	class Xmlmaxattributescheck:
		ON = "ON"
		OFF = "OFF"

	class Jsonmaxcontainerdepthcheck:
		ON = "ON"
		OFF = "OFF"

	class Action:
		none = "none"
		block = "block"
		log = "log"
		remove = "remove"
		stats = "stats"
		xout = "xout"

	class As_value_type_xss:
		Tag = "Tag"
		Attribute = "Attribute"
		Pattern = "Pattern"

	class Xmlblockexternalentities:
		ON = "ON"
		OFF = "OFF"

class appfwprofile_jsondosurl_binding_response(base_response) :
	def __init__(self, length=1) :
		self.appfwprofile_jsondosurl_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appfwprofile_jsondosurl_binding = [appfwprofile_jsondosurl_binding() for _ in range(length)]

