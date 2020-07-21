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

class nsconfig(base_resource) :
	""" Configuration for system config resource. """
	def __init__(self) :
		self._force = None
		self._level = None
		self._rbaconfig = None
		self._ipaddress = None
		self._netmask = None
		self._nsvlan = None
		self._ifnum = None
		self._tagged = None
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
		self._all = None
		self._config1 = None
		self._config2 = None
		self._outtype = None
		self._template = None
		self._ignoredevicespecific = None
		self._weakpassword = None
		self._config = None
		self._message = None
		self._mappedip = None
		self._range = None
		self._systemtype = None
		self._primaryip = None
		self._primaryip6 = None
		self._flags = None
		self._lastconfigchangedtime = None
		self._lastconfigsavetime = None
		self._currentsytemtime = None
		self._systemtime = None
		self._configchanged = None
		self._response = None

	@property
	def force(self) :
		r"""Configurations will be cleared without prompting for confirmation.
		"""
		try :
			return self._force
		except Exception as e:
			raise e

	@force.setter
	def force(self, force) :
		r"""Configurations will be cleared without prompting for confirmation.
		"""
		try :
			self._force = force
		except Exception as e:
			raise e

	@property
	def level(self) :
		r"""Types of configurations to be cleared.
		* basic: Clears all configurations except the following:
		- NSIP, default route (gateway), MIPs, and SNIPs
		- Network settings (DG, VLAN, RHI and DNS settings)
		- Cluster settings
		- HA node definitions
		- Feature and mode settings
		- nsroot password
		* extended: Clears the same configurations as the 'basic' option. In addition, it clears the feature and mode settings.
		* full: Clears all configurations except NSIP, default route, and interface settings.
		Note: When you clear the configurations through the cluster IP address, by specifying the level as 'full', the cluster is deleted and all cluster nodes become standalone appliances. The 'basic' and 'extended' levels are propagated to the cluster nodes.<br/>Possible values = basic, extended, full.
		"""
		try :
			return self._level
		except Exception as e:
			raise e

	@level.setter
	def level(self, level) :
		r"""Types of configurations to be cleared.
		* basic: Clears all configurations except the following:
		- NSIP, default route (gateway), MIPs, and SNIPs
		- Network settings (DG, VLAN, RHI and DNS settings)
		- Cluster settings
		- HA node definitions
		- Feature and mode settings
		- nsroot password
		* extended: Clears the same configurations as the 'basic' option. In addition, it clears the feature and mode settings.
		* full: Clears all configurations except NSIP, default route, and interface settings.
		Note: When you clear the configurations through the cluster IP address, by specifying the level as 'full', the cluster is deleted and all cluster nodes become standalone appliances. The 'basic' and 'extended' levels are propagated to the cluster nodes.<br/>Possible values = basic, extended, full
		"""
		try :
			self._level = level
		except Exception as e:
			raise e

	@property
	def rbaconfig(self) :
		r"""RBA configurations and TACACS policies bound to system global will not be cleared if RBA is set to NO.This option is applicable only for BASIC level of clear configuration.Default is YES, which will clear rba configurations.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._rbaconfig
		except Exception as e:
			raise e

	@rbaconfig.setter
	def rbaconfig(self, rbaconfig) :
		r"""RBA configurations and TACACS policies bound to system global will not be cleared if RBA is set to NO.This option is applicable only for BASIC level of clear configuration.Default is YES, which will clear rba configurations.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._rbaconfig = rbaconfig
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		r"""IP address of the Citrix ADC. Commonly referred to as NSIP address. This parameter is mandatory to bring up the appliance.<br/>Minimum length =  1.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@ipaddress.setter
	def ipaddress(self, ipaddress) :
		r"""IP address of the Citrix ADC. Commonly referred to as NSIP address. This parameter is mandatory to bring up the appliance.<br/>Minimum length =  1
		"""
		try :
			self._ipaddress = ipaddress
		except Exception as e:
			raise e

	@property
	def netmask(self) :
		r"""Netmask corresponding to the IP address. This parameter is mandatory to bring up the appliance.
		"""
		try :
			return self._netmask
		except Exception as e:
			raise e

	@netmask.setter
	def netmask(self, netmask) :
		r"""Netmask corresponding to the IP address. This parameter is mandatory to bring up the appliance.
		"""
		try :
			self._netmask = netmask
		except Exception as e:
			raise e

	@property
	def nsvlan(self) :
		r"""VLAN (NSVLAN) for the subnet on which the IP address resides.<br/>Minimum length =  2<br/>Maximum length =  4094.
		"""
		try :
			return self._nsvlan
		except Exception as e:
			raise e

	@nsvlan.setter
	def nsvlan(self, nsvlan) :
		r"""VLAN (NSVLAN) for the subnet on which the IP address resides.<br/>Minimum length =  2<br/>Maximum length =  4094
		"""
		try :
			self._nsvlan = nsvlan
		except Exception as e:
			raise e

	@property
	def ifnum(self) :
		r"""Interfaces of the appliances that must be bound to the NSVLAN.<br/>Minimum length =  1.
		"""
		try :
			return self._ifnum
		except Exception as e:
			raise e

	@ifnum.setter
	def ifnum(self, ifnum) :
		r"""Interfaces of the appliances that must be bound to the NSVLAN.<br/>Minimum length =  1
		"""
		try :
			self._ifnum = ifnum
		except Exception as e:
			raise e

	@property
	def tagged(self) :
		r"""Specifies that the interfaces will be added as 802.1q tagged interfaces. Packets sent on these interface on this VLAN will have an additional 4-byte 802.1q tag which identifies the VLAN.
		To use 802.1q tagging, the switch connected to the appliance's interfaces must also be configured for tagging.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._tagged
		except Exception as e:
			raise e

	@tagged.setter
	def tagged(self, tagged) :
		r"""Specifies that the interfaces will be added as 802.1q tagged interfaces. Packets sent on these interface on this VLAN will have an additional 4-byte 802.1q tag which identifies the VLAN.
		To use 802.1q tagging, the switch connected to the appliance's interfaces must also be configured for tagging.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._tagged = tagged
		except Exception as e:
			raise e

	@property
	def httpport(self) :
		r"""The HTTP ports on the Web server. This allows the system to perform connection off-load for any client request that has a destination port matching one of these configured ports.<br/>Minimum length =  1.
		"""
		try :
			return self._httpport
		except Exception as e:
			raise e

	@httpport.setter
	def httpport(self, httpport) :
		r"""The HTTP ports on the Web server. This allows the system to perform connection off-load for any client request that has a destination port matching one of these configured ports.<br/>Minimum length =  1
		"""
		try :
			self._httpport = httpport
		except Exception as e:
			raise e

	@property
	def maxconn(self) :
		r"""The maximum number of connections that will be made from the system to the web server(s) attached to it. The value entered here is applied globally to all attached servers.<br/>Maximum length =  4294967294.
		"""
		try :
			return self._maxconn
		except Exception as e:
			raise e

	@maxconn.setter
	def maxconn(self, maxconn) :
		r"""The maximum number of connections that will be made from the system to the web server(s) attached to it. The value entered here is applied globally to all attached servers.<br/>Maximum length =  4294967294
		"""
		try :
			self._maxconn = maxconn
		except Exception as e:
			raise e

	@property
	def maxreq(self) :
		r"""The maximum number of requests that the system can pass on a particular connection between the system and a server attached to it. Setting this value to 0 allows an unlimited number of requests to be passed.<br/>Maximum length =  65535.
		"""
		try :
			return self._maxreq
		except Exception as e:
			raise e

	@maxreq.setter
	def maxreq(self, maxreq) :
		r"""The maximum number of requests that the system can pass on a particular connection between the system and a server attached to it. Setting this value to 0 allows an unlimited number of requests to be passed.<br/>Maximum length =  65535
		"""
		try :
			self._maxreq = maxreq
		except Exception as e:
			raise e

	@property
	def cip(self) :
		r"""The option to control (enable or disable) the insertion of the actual client IP address into the HTTP header request passed from the client to one, some, or all servers attached to the system.
		The passed address can then be accessed through a minor modification to the server.
		l    If cipHeader is specified, it will be used as the client IP header.
		l    If it is not specified, then the value that has been set by the set ns config CLI command will be used as the client IP header.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cip
		except Exception as e:
			raise e

	@cip.setter
	def cip(self, cip) :
		r"""The option to control (enable or disable) the insertion of the actual client IP address into the HTTP header request passed from the client to one, some, or all servers attached to the system.
		The passed address can then be accessed through a minor modification to the server.
		l    If cipHeader is specified, it will be used as the client IP header.
		l    If it is not specified, then the value that has been set by the set ns config CLI command will be used as the client IP header.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cip = cip
		except Exception as e:
			raise e

	@property
	def cipheader(self) :
		r"""The text that will be used as the client IP header.<br/>Minimum length =  1.
		"""
		try :
			return self._cipheader
		except Exception as e:
			raise e

	@cipheader.setter
	def cipheader(self, cipheader) :
		r"""The text that will be used as the client IP header.<br/>Minimum length =  1
		"""
		try :
			self._cipheader = cipheader
		except Exception as e:
			raise e

	@property
	def cookieversion(self) :
		r"""The version of the cookie inserted by system.<br/>Possible values = 0, 1.
		"""
		try :
			return self._cookieversion
		except Exception as e:
			raise e

	@cookieversion.setter
	def cookieversion(self, cookieversion) :
		r"""The version of the cookie inserted by system.<br/>Possible values = 0, 1
		"""
		try :
			self._cookieversion = cookieversion
		except Exception as e:
			raise e

	@property
	def securecookie(self) :
		r"""enable/disable secure flag for persistence cookie.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._securecookie
		except Exception as e:
			raise e

	@securecookie.setter
	def securecookie(self, securecookie) :
		r"""enable/disable secure flag for persistence cookie.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._securecookie = securecookie
		except Exception as e:
			raise e

	@property
	def pmtumin(self) :
		r"""The minimum Path MTU.<br/>Default value: 576<br/>Minimum length =  168<br/>Maximum length =  1500.
		"""
		try :
			return self._pmtumin
		except Exception as e:
			raise e

	@pmtumin.setter
	def pmtumin(self, pmtumin) :
		r"""The minimum Path MTU.<br/>Default value: 576<br/>Minimum length =  168<br/>Maximum length =  1500
		"""
		try :
			self._pmtumin = pmtumin
		except Exception as e:
			raise e

	@property
	def pmtutimeout(self) :
		r"""The timeout value in minutes.<br/>Default value: 10<br/>Minimum length =  1<br/>Maximum length =  1440.
		"""
		try :
			return self._pmtutimeout
		except Exception as e:
			raise e

	@pmtutimeout.setter
	def pmtutimeout(self, pmtutimeout) :
		r"""The timeout value in minutes.<br/>Default value: 10<br/>Minimum length =  1<br/>Maximum length =  1440
		"""
		try :
			self._pmtutimeout = pmtutimeout
		except Exception as e:
			raise e

	@property
	def ftpportrange(self) :
		r"""Port range configured for FTP services.<br/>Minimum length =  1024<br/>Maximum length =  64000.
		"""
		try :
			return self._ftpportrange
		except Exception as e:
			raise e

	@ftpportrange.setter
	def ftpportrange(self, ftpportrange) :
		r"""Port range configured for FTP services.<br/>Minimum length =  1024<br/>Maximum length =  64000
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
		r"""Name of the timezone.<br/>Default value: CoordinatedUniversalTime<br/>Minimum length =  1<br/>Maximum length =  64.
		"""
		try :
			return self._timezone
		except Exception as e:
			raise e

	@timezone.setter
	def timezone(self, timezone) :
		r"""Name of the timezone.<br/>Default value: CoordinatedUniversalTime<br/>Minimum length =  1<br/>Maximum length =  64
		"""
		try :
			self._timezone = timezone
		except Exception as e:
			raise e

	@property
	def grantquotamaxclient(self) :
		r"""The percentage of shared quota to be granted at a time for maxClient.<br/>Default value: 10<br/>Maximum length =  100.
		"""
		try :
			return self._grantquotamaxclient
		except Exception as e:
			raise e

	@grantquotamaxclient.setter
	def grantquotamaxclient(self, grantquotamaxclient) :
		r"""The percentage of shared quota to be granted at a time for maxClient.<br/>Default value: 10<br/>Maximum length =  100
		"""
		try :
			self._grantquotamaxclient = grantquotamaxclient
		except Exception as e:
			raise e

	@property
	def exclusivequotamaxclient(self) :
		r"""The percentage of maxClient to be given to PEs.<br/>Default value: 80<br/>Maximum length =  100.
		"""
		try :
			return self._exclusivequotamaxclient
		except Exception as e:
			raise e

	@exclusivequotamaxclient.setter
	def exclusivequotamaxclient(self, exclusivequotamaxclient) :
		r"""The percentage of maxClient to be given to PEs.<br/>Default value: 80<br/>Maximum length =  100
		"""
		try :
			self._exclusivequotamaxclient = exclusivequotamaxclient
		except Exception as e:
			raise e

	@property
	def grantquotaspillover(self) :
		r"""The percentage of shared quota to be granted at a time for spillover.<br/>Default value: 10<br/>Maximum length =  100.
		"""
		try :
			return self._grantquotaspillover
		except Exception as e:
			raise e

	@grantquotaspillover.setter
	def grantquotaspillover(self, grantquotaspillover) :
		r"""The percentage of shared quota to be granted at a time for spillover.<br/>Default value: 10<br/>Maximum length =  100
		"""
		try :
			self._grantquotaspillover = grantquotaspillover
		except Exception as e:
			raise e

	@property
	def exclusivequotaspillover(self) :
		r"""The percentage of max limit to be given to PEs.<br/>Default value: 80<br/>Maximum length =  100.
		"""
		try :
			return self._exclusivequotaspillover
		except Exception as e:
			raise e

	@exclusivequotaspillover.setter
	def exclusivequotaspillover(self, exclusivequotaspillover) :
		r"""The percentage of max limit to be given to PEs.<br/>Default value: 80<br/>Maximum length =  100
		"""
		try :
			self._exclusivequotaspillover = exclusivequotaspillover
		except Exception as e:
			raise e

	@property
	def all(self) :
		r"""Use this option to do saveconfig for all partitions.
		"""
		try :
			return self._all
		except Exception as e:
			raise e

	@all.setter
	def all(self, all) :
		r"""Use this option to do saveconfig for all partitions.
		"""
		try :
			self._all = all
		except Exception as e:
			raise e

	@property
	def config1(self) :
		r"""Location of the configurations.
		"""
		try :
			return self._config1
		except Exception as e:
			raise e

	@config1.setter
	def config1(self, config1) :
		r"""Location of the configurations.
		"""
		try :
			self._config1 = config1
		except Exception as e:
			raise e

	@property
	def config2(self) :
		r"""Location of the configurations.
		"""
		try :
			return self._config2
		except Exception as e:
			raise e

	@config2.setter
	def config2(self, config2) :
		r"""Location of the configurations.
		"""
		try :
			self._config2 = config2
		except Exception as e:
			raise e

	@property
	def outtype(self) :
		r"""Format to display the difference in configurations.<br/>Possible values = cli, xml.
		"""
		try :
			return self._outtype
		except Exception as e:
			raise e

	@outtype.setter
	def outtype(self, outtype) :
		r"""Format to display the difference in configurations.<br/>Possible values = cli, xml
		"""
		try :
			self._outtype = outtype
		except Exception as e:
			raise e

	@property
	def template(self) :
		r"""File that contains the commands to be compared.
		"""
		try :
			return self._template
		except Exception as e:
			raise e

	@template.setter
	def template(self, template) :
		r"""File that contains the commands to be compared.
		"""
		try :
			self._template = template
		except Exception as e:
			raise e

	@property
	def ignoredevicespecific(self) :
		r"""Suppress device specific differences.
		"""
		try :
			return self._ignoredevicespecific
		except Exception as e:
			raise e

	@ignoredevicespecific.setter
	def ignoredevicespecific(self, ignoredevicespecific) :
		r"""Suppress device specific differences.
		"""
		try :
			self._ignoredevicespecific = ignoredevicespecific
		except Exception as e:
			raise e

	@property
	def weakpassword(self) :
		r"""Option to list all weak passwords (not adhering to strong password requirements). Takes config file as input, if no input specified, running configuration is considered. Command => query ns config -weakpassword  / query ns config -weakpassword /nsconfig/ns.conf.
		"""
		try :
			return self._weakpassword
		except Exception as e:
			raise e

	@weakpassword.setter
	def weakpassword(self, weakpassword) :
		r"""Option to list all weak passwords (not adhering to strong password requirements). Takes config file as input, if no input specified, running configuration is considered. Command => query ns config -weakpassword  / query ns config -weakpassword /nsconfig/ns.conf.
		"""
		try :
			self._weakpassword = weakpassword
		except Exception as e:
			raise e

	@property
	def config(self) :
		r"""configuration File to be used to find weak passwords, if not specified, running config is taken as input.
		"""
		try :
			return self._config
		except Exception as e:
			raise e

	@config.setter
	def config(self, config) :
		r"""configuration File to be used to find weak passwords, if not specified, running config is taken as input.
		"""
		try :
			self._config = config
		except Exception as e:
			raise e

	@property
	def message(self) :
		try :
			return self._message
		except Exception as e:
			raise e

	@property
	def mappedip(self) :
		r"""Mapped IP Address of the System.<br/>Minimum length =  1.
		"""
		try :
			return self._mappedip
		except Exception as e:
			raise e

	@property
	def range(self) :
		r"""The range of Mapped IP addresses to be configured.<br/>Minimum value =  1.
		"""
		try :
			return self._range
		except Exception as e:
			raise e

	@property
	def systemtype(self) :
		r"""The type of the System. Possible Values: Standalone, HA, Cluster.<br/>Possible values = Stand-alone, HA, Cluster.
		"""
		try :
			return self._systemtype
		except Exception as e:
			raise e

	@property
	def primaryip(self) :
		r"""HA Master Node IP address.
		"""
		try :
			return self._primaryip
		except Exception as e:
			raise e

	@property
	def primaryip6(self) :
		try :
			return self._primaryip6
		except Exception as e:
			raise e

	@property
	def flags(self) :
		r"""The flags for this entry.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@property
	def lastconfigchangedtime(self) :
		r"""Time when the configuration was last modified.
		"""
		try :
			return self._lastconfigchangedtime
		except Exception as e:
			raise e

	@property
	def lastconfigsavetime(self) :
		r"""Time when the configuration was last saved through savensconfig.
		"""
		try :
			return self._lastconfigsavetime
		except Exception as e:
			raise e

	@property
	def currentsytemtime(self) :
		r"""current system time in date format.
		"""
		try :
			return self._currentsytemtime
		except Exception as e:
			raise e

	@property
	def systemtime(self) :
		r"""current system time.
		"""
		try :
			return self._systemtime
		except Exception as e:
			raise e

	@property
	def configchanged(self) :
		r"""returns True if configuration has changed since last saved config.
		"""
		try :
			return self._configchanged
		except Exception as e:
			raise e

	@property
	def response(self) :
		try :
			return self._response
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsconfig_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsconfig
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
	def clear(cls, client, resource) :
		r""" Use this API to clear nsconfig.
		"""
		try :
			if type(resource) is not list :
				clearresource = nsconfig()
				clearresource.force = resource.force
				clearresource.level = resource.level
				clearresource.rbaconfig = resource.rbaconfig
				return clearresource.perform_operation(client,"clear")
		except Exception as e :
			raise e

	@classmethod
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = nsconfig()
		updateresource.ipaddress = resource.ipaddress
		updateresource.netmask = resource.netmask
		updateresource.nsvlan = resource.nsvlan
		updateresource.ifnum = resource.ifnum
		updateresource.tagged = resource.tagged
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
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nsconfig.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nsconfig resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nsconfig()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def save(cls, client, resource) :
		r""" Use this API to save nsconfig.
		"""
		try :
			if type(resource) is not list :
				saveresource = nsconfig()
				saveresource.all = resource.all
				return saveresource.perform_operation(client,"save")
		except Exception as e :
			raise e

	@classmethod
	def diff(cls, client, resource) :
		r""" Use this API to diff nsconfig.
		"""
		try :
			if type(resource) is not list :
				diffresource = nsconfig()
				diffresource.config1 = resource.config1
				diffresource.config2 = resource.config2
				diffresource.outtype = resource.outtype
				diffresource.template = resource.template
				diffresource.ignoredevicespecific = resource.ignoredevicespecific
				return diffresource.perform_operationEx(client,"diff")
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nsconfig resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsconfig()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Outtype:
		cli = "cli"
		xml = "xml"

	class Cip:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Tagged:
		YES = "YES"
		NO = "NO"

	class Rbaconfig:
		YES = "YES"
		NO = "NO"

	class Systemtype:
		Stand_alone = "Stand-alone"
		HA = "HA"
		Cluster = "Cluster"

	class Securecookie:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cookieversion:
		_0 = "0"
		_1 = "1"

	class Level:
		basic = "basic"
		extended = "extended"
		full = "full"

class nsconfig_response(base_response) :
	def __init__(self, length=1) :
		self.nsconfig = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsconfig = [nsconfig() for _ in range(length)]

