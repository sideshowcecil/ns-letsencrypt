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

class contentinspectionaction(base_resource) :
	""" Configuration for Content Inspection action resource. """
	def __init__(self) :
		self._name = None
		self._type = None
		self._servername = None
		self._serverip = None
		self._serverport = None
		self._icapprofilename = None
		self._ifserverdown = None
		self._reqtimeout = None
		self._reqtimeoutaction = None
		self._hits = None
		self._referencecount = None
		self._undefhits = None
		self._builtin = None
		self._feature = None
		self.___count = None

	@property
	def name(self) :
		r"""Name of the remote service action. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the remote service action. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""Type of operation this action is going to perform. following actions are available to configure:
		* ICAP - forward the incoming request or response to an ICAP server for modification.
		* INLINEINSPECTION - forward the incoming or outgoing packets to IPS server for Intrusion Prevention.
		* MIRROR - Forwards cloned packets for Intrusion Detection.
		* NOINSPECTION - This does not forward incoming and outgoing packets to the Inspection device.
		* NSTRACE - capture current and further incoming packets on this transaction.<br/>Possible values = ICAP, INLINEINSPECTION, MIRROR, NOINSPECTION.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Type of operation this action is going to perform. following actions are available to configure:
		* ICAP - forward the incoming request or response to an ICAP server for modification.
		* INLINEINSPECTION - forward the incoming or outgoing packets to IPS server for Intrusion Prevention.
		* MIRROR - Forwards cloned packets for Intrusion Detection.
		* NOINSPECTION - This does not forward incoming and outgoing packets to the Inspection device.
		* NSTRACE - capture current and further incoming packets on this transaction.<br/>Possible values = ICAP, INLINEINSPECTION, MIRROR, NOINSPECTION
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def servername(self) :
		r"""Name of the LB vserver or service.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._servername
		except Exception as e:
			raise e

	@servername.setter
	def servername(self, servername) :
		r"""Name of the LB vserver or service.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._servername = servername
		except Exception as e:
			raise e

	@property
	def serverip(self) :
		r"""IP address of remoteService.<br/>Minimum length =  1.
		"""
		try :
			return self._serverip
		except Exception as e:
			raise e

	@serverip.setter
	def serverip(self, serverip) :
		r"""IP address of remoteService.<br/>Minimum length =  1
		"""
		try :
			self._serverip = serverip
		except Exception as e:
			raise e

	@property
	def serverport(self) :
		r"""Port of remoteService.<br/>Default value: 1344<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._serverport
		except Exception as e:
			raise e

	@serverport.setter
	def serverport(self, serverport) :
		r"""Port of remoteService.<br/>Default value: 1344<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._serverport = serverport
		except Exception as e:
			raise e

	@property
	def icapprofilename(self) :
		r"""Name of the ICAP profile to be attached to the contentInspection action.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._icapprofilename
		except Exception as e:
			raise e

	@icapprofilename.setter
	def icapprofilename(self, icapprofilename) :
		r"""Name of the ICAP profile to be attached to the contentInspection action.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._icapprofilename = icapprofilename
		except Exception as e:
			raise e

	@property
	def ifserverdown(self) :
		r"""Name of the action to perform if the Vserver representing the remote service is not UP. This is not supported for NOINSPECTION Type. The Supported actions are:
		* RESET - Reset the client connection by closing it. The client program, such as a browser, will handle this and may inform the user. The client may then resend the request if desired.
		* DROP - Drop the request without sending a response to the user.
		* CONTINUE - It bypasses the ContentIsnpection and Continues/resumes the Traffic-Flow to Client/Server.<br/>Default value: RESET<br/>Possible values = CONTINUE, DROP, RESET.
		"""
		try :
			return self._ifserverdown
		except Exception as e:
			raise e

	@ifserverdown.setter
	def ifserverdown(self, ifserverdown) :
		r"""Name of the action to perform if the Vserver representing the remote service is not UP. This is not supported for NOINSPECTION Type. The Supported actions are:
		* RESET - Reset the client connection by closing it. The client program, such as a browser, will handle this and may inform the user. The client may then resend the request if desired.
		* DROP - Drop the request without sending a response to the user.
		* CONTINUE - It bypasses the ContentIsnpection and Continues/resumes the Traffic-Flow to Client/Server.<br/>Default value: RESET<br/>Possible values = CONTINUE, DROP, RESET
		"""
		try :
			self._ifserverdown = ifserverdown
		except Exception as e:
			raise e

	@property
	def reqtimeout(self) :
		r"""Time, in seconds, within which the remote service request must complete. This is not supported for NOINSPECTION action type. If the request does not complete within this time, the specified request timeout action is executed. Zero disables the timeout.<br/>Default value: 0<br/>Minimum value =  0<br/>Maximum value =  86400.
		"""
		try :
			return self._reqtimeout
		except Exception as e:
			raise e

	@property
	def reqtimeoutaction(self) :
		r"""Name of the action to perform if the Vserver representing the remote service does not respond. This is not supported for NOINSPECTION action type. There are also some built-in actions which can be used. These are:
		* RESET - Reset the client connection by closing it. The client program, such as a browser, will handle this and may inform the user. The client may then resend the request if desired.
		* DROP - Drop the request without sending a response to the user.<br/>Default value: BYPASS<br/>Possible values = BYPASS, DROP, RESET.
		"""
		try :
			return self._reqtimeoutaction
		except Exception as e:
			raise e

	@property
	def hits(self) :
		r"""The number of times the action has been taken.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def referencecount(self) :
		r"""The number of references to the action.
		"""
		try :
			return self._referencecount
		except Exception as e:
			raise e

	@property
	def undefhits(self) :
		r"""The number of times the action resulted in UNDEF.
		"""
		try :
			return self._undefhits
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r"""Flag to determine whether contentinspection action is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	@property
	def feature(self) :
		r"""The feature to be checked while applying this config.
		"""
		try :
			return self._feature
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(contentinspectionaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.contentinspectionaction
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
		addresource = contentinspectionaction()
		addresource.name = resource.name
		addresource.type = resource.type
		addresource.servername = resource.servername
		addresource.serverip = resource.serverip
		addresource.serverport = resource.serverport
		addresource.icapprofilename = resource.icapprofilename
		addresource.ifserverdown = resource.ifserverdown
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add contentinspectionaction.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ contentinspectionaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i] = cls.filter_add_parameters(resource[i])
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = contentinspectionaction()
		updateresource.name = resource.name
		updateresource.servername = resource.servername
		updateresource.serverip = resource.serverip
		updateresource.serverport = resource.serverport
		updateresource.icapprofilename = resource.icapprofilename
		updateresource.ifserverdown = resource.ifserverdown
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update contentinspectionaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ contentinspectionaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of contentinspectionaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = contentinspectionaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ contentinspectionaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ contentinspectionaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = contentinspectionaction()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete contentinspectionaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = contentinspectionaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ contentinspectionaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ contentinspectionaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i] = cls.filter_delete_parameters(resource)
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the contentinspectionaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = contentinspectionaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = contentinspectionaction()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [contentinspectionaction() for _ in range(len(name))]
						obj = [contentinspectionaction() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = contentinspectionaction()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of contentinspectionaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = contentinspectionaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the contentinspectionaction resources configured on NetScaler.
		"""
		try :
			obj = contentinspectionaction()
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
		r""" Use this API to count filtered the set of contentinspectionaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = contentinspectionaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Feature:
		WL = "WL"
		WebLogging = "WebLogging"
		SP = "SP"
		SurgeProtection = "SurgeProtection"
		LB = "LB"
		LoadBalancing = "LoadBalancing"
		CS = "CS"
		ContentSwitching = "ContentSwitching"
		CR = "CR"
		CacheRedirection = "CacheRedirection"
		SC = "SC"
		SureConnect = "SureConnect"
		CMP = "CMP"
		CMPcntl = "CMPcntl"
		CompressionControl = "CompressionControl"
		PQ = "PQ"
		PriorityQueuing = "PriorityQueuing"
		HDOSP = "HDOSP"
		HttpDoSProtection = "HttpDoSProtection"
		SSLVPN = "SSLVPN"
		AAA = "AAA"
		GSLB = "GSLB"
		GlobalServerLoadBalancing = "GlobalServerLoadBalancing"
		SSL = "SSL"
		SSLOffload = "SSLOffload"
		SSLOffloading = "SSLOffloading"
		CF = "CF"
		ContentFiltering = "ContentFiltering"
		IC = "IC"
		IntegratedCaching = "IntegratedCaching"
		OSPF = "OSPF"
		OSPFRouting = "OSPFRouting"
		RIP = "RIP"
		RIPRouting = "RIPRouting"
		BGP = "BGP"
		BGPRouting = "BGPRouting"
		REWRITE = "REWRITE"
		IPv6PT = "IPv6PT"
		IPv6protocoltranslation = "IPv6protocoltranslation"
		AppFw = "AppFw"
		ApplicationFirewall = "ApplicationFirewall"
		RESPONDER = "RESPONDER"
		HTMLInjection = "HTMLInjection"
		push = "push"
		NSPush = "NSPush"
		NetScalerPush = "NetScalerPush"
		AppFlow = "AppFlow"
		CloudBridge = "CloudBridge"
		ISIS = "ISIS"
		ISISRouting = "ISISRouting"
		CH = "CH"
		CallHome = "CallHome"
		AppQoE = "AppQoE"
		ContentAccelerator = "ContentAccelerator"
		SYSTEM = "SYSTEM"
		RISE = "RISE"
		FEO = "FEO"
		LSN = "LSN"
		LargeScaleNAT = "LargeScaleNAT"
		RDPProxy = "RDPProxy"
		Rep = "Rep"
		Reputation = "Reputation"
		URLFiltering = "URLFiltering"
		VideoOptimization = "VideoOptimization"
		ForwardProxy = "ForwardProxy"
		SSLInterception = "SSLInterception"
		AdaptiveTCP = "AdaptiveTCP"
		CQA = "CQA"
		CI = "CI"
		ContentInspection = "ContentInspection"
		Bot = "Bot"

	class Reqtimeoutaction:
		BYPASS = "BYPASS"
		DROP = "DROP"
		RESET = "RESET"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

	class Type:
		ICAP = "ICAP"
		INLINEINSPECTION = "INLINEINSPECTION"
		MIRROR = "MIRROR"
		NOINSPECTION = "NOINSPECTION"

	class Ifserverdown:
		CONTINUE = "CONTINUE"
		DROP = "DROP"
		RESET = "RESET"

class contentinspectionaction_response(base_response) :
	def __init__(self, length=1) :
		self.contentinspectionaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.contentinspectionaction = [contentinspectionaction() for _ in range(length)]

