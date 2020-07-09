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

class server(base_resource) :
	""" Configuration for server resource. """
	def __init__(self) :
		self._name = None
		self._ipaddress = None
		self._domain = None
		self._translationip = None
		self._translationmask = None
		self._domainresolveretry = None
		self._state = None
		self._ipv6address = None
		self._comment = None
		self._td = None
		self._querytype = None
		self._domainresolvenow = None
		self._delay = None
		self._graceful = None
		self._Internal = None
		self._newname = None
		self._statechangetimesec = None
		self._tickssincelaststatechange = None
		self._autoscale = None
		self._usip = None
		self._cka = None
		self._tcpb = None
		self._cmp = None
		self._cacheable = None
		self._sc = None
		self._sp = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the server. 
		Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
		Can be changed after the name is created.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the server. 
		Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
		Can be changed after the name is created.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		r"""IPv4 or IPv6 address of the server. If you create an IP address based server, you can specify the name of the server, instead of its IP address, when creating a service. Note: If you do not create a server entry, the server IP address that you enter when you create a service becomes the name of the server.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@ipaddress.setter
	def ipaddress(self, ipaddress) :
		r"""IPv4 or IPv6 address of the server. If you create an IP address based server, you can specify the name of the server, instead of its IP address, when creating a service. Note: If you do not create a server entry, the server IP address that you enter when you create a service becomes the name of the server.
		"""
		try :
			self._ipaddress = ipaddress
		except Exception as e:
			raise e

	@property
	def domain(self) :
		r"""Domain name of the server. For a domain based configuration, you must create the server first.<br/>Minimum length =  1.
		"""
		try :
			return self._domain
		except Exception as e:
			raise e

	@domain.setter
	def domain(self, domain) :
		r"""Domain name of the server. For a domain based configuration, you must create the server first.<br/>Minimum length =  1
		"""
		try :
			self._domain = domain
		except Exception as e:
			raise e

	@property
	def translationip(self) :
		r"""IP address used to transform the server's DNS-resolved IP address.
		"""
		try :
			return self._translationip
		except Exception as e:
			raise e

	@translationip.setter
	def translationip(self, translationip) :
		r"""IP address used to transform the server's DNS-resolved IP address.
		"""
		try :
			self._translationip = translationip
		except Exception as e:
			raise e

	@property
	def translationmask(self) :
		r"""The netmask of the translation ip.
		"""
		try :
			return self._translationmask
		except Exception as e:
			raise e

	@translationmask.setter
	def translationmask(self, translationmask) :
		r"""The netmask of the translation ip.
		"""
		try :
			self._translationmask = translationmask
		except Exception as e:
			raise e

	@property
	def domainresolveretry(self) :
		r"""Time, in seconds, for which the Citrix ADC must wait, after DNS resolution fails, before sending the next DNS query to resolve the domain name.<br/>Default value: 5<br/>Minimum length =  5<br/>Maximum length =  20939.
		"""
		try :
			return self._domainresolveretry
		except Exception as e:
			raise e

	@domainresolveretry.setter
	def domainresolveretry(self, domainresolveretry) :
		r"""Time, in seconds, for which the Citrix ADC must wait, after DNS resolution fails, before sending the next DNS query to resolve the domain name.<br/>Default value: 5<br/>Minimum length =  5<br/>Maximum length =  20939
		"""
		try :
			self._domainresolveretry = domainresolveretry
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Initial state of the server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""Initial state of the server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def ipv6address(self) :
		r"""Support IPv6 addressing mode. If you configure a server with the IPv6 addressing mode, you cannot use the server in the IPv4 addressing mode.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._ipv6address
		except Exception as e:
			raise e

	@ipv6address.setter
	def ipv6address(self, ipv6address) :
		r"""Support IPv6 addressing mode. If you configure a server with the IPv6 addressing mode, you cannot use the server in the IPv4 addressing mode.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._ipv6address = ipv6address
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Any information about the server.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Any information about the server.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def td(self) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def querytype(self) :
		r"""Specify the type of DNS resolution to be done on the configured domain to get the backend services. Valid query types are A, AAAA and SRV with A being the default querytype. The type of DNS resolution done on the domains in SRV records is inherited from ipv6 argument.<br/>Default value: A<br/>Possible values = A, AAAA, SRV.
		"""
		try :
			return self._querytype
		except Exception as e:
			raise e

	@querytype.setter
	def querytype(self, querytype) :
		r"""Specify the type of DNS resolution to be done on the configured domain to get the backend services. Valid query types are A, AAAA and SRV with A being the default querytype. The type of DNS resolution done on the domains in SRV records is inherited from ipv6 argument.<br/>Default value: A<br/>Possible values = A, AAAA, SRV
		"""
		try :
			self._querytype = querytype
		except Exception as e:
			raise e

	@property
	def domainresolvenow(self) :
		r"""Immediately send a DNS query to resolve the server's domain name.
		"""
		try :
			return self._domainresolvenow
		except Exception as e:
			raise e

	@domainresolvenow.setter
	def domainresolvenow(self, domainresolvenow) :
		r"""Immediately send a DNS query to resolve the server's domain name.
		"""
		try :
			self._domainresolvenow = domainresolvenow
		except Exception as e:
			raise e

	@property
	def delay(self) :
		r"""Time, in seconds, after which all the services configured on the server are disabled.
		"""
		try :
			return self._delay
		except Exception as e:
			raise e

	@delay.setter
	def delay(self, delay) :
		r"""Time, in seconds, after which all the services configured on the server are disabled.
		"""
		try :
			self._delay = delay
		except Exception as e:
			raise e

	@property
	def graceful(self) :
		r"""Shut down gracefully, without accepting any new connections, and disabling each service when all of its connections are closed.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._graceful
		except Exception as e:
			raise e

	@graceful.setter
	def graceful(self, graceful) :
		r"""Shut down gracefully, without accepting any new connections, and disabling each service when all of its connections are closed.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._graceful = graceful
		except Exception as e:
			raise e

	@property
	def Internal(self) :
		r"""Display names of the servers that have been created for internal use.
		"""
		try :
			return self._Internal
		except Exception as e:
			raise e

	@Internal.setter
	def Internal(self, Internal) :
		r"""Display names of the servers that have been created for internal use.
		"""
		try :
			self._Internal = Internal
		except Exception as e:
			raise e

	@property
	def newname(self) :
		r"""New name for the server. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		r"""New name for the server. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def statechangetimesec(self) :
		r"""Time when last state change happened. Seconds part.
		"""
		try :
			return self._statechangetimesec
		except Exception as e:
			raise e

	@property
	def tickssincelaststatechange(self) :
		r"""Time in 10 millisecond ticks since the last state change.
		"""
		try :
			return self._tickssincelaststatechange
		except Exception as e:
			raise e

	@property
	def autoscale(self) :
		r"""Auto scale option for a servicegroup.<br/>Default value: DISABLED<br/>Possible values = DISABLED, DNS, POLICY, CLOUD, API.
		"""
		try :
			return self._autoscale
		except Exception as e:
			raise e

	@property
	def usip(self) :
		r"""Use the client's IP address as the source IP address when initiating a connection to the server. When creating a service, if you do not set this parameter, the service inherits the global Use Source IP setting (available in the enable ns mode and disable ns mode CLI commands, or in the System > Settings > Configure modes > Configure Modes dialog box). However, you can override this setting after you create the service.<br/>Possible values = YES, NO.
		"""
		try :
			return self._usip
		except Exception as e:
			raise e

	@property
	def cka(self) :
		r"""Enable client keep-alive for the service group.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cka
		except Exception as e:
			raise e

	@property
	def tcpb(self) :
		r"""Enable TCP buffering for the service group.<br/>Possible values = YES, NO.
		"""
		try :
			return self._tcpb
		except Exception as e:
			raise e

	@property
	def cmp(self) :
		r"""Enable compression for the specified service.<br/>Possible values = YES, NO.
		"""
		try :
			return self._cmp
		except Exception as e:
			raise e

	@property
	def cacheable(self) :
		r"""Use the transparent cache redirection virtual server to forward the request to the cache server.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._cacheable
		except Exception as e:
			raise e

	@property
	def sc(self) :
		r"""State of the SureConnect feature for the service group.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sc
		except Exception as e:
			raise e

	@property
	def sp(self) :
		r"""Enable surge protection for the service group.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sp
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(server_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.server
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
		addresource = server()
		addresource.name = resource.name
		addresource.ipaddress = resource.ipaddress
		addresource.domain = resource.domain
		addresource.translationip = resource.translationip
		addresource.translationmask = resource.translationmask
		addresource.domainresolveretry = resource.domainresolveretry
		addresource.state = resource.state
		addresource.ipv6address = resource.ipv6address
		addresource.comment = resource.comment
		addresource.td = resource.td
		addresource.querytype = resource.querytype
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add server.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ server() for _ in range(len(resource))]
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
		deleteresource = server()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete server.
		"""
		try :
			if type(resource) is not list :
				deleteresource = server()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ server() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ server() for _ in range(len(resource))]
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
		updateresource = server()
		updateresource.name = resource.name
		updateresource.ipaddress = resource.ipaddress
		updateresource.domainresolveretry = resource.domainresolveretry
		updateresource.translationip = resource.translationip
		updateresource.translationmask = resource.translationmask
		updateresource.domainresolvenow = resource.domainresolvenow
		updateresource.comment = resource.comment
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update server.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ server() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of server resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = server()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ server() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ server() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		r""" Use this API to enable server.
		"""
		try :
			if type(resource) is not list :
				enableresource = server()
				if type(resource) !=  type(enableresource):
					enableresource.name = resource
				else :
					enableresource.name = resource.name
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ server() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ server() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].name = resource[i].name
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		r""" Use this API to disable server.
		"""
		try :
			if type(resource) is not list :
				disableresource = server()
				if type(resource) !=  type(disableresource):
					disableresource.name = resource
				else :
					disableresource.name = resource.name
					disableresource.delay = resource.delay
					disableresource.graceful = resource.graceful
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ server() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ server() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].name = resource[i].name
							disableresources[i].delay = resource[i].delay
							disableresources[i].graceful = resource[i].graceful
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_name) :
		r""" Use this API to rename a server resource.
		"""
		try :
			renameresource = server()
			if type(resource) == cls :
				renameresource.name = resource.name
			else :
				renameresource.name = resource
			return renameresource.rename_resource(client,new_name)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the server resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = server()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = server()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [server() for _ in range(len(name))]
						obj = [server() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = server()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the server resources that are configured on netscaler.
	# This uses server_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = server()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of server resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = server()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the server resources configured on NetScaler.
		"""
		try :
			obj = server()
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
		r""" Use this API to count filtered the set of server resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = server()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Sp:
		ON = "ON"
		OFF = "OFF"

	class Sc:
		ON = "ON"
		OFF = "OFF"

	class Ipv6address:
		YES = "YES"
		NO = "NO"

	class Usip:
		YES = "YES"
		NO = "NO"

	class Cacheable:
		YES = "YES"
		NO = "NO"

	class Autoscale:
		DISABLED = "DISABLED"
		DNS = "DNS"
		POLICY = "POLICY"
		CLOUD = "CLOUD"
		API = "API"

	class Tcpb:
		YES = "YES"
		NO = "NO"

	class Cka:
		YES = "YES"
		NO = "NO"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cmp:
		YES = "YES"
		NO = "NO"

	class Graceful:
		YES = "YES"
		NO = "NO"

	class Querytype:
		A = "A"
		AAAA = "AAAA"
		SRV = "SRV"

class server_response(base_response) :
	def __init__(self, length=1) :
		self.server = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.server = [server() for _ in range(length)]

