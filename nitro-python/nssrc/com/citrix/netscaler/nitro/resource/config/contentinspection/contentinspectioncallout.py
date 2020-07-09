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

class contentinspectioncallout(base_resource) :
	""" Configuration for Content Inspection callout resource. """
	def __init__(self) :
		self._name = None
		self._type = None
		self._profilename = None
		self._servername = None
		self._serverip = None
		self._serverport = None
		self._returntype = None
		self._resultexpr = None
		self._comment = None
		self._hits = None
		self._undefhits = None
		self._undefreason = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the Content Inspection callout. Not case sensitive. Must begin with an ASCII letter or underscore (_) character, and must consist only of ASCII alphanumeric or underscore characters. Must not begin with 're' or 'xp' or be a word reserved for use as an expression qualifier prefix (such as HTTP) or enumeration value (such as ASCII). Must not be the name of an existing named expression, pattern set, dataset, stringmap, or callout.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the Content Inspection callout. Not case sensitive. Must begin with an ASCII letter or underscore (_) character, and must consist only of ASCII alphanumeric or underscore characters. Must not begin with 're' or 'xp' or be a word reserved for use as an expression qualifier prefix (such as HTTP) or enumeration value (such as ASCII). Must not be the name of an existing named expression, pattern set, dataset, stringmap, or callout.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""Type of the Content Inspection callout. It must be one of the following:
		* ICAP - Sends ICAP request to the configured ICAP server.<br/>Possible values = ICAP.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Type of the Content Inspection callout. It must be one of the following:
		* ICAP - Sends ICAP request to the configured ICAP server.<br/>Possible values = ICAP
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def profilename(self) :
		r"""Name of the Content Inspection profile. The type of the configured profile must match the type specified using -type argument.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._profilename
		except Exception as e:
			raise e

	@profilename.setter
	def profilename(self, profilename) :
		r"""Name of the Content Inspection profile. The type of the configured profile must match the type specified using -type argument.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._profilename = profilename
		except Exception as e:
			raise e

	@property
	def servername(self) :
		r"""Name of the load balancing or content switching virtual server or service to which the Content Inspection request is issued. Mutually exclusive with server IP address and port parameters. The service type must be TCP or SSL_TCP. If there are vservers and services with the same name, then vserver is selected.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._servername
		except Exception as e:
			raise e

	@servername.setter
	def servername(self, servername) :
		r"""Name of the load balancing or content switching virtual server or service to which the Content Inspection request is issued. Mutually exclusive with server IP address and port parameters. The service type must be TCP or SSL_TCP. If there are vservers and services with the same name, then vserver is selected.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._servername = servername
		except Exception as e:
			raise e

	@property
	def serverip(self) :
		r"""IP address of Content Inspection server. Mutually exclusive with the server name parameter.<br/>Minimum length =  1.
		"""
		try :
			return self._serverip
		except Exception as e:
			raise e

	@serverip.setter
	def serverip(self, serverip) :
		r"""IP address of Content Inspection server. Mutually exclusive with the server name parameter.<br/>Minimum length =  1
		"""
		try :
			self._serverip = serverip
		except Exception as e:
			raise e

	@property
	def serverport(self) :
		r"""Port of the Content Inspection server.<br/>Default value: 1344<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._serverport
		except Exception as e:
			raise e

	@serverport.setter
	def serverport(self, serverport) :
		r"""Port of the Content Inspection server.<br/>Default value: 1344<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._serverport = serverport
		except Exception as e:
			raise e

	@property
	def returntype(self) :
		r"""Type of data that the target callout agent returns in response to the callout.
		Available settings function as follows:
		* TEXT - Treat the returned value as a text string.
		* NUM - Treat the returned value as a number.
		* BOOL - Treat the returned value as a Boolean value.
		Note: You cannot change the return type after it is set.<br/>Possible values = BOOL, NUM, TEXT.
		"""
		try :
			return self._returntype
		except Exception as e:
			raise e

	@returntype.setter
	def returntype(self, returntype) :
		r"""Type of data that the target callout agent returns in response to the callout.
		Available settings function as follows:
		* TEXT - Treat the returned value as a text string.
		* NUM - Treat the returned value as a number.
		* BOOL - Treat the returned value as a Boolean value.
		Note: You cannot change the return type after it is set.<br/>Possible values = BOOL, NUM, TEXT
		"""
		try :
			self._returntype = returntype
		except Exception as e:
			raise e

	@property
	def resultexpr(self) :
		r"""Expression that extracts the callout results from the response sent by the CI callout agent. Must be a response based expression, that is, it must begin with ICAP.RES. The operations in this expression must match the return type. For example, if you configure a return type of TEXT, the result expression must be a text based expression, as in the following example: icap.res.header("ISTag").<br/>Minimum length =  1.
		"""
		try :
			return self._resultexpr
		except Exception as e:
			raise e

	@resultexpr.setter
	def resultexpr(self, resultexpr) :
		r"""Expression that extracts the callout results from the response sent by the CI callout agent. Must be a response based expression, that is, it must begin with ICAP.RES. The operations in this expression must match the return type. For example, if you configure a return type of TEXT, the result expression must be a text based expression, as in the following example: icap.res.header("ISTag").<br/>Minimum length =  1
		"""
		try :
			self._resultexpr = resultexpr
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Any comments to preserve information about this Content Inspection callout.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Any comments to preserve information about this Content Inspection callout.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def hits(self) :
		r"""Total hits.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def undefhits(self) :
		r"""Total undefs.
		"""
		try :
			return self._undefhits
		except Exception as e:
			raise e

	@property
	def undefreason(self) :
		r"""Reason for last undef.<br/>Possible values = Failed to add service, Vserver not found, Not a HTTP or SSL vserver, Generated callout request is invalid, Content-Length header not found in callout request, Not enough space to put Content-Length value, Config incomplete, Server is DOWN, Creating callout connection failed, No memory to generate callout request packets, No memory to create callout task, No memory to create callout async, Callout request expression undef, No callout response expression, Skipped callout response eval, Callout response pixl init undef, Callout response expression undef.
		"""
		try :
			return self._undefreason
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(contentinspectioncallout_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.contentinspectioncallout
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
		addresource = contentinspectioncallout()
		addresource.name = resource.name
		addresource.type = resource.type
		addresource.profilename = resource.profilename
		addresource.servername = resource.servername
		addresource.serverip = resource.serverip
		addresource.serverport = resource.serverport
		addresource.returntype = resource.returntype
		addresource.resultexpr = resource.resultexpr
		addresource.comment = resource.comment
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add contentinspectioncallout.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ contentinspectioncallout() for _ in range(len(resource))]
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
		deleteresource = contentinspectioncallout()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete contentinspectioncallout.
		"""
		try :
			if type(resource) is not list :
				deleteresource = contentinspectioncallout()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ contentinspectioncallout() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ contentinspectioncallout() for _ in range(len(resource))]
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
		updateresource = contentinspectioncallout()
		updateresource.name = resource.name
		updateresource.servername = resource.servername
		updateresource.serverip = resource.serverip
		updateresource.serverport = resource.serverport
		updateresource.profilename = resource.profilename
		updateresource.returntype = resource.returntype
		updateresource.resultexpr = resource.resultexpr
		updateresource.comment = resource.comment
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update contentinspectioncallout.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ contentinspectioncallout() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of contentinspectioncallout resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = contentinspectioncallout()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ contentinspectioncallout() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ contentinspectioncallout() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the contentinspectioncallout resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = contentinspectioncallout()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = contentinspectioncallout()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [contentinspectioncallout() for _ in range(len(name))]
						obj = [contentinspectioncallout() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = contentinspectioncallout()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of contentinspectioncallout resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = contentinspectioncallout()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the contentinspectioncallout resources configured on NetScaler.
		"""
		try :
			obj = contentinspectioncallout()
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
		r""" Use this API to count filtered the set of contentinspectioncallout resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = contentinspectioncallout()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Type:
		ICAP = "ICAP"

	class Returntype:
		BOOL = "BOOL"
		NUM = "NUM"
		TEXT = "TEXT"

	class Undefreason:
		Failed_to_add_service = "Failed to add service"
		Vserver_not_found = "Vserver not found"
		Not_a_HTTP_or_SSL_vserver = "Not a HTTP or SSL vserver"
		Generated_callout_request_is_invalid = "Generated callout request is invalid"
		Content_Length_header_not_found_in_callout_request = "Content-Length header not found in callout request"
		Not_enough_space_to_put_Content_Length_value = "Not enough space to put Content-Length value"
		Config_incomplete = "Config incomplete"
		Server_is_DOWN = "Server is DOWN"
		Creating_callout_connection_failed = "Creating callout connection failed"
		No_memory_to_generate_callout_request_packets = "No memory to generate callout request packets"
		No_memory_to_create_callout_task = "No memory to create callout task"
		No_memory_to_create_callout_async = "No memory to create callout async"
		Callout_request_expression_undef = "Callout request expression undef"
		No_callout_response_expression = "No callout response expression"
		Skipped_callout_response_eval = "Skipped callout response eval"
		Callout_response_pixl_init_undef = "Callout response pixl init undef"
		Callout_response_expression_undef = "Callout response expression undef"

class contentinspectioncallout_response(base_response) :
	def __init__(self, length=1) :
		self.contentinspectioncallout = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.contentinspectioncallout = [contentinspectioncallout() for _ in range(length)]

