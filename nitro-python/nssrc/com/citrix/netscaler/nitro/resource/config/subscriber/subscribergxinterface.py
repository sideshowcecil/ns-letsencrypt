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

class subscribergxinterface(base_resource) :
	""" Configuration for Gx interface Parameters resource. """
	def __init__(self) :
		self._vserver = None
		self._service = None
		self._pcrfrealm = None
		self._holdonsubscriberabsence = None
		self._requesttimeout = None
		self._requestretryattempts = None
		self._idlettl = None
		self._revalidationtimeout = None
		self._healthcheck = None
		self._healthcheckttl = None
		self._cerrequesttimeout = None
		self._negativettl = None
		self._negativettllimitedsuccess = None
		self._purgesdbongxfailure = None
		self._servicepathavp = None
		self._servicepathvendorid = None
		self._nodeid = None
		self._svrstate = None
		self._identity = None
		self._realm = None
		self._status = None
		self._servicepathinfomode = None
		self._gxreportingavp1 = None
		self._gxreportingavp1vendorid = None
		self._gxreportingavp1type = None
		self._gxreportingavp2 = None
		self._gxreportingavp2vendorid = None
		self._gxreportingavp2type = None
		self._gxreportingavp3 = None
		self._gxreportingavp3vendorid = None
		self._gxreportingavp3type = None
		self._gxreportingavp4 = None
		self._gxreportingavp4vendorid = None
		self._gxreportingavp4type = None
		self._gxreportingavp5 = None
		self._gxreportingavp5vendorid = None
		self._gxreportingavp5type = None

	@property
	def vserver(self) :
		r"""Name of the load balancing, or content switching vserver to which the Gx connections are established. The service type of the virtual server must be DIAMETER/SSL_DIAMETER. Mutually exclusive with the service parameter. Therefore, you cannot set both service and the Virtual Server in the Gx Interface.<br/>Minimum length =  1.
		"""
		try :
			return self._vserver
		except Exception as e:
			raise e

	@vserver.setter
	def vserver(self, vserver) :
		r"""Name of the load balancing, or content switching vserver to which the Gx connections are established. The service type of the virtual server must be DIAMETER/SSL_DIAMETER. Mutually exclusive with the service parameter. Therefore, you cannot set both service and the Virtual Server in the Gx Interface.<br/>Minimum length =  1
		"""
		try :
			self._vserver = vserver
		except Exception as e:
			raise e

	@property
	def service(self) :
		r"""Name of DIAMETER/SSL_DIAMETER service corresponding to PCRF to which the Gx connection is established. The service type of the service must be DIAMETER/SSL_DIAMETER. Mutually exclusive with vserver parameter. Therefore, you cannot set both Service and the Virtual Server in the Gx Interface.<br/>Minimum length =  1.
		"""
		try :
			return self._service
		except Exception as e:
			raise e

	@service.setter
	def service(self, service) :
		r"""Name of DIAMETER/SSL_DIAMETER service corresponding to PCRF to which the Gx connection is established. The service type of the service must be DIAMETER/SSL_DIAMETER. Mutually exclusive with vserver parameter. Therefore, you cannot set both Service and the Virtual Server in the Gx Interface.<br/>Minimum length =  1
		"""
		try :
			self._service = service
		except Exception as e:
			raise e

	@property
	def pcrfrealm(self) :
		r"""PCRF realm is of type DiameterIdentity and contains the realm of PCRF to which the message is to be routed. This is the realm used in Destination-Realm AVP by Citrix ADC Gx client (as a Diameter node).
		<br/>Minimum length =  1.
		"""
		try :
			return self._pcrfrealm
		except Exception as e:
			raise e

	@pcrfrealm.setter
	def pcrfrealm(self, pcrfrealm) :
		r"""PCRF realm is of type DiameterIdentity and contains the realm of PCRF to which the message is to be routed. This is the realm used in Destination-Realm AVP by Citrix ADC Gx client (as a Diameter node).
		<br/>Minimum length =  1
		"""
		try :
			self._pcrfrealm = pcrfrealm
		except Exception as e:
			raise e

	@property
	def holdonsubscriberabsence(self) :
		r"""Set this setting to yes if Citrix ADC needs to Hold pakcets till subscriber session is fetched from PCRF. Else set to NO. By default set to yes. If this setting is set to NO, then till Citrix ADC fetches subscriber from PCRF, default subscriber profile will be applied to this subscriber if configured. If default subscriber profile is also not configured an undef would be raised to expressions which use Subscriber attributes. .<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._holdonsubscriberabsence
		except Exception as e:
			raise e

	@holdonsubscriberabsence.setter
	def holdonsubscriberabsence(self, holdonsubscriberabsence) :
		r"""Set this setting to yes if Citrix ADC needs to Hold pakcets till subscriber session is fetched from PCRF. Else set to NO. By default set to yes. If this setting is set to NO, then till Citrix ADC fetches subscriber from PCRF, default subscriber profile will be applied to this subscriber if configured. If default subscriber profile is also not configured an undef would be raised to expressions which use Subscriber attributes. .<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._holdonsubscriberabsence = holdonsubscriberabsence
		except Exception as e:
			raise e

	@property
	def requesttimeout(self) :
		r"""q!Time, in seconds, within which the Gx CCR request must complete. If the request does not complete within this time, the request is retransmitted for requestRetryAttempts time. If still reuqest is not complete then default subscriber profile will be applied to this subscriber if configured. If default subscriber profile is also not configured an undef would be raised to expressions which use Subscriber attributes.
		Zero disables the timeout. !.<br/>Default value: 10<br/>Maximum length =  86400.
		"""
		try :
			return self._requesttimeout
		except Exception as e:
			raise e

	@requesttimeout.setter
	def requesttimeout(self, requesttimeout) :
		r"""q!Time, in seconds, within which the Gx CCR request must complete. If the request does not complete within this time, the request is retransmitted for requestRetryAttempts time. If still reuqest is not complete then default subscriber profile will be applied to this subscriber if configured. If default subscriber profile is also not configured an undef would be raised to expressions which use Subscriber attributes.
		Zero disables the timeout. !.<br/>Default value: 10<br/>Maximum length =  86400
		"""
		try :
			self._requesttimeout = requesttimeout
		except Exception as e:
			raise e

	@property
	def requestretryattempts(self) :
		r"""If the request does not complete within requestTimeout time, the request is retransmitted for requestRetryAttempts time.<br/>Default value: 3.
		"""
		try :
			return self._requestretryattempts
		except Exception as e:
			raise e

	@requestretryattempts.setter
	def requestretryattempts(self, requestretryattempts) :
		r"""If the request does not complete within requestTimeout time, the request is retransmitted for requestRetryAttempts time.<br/>Default value: 3
		"""
		try :
			self._requestretryattempts = requestretryattempts
		except Exception as e:
			raise e

	@property
	def idlettl(self) :
		r"""q!Idle Time, in seconds, after which the Gx CCR-U request will be sent after any PCRF activity on a session. Any RAR or CCA message resets the timer.
		Zero value disables the idle timeout. !.<br/>Default value: 900<br/>Maximum length =  86400.
		"""
		try :
			return self._idlettl
		except Exception as e:
			raise e

	@idlettl.setter
	def idlettl(self, idlettl) :
		r"""q!Idle Time, in seconds, after which the Gx CCR-U request will be sent after any PCRF activity on a session. Any RAR or CCA message resets the timer.
		Zero value disables the idle timeout. !.<br/>Default value: 900<br/>Maximum length =  86400
		"""
		try :
			self._idlettl = idlettl
		except Exception as e:
			raise e

	@property
	def revalidationtimeout(self) :
		r"""q!Revalidation Timeout, in seconds, after which the Gx CCR-U request will be sent after any PCRF activity on a session. Any RAR or CCA message resets the timer.
		Zero value disables the idle timeout. !.<br/>Default value: 0<br/>Maximum length =  86400.
		"""
		try :
			return self._revalidationtimeout
		except Exception as e:
			raise e

	@revalidationtimeout.setter
	def revalidationtimeout(self, revalidationtimeout) :
		r"""q!Revalidation Timeout, in seconds, after which the Gx CCR-U request will be sent after any PCRF activity on a session. Any RAR or CCA message resets the timer.
		Zero value disables the idle timeout. !.<br/>Default value: 0<br/>Maximum length =  86400
		"""
		try :
			self._revalidationtimeout = revalidationtimeout
		except Exception as e:
			raise e

	@property
	def healthcheck(self) :
		r"""q!Set this setting to yes if Citrix ADC should send DWR packets to PCRF server. When the session is idle, healthcheck timer expires and DWR packets are initiated in order to check that PCRF server is active. By default set to No. !.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._healthcheck
		except Exception as e:
			raise e

	@healthcheck.setter
	def healthcheck(self, healthcheck) :
		r"""q!Set this setting to yes if Citrix ADC should send DWR packets to PCRF server. When the session is idle, healthcheck timer expires and DWR packets are initiated in order to check that PCRF server is active. By default set to No. !.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._healthcheck = healthcheck
		except Exception as e:
			raise e

	@property
	def healthcheckttl(self) :
		r"""q!Healthcheck timeout, in seconds, after which the DWR will be sent in order to ensure the state of the PCRF server. Any CCR, CCA, RAR or RRA message resets the timer. !.<br/>Default value: 30<br/>Minimum length =  6<br/>Maximum length =  86400.
		"""
		try :
			return self._healthcheckttl
		except Exception as e:
			raise e

	@healthcheckttl.setter
	def healthcheckttl(self, healthcheckttl) :
		r"""q!Healthcheck timeout, in seconds, after which the DWR will be sent in order to ensure the state of the PCRF server. Any CCR, CCA, RAR or RRA message resets the timer. !.<br/>Default value: 30<br/>Minimum length =  6<br/>Maximum length =  86400
		"""
		try :
			self._healthcheckttl = healthcheckttl
		except Exception as e:
			raise e

	@property
	def cerrequesttimeout(self) :
		r"""q!Healthcheck request timeout, in seconds, after which the Citrix ADC considers that no CCA packet received to the initiated CCR. After this time Citrix ADC should send again CCR to PCRF server. !.<br/>Default value: 0<br/>Maximum length =  86400.
		"""
		try :
			return self._cerrequesttimeout
		except Exception as e:
			raise e

	@cerrequesttimeout.setter
	def cerrequesttimeout(self, cerrequesttimeout) :
		r"""q!Healthcheck request timeout, in seconds, after which the Citrix ADC considers that no CCA packet received to the initiated CCR. After this time Citrix ADC should send again CCR to PCRF server. !.<br/>Default value: 0<br/>Maximum length =  86400
		"""
		try :
			self._cerrequesttimeout = cerrequesttimeout
		except Exception as e:
			raise e

	@property
	def negativettl(self) :
		r"""q!Negative TTL, in seconds, after which the Gx CCR-I request will be resent for sessions that have not been resolved by PCRF due to server being down or no response or failed response. Instead of polling the PCRF server constantly, negative-TTL makes Citrix ADC stick to un-resolved session. Meanwhile Citrix ADC installs a negative session to avoid going to PCRF.
		For Negative Sessions, Netcaler inherits the attributes from default subscriber profile if default subscriber is configured. A default subscriber could be configured as 'add subscriber profile *'. Or these attributes can be inherited from Radius as well if Radius is configued.
		Zero value disables the Negative Sessions. And Citrix ADC does not install Negative sessions even if subscriber session could not be fetched. !.<br/>Default value: 600<br/>Maximum length =  86400.
		"""
		try :
			return self._negativettl
		except Exception as e:
			raise e

	@negativettl.setter
	def negativettl(self, negativettl) :
		r"""q!Negative TTL, in seconds, after which the Gx CCR-I request will be resent for sessions that have not been resolved by PCRF due to server being down or no response or failed response. Instead of polling the PCRF server constantly, negative-TTL makes Citrix ADC stick to un-resolved session. Meanwhile Citrix ADC installs a negative session to avoid going to PCRF.
		For Negative Sessions, Netcaler inherits the attributes from default subscriber profile if default subscriber is configured. A default subscriber could be configured as 'add subscriber profile *'. Or these attributes can be inherited from Radius as well if Radius is configued.
		Zero value disables the Negative Sessions. And Citrix ADC does not install Negative sessions even if subscriber session could not be fetched. !.<br/>Default value: 600<br/>Maximum length =  86400
		"""
		try :
			self._negativettl = negativettl
		except Exception as e:
			raise e

	@property
	def negativettllimitedsuccess(self) :
		r"""Set this to YES if Citrix ADC should create negative session for Result-Code DIAMETER_LIMITED_SUCCESS (2002) received in CCA-I. If set to NO, regular session is created.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._negativettllimitedsuccess
		except Exception as e:
			raise e

	@negativettllimitedsuccess.setter
	def negativettllimitedsuccess(self, negativettllimitedsuccess) :
		r"""Set this to YES if Citrix ADC should create negative session for Result-Code DIAMETER_LIMITED_SUCCESS (2002) received in CCA-I. If set to NO, regular session is created.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._negativettllimitedsuccess = negativettllimitedsuccess
		except Exception as e:
			raise e

	@property
	def purgesdbongxfailure(self) :
		r"""Set this setting to YES if needed to purge Subscriber Database in case of Gx failure. By default set to NO. .<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._purgesdbongxfailure
		except Exception as e:
			raise e

	@purgesdbongxfailure.setter
	def purgesdbongxfailure(self, purgesdbongxfailure) :
		r"""Set this setting to YES if needed to purge Subscriber Database in case of Gx failure. By default set to NO. .<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._purgesdbongxfailure = purgesdbongxfailure
		except Exception as e:
			raise e

	@property
	def servicepathavp(self) :
		r""" The AVP code in which PCRF sends service path applicable for subscriber.<br/>Minimum length =  1.
		"""
		try :
			return self._servicepathavp
		except Exception as e:
			raise e

	@servicepathavp.setter
	def servicepathavp(self, servicepathavp) :
		r""" The AVP code in which PCRF sends service path applicable for subscriber.<br/>Minimum length =  1
		"""
		try :
			self._servicepathavp = servicepathavp
		except Exception as e:
			raise e

	@property
	def servicepathvendorid(self) :
		r""" The vendorid of the AVP in which PCRF sends service path for subscriber.
		"""
		try :
			return self._servicepathvendorid
		except Exception as e:
			raise e

	@servicepathvendorid.setter
	def servicepathvendorid(self, servicepathvendorid) :
		r""" The vendorid of the AVP in which PCRF sends service path for subscriber.
		"""
		try :
			self._servicepathvendorid = servicepathvendorid
		except Exception as e:
			raise e

	@property
	def nodeid(self) :
		r"""Unique number that identifies the cluster node.<br/>Maximum length =  31.
		"""
		try :
			return self._nodeid
		except Exception as e:
			raise e

	@nodeid.setter
	def nodeid(self, nodeid) :
		r"""Unique number that identifies the cluster node.<br/>Maximum length =  31
		"""
		try :
			self._nodeid = nodeid
		except Exception as e:
			raise e

	@property
	def svrstate(self) :
		r"""The state of the gx service.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED.
		"""
		try :
			return self._svrstate
		except Exception as e:
			raise e

	@property
	def identity(self) :
		r"""DiameterIdentity to be used by NS. DiameterIdentity is used to identify a Diameter node uniquely. Before setting up diameter configuration, Citrix ADC (as a Diameter node) MUST be assigned a unique DiameterIdentity.
		example =>
		set ns diameter -identity Citrix ADC.com
		Now whenever Citrix ADC system needs to use identity in diameter messages. It will use 'netscaler.com' as Origin-Host AVP as defined in RFC3588
		.<br/>Minimum length =  1.
		"""
		try :
			return self._identity
		except Exception as e:
			raise e

	@property
	def realm(self) :
		r"""Diameter Realm to be used by NS.
		example =>
		set ns diameter -realm com
		Now whenever Citrix ADC system needs to use realm in diameter messages. It will use 'com' as Origin-Realm AVP as defined in RFC3588
		.<br/>Minimum length =  1.
		"""
		try :
			return self._realm
		except Exception as e:
			raise e

	@property
	def status(self) :
		r"""Citrix ADC PCRF connection Status. (Gx Protocol State).
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	@property
	def servicepathinfomode(self) :
		r""" The type of info in which service path is passed from PCRF,
		SERVICE_FUNCTION: Denotes the service chain is passed as servicefunction names in-order in AVPS with code servicepathAVP
		SERVICE_PATH: Denotes the service path name is passed in AVPS with code servicepathAVP.q.<br/>Default value: SERVICEPATH<br/>Possible values = SERVICEFUNCTIONS, SERVICEPATH.
		"""
		try :
			return self._servicepathinfomode
		except Exception as e:
			raise e

	@property
	def gxreportingavp1(self) :
		r""" The AVP code to report as 1st custom AVP.<br/>Minimum value =  1.
		"""
		try :
			return self._gxreportingavp1
		except Exception as e:
			raise e

	@property
	def gxreportingavp1vendorid(self) :
		r""" The vendorid of the AVP which will be reported as 1st custom AVP.
		"""
		try :
			return self._gxreportingavp1vendorid
		except Exception as e:
			raise e

	@property
	def gxreportingavp1type(self) :
		r""" The type of the AVP which will be reported as 1st custom AVP.<br/>Default value: OctetString<br/>Possible values = OctetString, Integer32, Integer64, Unsigned32, Unsigned64, Float32, Float64.
		"""
		try :
			return self._gxreportingavp1type
		except Exception as e:
			raise e

	@property
	def gxreportingavp2(self) :
		r""" The AVP code to report as 2nd custom AVP.<br/>Minimum value =  1.
		"""
		try :
			return self._gxreportingavp2
		except Exception as e:
			raise e

	@property
	def gxreportingavp2vendorid(self) :
		r""" The vendorid of the AVP which will be reported as 2nd custom AVP.
		"""
		try :
			return self._gxreportingavp2vendorid
		except Exception as e:
			raise e

	@property
	def gxreportingavp2type(self) :
		r""" The type of the AVP which will be reported as 2nd custom AVP.<br/>Default value: OctetString<br/>Possible values = OctetString, Integer32, Integer64, Unsigned32, Unsigned64, Float32, Float64.
		"""
		try :
			return self._gxreportingavp2type
		except Exception as e:
			raise e

	@property
	def gxreportingavp3(self) :
		r""" The AVP code to report as 3rd custom AVP.<br/>Minimum value =  1.
		"""
		try :
			return self._gxreportingavp3
		except Exception as e:
			raise e

	@property
	def gxreportingavp3vendorid(self) :
		r""" The vendorid of the AVP which will be reported as 3rd custom AVP.
		"""
		try :
			return self._gxreportingavp3vendorid
		except Exception as e:
			raise e

	@property
	def gxreportingavp3type(self) :
		r""" The type of the AVP which will be reported as 3rd custom AVP.<br/>Default value: OctetString<br/>Possible values = OctetString, Integer32, Integer64, Unsigned32, Unsigned64, Float32, Float64.
		"""
		try :
			return self._gxreportingavp3type
		except Exception as e:
			raise e

	@property
	def gxreportingavp4(self) :
		r""" The AVP code to report as 4th custom AVP.<br/>Minimum value =  1.
		"""
		try :
			return self._gxreportingavp4
		except Exception as e:
			raise e

	@property
	def gxreportingavp4vendorid(self) :
		r""" The vendorid of the AVP which will be reported as 4th custom AVP.
		"""
		try :
			return self._gxreportingavp4vendorid
		except Exception as e:
			raise e

	@property
	def gxreportingavp4type(self) :
		r""" The type of the AVP which will be reported as 4th custom AVP.<br/>Default value: OctetString<br/>Possible values = OctetString, Integer32, Integer64, Unsigned32, Unsigned64, Float32, Float64.
		"""
		try :
			return self._gxreportingavp4type
		except Exception as e:
			raise e

	@property
	def gxreportingavp5(self) :
		r""" The AVP code to report as 5th custom AVP.<br/>Minimum value =  1.
		"""
		try :
			return self._gxreportingavp5
		except Exception as e:
			raise e

	@property
	def gxreportingavp5vendorid(self) :
		r""" The vendorid of the AVP which will be reported as 5th custom AVP.
		"""
		try :
			return self._gxreportingavp5vendorid
		except Exception as e:
			raise e

	@property
	def gxreportingavp5type(self) :
		r""" The type of the AVP which will be reported as 5th custom AVP.<br/>Default value: OctetString<br/>Possible values = OctetString, Integer32, Integer64, Unsigned32, Unsigned64, Float32, Float64.
		"""
		try :
			return self._gxreportingavp5type
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(subscribergxinterface_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.subscribergxinterface
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
		updateresource = subscribergxinterface()
		updateresource.vserver = resource.vserver
		updateresource.service = resource.service
		updateresource.pcrfrealm = resource.pcrfrealm
		updateresource.holdonsubscriberabsence = resource.holdonsubscriberabsence
		updateresource.requesttimeout = resource.requesttimeout
		updateresource.requestretryattempts = resource.requestretryattempts
		updateresource.idlettl = resource.idlettl
		updateresource.revalidationtimeout = resource.revalidationtimeout
		updateresource.healthcheck = resource.healthcheck
		updateresource.healthcheckttl = resource.healthcheckttl
		updateresource.cerrequesttimeout = resource.cerrequesttimeout
		updateresource.negativettl = resource.negativettl
		updateresource.negativettllimitedsuccess = resource.negativettllimitedsuccess
		updateresource.purgesdbongxfailure = resource.purgesdbongxfailure
		updateresource.servicepathavp = resource.servicepathavp
		updateresource.servicepathvendorid = resource.servicepathvendorid
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update subscribergxinterface.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of subscribergxinterface resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = subscribergxinterface()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the subscribergxinterface resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = subscribergxinterface()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the subscribergxinterface resources that are configured on netscaler.
	# This uses subscribergxinterface_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = subscribergxinterface()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Gxreportingavp3type:
		OctetString = "OctetString"
		Integer32 = "Integer32"
		Integer64 = "Integer64"
		Unsigned32 = "Unsigned32"
		Unsigned64 = "Unsigned64"
		Float32 = "Float32"
		Float64 = "Float64"

	class Gxreportingavp4type:
		OctetString = "OctetString"
		Integer32 = "Integer32"
		Integer64 = "Integer64"
		Unsigned32 = "Unsigned32"
		Unsigned64 = "Unsigned64"
		Float32 = "Float32"
		Float64 = "Float64"

	class Gxreportingavp5type:
		OctetString = "OctetString"
		Integer32 = "Integer32"
		Integer64 = "Integer64"
		Unsigned32 = "Unsigned32"
		Unsigned64 = "Unsigned64"
		Float32 = "Float32"
		Float64 = "Float64"

	class Servicepathinfomode:
		SERVICEFUNCTIONS = "SERVICEFUNCTIONS"
		SERVICEPATH = "SERVICEPATH"

	class Negativettllimitedsuccess:
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

	class Gxreportingavp2type:
		OctetString = "OctetString"
		Integer32 = "Integer32"
		Integer64 = "Integer64"
		Unsigned32 = "Unsigned32"
		Unsigned64 = "Unsigned64"
		Float32 = "Float32"
		Float64 = "Float64"

	class Gxreportingavp1type:
		OctetString = "OctetString"
		Integer32 = "Integer32"
		Integer64 = "Integer64"
		Unsigned32 = "Unsigned32"
		Unsigned64 = "Unsigned64"
		Float32 = "Float32"
		Float64 = "Float64"

	class Healthcheck:
		YES = "YES"
		NO = "NO"

	class Holdonsubscriberabsence:
		YES = "YES"
		NO = "NO"

	class Purgesdbongxfailure:
		YES = "YES"
		NO = "NO"

class subscribergxinterface_response(base_response) :
	def __init__(self, length=1) :
		self.subscribergxinterface = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.subscribergxinterface = [subscribergxinterface() for _ in range(length)]

