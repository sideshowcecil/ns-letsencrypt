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

class gslbservicegroup(base_resource) :
	""" Configuration for GSLB service group resource. """
	def __init__(self) :
		self._servicegroupname = None
		self._servicetype = None
		self._maxclient = None
		self._cip = None
		self._cipheader = None
		self._healthmonitor = None
		self._clttimeout = None
		self._svrtimeout = None
		self._maxbandwidth = None
		self._monthreshold = None
		self._state = None
		self._downstateflush = None
		self._comment = None
		self._appflowlog = None
		self._autoscale = None
		self._sitename = None
		self._sitepersistence = None
		self._servername = None
		self._port = None
		self._weight = None
		self._hashid = None
		self._publicip = None
		self._publicport = None
		self._siteprefix = None
		self._monitor_name_svc = None
		self._dup_weight = None
		self._delay = None
		self._graceful = None
		self._includemembers = None
		self._newname = None
		self._numofconnections = None
		self._serviceconftype = None
		self._value = None
		self._svrstate = None
		self._ip = None
		self._monstatcode = None
		self._monstatparam1 = None
		self._monstatparam2 = None
		self._monstatparam3 = None
		self._statechangetimemsec = None
		self._stateupdatereason = None
		self._clmonowner = None
		self._clmonview = None
		self._groupcount = None
		self._serviceipstr = None
		self._servicegroupeffectivestate = None
		self._gslb = None
		self._svreffgslbstate = None
		self._nodefaultbindings = None
		self.___count = None

	@property
	def servicegroupname(self) :
		r"""Name of the GSLB service group. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the name is created.<br/>Minimum length =  1.
		"""
		try :
			return self._servicegroupname
		except Exception as e:
			raise e

	@servicegroupname.setter
	def servicegroupname(self, servicegroupname) :
		r"""Name of the GSLB service group. Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the name is created.<br/>Minimum length =  1
		"""
		try :
			self._servicegroupname = servicegroupname
		except Exception as e:
			raise e

	@property
	def servicetype(self) :
		r"""Protocol used to exchange data with the GSLB service.<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, NNTP, ANY, SIP_UDP, SIP_TCP, SIP_SSL, RADIUS, RDP, RTSP, MYSQL, MSSQL, ORACLE.
		"""
		try :
			return self._servicetype
		except Exception as e:
			raise e

	@servicetype.setter
	def servicetype(self, servicetype) :
		r"""Protocol used to exchange data with the GSLB service.<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, NNTP, ANY, SIP_UDP, SIP_TCP, SIP_SSL, RADIUS, RDP, RTSP, MYSQL, MSSQL, ORACLE
		"""
		try :
			self._servicetype = servicetype
		except Exception as e:
			raise e

	@property
	def maxclient(self) :
		r"""Maximum number of simultaneous open connections for the GSLB service group.<br/>Maximum length =  4294967294.
		"""
		try :
			return self._maxclient
		except Exception as e:
			raise e

	@maxclient.setter
	def maxclient(self, maxclient) :
		r"""Maximum number of simultaneous open connections for the GSLB service group.<br/>Maximum length =  4294967294
		"""
		try :
			self._maxclient = maxclient
		except Exception as e:
			raise e

	@property
	def cip(self) :
		r"""Insert the Client IP header in requests forwarded to the GSLB service.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cip
		except Exception as e:
			raise e

	@cip.setter
	def cip(self, cip) :
		r"""Insert the Client IP header in requests forwarded to the GSLB service.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cip = cip
		except Exception as e:
			raise e

	@property
	def cipheader(self) :
		r"""Name of the HTTP header whose value must be set to the IP address of the client. Used with the Client IP parameter. If client IP insertion is enabled, and the client IP header is not specified, the value of Client IP Header parameter or the value set by the set ns config command is used as client's IP header name.<br/>Minimum length =  1.
		"""
		try :
			return self._cipheader
		except Exception as e:
			raise e

	@cipheader.setter
	def cipheader(self, cipheader) :
		r"""Name of the HTTP header whose value must be set to the IP address of the client. Used with the Client IP parameter. If client IP insertion is enabled, and the client IP header is not specified, the value of Client IP Header parameter or the value set by the set ns config command is used as client's IP header name.<br/>Minimum length =  1
		"""
		try :
			self._cipheader = cipheader
		except Exception as e:
			raise e

	@property
	def healthmonitor(self) :
		r"""Monitor the health of this GSLB service.Available settings function are as follows:
		YES - Send probes to check the health of the GSLB service.
		NO - Do not send probes to check the health of the GSLB service. With the NO option, the appliance shows the service as UP at all times.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._healthmonitor
		except Exception as e:
			raise e

	@healthmonitor.setter
	def healthmonitor(self, healthmonitor) :
		r"""Monitor the health of this GSLB service.Available settings function are as follows:
		YES - Send probes to check the health of the GSLB service.
		NO - Do not send probes to check the health of the GSLB service. With the NO option, the appliance shows the service as UP at all times.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._healthmonitor = healthmonitor
		except Exception as e:
			raise e

	@property
	def clttimeout(self) :
		r"""Time, in seconds, after which to terminate an idle client connection.<br/>Maximum length =  31536000.
		"""
		try :
			return self._clttimeout
		except Exception as e:
			raise e

	@clttimeout.setter
	def clttimeout(self, clttimeout) :
		r"""Time, in seconds, after which to terminate an idle client connection.<br/>Maximum length =  31536000
		"""
		try :
			self._clttimeout = clttimeout
		except Exception as e:
			raise e

	@property
	def svrtimeout(self) :
		r"""Time, in seconds, after which to terminate an idle server connection.<br/>Maximum length =  31536000.
		"""
		try :
			return self._svrtimeout
		except Exception as e:
			raise e

	@svrtimeout.setter
	def svrtimeout(self, svrtimeout) :
		r"""Time, in seconds, after which to terminate an idle server connection.<br/>Maximum length =  31536000
		"""
		try :
			self._svrtimeout = svrtimeout
		except Exception as e:
			raise e

	@property
	def maxbandwidth(self) :
		r"""Maximum bandwidth, in Kbps, allocated for all the services in the GSLB service group.<br/>Maximum length =  4294967287.
		"""
		try :
			return self._maxbandwidth
		except Exception as e:
			raise e

	@maxbandwidth.setter
	def maxbandwidth(self, maxbandwidth) :
		r"""Maximum bandwidth, in Kbps, allocated for all the services in the GSLB service group.<br/>Maximum length =  4294967287
		"""
		try :
			self._maxbandwidth = maxbandwidth
		except Exception as e:
			raise e

	@property
	def monthreshold(self) :
		r"""Minimum sum of weights of the monitors that are bound to this GSLB service. Used to determine whether to mark a GSLB service as UP or DOWN.<br/>Maximum length =  65535.
		"""
		try :
			return self._monthreshold
		except Exception as e:
			raise e

	@monthreshold.setter
	def monthreshold(self, monthreshold) :
		r"""Minimum sum of weights of the monitors that are bound to this GSLB service. Used to determine whether to mark a GSLB service as UP or DOWN.<br/>Maximum length =  65535
		"""
		try :
			self._monthreshold = monthreshold
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Initial state of the GSLB service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""Initial state of the GSLB service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def downstateflush(self) :
		r"""Flush all active transactions associated with all the services in the GSLB service group whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._downstateflush
		except Exception as e:
			raise e

	@downstateflush.setter
	def downstateflush(self, downstateflush) :
		r"""Flush all active transactions associated with all the services in the GSLB service group whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._downstateflush = downstateflush
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Any information about the GSLB service group.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Any information about the GSLB service group.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def appflowlog(self) :
		r"""Enable logging of AppFlow information for the specified GSLB service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._appflowlog
		except Exception as e:
			raise e

	@appflowlog.setter
	def appflowlog(self, appflowlog) :
		r"""Enable logging of AppFlow information for the specified GSLB service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._appflowlog = appflowlog
		except Exception as e:
			raise e

	@property
	def autoscale(self) :
		r"""Auto scale option for a GSLB servicegroup.<br/>Default value: DISABLED<br/>Possible values = DISABLED, DNS.
		"""
		try :
			return self._autoscale
		except Exception as e:
			raise e

	@autoscale.setter
	def autoscale(self, autoscale) :
		r"""Auto scale option for a GSLB servicegroup.<br/>Default value: DISABLED<br/>Possible values = DISABLED, DNS
		"""
		try :
			self._autoscale = autoscale
		except Exception as e:
			raise e

	@property
	def sitename(self) :
		r"""Name of the GSLB site to which the service group belongs.<br/>Minimum length =  1.
		"""
		try :
			return self._sitename
		except Exception as e:
			raise e

	@sitename.setter
	def sitename(self, sitename) :
		r"""Name of the GSLB site to which the service group belongs.<br/>Minimum length =  1
		"""
		try :
			self._sitename = sitename
		except Exception as e:
			raise e

	@property
	def sitepersistence(self) :
		r"""Use cookie-based site persistence. Applicable only to HTTP and SSL non-autoscale enabled GSLB servicegroups.<br/>Possible values = ConnectionProxy, HTTPRedirect, NONE.
		"""
		try :
			return self._sitepersistence
		except Exception as e:
			raise e

	@sitepersistence.setter
	def sitepersistence(self, sitepersistence) :
		r"""Use cookie-based site persistence. Applicable only to HTTP and SSL non-autoscale enabled GSLB servicegroups.<br/>Possible values = ConnectionProxy, HTTPRedirect, NONE
		"""
		try :
			self._sitepersistence = sitepersistence
		except Exception as e:
			raise e

	@property
	def servername(self) :
		r"""Name of the server to which to bind the service group.<br/>Minimum length =  1.
		"""
		try :
			return self._servername
		except Exception as e:
			raise e

	@servername.setter
	def servername(self, servername) :
		r"""Name of the server to which to bind the service group.<br/>Minimum length =  1
		"""
		try :
			self._servername = servername
		except Exception as e:
			raise e

	@property
	def port(self) :
		r"""Server port number.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		r"""Server port number.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	@property
	def weight(self) :
		r"""Weight to assign to the servers in the service group. Specifies the capacity of the servers relative to the other servers in the load balancing configuration. The higher the weight, the higher the percentage of requests sent to the service.<br/>Minimum length =  1<br/>Maximum length =  100.
		"""
		try :
			return self._weight
		except Exception as e:
			raise e

	@weight.setter
	def weight(self, weight) :
		r"""Weight to assign to the servers in the service group. Specifies the capacity of the servers relative to the other servers in the load balancing configuration. The higher the weight, the higher the percentage of requests sent to the service.<br/>Minimum length =  1<br/>Maximum length =  100
		"""
		try :
			self._weight = weight
		except Exception as e:
			raise e

	@property
	def hashid(self) :
		r"""The hash identifier for the service. This must be unique for each service. This parameter is used by hash based load balancing methods.<br/>Minimum length =  1.
		"""
		try :
			return self._hashid
		except Exception as e:
			raise e

	@hashid.setter
	def hashid(self, hashid) :
		r"""The hash identifier for the service. This must be unique for each service. This parameter is used by hash based load balancing methods.<br/>Minimum length =  1
		"""
		try :
			self._hashid = hashid
		except Exception as e:
			raise e

	@property
	def publicip(self) :
		r"""The public IP address that a NAT device translates to the GSLB service's private IP address. Optional.<br/>Minimum length =  1.
		"""
		try :
			return self._publicip
		except Exception as e:
			raise e

	@publicip.setter
	def publicip(self, publicip) :
		r"""The public IP address that a NAT device translates to the GSLB service's private IP address. Optional.<br/>Minimum length =  1
		"""
		try :
			self._publicip = publicip
		except Exception as e:
			raise e

	@property
	def publicport(self) :
		r"""The public port associated with the GSLB service's public IP address. The port is mapped to the service's private port number. Applicable to the local GSLB service. Optional.<br/>Minimum length =  1.
		"""
		try :
			return self._publicport
		except Exception as e:
			raise e

	@publicport.setter
	def publicport(self, publicport) :
		r"""The public port associated with the GSLB service's public IP address. The port is mapped to the service's private port number. Applicable to the local GSLB service. Optional.<br/>Minimum length =  1
		"""
		try :
			self._publicport = publicport
		except Exception as e:
			raise e

	@property
	def siteprefix(self) :
		r"""The site's prefix string. When the GSLB service group is bound to a GSLB virtual server, a GSLB site domain is generated internally for each bound serviceitem-domain pair by concatenating the site prefix of the service item and the name of the domain. If the special string NONE is specified, the site-prefix string is unset. When implementing HTTP redirect site persistence, the Citrix ADC redirects GSLB requests to GSLB services by using their site domains.
		"""
		try :
			return self._siteprefix
		except Exception as e:
			raise e

	@siteprefix.setter
	def siteprefix(self, siteprefix) :
		r"""The site's prefix string. When the GSLB service group is bound to a GSLB virtual server, a GSLB site domain is generated internally for each bound serviceitem-domain pair by concatenating the site prefix of the service item and the name of the domain. If the special string NONE is specified, the site-prefix string is unset. When implementing HTTP redirect site persistence, the Citrix ADC redirects GSLB requests to GSLB services by using their site domains.
		"""
		try :
			self._siteprefix = siteprefix
		except Exception as e:
			raise e

	@property
	def monitor_name_svc(self) :
		r"""Name of the monitor bound to the GSLB service group. Used to assign a weight to the monitor.<br/>Minimum length =  1.
		"""
		try :
			return self._monitor_name_svc
		except Exception as e:
			raise e

	@monitor_name_svc.setter
	def monitor_name_svc(self, monitor_name_svc) :
		r"""Name of the monitor bound to the GSLB service group. Used to assign a weight to the monitor.<br/>Minimum length =  1
		"""
		try :
			self._monitor_name_svc = monitor_name_svc
		except Exception as e:
			raise e

	@property
	def dup_weight(self) :
		r"""weight of the monitor that is bound to GSLB servicegroup.<br/>Minimum length =  1.
		"""
		try :
			return self._dup_weight
		except Exception as e:
			raise e

	@dup_weight.setter
	def dup_weight(self, dup_weight) :
		r"""weight of the monitor that is bound to GSLB servicegroup.<br/>Minimum length =  1
		"""
		try :
			self._dup_weight = dup_weight
		except Exception as e:
			raise e

	@property
	def delay(self) :
		r"""The time allowed (in seconds) for a graceful shutdown. During this period, new connections or requests will continue to be sent to this service for clients who already have a persistent session on the system. Connections or requests from fresh or new clients who do not yet have a persistence sessions on the system will not be sent to the service. Instead, they will be load balanced among other available services. After the delay time expires, no new requests or connections will be sent to the service.
		"""
		try :
			return self._delay
		except Exception as e:
			raise e

	@delay.setter
	def delay(self, delay) :
		r"""The time allowed (in seconds) for a graceful shutdown. During this period, new connections or requests will continue to be sent to this service for clients who already have a persistent session on the system. Connections or requests from fresh or new clients who do not yet have a persistence sessions on the system will not be sent to the service. Instead, they will be load balanced among other available services. After the delay time expires, no new requests or connections will be sent to the service.
		"""
		try :
			self._delay = delay
		except Exception as e:
			raise e

	@property
	def graceful(self) :
		r"""Wait for all existing connections to the service to terminate before shutting down the service.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._graceful
		except Exception as e:
			raise e

	@graceful.setter
	def graceful(self, graceful) :
		r"""Wait for all existing connections to the service to terminate before shutting down the service.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._graceful = graceful
		except Exception as e:
			raise e

	@property
	def includemembers(self) :
		r"""Display the members of the listed GSLB service groups in addition to their settings. Can be specified when no service group name is provided in the command. In that case, the details displayed for each service group are identical to the details displayed when a service group name is provided, except that bound monitors are not displayed.
		"""
		try :
			return self._includemembers
		except Exception as e:
			raise e

	@includemembers.setter
	def includemembers(self, includemembers) :
		r"""Display the members of the listed GSLB service groups in addition to their settings. Can be specified when no service group name is provided in the command. In that case, the details displayed for each service group are identical to the details displayed when a service group name is provided, except that bound monitors are not displayed.
		"""
		try :
			self._includemembers = includemembers
		except Exception as e:
			raise e

	@property
	def newname(self) :
		r"""New name for the GSLB service group.<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		r"""New name for the GSLB service group.<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	@property
	def numofconnections(self) :
		r"""This will tell the number of client side connections are still open.
		"""
		try :
			return self._numofconnections
		except Exception as e:
			raise e

	@property
	def serviceconftype(self) :
		r"""The configuration type of the GSLB service group.
		"""
		try :
			return self._serviceconftype
		except Exception as e:
			raise e

	@property
	def value(self) :
		r"""SSL Status.<br/>Possible values = Certkey not bound, SSL feature disabled.
		"""
		try :
			return self._value
		except Exception as e:
			raise e

	@property
	def svrstate(self) :
		r"""The state of the GSLB service.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._svrstate
		except Exception as e:
			raise e

	@property
	def ip(self) :
		r"""IP Address.
		"""
		try :
			return self._ip
		except Exception as e:
			raise e

	@property
	def monstatcode(self) :
		r"""The code indicating the monitor response.
		"""
		try :
			return self._monstatcode
		except Exception as e:
			raise e

	@property
	def monstatparam1(self) :
		r"""First parameter for use with message code.
		"""
		try :
			return self._monstatparam1
		except Exception as e:
			raise e

	@property
	def monstatparam2(self) :
		r"""Second parameter for use with message code.
		"""
		try :
			return self._monstatparam2
		except Exception as e:
			raise e

	@property
	def monstatparam3(self) :
		r"""Third parameter for use with message code.
		"""
		try :
			return self._monstatparam3
		except Exception as e:
			raise e

	@property
	def statechangetimemsec(self) :
		r"""Time when last state change occurred. Milliseconds part.
		"""
		try :
			return self._statechangetimemsec
		except Exception as e:
			raise e

	@property
	def stateupdatereason(self) :
		r"""Checks state update reason on the secondary node.
		"""
		try :
			return self._stateupdatereason
		except Exception as e:
			raise e

	@property
	def clmonowner(self) :
		r"""Tells the mon owner of the service.
		"""
		try :
			return self._clmonowner
		except Exception as e:
			raise e

	@property
	def clmonview(self) :
		r"""Tells the view id of the monitoring owner.
		"""
		try :
			return self._clmonview
		except Exception as e:
			raise e

	@property
	def groupcount(self) :
		r"""Servicegroup Count.
		"""
		try :
			return self._groupcount
		except Exception as e:
			raise e

	@property
	def serviceipstr(self) :
		r"""This field has been intorduced to show the dbs services ip.
		"""
		try :
			return self._serviceipstr
		except Exception as e:
			raise e

	@property
	def servicegroupeffectivestate(self) :
		r"""Indicates the effective GSLB servicegroup state based on the state of the bound service items.If all services are UP the effective state is UP, if all are DOWN its DOWN,if all are OFS its OFS.If atleast one serviceis UP and rest are either DOWN or OFS, the effective state is PARTIAL-UP.If atleast one bound service is DOWN and rest are OFS the effective state is PARTIAL DOWN.<br/>Possible values = UP, DOWN, OUT OF SERVICE, PARTIAL-UP, PARTIAL-DOWN.
		"""
		try :
			return self._servicegroupeffectivestate
		except Exception as e:
			raise e

	@property
	def gslb(self) :
		r""".<br/>Default value: GSLB<br/>Possible values = REMOTE, LOCAL.
		"""
		try :
			return self._gslb
		except Exception as e:
			raise e

	@property
	def svreffgslbstate(self) :
		r"""Effective state of the gslb svc.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._svreffgslbstate
		except Exception as e:
			raise e

	@property
	def nodefaultbindings(self) :
		r"""to determine if the configuration is from stylebooks.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._nodefaultbindings
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(gslbservicegroup_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.gslbservicegroup
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.servicegroupname is not None :
				return str(self.servicegroupname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = gslbservicegroup()
		addresource.servicegroupname = resource.servicegroupname
		addresource.servicetype = resource.servicetype
		addresource.maxclient = resource.maxclient
		addresource.cip = resource.cip
		addresource.cipheader = resource.cipheader
		addresource.healthmonitor = resource.healthmonitor
		addresource.clttimeout = resource.clttimeout
		addresource.svrtimeout = resource.svrtimeout
		addresource.maxbandwidth = resource.maxbandwidth
		addresource.monthreshold = resource.monthreshold
		addresource.state = resource.state
		addresource.downstateflush = resource.downstateflush
		addresource.comment = resource.comment
		addresource.appflowlog = resource.appflowlog
		addresource.autoscale = resource.autoscale
		addresource.sitename = resource.sitename
		addresource.sitepersistence = resource.sitepersistence
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add gslbservicegroup.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ gslbservicegroup() for _ in range(len(resource))]
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
		deleteresource = gslbservicegroup()
		deleteresource.servicegroupname = resource.servicegroupname
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete gslbservicegroup.
		"""
		try :
			if type(resource) is not list :
				deleteresource = gslbservicegroup()
				if type(resource) !=  type(deleteresource):
					deleteresource.servicegroupname = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ gslbservicegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].servicegroupname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ gslbservicegroup() for _ in range(len(resource))]
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
		updateresource = gslbservicegroup()
		updateresource.servicegroupname = resource.servicegroupname
		updateresource.servername = resource.servername
		updateresource.port = resource.port
		updateresource.weight = resource.weight
		updateresource.hashid = resource.hashid
		updateresource.publicip = resource.publicip
		updateresource.publicport = resource.publicport
		updateresource.siteprefix = resource.siteprefix
		updateresource.monitor_name_svc = resource.monitor_name_svc
		updateresource.dup_weight = resource.dup_weight
		updateresource.maxclient = resource.maxclient
		updateresource.healthmonitor = resource.healthmonitor
		updateresource.cip = resource.cip
		updateresource.cipheader = resource.cipheader
		updateresource.clttimeout = resource.clttimeout
		updateresource.svrtimeout = resource.svrtimeout
		updateresource.maxbandwidth = resource.maxbandwidth
		updateresource.monthreshold = resource.monthreshold
		updateresource.downstateflush = resource.downstateflush
		updateresource.comment = resource.comment
		updateresource.appflowlog = resource.appflowlog
		updateresource.sitepersistence = resource.sitepersistence
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update gslbservicegroup.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ gslbservicegroup() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of gslbservicegroup resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = gslbservicegroup()
				if type(resource) !=  type(unsetresource):
					unsetresource.servicegroupname = resource
				else :
					unsetresource.servicegroupname = resource.servicegroupname
					unsetresource.servername = resource.servername
					unsetresource.port = resource.port
					unsetresource.weight = resource.weight
					unsetresource.hashid = resource.hashid
					unsetresource.publicip = resource.publicip
					unsetresource.publicport = resource.publicport
					unsetresource.siteprefix = resource.siteprefix
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ gslbservicegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].servicegroupname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ gslbservicegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].servicegroupname = resource[i].servicegroupname
							unsetresources[i].servername = resource[i].servername
							unsetresources[i].port = resource[i].port
							unsetresources[i].weight = resource[i].weight
							unsetresources[i].hashid = resource[i].hashid
							unsetresources[i].publicip = resource[i].publicip
							unsetresources[i].publicport = resource[i].publicport
							unsetresources[i].siteprefix = resource[i].siteprefix
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		r""" Use this API to enable gslbservicegroup.
		"""
		try :
			if type(resource) is not list :
				enableresource = gslbservicegroup()
				if type(resource) !=  type(enableresource):
					enableresource.servicegroupname = resource
				else :
					enableresource.servicegroupname = resource.servicegroupname
					enableresource.servername = resource.servername
					enableresource.port = resource.port
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ gslbservicegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].servicegroupname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ gslbservicegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].servicegroupname = resource[i].servicegroupname
							enableresources[i].servername = resource[i].servername
							enableresources[i].port = resource[i].port
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		r""" Use this API to disable gslbservicegroup.
		"""
		try :
			if type(resource) is not list :
				disableresource = gslbservicegroup()
				if type(resource) !=  type(disableresource):
					disableresource.servicegroupname = resource
				else :
					disableresource.servicegroupname = resource.servicegroupname
					disableresource.servername = resource.servername
					disableresource.port = resource.port
					disableresource.delay = resource.delay
					disableresource.graceful = resource.graceful
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ gslbservicegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].servicegroupname = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ gslbservicegroup() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].servicegroupname = resource[i].servicegroupname
							disableresources[i].servername = resource[i].servername
							disableresources[i].port = resource[i].port
							disableresources[i].delay = resource[i].delay
							disableresources[i].graceful = resource[i].graceful
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_servicegroupname) :
		r""" Use this API to rename a gslbservicegroup resource.
		"""
		try :
			renameresource = gslbservicegroup()
			if type(resource) == cls :
				renameresource.servicegroupname = resource.servicegroupname
			else :
				renameresource.servicegroupname = resource
			return renameresource.rename_resource(client,new_servicegroupname)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the gslbservicegroup resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = gslbservicegroup()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = gslbservicegroup()
					obj.servicegroupname = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [gslbservicegroup() for _ in range(len(name))]
						obj = [gslbservicegroup() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = gslbservicegroup()
							obj[i].servicegroupname = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the gslbservicegroup resources that are configured on netscaler.
	# This uses gslbservicegroup_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = gslbservicegroup()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of gslbservicegroup resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbservicegroup()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the gslbservicegroup resources configured on NetScaler.
		"""
		try :
			obj = gslbservicegroup()
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
		r""" Use this API to count filtered the set of gslbservicegroup resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = gslbservicegroup()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Downstateflush:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Servicetype:
		HTTP = "HTTP"
		FTP = "FTP"
		TCP = "TCP"
		UDP = "UDP"
		SSL = "SSL"
		SSL_BRIDGE = "SSL_BRIDGE"
		SSL_TCP = "SSL_TCP"
		NNTP = "NNTP"
		ANY = "ANY"
		SIP_UDP = "SIP_UDP"
		SIP_TCP = "SIP_TCP"
		SIP_SSL = "SIP_SSL"
		RADIUS = "RADIUS"
		RDP = "RDP"
		RTSP = "RTSP"
		MYSQL = "MYSQL"
		MSSQL = "MSSQL"
		ORACLE = "ORACLE"

	class Autoscale:
		DISABLED = "DISABLED"
		DNS = "DNS"

	class Sitepersistence:
		ConnectionProxy = "ConnectionProxy"
		HTTPRedirect = "HTTPRedirect"
		NONE = "NONE"

	class Healthmonitor:
		YES = "YES"
		NO = "NO"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Nodefaultbindings:
		YES = "YES"
		NO = "NO"

	class Svrstate:
		UP = "UP"
		DOWN = "DOWN"
		UNKNOWN = "UNKNOWN"
		BUSY = "BUSY"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
		DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
		NS_EMPTY_STR = "NS_EMPTY_STR"
		Unknown = "Unknown"
		DISABLED = "DISABLED"

	class Value:
		Certkey_not_bound = "Certkey not bound"
		SSL_feature_disabled = "SSL feature disabled"

	class Gslb:
		REMOTE = "REMOTE"
		LOCAL = "LOCAL"

	class Svreffgslbstate:
		UP = "UP"
		DOWN = "DOWN"
		UNKNOWN = "UNKNOWN"
		BUSY = "BUSY"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
		DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
		NS_EMPTY_STR = "NS_EMPTY_STR"
		Unknown = "Unknown"
		DISABLED = "DISABLED"

	class Servicegroupeffectivestate:
		UP = "UP"
		DOWN = "DOWN"
		OUT_OF_SERVICE = "OUT OF SERVICE"
		PARTIAL_UP = "PARTIAL-UP"
		PARTIAL_DOWN = "PARTIAL-DOWN"

	class Cip:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Appflowlog:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Graceful:
		YES = "YES"
		NO = "NO"

class gslbservicegroup_response(base_response) :
	def __init__(self, length=1) :
		self.gslbservicegroup = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.gslbservicegroup = [gslbservicegroup() for _ in range(length)]

