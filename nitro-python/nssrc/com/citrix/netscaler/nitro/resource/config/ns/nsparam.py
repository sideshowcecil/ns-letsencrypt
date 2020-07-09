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

class nsparam(base_resource) :
	""" Configuration for Citrix ADC parameters resource. """
	def __init__(self) :
		self._httpport = None
		self._maxconn = None
		self._maxreq = None
		self._cip = None
		self._cipheader = None
		self._cookieversion = None
		self._securecookie = None
		self._pmtumin = None
		self._pmtutimeout = None
		self._ftpportrange = None
		self._crportrange = None
		self._timezone = None
		self._grantquotamaxclient = None
		self._exclusivequotamaxclient = None
		self._grantquotaspillover = None
		self._exclusivequotaspillover = None
		self._useproxyport = None
		self._internaluserlogin = None
		self._aftpallowrandomsourceport = None
		self._icaports = None
		self._tcpcip = None
		self._servicepathingressvlan = None
		self._secureicaports = None
		self._mgmthttpport = None
		self._mgmthttpsport = None
		self._proxyprotocol = None
		self._advancedanalyticsstats = None

	@property
	def httpport(self) :
		r"""HTTP ports on the web server. This allows the system to perform connection off-load for any client request that has a destination port matching one of these configured ports.<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._httpport
		except Exception as e:
			raise e

	@httpport.setter
	def httpport(self, httpport) :
		r"""HTTP ports on the web server. This allows the system to perform connection off-load for any client request that has a destination port matching one of these configured ports.<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._httpport = httpport
		except Exception as e:
			raise e

	@property
	def maxconn(self) :
		r"""Maximum number of connections that will be made from the appliance to the web server(s) attached to it. The value entered here is applied globally to all attached servers.<br/>Default value: 0<br/>Maximum length =  4294967294.
		"""
		try :
			return self._maxconn
		except Exception as e:
			raise e

	@maxconn.setter
	def maxconn(self, maxconn) :
		r"""Maximum number of connections that will be made from the appliance to the web server(s) attached to it. The value entered here is applied globally to all attached servers.<br/>Default value: 0<br/>Maximum length =  4294967294
		"""
		try :
			self._maxconn = maxconn
		except Exception as e:
			raise e

	@property
	def maxreq(self) :
		r"""Maximum number of requests that the system can pass on a particular connection between the appliance and a server attached to it. Setting this value to 0 allows an unlimited number of requests to be passed. This value is overridden by the maximum number of requests configured on the individual service.<br/>Maximum length =  65535.
		"""
		try :
			return self._maxreq
		except Exception as e:
			raise e

	@maxreq.setter
	def maxreq(self, maxreq) :
		r"""Maximum number of requests that the system can pass on a particular connection between the appliance and a server attached to it. Setting this value to 0 allows an unlimited number of requests to be passed. This value is overridden by the maximum number of requests configured on the individual service.<br/>Maximum length =  65535
		"""
		try :
			self._maxreq = maxreq
		except Exception as e:
			raise e

	@property
	def cip(self) :
		r"""Enable or disable the insertion of the actual client IP address into the HTTP header request passed from the client to one, some, or all servers attached to the system. The passed address can then be accessed through a minor modification to the server.
		* If the CIP header is specified, it will be used as the client IP header.
		* If the CIP header is not specified, the value that has been set will be used as the client IP header.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cip
		except Exception as e:
			raise e

	@cip.setter
	def cip(self, cip) :
		r"""Enable or disable the insertion of the actual client IP address into the HTTP header request passed from the client to one, some, or all servers attached to the system. The passed address can then be accessed through a minor modification to the server.
		* If the CIP header is specified, it will be used as the client IP header.
		* If the CIP header is not specified, the value that has been set will be used as the client IP header.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cip = cip
		except Exception as e:
			raise e

	@property
	def cipheader(self) :
		r"""Text that will be used as the client IP address header.<br/>Minimum length =  1.
		"""
		try :
			return self._cipheader
		except Exception as e:
			raise e

	@cipheader.setter
	def cipheader(self, cipheader) :
		r"""Text that will be used as the client IP address header.<br/>Minimum length =  1
		"""
		try :
			self._cipheader = cipheader
		except Exception as e:
			raise e

	@property
	def cookieversion(self) :
		r"""Version of the cookie inserted by the system.<br/>Possible values = 0, 1.
		"""
		try :
			return self._cookieversion
		except Exception as e:
			raise e

	@cookieversion.setter
	def cookieversion(self, cookieversion) :
		r"""Version of the cookie inserted by the system.<br/>Possible values = 0, 1
		"""
		try :
			self._cookieversion = cookieversion
		except Exception as e:
			raise e

	@property
	def securecookie(self) :
		r"""Enable or disable secure flag for persistence cookie.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._securecookie
		except Exception as e:
			raise e

	@securecookie.setter
	def securecookie(self, securecookie) :
		r"""Enable or disable secure flag for persistence cookie.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._securecookie = securecookie
		except Exception as e:
			raise e

	@property
	def pmtumin(self) :
		r"""Minimum path MTU value that Citrix ADC will process in the ICMP fragmentation needed message. If the ICMP message contains a value less than this value, then this value is used instead.<br/>Default value: 576<br/>Minimum length =  168<br/>Maximum length =  1500.
		"""
		try :
			return self._pmtumin
		except Exception as e:
			raise e

	@pmtumin.setter
	def pmtumin(self, pmtumin) :
		r"""Minimum path MTU value that Citrix ADC will process in the ICMP fragmentation needed message. If the ICMP message contains a value less than this value, then this value is used instead.<br/>Default value: 576<br/>Minimum length =  168<br/>Maximum length =  1500
		"""
		try :
			self._pmtumin = pmtumin
		except Exception as e:
			raise e

	@property
	def pmtutimeout(self) :
		r"""Interval, in minutes, for flushing the PMTU entries.<br/>Default value: 10<br/>Minimum length =  1<br/>Maximum length =  1440.
		"""
		try :
			return self._pmtutimeout
		except Exception as e:
			raise e

	@pmtutimeout.setter
	def pmtutimeout(self, pmtutimeout) :
		r"""Interval, in minutes, for flushing the PMTU entries.<br/>Default value: 10<br/>Minimum length =  1<br/>Maximum length =  1440
		"""
		try :
			self._pmtutimeout = pmtutimeout
		except Exception as e:
			raise e

	@property
	def ftpportrange(self) :
		r"""Minimum and maximum port (port range) that FTP services are allowed to use.<br/>Minimum length =  1024<br/>Maximum length =  64000.
		"""
		try :
			return self._ftpportrange
		except Exception as e:
			raise e

	@ftpportrange.setter
	def ftpportrange(self, ftpportrange) :
		r"""Minimum and maximum port (port range) that FTP services are allowed to use.<br/>Minimum length =  1024<br/>Maximum length =  64000
		"""
		try :
			self._ftpportrange = ftpportrange
		except Exception as e:
			raise e

	@property
	def crportrange(self) :
		r"""Port range for cache redirection services.<br/>Minimum length =  1<br/>Maximum length =  65535.
		"""
		try :
			return self._crportrange
		except Exception as e:
			raise e

	@crportrange.setter
	def crportrange(self, crportrange) :
		r"""Port range for cache redirection services.<br/>Minimum length =  1<br/>Maximum length =  65535
		"""
		try :
			self._crportrange = crportrange
		except Exception as e:
			raise e

	@property
	def timezone(self) :
		r"""Time zone for the Citrix ADC. Name of the time zone should be specified as argument.<br/>Default value: CoordinatedUniversalTime<br/>Minimum length =  1<br/>Maximum length =  63.
		"""
		try :
			return self._timezone
		except Exception as e:
			raise e

	@timezone.setter
	def timezone(self, timezone) :
		r"""Time zone for the Citrix ADC. Name of the time zone should be specified as argument.<br/>Default value: CoordinatedUniversalTime<br/>Minimum length =  1<br/>Maximum length =  63
		"""
		try :
			self._timezone = timezone
		except Exception as e:
			raise e

	@property
	def grantquotamaxclient(self) :
		r"""Percentage of shared quota to be granted at a time for maxClient.<br/>Default value: 10<br/>Maximum length =  100.
		"""
		try :
			return self._grantquotamaxclient
		except Exception as e:
			raise e

	@grantquotamaxclient.setter
	def grantquotamaxclient(self, grantquotamaxclient) :
		r"""Percentage of shared quota to be granted at a time for maxClient.<br/>Default value: 10<br/>Maximum length =  100
		"""
		try :
			self._grantquotamaxclient = grantquotamaxclient
		except Exception as e:
			raise e

	@property
	def exclusivequotamaxclient(self) :
		r"""Percentage of maxClient to be given to PEs.<br/>Default value: 80<br/>Maximum length =  100.
		"""
		try :
			return self._exclusivequotamaxclient
		except Exception as e:
			raise e

	@exclusivequotamaxclient.setter
	def exclusivequotamaxclient(self, exclusivequotamaxclient) :
		r"""Percentage of maxClient to be given to PEs.<br/>Default value: 80<br/>Maximum length =  100
		"""
		try :
			self._exclusivequotamaxclient = exclusivequotamaxclient
		except Exception as e:
			raise e

	@property
	def grantquotaspillover(self) :
		r"""Percentage of shared quota to be granted at a time for spillover.<br/>Default value: 10<br/>Maximum length =  100.
		"""
		try :
			return self._grantquotaspillover
		except Exception as e:
			raise e

	@grantquotaspillover.setter
	def grantquotaspillover(self, grantquotaspillover) :
		r"""Percentage of shared quota to be granted at a time for spillover.<br/>Default value: 10<br/>Maximum length =  100
		"""
		try :
			self._grantquotaspillover = grantquotaspillover
		except Exception as e:
			raise e

	@property
	def exclusivequotaspillover(self) :
		r"""Percentage of maximum limit to be given to PEs.<br/>Default value: 80<br/>Maximum length =  100.
		"""
		try :
			return self._exclusivequotaspillover
		except Exception as e:
			raise e

	@exclusivequotaspillover.setter
	def exclusivequotaspillover(self, exclusivequotaspillover) :
		r"""Percentage of maximum limit to be given to PEs.<br/>Default value: 80<br/>Maximum length =  100
		"""
		try :
			self._exclusivequotaspillover = exclusivequotaspillover
		except Exception as e:
			raise e

	@property
	def useproxyport(self) :
		r"""Enable/Disable use_proxy_port setting.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._useproxyport
		except Exception as e:
			raise e

	@useproxyport.setter
	def useproxyport(self, useproxyport) :
		r"""Enable/Disable use_proxy_port setting.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._useproxyport = useproxyport
		except Exception as e:
			raise e

	@property
	def internaluserlogin(self) :
		r"""Enables/disables the internal user from logging in to the appliance. Before disabling internal user login, you must have key-based authentication set up on the appliance. The file name for the key pair must be "ns_comm_key".<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._internaluserlogin
		except Exception as e:
			raise e

	@internaluserlogin.setter
	def internaluserlogin(self, internaluserlogin) :
		r"""Enables/disables the internal user from logging in to the appliance. Before disabling internal user login, you must have key-based authentication set up on the appliance. The file name for the key pair must be "ns_comm_key".<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._internaluserlogin = internaluserlogin
		except Exception as e:
			raise e

	@property
	def aftpallowrandomsourceport(self) :
		r"""Allow the FTP server to come from a random source port for active FTP data connections.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._aftpallowrandomsourceport
		except Exception as e:
			raise e

	@aftpallowrandomsourceport.setter
	def aftpallowrandomsourceport(self, aftpallowrandomsourceport) :
		r"""Allow the FTP server to come from a random source port for active FTP data connections.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._aftpallowrandomsourceport = aftpallowrandomsourceport
		except Exception as e:
			raise e

	@property
	def icaports(self) :
		r"""The ICA ports on the Web server. This allows the system to perform connection off-load for any
		client request that has a destination port matching one of these configured ports.<br/>Minimum length =  1.
		"""
		try :
			return self._icaports
		except Exception as e:
			raise e

	@icaports.setter
	def icaports(self, icaports) :
		r"""The ICA ports on the Web server. This allows the system to perform connection off-load for any
		client request that has a destination port matching one of these configured ports.<br/>Minimum length =  1
		"""
		try :
			self._icaports = icaports
		except Exception as e:
			raise e

	@property
	def tcpcip(self) :
		r"""Enable or disable the insertion of the client TCP/IP header in TCP payload passed from the client to one, some, or all servers attached to the system. The passed address can then be accessed through a minor modification to the server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tcpcip
		except Exception as e:
			raise e

	@tcpcip.setter
	def tcpcip(self, tcpcip) :
		r"""Enable or disable the insertion of the client TCP/IP header in TCP payload passed from the client to one, some, or all servers attached to the system. The passed address can then be accessed through a minor modification to the server.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tcpcip = tcpcip
		except Exception as e:
			raise e

	@property
	def servicepathingressvlan(self) :
		r"""VLAN on which the subscriber traffic arrives on the appliance.<br/>Minimum length =  1.
		"""
		try :
			return self._servicepathingressvlan
		except Exception as e:
			raise e

	@servicepathingressvlan.setter
	def servicepathingressvlan(self, servicepathingressvlan) :
		r"""VLAN on which the subscriber traffic arrives on the appliance.<br/>Minimum length =  1
		"""
		try :
			self._servicepathingressvlan = servicepathingressvlan
		except Exception as e:
			raise e

	@property
	def secureicaports(self) :
		r"""The Secure ICA ports on the Web server. This allows the system to perform connection off-load for any
		client request that has a destination port matching one of these configured ports.<br/>Minimum length =  1.
		"""
		try :
			return self._secureicaports
		except Exception as e:
			raise e

	@secureicaports.setter
	def secureicaports(self, secureicaports) :
		r"""The Secure ICA ports on the Web server. This allows the system to perform connection off-load for any
		client request that has a destination port matching one of these configured ports.<br/>Minimum length =  1
		"""
		try :
			self._secureicaports = secureicaports
		except Exception as e:
			raise e

	@property
	def mgmthttpport(self) :
		r"""This allow the configuration of management HTTP port.<br/>Default value: 80<br/>Minimum length =  1<br/>Maximum length =  65534.
		"""
		try :
			return self._mgmthttpport
		except Exception as e:
			raise e

	@mgmthttpport.setter
	def mgmthttpport(self, mgmthttpport) :
		r"""This allow the configuration of management HTTP port.<br/>Default value: 80<br/>Minimum length =  1<br/>Maximum length =  65534
		"""
		try :
			self._mgmthttpport = mgmthttpport
		except Exception as e:
			raise e

	@property
	def mgmthttpsport(self) :
		r"""This allows the configuration of management HTTPS port.<br/>Default value: 443<br/>Minimum length =  1<br/>Maximum length =  65534.
		"""
		try :
			return self._mgmthttpsport
		except Exception as e:
			raise e

	@mgmthttpsport.setter
	def mgmthttpsport(self, mgmthttpsport) :
		r"""This allows the configuration of management HTTPS port.<br/>Default value: 443<br/>Minimum length =  1<br/>Maximum length =  65534
		"""
		try :
			self._mgmthttpsport = mgmthttpsport
		except Exception as e:
			raise e

	@property
	def proxyprotocol(self) :
		r"""Disable/Enable v1 or v2 proxy protocol header for client info insertion.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._proxyprotocol
		except Exception as e:
			raise e

	@proxyprotocol.setter
	def proxyprotocol(self, proxyprotocol) :
		r"""Disable/Enable v1 or v2 proxy protocol header for client info insertion.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._proxyprotocol = proxyprotocol
		except Exception as e:
			raise e

	@property
	def advancedanalyticsstats(self) :
		r"""Disable/Enable advanace analytics stats.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._advancedanalyticsstats
		except Exception as e:
			raise e

	@advancedanalyticsstats.setter
	def advancedanalyticsstats(self, advancedanalyticsstats) :
		r"""Disable/Enable advanace analytics stats.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._advancedanalyticsstats = advancedanalyticsstats
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsparam
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
		updateresource = nsparam()
		updateresource.httpport = resource.httpport
		updateresource.maxconn = resource.maxconn
		updateresource.maxreq = resource.maxreq
		updateresource.cip = resource.cip
		updateresource.cipheader = resource.cipheader
		updateresource.cookieversion = resource.cookieversion
		updateresource.securecookie = resource.securecookie
		updateresource.pmtumin = resource.pmtumin
		updateresource.pmtutimeout = resource.pmtutimeout
		updateresource.ftpportrange = resource.ftpportrange
		updateresource.crportrange = resource.crportrange
		updateresource.timezone = resource.timezone
		updateresource.grantquotamaxclient = resource.grantquotamaxclient
		updateresource.exclusivequotamaxclient = resource.exclusivequotamaxclient
		updateresource.grantquotaspillover = resource.grantquotaspillover
		updateresource.exclusivequotaspillover = resource.exclusivequotaspillover
		updateresource.useproxyport = resource.useproxyport
		updateresource.internaluserlogin = resource.internaluserlogin
		updateresource.aftpallowrandomsourceport = resource.aftpallowrandomsourceport
		updateresource.icaports = resource.icaports
		updateresource.tcpcip = resource.tcpcip
		updateresource.servicepathingressvlan = resource.servicepathingressvlan
		updateresource.secureicaports = resource.secureicaports
		updateresource.mgmthttpport = resource.mgmthttpport
		updateresource.mgmthttpsport = resource.mgmthttpsport
		updateresource.proxyprotocol = resource.proxyprotocol
		updateresource.advancedanalyticsstats = resource.advancedanalyticsstats
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nsparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nsparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nsparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nsparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Proxyprotocol:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Advancedanalyticsstats:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Securecookie:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Tcpcip:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cookieversion:
		_0 = "0"
		_1 = "1"

	class Internaluserlogin:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Useproxyport:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cip:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Aftpallowrandomsourceport:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class nsparam_response(base_response) :
	def __init__(self, length=1) :
		self.nsparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsparam = [nsparam() for _ in range(length)]

