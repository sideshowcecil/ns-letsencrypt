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

class nsicapprofile(base_resource) :
	""" Configuration for ICAP profile resource. """
	def __init__(self) :
		self._name = None
		self._preview = None
		self._previewlength = None
		self._uri = None
		self._hostheader = None
		self._useragent = None
		self._mode = None
		self._queryparams = None
		self._connectionkeepalive = None
		self._allow204 = None
		self._inserticapheaders = None
		self._inserthttprequest = None
		self._reqtimeout = None
		self._reqtimeoutaction = None
		self._logaction = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for an ICAP profile. Must begin with a letter, number, or the underscore \(_\) character. Other characters allowed, after the first character, are the hyphen \(-\), period \(.\), hash \(\#\), space \( \), at \(@\), colon \(:\), and equal \(=\) characters. The name of a ICAP profile cannot be changed after it is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks \(for example, "my icap profile" or 'my icap profile'\).<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for an ICAP profile. Must begin with a letter, number, or the underscore \(_\) character. Other characters allowed, after the first character, are the hyphen \(-\), period \(.\), hash \(\#\), space \( \), at \(@\), colon \(:\), and equal \(=\) characters. The name of a ICAP profile cannot be changed after it is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks \(for example, "my icap profile" or 'my icap profile'\).<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def preview(self) :
		r"""Enable or Disable preview header with ICAP request. This feature allows an ICAP server to see the beginning of a transaction, then decide if it wants to opt-out of the transaction early instead of receiving the remainder of the request message.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._preview
		except Exception as e:
			raise e

	@preview.setter
	def preview(self, preview) :
		r"""Enable or Disable preview header with ICAP request. This feature allows an ICAP server to see the beginning of a transaction, then decide if it wants to opt-out of the transaction early instead of receiving the remainder of the request message.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._preview = preview
		except Exception as e:
			raise e

	@property
	def previewlength(self) :
		r"""Value of Preview Header field. Citrix ADC uses the minimum of this set value and the preview size received on OPTIONS response.<br/>Default value: 4096<br/>Maximum length =  0xFFFFFFFE.
		"""
		try :
			return self._previewlength
		except Exception as e:
			raise e

	@previewlength.setter
	def previewlength(self, previewlength) :
		r"""Value of Preview Header field. Citrix ADC uses the minimum of this set value and the preview size received on OPTIONS response.<br/>Default value: 4096<br/>Maximum length =  0xFFFFFFFE
		"""
		try :
			self._previewlength = previewlength
		except Exception as e:
			raise e

	@property
	def uri(self) :
		r"""URI representing icap service. It is a mandatory argument while creating an icapprofile.<br/>Minimum length =  1.
		"""
		try :
			return self._uri
		except Exception as e:
			raise e

	@uri.setter
	def uri(self, uri) :
		r"""URI representing icap service. It is a mandatory argument while creating an icapprofile.<br/>Minimum length =  1
		"""
		try :
			self._uri = uri
		except Exception as e:
			raise e

	@property
	def hostheader(self) :
		r"""ICAP Host Header.<br/>Minimum length =  1.
		"""
		try :
			return self._hostheader
		except Exception as e:
			raise e

	@hostheader.setter
	def hostheader(self, hostheader) :
		r"""ICAP Host Header.<br/>Minimum length =  1
		"""
		try :
			self._hostheader = hostheader
		except Exception as e:
			raise e

	@property
	def useragent(self) :
		r"""ICAP User Agent Header String.<br/>Minimum length =  1.
		"""
		try :
			return self._useragent
		except Exception as e:
			raise e

	@useragent.setter
	def useragent(self, useragent) :
		r"""ICAP User Agent Header String.<br/>Minimum length =  1
		"""
		try :
			self._useragent = useragent
		except Exception as e:
			raise e

	@property
	def mode(self) :
		r"""ICAP Mode of operation. It is a mandatory argument while creating an icapprofile.<br/>Possible values = REQMOD, RESPMOD.
		"""
		try :
			return self._mode
		except Exception as e:
			raise e

	@mode.setter
	def mode(self, mode) :
		r"""ICAP Mode of operation. It is a mandatory argument while creating an icapprofile.<br/>Possible values = REQMOD, RESPMOD
		"""
		try :
			self._mode = mode
		except Exception as e:
			raise e

	@property
	def queryparams(self) :
		r"""Query parameters to be included with ICAP request URI. Entered values should be in arg=value format. For more than one parameters, add & separated values. e.g.: arg1=val1&arg2=val2.<br/>Minimum length =  1.
		"""
		try :
			return self._queryparams
		except Exception as e:
			raise e

	@queryparams.setter
	def queryparams(self, queryparams) :
		r"""Query parameters to be included with ICAP request URI. Entered values should be in arg=value format. For more than one parameters, add & separated values. e.g.: arg1=val1&arg2=val2.<br/>Minimum length =  1
		"""
		try :
			self._queryparams = queryparams
		except Exception as e:
			raise e

	@property
	def connectionkeepalive(self) :
		r"""If enabled, Citrix ADC keeps the ICAP connection alive after a transaction to reuse it to send next ICAP request.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._connectionkeepalive
		except Exception as e:
			raise e

	@connectionkeepalive.setter
	def connectionkeepalive(self, connectionkeepalive) :
		r"""If enabled, Citrix ADC keeps the ICAP connection alive after a transaction to reuse it to send next ICAP request.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._connectionkeepalive = connectionkeepalive
		except Exception as e:
			raise e

	@property
	def allow204(self) :
		r"""Enable or Disable sending Allow: 204 header in ICAP request.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._allow204
		except Exception as e:
			raise e

	@allow204.setter
	def allow204(self, allow204) :
		r"""Enable or Disable sending Allow: 204 header in ICAP request.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._allow204 = allow204
		except Exception as e:
			raise e

	@property
	def inserticapheaders(self) :
		r"""Insert custom ICAP headers in the ICAP request to send to ICAP server. The headers can be static or can be dynamically constructed using PI Policy Expression. For example, to send static user agent and Client's IP address, the expression can be specified as "User-Agent: NS-ICAP-Client/V1.0\r\nX-Client-IP: "+CLIENT.IP.SRC+"\r\n".
		The Citrix ADC does not check the validity of the specified header name-value. You must manually validate the specified header syntax.<br/>Minimum length =  1.
		"""
		try :
			return self._inserticapheaders
		except Exception as e:
			raise e

	@inserticapheaders.setter
	def inserticapheaders(self, inserticapheaders) :
		r"""Insert custom ICAP headers in the ICAP request to send to ICAP server. The headers can be static or can be dynamically constructed using PI Policy Expression. For example, to send static user agent and Client's IP address, the expression can be specified as "User-Agent: NS-ICAP-Client/V1.0\r\nX-Client-IP: "+CLIENT.IP.SRC+"\r\n".
		The Citrix ADC does not check the validity of the specified header name-value. You must manually validate the specified header syntax.<br/>Minimum length =  1
		"""
		try :
			self._inserticapheaders = inserticapheaders
		except Exception as e:
			raise e

	@property
	def inserthttprequest(self) :
		r"""Exact HTTP request, in the form of an expression, which the Citrix ADC encapsulates and sends to the ICAP server. If you set this parameter, the ICAP request is sent using only this header. This can be used when the HTTP header is not available to send or ICAP server only needs part of the incoming HTTP request. The request expression is constrained by the feature for which it is used.
		The Citrix ADC does not check the validity of this request. You must manually validate the request.<br/>Minimum length =  1.
		"""
		try :
			return self._inserthttprequest
		except Exception as e:
			raise e

	@inserthttprequest.setter
	def inserthttprequest(self, inserthttprequest) :
		r"""Exact HTTP request, in the form of an expression, which the Citrix ADC encapsulates and sends to the ICAP server. If you set this parameter, the ICAP request is sent using only this header. This can be used when the HTTP header is not available to send or ICAP server only needs part of the incoming HTTP request. The request expression is constrained by the feature for which it is used.
		The Citrix ADC does not check the validity of this request. You must manually validate the request.<br/>Minimum length =  1
		"""
		try :
			self._inserthttprequest = inserthttprequest
		except Exception as e:
			raise e

	@property
	def reqtimeout(self) :
		r"""Time, in seconds, within which the remote server should respond to the ICAP-request. If the Netscaler does not receive any response with this time, the specified request timeout action is performed. Zero value disables this timeout functionality.<br/>Default value: 0<br/>Maximum length =  86400.
		"""
		try :
			return self._reqtimeout
		except Exception as e:
			raise e

	@reqtimeout.setter
	def reqtimeout(self, reqtimeout) :
		r"""Time, in seconds, within which the remote server should respond to the ICAP-request. If the Netscaler does not receive any response with this time, the specified request timeout action is performed. Zero value disables this timeout functionality.<br/>Default value: 0<br/>Maximum length =  86400
		"""
		try :
			self._reqtimeout = reqtimeout
		except Exception as e:
			raise e

	@property
	def reqtimeoutaction(self) :
		r"""Name of the action to perform if the Vserver/Server representing the remote service does not respond with any response within the timeout value configured. The Supported actions are
		* BYPASS - This Ignores the remote server response and sends the request/response to Client/Server.
		* If the ICAP response with Encapsulated headers is not received within the request-timeout value configured, this Ignores the remote ICAP server response and sends the Full request/response to Server/Client.
		* RESET - Reset the client connection by closing it. The client program, such as a browser, will handle this and may inform the user. The client may then resend the request if desired.
		* DROP - Drop the request without sending a response to the user.<br/>Default value: RESET<br/>Possible values = BYPASS, DROP, RESET.
		"""
		try :
			return self._reqtimeoutaction
		except Exception as e:
			raise e

	@reqtimeoutaction.setter
	def reqtimeoutaction(self, reqtimeoutaction) :
		r"""Name of the action to perform if the Vserver/Server representing the remote service does not respond with any response within the timeout value configured. The Supported actions are
		* BYPASS - This Ignores the remote server response and sends the request/response to Client/Server.
		* If the ICAP response with Encapsulated headers is not received within the request-timeout value configured, this Ignores the remote ICAP server response and sends the Full request/response to Server/Client.
		* RESET - Reset the client connection by closing it. The client program, such as a browser, will handle this and may inform the user. The client may then resend the request if desired.
		* DROP - Drop the request without sending a response to the user.<br/>Default value: RESET<br/>Possible values = BYPASS, DROP, RESET
		"""
		try :
			self._reqtimeoutaction = reqtimeoutaction
		except Exception as e:
			raise e

	@property
	def logaction(self) :
		r"""Name of the audit message action which would be evaluated on receiving the ICAP response to emit the logs.
		"""
		try :
			return self._logaction
		except Exception as e:
			raise e

	@logaction.setter
	def logaction(self, logaction) :
		r"""Name of the audit message action which would be evaluated on receiving the ICAP response to emit the logs.
		"""
		try :
			self._logaction = logaction
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsicapprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsicapprofile
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
		addresource = nsicapprofile()
		addresource.name = resource.name
		addresource.preview = resource.preview
		addresource.previewlength = resource.previewlength
		addresource.uri = resource.uri
		addresource.hostheader = resource.hostheader
		addresource.useragent = resource.useragent
		addresource.mode = resource.mode
		addresource.queryparams = resource.queryparams
		addresource.connectionkeepalive = resource.connectionkeepalive
		addresource.allow204 = resource.allow204
		addresource.inserticapheaders = resource.inserticapheaders
		addresource.inserthttprequest = resource.inserthttprequest
		addresource.reqtimeout = resource.reqtimeout
		addresource.reqtimeoutaction = resource.reqtimeoutaction
		addresource.logaction = resource.logaction
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add nsicapprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nsicapprofile() for _ in range(len(resource))]
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
		deleteresource = nsicapprofile()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete nsicapprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nsicapprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsicapprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nsicapprofile() for _ in range(len(resource))]
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
		updateresource = nsicapprofile()
		updateresource.name = resource.name
		updateresource.preview = resource.preview
		updateresource.previewlength = resource.previewlength
		updateresource.uri = resource.uri
		updateresource.hostheader = resource.hostheader
		updateresource.useragent = resource.useragent
		updateresource.mode = resource.mode
		updateresource.queryparams = resource.queryparams
		updateresource.connectionkeepalive = resource.connectionkeepalive
		updateresource.allow204 = resource.allow204
		updateresource.inserticapheaders = resource.inserticapheaders
		updateresource.inserthttprequest = resource.inserthttprequest
		updateresource.reqtimeout = resource.reqtimeout
		updateresource.reqtimeoutaction = resource.reqtimeoutaction
		updateresource.logaction = resource.logaction
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nsicapprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nsicapprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nsicapprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nsicapprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ nsicapprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ nsicapprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nsicapprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsicapprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = nsicapprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [nsicapprofile() for _ in range(len(name))]
						obj = [nsicapprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = nsicapprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of nsicapprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsicapprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the nsicapprofile resources configured on NetScaler.
		"""
		try :
			obj = nsicapprofile()
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
		r""" Use this API to count filtered the set of nsicapprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsicapprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Mode:
		REQMOD = "REQMOD"
		RESPMOD = "RESPMOD"

	class Reqtimeoutaction:
		BYPASS = "BYPASS"
		DROP = "DROP"
		RESET = "RESET"

	class Connectionkeepalive:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Preview:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Allow204:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class nsicapprofile_response(base_response) :
	def __init__(self, length=1) :
		self.nsicapprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsicapprofile = [nsicapprofile() for _ in range(length)]

