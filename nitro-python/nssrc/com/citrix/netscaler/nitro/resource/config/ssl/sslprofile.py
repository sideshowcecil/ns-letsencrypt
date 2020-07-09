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

class sslprofile(base_resource) :
	""" Configuration for SSL profile resource. """
	def __init__(self) :
		self._name = None
		self._sslprofiletype = None
		self._ssllogprofile = None
		self._dhcount = None
		self._dh = None
		self._dhfile = None
		self._ersa = None
		self._ersacount = None
		self._sessreuse = None
		self._sesstimeout = None
		self._cipherredirect = None
		self._cipherurl = None
		self._clientauth = None
		self._clientcert = None
		self._dhkeyexpsizelimit = None
		self._sslredirect = None
		self._redirectportrewrite = None
		self._ssl3 = None
		self._tls1 = None
		self._tls11 = None
		self._tls12 = None
		self._tls13 = None
		self._snienable = None
		self._ocspstapling = None
		self._serverauth = None
		self._commonname = None
		self._pushenctrigger = None
		self._sendclosenotify = None
		self._cleartextport = None
		self._insertionencoding = None
		self._denysslreneg = None
		self._quantumsize = None
		self._strictcachecks = None
		self._encrypttriggerpktcount = None
		self._pushflag = None
		self._dropreqwithnohostheader = None
		self._pushenctriggertimeout = None
		self._ssltriggertimeout = None
		self._clientauthuseboundcachain = None
		self._sslinterception = None
		self._sslireneg = None
		self._ssliocspcheck = None
		self._sslimaxsessperserver = None
		self._sessionticket = None
		self._sessionticketlifetime = None
		self._sessionticketkeyrefresh = None
		self._sessionticketkeydata = None
		self._sessionkeylifetime = None
		self._prevsessionkeylifetime = None
		self._hsts = None
		self._maxage = None
		self._includesubdomains = None
		self._preload = None
		self._skipclientcertpolicycheck = None
		self._zerorttearlydata = None
		self._tls13sessionticketsperauthcontext = None
		self._dhekeyexchangewithpsk = None
		self._ciphername = None
		self._cipherpriority = None
		self._strictsigdigestcheck = None
		self._nonfipsciphers = None
		self._crlcheck = None
		self._ocspcheck = None
		self._snicert = None
		self._skipcaname = None
		self._invoke = None
		self._labeltype = None
		self._service = None
		self._builtin = None
		self._feature = None
		self._sslpfobjecttype = None
		self._ssliverifyservercertforreuse = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the SSL profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the profile is created.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the SSL profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the profile is created.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def sslprofiletype(self) :
		r"""Type of profile. Front end profiles apply to the entity that receives requests from a client. Backend profiles apply to the entity that sends client requests to a server.<br/>Default value: FrontEnd<br/>Possible values = BackEnd, FrontEnd.
		"""
		try :
			return self._sslprofiletype
		except Exception as e:
			raise e

	@sslprofiletype.setter
	def sslprofiletype(self, sslprofiletype) :
		r"""Type of profile. Front end profiles apply to the entity that receives requests from a client. Backend profiles apply to the entity that sends client requests to a server.<br/>Default value: FrontEnd<br/>Possible values = BackEnd, FrontEnd
		"""
		try :
			self._sslprofiletype = sslprofiletype
		except Exception as e:
			raise e

	@property
	def ssllogprofile(self) :
		r"""The name of the ssllogprofile.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._ssllogprofile
		except Exception as e:
			raise e

	@ssllogprofile.setter
	def ssllogprofile(self, ssllogprofile) :
		r"""The name of the ssllogprofile.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._ssllogprofile = ssllogprofile
		except Exception as e:
			raise e

	@property
	def dhcount(self) :
		r"""Number of interactions, between the client and the Citrix ADC, after which the DH private-public pair is regenerated. A value of zero (0) specifies infinite use (no refresh).
		This parameter is not applicable when configuring a backend profile. Allowed DH count values are 0 and >= 500.<br/>Maximum length =  65534.
		"""
		try :
			return self._dhcount
		except Exception as e:
			raise e

	@dhcount.setter
	def dhcount(self, dhcount) :
		r"""Number of interactions, between the client and the Citrix ADC, after which the DH private-public pair is regenerated. A value of zero (0) specifies infinite use (no refresh).
		This parameter is not applicable when configuring a backend profile. Allowed DH count values are 0 and >= 500.<br/>Maximum length =  65534
		"""
		try :
			self._dhcount = dhcount
		except Exception as e:
			raise e

	@property
	def dh(self) :
		r"""State of Diffie-Hellman (DH) key exchange.
		This parameter is not applicable when configuring a backend profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dh
		except Exception as e:
			raise e

	@dh.setter
	def dh(self, dh) :
		r"""State of Diffie-Hellman (DH) key exchange.
		This parameter is not applicable when configuring a backend profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dh = dh
		except Exception as e:
			raise e

	@property
	def dhfile(self) :
		r"""The file name and path for the DH parameter.<br/>Minimum length =  1.
		"""
		try :
			return self._dhfile
		except Exception as e:
			raise e

	@dhfile.setter
	def dhfile(self, dhfile) :
		r"""The file name and path for the DH parameter.<br/>Minimum length =  1
		"""
		try :
			self._dhfile = dhfile
		except Exception as e:
			raise e

	@property
	def ersa(self) :
		r"""State of Ephemeral RSA (eRSA) key exchange. Ephemeral RSA allows clients that support only export ciphers to communicate with the secure server even if the server certificate does not support export clients. The ephemeral RSA key is automatically generated when you bind an export cipher to an SSL or TCP-based SSL virtual server or service. When you remove the export cipher, the eRSA key is not deleted. It is reused at a later date when another export cipher is bound to an SSL or TCP-based SSL virtual server or service. The eRSA key is deleted when the appliance restarts.
		This parameter is not applicable when configuring a backend profile.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ersa
		except Exception as e:
			raise e

	@ersa.setter
	def ersa(self, ersa) :
		r"""State of Ephemeral RSA (eRSA) key exchange. Ephemeral RSA allows clients that support only export ciphers to communicate with the secure server even if the server certificate does not support export clients. The ephemeral RSA key is automatically generated when you bind an export cipher to an SSL or TCP-based SSL virtual server or service. When you remove the export cipher, the eRSA key is not deleted. It is reused at a later date when another export cipher is bound to an SSL or TCP-based SSL virtual server or service. The eRSA key is deleted when the appliance restarts.
		This parameter is not applicable when configuring a backend profile.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ersa = ersa
		except Exception as e:
			raise e

	@property
	def ersacount(self) :
		r"""The  refresh  count  for the re-generation of RSA public-key and private-key pair.<br/>Maximum length =  65534.
		"""
		try :
			return self._ersacount
		except Exception as e:
			raise e

	@ersacount.setter
	def ersacount(self, ersacount) :
		r"""The  refresh  count  for the re-generation of RSA public-key and private-key pair.<br/>Maximum length =  65534
		"""
		try :
			self._ersacount = ersacount
		except Exception as e:
			raise e

	@property
	def sessreuse(self) :
		r"""State of session reuse. Establishing the initial handshake requires CPU-intensive public key encryption operations. With the ENABLED setting, session key exchange is avoided for session resumption requests received from the client.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sessreuse
		except Exception as e:
			raise e

	@sessreuse.setter
	def sessreuse(self, sessreuse) :
		r"""State of session reuse. Establishing the initial handshake requires CPU-intensive public key encryption operations. With the ENABLED setting, session key exchange is avoided for session resumption requests received from the client.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sessreuse = sessreuse
		except Exception as e:
			raise e

	@property
	def sesstimeout(self) :
		r"""The Session timeout value in seconds.<br/>Maximum length =  0xFFFFFFFE.
		"""
		try :
			return self._sesstimeout
		except Exception as e:
			raise e

	@sesstimeout.setter
	def sesstimeout(self, sesstimeout) :
		r"""The Session timeout value in seconds.<br/>Maximum length =  0xFFFFFFFE
		"""
		try :
			self._sesstimeout = sesstimeout
		except Exception as e:
			raise e

	@property
	def cipherredirect(self) :
		r"""State of Cipher Redirect. If this parameter is set to ENABLED, you can configure an SSL virtual server or service to display meaningful error messages if the SSL handshake fails because of a cipher mismatch between the virtual server or service and the client.
		This parameter is not applicable when configuring a backend profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cipherredirect
		except Exception as e:
			raise e

	@cipherredirect.setter
	def cipherredirect(self, cipherredirect) :
		r"""State of Cipher Redirect. If this parameter is set to ENABLED, you can configure an SSL virtual server or service to display meaningful error messages if the SSL handshake fails because of a cipher mismatch between the virtual server or service and the client.
		This parameter is not applicable when configuring a backend profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cipherredirect = cipherredirect
		except Exception as e:
			raise e

	@property
	def cipherurl(self) :
		r"""The redirect URL to be used with the Cipher Redirect feature.
		"""
		try :
			return self._cipherurl
		except Exception as e:
			raise e

	@cipherurl.setter
	def cipherurl(self, cipherurl) :
		r"""The redirect URL to be used with the Cipher Redirect feature.
		"""
		try :
			self._cipherurl = cipherurl
		except Exception as e:
			raise e

	@property
	def clientauth(self) :
		r"""State of client authentication. In service-based SSL offload, the service terminates the SSL handshake if the SSL client does not provide a valid certificate. 
		This parameter is not applicable when configuring a backend profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._clientauth
		except Exception as e:
			raise e

	@clientauth.setter
	def clientauth(self, clientauth) :
		r"""State of client authentication. In service-based SSL offload, the service terminates the SSL handshake if the SSL client does not provide a valid certificate. 
		This parameter is not applicable when configuring a backend profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._clientauth = clientauth
		except Exception as e:
			raise e

	@property
	def clientcert(self) :
		r"""The rule for client certificate requirement in client authentication.<br/>Possible values = Mandatory, Optional.
		"""
		try :
			return self._clientcert
		except Exception as e:
			raise e

	@clientcert.setter
	def clientcert(self, clientcert) :
		r"""The rule for client certificate requirement in client authentication.<br/>Possible values = Mandatory, Optional
		"""
		try :
			self._clientcert = clientcert
		except Exception as e:
			raise e

	@property
	def dhkeyexpsizelimit(self) :
		r"""This option enables the use of NIST recommended (NIST Special Publication 800-56A) bit size for private-key size. For example, for DH params of size 2048bit, the private-key size recommended is 224bits. This is rounded-up to 256bits.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dhkeyexpsizelimit
		except Exception as e:
			raise e

	@dhkeyexpsizelimit.setter
	def dhkeyexpsizelimit(self, dhkeyexpsizelimit) :
		r"""This option enables the use of NIST recommended (NIST Special Publication 800-56A) bit size for private-key size. For example, for DH params of size 2048bit, the private-key size recommended is 224bits. This is rounded-up to 256bits.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dhkeyexpsizelimit = dhkeyexpsizelimit
		except Exception as e:
			raise e

	@property
	def sslredirect(self) :
		r"""State of HTTPS redirects for the SSL service. 
		For an SSL session, if the client browser receives a redirect message, the browser tries to connect to the new location. However, the secure SSL session breaks if the object has moved from a secure site (https://) to an unsecure site (http://). Typically, a warning message appears on the screen, prompting the user to continue or disconnect.
		If SSL Redirect is ENABLED, the redirect message is automatically converted from http:// to https:// and the SSL session does not break.
		This parameter is not applicable when configuring a backend profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sslredirect
		except Exception as e:
			raise e

	@sslredirect.setter
	def sslredirect(self, sslredirect) :
		r"""State of HTTPS redirects for the SSL service. 
		For an SSL session, if the client browser receives a redirect message, the browser tries to connect to the new location. However, the secure SSL session breaks if the object has moved from a secure site (https://) to an unsecure site (http://). Typically, a warning message appears on the screen, prompting the user to continue or disconnect.
		If SSL Redirect is ENABLED, the redirect message is automatically converted from http:// to https:// and the SSL session does not break.
		This parameter is not applicable when configuring a backend profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sslredirect = sslredirect
		except Exception as e:
			raise e

	@property
	def redirectportrewrite(self) :
		r"""State of the port rewrite while performing HTTPS redirect. If this parameter is set to ENABLED, and the URL from the server does not contain the standard port, the port is rewritten to the standard.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._redirectportrewrite
		except Exception as e:
			raise e

	@redirectportrewrite.setter
	def redirectportrewrite(self, redirectportrewrite) :
		r"""State of the port rewrite while performing HTTPS redirect. If this parameter is set to ENABLED, and the URL from the server does not contain the standard port, the port is rewritten to the standard.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._redirectportrewrite = redirectportrewrite
		except Exception as e:
			raise e

	@property
	def ssl3(self) :
		r"""State of SSLv3 protocol support for the SSL profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ssl3
		except Exception as e:
			raise e

	@ssl3.setter
	def ssl3(self, ssl3) :
		r"""State of SSLv3 protocol support for the SSL profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ssl3 = ssl3
		except Exception as e:
			raise e

	@property
	def tls1(self) :
		r"""State of TLSv1.0 protocol support for the SSL profile.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tls1
		except Exception as e:
			raise e

	@tls1.setter
	def tls1(self, tls1) :
		r"""State of TLSv1.0 protocol support for the SSL profile.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tls1 = tls1
		except Exception as e:
			raise e

	@property
	def tls11(self) :
		r"""State of TLSv1.1 protocol support for the SSL profile.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tls11
		except Exception as e:
			raise e

	@tls11.setter
	def tls11(self, tls11) :
		r"""State of TLSv1.1 protocol support for the SSL profile.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tls11 = tls11
		except Exception as e:
			raise e

	@property
	def tls12(self) :
		r"""State of TLSv1.2 protocol support for the SSL profile.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tls12
		except Exception as e:
			raise e

	@tls12.setter
	def tls12(self, tls12) :
		r"""State of TLSv1.2 protocol support for the SSL profile.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tls12 = tls12
		except Exception as e:
			raise e

	@property
	def tls13(self) :
		r"""State of TLSv1.3 protocol support for the SSL profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._tls13
		except Exception as e:
			raise e

	@tls13.setter
	def tls13(self, tls13) :
		r"""State of TLSv1.3 protocol support for the SSL profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._tls13 = tls13
		except Exception as e:
			raise e

	@property
	def snienable(self) :
		r"""State of the Server Name Indication (SNI) feature on the virtual server and service-based offload. SNI helps to enable SSL encryption on multiple domains on a single virtual server or service if the domains are controlled by the same organization and share the same second-level domain name. For example, *.sports.net can be used to secure domains such as login.sports.net and help.sports.net.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._snienable
		except Exception as e:
			raise e

	@snienable.setter
	def snienable(self, snienable) :
		r"""State of the Server Name Indication (SNI) feature on the virtual server and service-based offload. SNI helps to enable SSL encryption on multiple domains on a single virtual server or service if the domains are controlled by the same organization and share the same second-level domain name. For example, *.sports.net can be used to secure domains such as login.sports.net and help.sports.net.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._snienable = snienable
		except Exception as e:
			raise e

	@property
	def ocspstapling(self) :
		r"""State of OCSP stapling support on the SSL virtual server. Supported only if the protocol used is higher than SSLv3. Possible values:
		ENABLED: The appliance sends a request to the OCSP responder to check the status of the server certificate and caches the response for the specified time. If the response is valid at the time of SSL handshake with the client, the OCSP-based server certificate status is sent to the client during the handshake.
		DISABLED: The appliance does not check the status of the server certificate. .<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ocspstapling
		except Exception as e:
			raise e

	@ocspstapling.setter
	def ocspstapling(self, ocspstapling) :
		r"""State of OCSP stapling support on the SSL virtual server. Supported only if the protocol used is higher than SSLv3. Possible values:
		ENABLED: The appliance sends a request to the OCSP responder to check the status of the server certificate and caches the response for the specified time. If the response is valid at the time of SSL handshake with the client, the OCSP-based server certificate status is sent to the client during the handshake.
		DISABLED: The appliance does not check the status of the server certificate. .<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ocspstapling = ocspstapling
		except Exception as e:
			raise e

	@property
	def serverauth(self) :
		r"""State of server authentication support for the SSL Backend profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._serverauth
		except Exception as e:
			raise e

	@serverauth.setter
	def serverauth(self, serverauth) :
		r"""State of server authentication support for the SSL Backend profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._serverauth = serverauth
		except Exception as e:
			raise e

	@property
	def commonname(self) :
		r"""Name to be checked against the CommonName (CN) field in the server certificate bound to the SSL server.<br/>Minimum length =  1.
		"""
		try :
			return self._commonname
		except Exception as e:
			raise e

	@commonname.setter
	def commonname(self, commonname) :
		r"""Name to be checked against the CommonName (CN) field in the server certificate bound to the SSL server.<br/>Minimum length =  1
		"""
		try :
			self._commonname = commonname
		except Exception as e:
			raise e

	@property
	def pushenctrigger(self) :
		r"""Trigger encryption on the basis of the PUSH flag value. Available settings function as follows:
		* ALWAYS - Any PUSH packet triggers encryption.
		* IGNORE - Ignore PUSH packet for triggering encryption.
		* MERGE - For a consecutive sequence of PUSH packets, the last PUSH packet triggers encryption.
		* TIMER - PUSH packet triggering encryption is delayed by the time defined in the set ssl parameter command or in the Change Advanced SSL Settings dialog box.<br/>Possible values = Always, Merge, Ignore, Timer.
		"""
		try :
			return self._pushenctrigger
		except Exception as e:
			raise e

	@pushenctrigger.setter
	def pushenctrigger(self, pushenctrigger) :
		r"""Trigger encryption on the basis of the PUSH flag value. Available settings function as follows:
		* ALWAYS - Any PUSH packet triggers encryption.
		* IGNORE - Ignore PUSH packet for triggering encryption.
		* MERGE - For a consecutive sequence of PUSH packets, the last PUSH packet triggers encryption.
		* TIMER - PUSH packet triggering encryption is delayed by the time defined in the set ssl parameter command or in the Change Advanced SSL Settings dialog box.<br/>Possible values = Always, Merge, Ignore, Timer
		"""
		try :
			self._pushenctrigger = pushenctrigger
		except Exception as e:
			raise e

	@property
	def sendclosenotify(self) :
		r"""Enable sending SSL Close-Notify at the end of a transaction.<br/>Default value: YES<br/>Possible values = YES, NO.
		"""
		try :
			return self._sendclosenotify
		except Exception as e:
			raise e

	@sendclosenotify.setter
	def sendclosenotify(self, sendclosenotify) :
		r"""Enable sending SSL Close-Notify at the end of a transaction.<br/>Default value: YES<br/>Possible values = YES, NO
		"""
		try :
			self._sendclosenotify = sendclosenotify
		except Exception as e:
			raise e

	@property
	def cleartextport(self) :
		r"""Port on which clear-text data is sent by the appliance to the server. Do not specify this parameter for SSL offloading with end-to-end encryption.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._cleartextport
		except Exception as e:
			raise e

	@cleartextport.setter
	def cleartextport(self, cleartextport) :
		r"""Port on which clear-text data is sent by the appliance to the server. Do not specify this parameter for SSL offloading with end-to-end encryption.<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API
		"""
		try :
			self._cleartextport = cleartextport
		except Exception as e:
			raise e

	@property
	def insertionencoding(self) :
		r"""Encoding method used to insert the subject or issuer's name in HTTP requests to servers.<br/>Default value: Unicode<br/>Possible values = Unicode, UTF-8.
		"""
		try :
			return self._insertionencoding
		except Exception as e:
			raise e

	@insertionencoding.setter
	def insertionencoding(self, insertionencoding) :
		r"""Encoding method used to insert the subject or issuer's name in HTTP requests to servers.<br/>Default value: Unicode<br/>Possible values = Unicode, UTF-8
		"""
		try :
			self._insertionencoding = insertionencoding
		except Exception as e:
			raise e

	@property
	def denysslreneg(self) :
		r"""Deny renegotiation in specified circumstances. Available settings function as follows:
		* NO - Allow SSL renegotiation.
		* FRONTEND_CLIENT - Deny secure and nonsecure SSL renegotiation initiated by the client.
		* FRONTEND_CLIENTSERVER - Deny secure and nonsecure SSL renegotiation initiated by the client or the Citrix ADC during policy-based client authentication. 
		* ALL - Deny all secure and nonsecure SSL renegotiation.
		* NONSECURE - Deny nonsecure SSL renegotiation. Allows only clients that support RFC 5746.<br/>Default value: ALL<br/>Possible values = NO, FRONTEND_CLIENT, FRONTEND_CLIENTSERVER, ALL, NONSECURE.
		"""
		try :
			return self._denysslreneg
		except Exception as e:
			raise e

	@denysslreneg.setter
	def denysslreneg(self, denysslreneg) :
		r"""Deny renegotiation in specified circumstances. Available settings function as follows:
		* NO - Allow SSL renegotiation.
		* FRONTEND_CLIENT - Deny secure and nonsecure SSL renegotiation initiated by the client.
		* FRONTEND_CLIENTSERVER - Deny secure and nonsecure SSL renegotiation initiated by the client or the Citrix ADC during policy-based client authentication. 
		* ALL - Deny all secure and nonsecure SSL renegotiation.
		* NONSECURE - Deny nonsecure SSL renegotiation. Allows only clients that support RFC 5746.<br/>Default value: ALL<br/>Possible values = NO, FRONTEND_CLIENT, FRONTEND_CLIENTSERVER, ALL, NONSECURE
		"""
		try :
			self._denysslreneg = denysslreneg
		except Exception as e:
			raise e

	@property
	def quantumsize(self) :
		r"""Amount of data to collect before the data is pushed to the crypto hardware for encryption. For large downloads, a larger quantum size better utilizes the crypto resources.<br/>Default value: 8192<br/>Possible values = 4096, 8192, 16384.
		"""
		try :
			return self._quantumsize
		except Exception as e:
			raise e

	@quantumsize.setter
	def quantumsize(self, quantumsize) :
		r"""Amount of data to collect before the data is pushed to the crypto hardware for encryption. For large downloads, a larger quantum size better utilizes the crypto resources.<br/>Default value: 8192<br/>Possible values = 4096, 8192, 16384
		"""
		try :
			self._quantumsize = quantumsize
		except Exception as e:
			raise e

	@property
	def strictcachecks(self) :
		r"""Enable strict CA certificate checks on the appliance.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._strictcachecks
		except Exception as e:
			raise e

	@strictcachecks.setter
	def strictcachecks(self, strictcachecks) :
		r"""Enable strict CA certificate checks on the appliance.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._strictcachecks = strictcachecks
		except Exception as e:
			raise e

	@property
	def encrypttriggerpktcount(self) :
		r"""Maximum number of queued packets after which encryption is triggered. Use this setting for SSL transactions that send small packets from server to Citrix ADC.<br/>Default value: 45<br/>Minimum length =  10<br/>Maximum length =  50.
		"""
		try :
			return self._encrypttriggerpktcount
		except Exception as e:
			raise e

	@encrypttriggerpktcount.setter
	def encrypttriggerpktcount(self, encrypttriggerpktcount) :
		r"""Maximum number of queued packets after which encryption is triggered. Use this setting for SSL transactions that send small packets from server to Citrix ADC.<br/>Default value: 45<br/>Minimum length =  10<br/>Maximum length =  50
		"""
		try :
			self._encrypttriggerpktcount = encrypttriggerpktcount
		except Exception as e:
			raise e

	@property
	def pushflag(self) :
		r"""Insert PUSH flag into decrypted, encrypted, or all records. If the PUSH flag is set to a value other than 0, the buffered records are forwarded on the basis of the value of the PUSH flag. Available settings function as follows:
		0 - Auto (PUSH flag is not set.)
		1 - Insert PUSH flag into every decrypted record.
		2 -Insert PUSH flag into every encrypted record.
		3 - Insert PUSH flag into every decrypted and encrypted record.<br/>Maximum length =  3.
		"""
		try :
			return self._pushflag
		except Exception as e:
			raise e

	@pushflag.setter
	def pushflag(self, pushflag) :
		r"""Insert PUSH flag into decrypted, encrypted, or all records. If the PUSH flag is set to a value other than 0, the buffered records are forwarded on the basis of the value of the PUSH flag. Available settings function as follows:
		0 - Auto (PUSH flag is not set.)
		1 - Insert PUSH flag into every decrypted record.
		2 -Insert PUSH flag into every encrypted record.
		3 - Insert PUSH flag into every decrypted and encrypted record.<br/>Maximum length =  3
		"""
		try :
			self._pushflag = pushflag
		except Exception as e:
			raise e

	@property
	def dropreqwithnohostheader(self) :
		r"""Host header check for SNI enabled sessions. If this check is enabled and the HTTP request does not contain the host header for SNI enabled sessions, the request is dropped. Also, please note that when the check is disabled, the request will not be dropped even if there is a mis-match between SNI and HTTP host-header.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._dropreqwithnohostheader
		except Exception as e:
			raise e

	@dropreqwithnohostheader.setter
	def dropreqwithnohostheader(self, dropreqwithnohostheader) :
		r"""Host header check for SNI enabled sessions. If this check is enabled and the HTTP request does not contain the host header for SNI enabled sessions, the request is dropped. Also, please note that when the check is disabled, the request will not be dropped even if there is a mis-match between SNI and HTTP host-header.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._dropreqwithnohostheader = dropreqwithnohostheader
		except Exception as e:
			raise e

	@property
	def pushenctriggertimeout(self) :
		r"""PUSH encryption trigger timeout value. The timeout value is applied only if you set the Push Encryption Trigger parameter to Timer in the SSL virtual server settings.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  200.
		"""
		try :
			return self._pushenctriggertimeout
		except Exception as e:
			raise e

	@pushenctriggertimeout.setter
	def pushenctriggertimeout(self, pushenctriggertimeout) :
		r"""PUSH encryption trigger timeout value. The timeout value is applied only if you set the Push Encryption Trigger parameter to Timer in the SSL virtual server settings.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  200
		"""
		try :
			self._pushenctriggertimeout = pushenctriggertimeout
		except Exception as e:
			raise e

	@property
	def ssltriggertimeout(self) :
		r"""Time, in milliseconds, after which encryption is triggered for transactions that are not tracked on the Citrix ADC because their length is not known. There can be a delay of up to 10ms from the specified timeout value before the packet is pushed into the queue.<br/>Default value: 100<br/>Minimum length =  1<br/>Maximum length =  200.
		"""
		try :
			return self._ssltriggertimeout
		except Exception as e:
			raise e

	@ssltriggertimeout.setter
	def ssltriggertimeout(self, ssltriggertimeout) :
		r"""Time, in milliseconds, after which encryption is triggered for transactions that are not tracked on the Citrix ADC because their length is not known. There can be a delay of up to 10ms from the specified timeout value before the packet is pushed into the queue.<br/>Default value: 100<br/>Minimum length =  1<br/>Maximum length =  200
		"""
		try :
			self._ssltriggertimeout = ssltriggertimeout
		except Exception as e:
			raise e

	@property
	def clientauthuseboundcachain(self) :
		r"""Certficates bound on the VIP are used for validating the client cert. Certficates came along with client cert are not used for validating the client cert.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._clientauthuseboundcachain
		except Exception as e:
			raise e

	@clientauthuseboundcachain.setter
	def clientauthuseboundcachain(self, clientauthuseboundcachain) :
		r"""Certficates bound on the VIP are used for validating the client cert. Certficates came along with client cert are not used for validating the client cert.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._clientauthuseboundcachain = clientauthuseboundcachain
		except Exception as e:
			raise e

	@property
	def sslinterception(self) :
		r"""Enable or disable transparent interception of SSL sessions.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sslinterception
		except Exception as e:
			raise e

	@sslinterception.setter
	def sslinterception(self, sslinterception) :
		r"""Enable or disable transparent interception of SSL sessions.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sslinterception = sslinterception
		except Exception as e:
			raise e

	@property
	def sslireneg(self) :
		r"""Enable or disable triggering the client renegotiation when renegotiation request is received from the origin server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sslireneg
		except Exception as e:
			raise e

	@sslireneg.setter
	def sslireneg(self, sslireneg) :
		r"""Enable or disable triggering the client renegotiation when renegotiation request is received from the origin server.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sslireneg = sslireneg
		except Exception as e:
			raise e

	@property
	def ssliocspcheck(self) :
		r"""Enable or disable OCSP check for origin server certificate.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ssliocspcheck
		except Exception as e:
			raise e

	@ssliocspcheck.setter
	def ssliocspcheck(self, ssliocspcheck) :
		r"""Enable or disable OCSP check for origin server certificate.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ssliocspcheck = ssliocspcheck
		except Exception as e:
			raise e

	@property
	def sslimaxsessperserver(self) :
		r"""Maximum ssl session to be cached per dynamic origin server. A unique ssl session is created for each SNI received from the client on ClientHello and the matching session is used for server session reuse.<br/>Default value: 10<br/>Minimum length =  1<br/>Maximum length =  1000.
		"""
		try :
			return self._sslimaxsessperserver
		except Exception as e:
			raise e

	@sslimaxsessperserver.setter
	def sslimaxsessperserver(self, sslimaxsessperserver) :
		r"""Maximum ssl session to be cached per dynamic origin server. A unique ssl session is created for each SNI received from the client on ClientHello and the matching session is used for server session reuse.<br/>Default value: 10<br/>Minimum length =  1<br/>Maximum length =  1000
		"""
		try :
			self._sslimaxsessperserver = sslimaxsessperserver
		except Exception as e:
			raise e

	@property
	def sessionticket(self) :
		r"""This option enables the use of session tickets, as per the RFC 5077.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sessionticket
		except Exception as e:
			raise e

	@sessionticket.setter
	def sessionticket(self, sessionticket) :
		r"""This option enables the use of session tickets, as per the RFC 5077.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sessionticket = sessionticket
		except Exception as e:
			raise e

	@property
	def sessionticketlifetime(self) :
		r"""This option sets the life time of session tickets issued by NS in secs.<br/>Default value: 300<br/>Maximum length =  172800.
		"""
		try :
			return self._sessionticketlifetime
		except Exception as e:
			raise e

	@sessionticketlifetime.setter
	def sessionticketlifetime(self, sessionticketlifetime) :
		r"""This option sets the life time of session tickets issued by NS in secs.<br/>Default value: 300<br/>Maximum length =  172800
		"""
		try :
			self._sessionticketlifetime = sessionticketlifetime
		except Exception as e:
			raise e

	@property
	def sessionticketkeyrefresh(self) :
		r"""This option enables the use of session tickets, as per the RFC 5077.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sessionticketkeyrefresh
		except Exception as e:
			raise e

	@sessionticketkeyrefresh.setter
	def sessionticketkeyrefresh(self, sessionticketkeyrefresh) :
		r"""This option enables the use of session tickets, as per the RFC 5077.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sessionticketkeyrefresh = sessionticketkeyrefresh
		except Exception as e:
			raise e

	@property
	def sessionticketkeydata(self) :
		r"""Session ticket enc/dec key , admin can set it.
		"""
		try :
			return self._sessionticketkeydata
		except Exception as e:
			raise e

	@sessionticketkeydata.setter
	def sessionticketkeydata(self, sessionticketkeydata) :
		r"""Session ticket enc/dec key , admin can set it.
		"""
		try :
			self._sessionticketkeydata = sessionticketkeydata
		except Exception as e:
			raise e

	@property
	def sessionkeylifetime(self) :
		r"""This option sets the life time of symm key used to generate session tickets issued by NS in secs.<br/>Default value: 3000<br/>Minimum length =  600<br/>Maximum length =  86400.
		"""
		try :
			return self._sessionkeylifetime
		except Exception as e:
			raise e

	@sessionkeylifetime.setter
	def sessionkeylifetime(self, sessionkeylifetime) :
		r"""This option sets the life time of symm key used to generate session tickets issued by NS in secs.<br/>Default value: 3000<br/>Minimum length =  600<br/>Maximum length =  86400
		"""
		try :
			self._sessionkeylifetime = sessionkeylifetime
		except Exception as e:
			raise e

	@property
	def prevsessionkeylifetime(self) :
		r"""This option sets the life time of symm key used to generate session tickets issued by NS in secs.<br/>Default value: 0<br/>Maximum length =  172800.
		"""
		try :
			return self._prevsessionkeylifetime
		except Exception as e:
			raise e

	@prevsessionkeylifetime.setter
	def prevsessionkeylifetime(self, prevsessionkeylifetime) :
		r"""This option sets the life time of symm key used to generate session tickets issued by NS in secs.<br/>Default value: 0<br/>Maximum length =  172800
		"""
		try :
			self._prevsessionkeylifetime = prevsessionkeylifetime
		except Exception as e:
			raise e

	@property
	def hsts(self) :
		r"""State of HSTS protocol support for the SSL profile. Using HSTS, a server can enforce the use of an HTTPS connection for all communication with a client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._hsts
		except Exception as e:
			raise e

	@hsts.setter
	def hsts(self, hsts) :
		r"""State of HSTS protocol support for the SSL profile. Using HSTS, a server can enforce the use of an HTTPS connection for all communication with a client.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._hsts = hsts
		except Exception as e:
			raise e

	@property
	def maxage(self) :
		r"""Set the maximum time, in seconds, in the strict transport security (STS) header during which the client must send only HTTPS requests to the server.<br/>Default value: 0<br/>Maximum length =  0xFFFFFFFE.
		"""
		try :
			return self._maxage
		except Exception as e:
			raise e

	@maxage.setter
	def maxage(self, maxage) :
		r"""Set the maximum time, in seconds, in the strict transport security (STS) header during which the client must send only HTTPS requests to the server.<br/>Default value: 0<br/>Maximum length =  0xFFFFFFFE
		"""
		try :
			self._maxage = maxage
		except Exception as e:
			raise e

	@property
	def includesubdomains(self) :
		r"""Enable HSTS for subdomains. If set to Yes, a client must send only HTTPS requests for subdomains.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._includesubdomains
		except Exception as e:
			raise e

	@includesubdomains.setter
	def includesubdomains(self, includesubdomains) :
		r"""Enable HSTS for subdomains. If set to Yes, a client must send only HTTPS requests for subdomains.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._includesubdomains = includesubdomains
		except Exception as e:
			raise e

	@property
	def preload(self) :
		r"""Flag indicates the consent of the site owner to have their domain preloaded.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._preload
		except Exception as e:
			raise e

	@preload.setter
	def preload(self, preload) :
		r"""Flag indicates the consent of the site owner to have their domain preloaded.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._preload = preload
		except Exception as e:
			raise e

	@property
	def skipclientcertpolicycheck(self) :
		r"""This flag controls the processing of X509 certificate policies. If this option is Enabled, then the policy check in Client authentication will be skipped. This option can be used only when Client Authentication is Enabled and ClientCert is set to Mandatory.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._skipclientcertpolicycheck
		except Exception as e:
			raise e

	@skipclientcertpolicycheck.setter
	def skipclientcertpolicycheck(self, skipclientcertpolicycheck) :
		r"""This flag controls the processing of X509 certificate policies. If this option is Enabled, then the policy check in Client authentication will be skipped. This option can be used only when Client Authentication is Enabled and ClientCert is set to Mandatory.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._skipclientcertpolicycheck = skipclientcertpolicycheck
		except Exception as e:
			raise e

	@property
	def zerorttearlydata(self) :
		r"""State of TLS 1.3 0-RTT early data support for the SSL Virtual Server. This setting only has an effect if resumption is enabled, as early data cannot be sent along with an initial handshake.
		Early application data has significantly different security properties - in particular there is no guarantee that the data cannot be replayed.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._zerorttearlydata
		except Exception as e:
			raise e

	@zerorttearlydata.setter
	def zerorttearlydata(self, zerorttearlydata) :
		r"""State of TLS 1.3 0-RTT early data support for the SSL Virtual Server. This setting only has an effect if resumption is enabled, as early data cannot be sent along with an initial handshake.
		Early application data has significantly different security properties - in particular there is no guarantee that the data cannot be replayed.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._zerorttearlydata = zerorttearlydata
		except Exception as e:
			raise e

	@property
	def tls13sessionticketsperauthcontext(self) :
		r"""Number of tickets the SSL Virtual Server will issue anytime TLS 1.3 is negotiated, ticket-based resumption is enabled, and either (1) a handshake completes or (2) post-handhsake client auth completes.
		This value can be increased to enable clients to open multiple parallel connections using a fresh ticket for each connection.
		No tickets are sent if resumption is disabled.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  10.
		"""
		try :
			return self._tls13sessionticketsperauthcontext
		except Exception as e:
			raise e

	@tls13sessionticketsperauthcontext.setter
	def tls13sessionticketsperauthcontext(self, tls13sessionticketsperauthcontext) :
		r"""Number of tickets the SSL Virtual Server will issue anytime TLS 1.3 is negotiated, ticket-based resumption is enabled, and either (1) a handshake completes or (2) post-handhsake client auth completes.
		This value can be increased to enable clients to open multiple parallel connections using a fresh ticket for each connection.
		No tickets are sent if resumption is disabled.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  10
		"""
		try :
			self._tls13sessionticketsperauthcontext = tls13sessionticketsperauthcontext
		except Exception as e:
			raise e

	@property
	def dhekeyexchangewithpsk(self) :
		r"""Whether or not the SSL Virtual Server will require a DHE key exchange to occur when a PSK is accepted during a TLS 1.3 resumption handshake.
		A DHE key exchange ensures forward secrecy even in the event that ticket keys are compromised, at the expense of an additional round trip and resources required to carry out the DHE key exchange.
		If disabled, a DHE key exchange will be performed when a PSK is accepted but only if requested by the client.
		If enabled, the server will require a DHE key exchange when a PSK is accepted regardless of whether the client supports combined PSK-DHE key exchange. This setting only has an effect when resumption is enabled.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._dhekeyexchangewithpsk
		except Exception as e:
			raise e

	@dhekeyexchangewithpsk.setter
	def dhekeyexchangewithpsk(self, dhekeyexchangewithpsk) :
		r"""Whether or not the SSL Virtual Server will require a DHE key exchange to occur when a PSK is accepted during a TLS 1.3 resumption handshake.
		A DHE key exchange ensures forward secrecy even in the event that ticket keys are compromised, at the expense of an additional round trip and resources required to carry out the DHE key exchange.
		If disabled, a DHE key exchange will be performed when a PSK is accepted but only if requested by the client.
		If enabled, the server will require a DHE key exchange when a PSK is accepted regardless of whether the client supports combined PSK-DHE key exchange. This setting only has an effect when resumption is enabled.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._dhekeyexchangewithpsk = dhekeyexchangewithpsk
		except Exception as e:
			raise e

	@property
	def ciphername(self) :
		r"""The cipher group/alias/individual cipher configuration.
		"""
		try :
			return self._ciphername
		except Exception as e:
			raise e

	@ciphername.setter
	def ciphername(self, ciphername) :
		r"""The cipher group/alias/individual cipher configuration.
		"""
		try :
			self._ciphername = ciphername
		except Exception as e:
			raise e

	@property
	def cipherpriority(self) :
		r"""cipher priority.<br/>Minimum length =  1.
		"""
		try :
			return self._cipherpriority
		except Exception as e:
			raise e

	@cipherpriority.setter
	def cipherpriority(self, cipherpriority) :
		r"""cipher priority.<br/>Minimum length =  1
		"""
		try :
			self._cipherpriority = cipherpriority
		except Exception as e:
			raise e

	@property
	def strictsigdigestcheck(self) :
		r"""Parameter indicating to check whether peer entity certificate during TLS1.2 handshake is signed with one of signature-hash combination supported by Citrix ADC.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._strictsigdigestcheck
		except Exception as e:
			raise e

	@strictsigdigestcheck.setter
	def strictsigdigestcheck(self, strictsigdigestcheck) :
		r"""Parameter indicating to check whether peer entity certificate during TLS1.2 handshake is signed with one of signature-hash combination supported by Citrix ADC.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._strictsigdigestcheck = strictsigdigestcheck
		except Exception as e:
			raise e

	@property
	def nonfipsciphers(self) :
		r"""State of usage of ciphers that are not FIPS approved. Valid only for an SSL service bound with a FIPS key and certificate.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._nonfipsciphers
		except Exception as e:
			raise e

	@property
	def crlcheck(self) :
		r"""The state of the CRL check parameter. (Mandatory/Optional).<br/>Possible values = Mandatory, Optional.
		"""
		try :
			return self._crlcheck
		except Exception as e:
			raise e

	@property
	def ocspcheck(self) :
		r"""The state of the OCSP check parameter. (Mandatory/Optional).<br/>Possible values = Mandatory, Optional.
		"""
		try :
			return self._ocspcheck
		except Exception as e:
			raise e

	@property
	def snicert(self) :
		r"""The name of the CertKey. Use this option to bind Certkey(s) which will be used in SNI processing.
		"""
		try :
			return self._snicert
		except Exception as e:
			raise e

	@property
	def skipcaname(self) :
		r"""The flag is used to indicate whether this
		particular CA certificate's CA_Name needs to be sent to
		the SSL client while requesting for client certificate
		in a SSL handshake.
		"""
		try :
			return self._skipcaname
		except Exception as e:
			raise e

	@property
	def invoke(self) :
		r"""Invoke flag. This attribute is relevant only for ADVANCED policies.
		"""
		try :
			return self._invoke
		except Exception as e:
			raise e

	@property
	def labeltype(self) :
		r"""Type of policy label invocation.<br/>Possible values = vserver, service, policylabel.
		"""
		try :
			return self._labeltype
		except Exception as e:
			raise e

	@property
	def service(self) :
		r"""Service.
		"""
		try :
			return self._service
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r"""Flag to determine whether ssl profile is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
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

	@property
	def sslpfobjecttype(self) :
		r"""Internal flag to indicate what type of object binds this profile: monitor or service.
		"""
		try :
			return self._sslpfobjecttype
		except Exception as e:
			raise e

	@property
	def ssliverifyservercertforreuse(self) :
		r"""Verify the origin server's certificate before reusing the front-end SSL session. Making it hidden since we always verify for now.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ssliverifyservercertforreuse
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(sslprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.sslprofile
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
		addresource = sslprofile()
		addresource.name = resource.name
		addresource.sslprofiletype = resource.sslprofiletype
		addresource.ssllogprofile = resource.ssllogprofile
		addresource.dhcount = resource.dhcount
		addresource.dh = resource.dh
		addresource.dhfile = resource.dhfile
		addresource.ersa = resource.ersa
		addresource.ersacount = resource.ersacount
		addresource.sessreuse = resource.sessreuse
		addresource.sesstimeout = resource.sesstimeout
		addresource.cipherredirect = resource.cipherredirect
		addresource.cipherurl = resource.cipherurl
		addresource.clientauth = resource.clientauth
		addresource.clientcert = resource.clientcert
		addresource.dhkeyexpsizelimit = resource.dhkeyexpsizelimit
		addresource.sslredirect = resource.sslredirect
		addresource.redirectportrewrite = resource.redirectportrewrite
		addresource.ssl3 = resource.ssl3
		addresource.tls1 = resource.tls1
		addresource.tls11 = resource.tls11
		addresource.tls12 = resource.tls12
		addresource.tls13 = resource.tls13
		addresource.snienable = resource.snienable
		addresource.ocspstapling = resource.ocspstapling
		addresource.serverauth = resource.serverauth
		addresource.commonname = resource.commonname
		addresource.pushenctrigger = resource.pushenctrigger
		addresource.sendclosenotify = resource.sendclosenotify
		addresource.cleartextport = resource.cleartextport
		addresource.insertionencoding = resource.insertionencoding
		addresource.denysslreneg = resource.denysslreneg
		addresource.quantumsize = resource.quantumsize
		addresource.strictcachecks = resource.strictcachecks
		addresource.encrypttriggerpktcount = resource.encrypttriggerpktcount
		addresource.pushflag = resource.pushflag
		addresource.dropreqwithnohostheader = resource.dropreqwithnohostheader
		addresource.pushenctriggertimeout = resource.pushenctriggertimeout
		addresource.ssltriggertimeout = resource.ssltriggertimeout
		addresource.clientauthuseboundcachain = resource.clientauthuseboundcachain
		addresource.sslinterception = resource.sslinterception
		addresource.sslireneg = resource.sslireneg
		addresource.ssliocspcheck = resource.ssliocspcheck
		addresource.sslimaxsessperserver = resource.sslimaxsessperserver
		addresource.sessionticket = resource.sessionticket
		addresource.sessionticketlifetime = resource.sessionticketlifetime
		addresource.sessionticketkeyrefresh = resource.sessionticketkeyrefresh
		addresource.sessionticketkeydata = resource.sessionticketkeydata
		addresource.sessionkeylifetime = resource.sessionkeylifetime
		addresource.prevsessionkeylifetime = resource.prevsessionkeylifetime
		addresource.hsts = resource.hsts
		addresource.maxage = resource.maxage
		addresource.includesubdomains = resource.includesubdomains
		addresource.preload = resource.preload
		addresource.skipclientcertpolicycheck = resource.skipclientcertpolicycheck
		addresource.zerorttearlydata = resource.zerorttearlydata
		addresource.tls13sessionticketsperauthcontext = resource.tls13sessionticketsperauthcontext
		addresource.dhekeyexchangewithpsk = resource.dhekeyexchangewithpsk
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add sslprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ sslprofile() for _ in range(len(resource))]
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
		deleteresource = sslprofile()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete sslprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = sslprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ sslprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ sslprofile() for _ in range(len(resource))]
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
		updateresource = sslprofile()
		updateresource.name = resource.name
		updateresource.ssllogprofile = resource.ssllogprofile
		updateresource.dh = resource.dh
		updateresource.dhfile = resource.dhfile
		updateresource.dhcount = resource.dhcount
		updateresource.dhkeyexpsizelimit = resource.dhkeyexpsizelimit
		updateresource.ersa = resource.ersa
		updateresource.ersacount = resource.ersacount
		updateresource.sessreuse = resource.sessreuse
		updateresource.sesstimeout = resource.sesstimeout
		updateresource.cipherredirect = resource.cipherredirect
		updateresource.cipherurl = resource.cipherurl
		updateresource.clientauth = resource.clientauth
		updateresource.clientcert = resource.clientcert
		updateresource.sslredirect = resource.sslredirect
		updateresource.redirectportrewrite = resource.redirectportrewrite
		updateresource.ssl3 = resource.ssl3
		updateresource.tls1 = resource.tls1
		updateresource.tls11 = resource.tls11
		updateresource.tls12 = resource.tls12
		updateresource.tls13 = resource.tls13
		updateresource.snienable = resource.snienable
		updateresource.ocspstapling = resource.ocspstapling
		updateresource.serverauth = resource.serverauth
		updateresource.commonname = resource.commonname
		updateresource.pushenctrigger = resource.pushenctrigger
		updateresource.sendclosenotify = resource.sendclosenotify
		updateresource.cleartextport = resource.cleartextport
		updateresource.insertionencoding = resource.insertionencoding
		updateresource.denysslreneg = resource.denysslreneg
		updateresource.quantumsize = resource.quantumsize
		updateresource.strictcachecks = resource.strictcachecks
		updateresource.encrypttriggerpktcount = resource.encrypttriggerpktcount
		updateresource.pushflag = resource.pushflag
		updateresource.dropreqwithnohostheader = resource.dropreqwithnohostheader
		updateresource.pushenctriggertimeout = resource.pushenctriggertimeout
		updateresource.ssltriggertimeout = resource.ssltriggertimeout
		updateresource.clientauthuseboundcachain = resource.clientauthuseboundcachain
		updateresource.sslinterception = resource.sslinterception
		updateresource.sslireneg = resource.sslireneg
		updateresource.ssliocspcheck = resource.ssliocspcheck
		updateresource.sslimaxsessperserver = resource.sslimaxsessperserver
		updateresource.hsts = resource.hsts
		updateresource.maxage = resource.maxage
		updateresource.includesubdomains = resource.includesubdomains
		updateresource.preload = resource.preload
		updateresource.sessionticket = resource.sessionticket
		updateresource.sessionticketlifetime = resource.sessionticketlifetime
		updateresource.sessionticketkeyrefresh = resource.sessionticketkeyrefresh
		updateresource.sessionticketkeydata = resource.sessionticketkeydata
		updateresource.sessionkeylifetime = resource.sessionkeylifetime
		updateresource.prevsessionkeylifetime = resource.prevsessionkeylifetime
		updateresource.ciphername = resource.ciphername
		updateresource.cipherpriority = resource.cipherpriority
		updateresource.strictsigdigestcheck = resource.strictsigdigestcheck
		updateresource.skipclientcertpolicycheck = resource.skipclientcertpolicycheck
		updateresource.zerorttearlydata = resource.zerorttearlydata
		updateresource.tls13sessionticketsperauthcontext = resource.tls13sessionticketsperauthcontext
		updateresource.dhekeyexchangewithpsk = resource.dhekeyexchangewithpsk
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update sslprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ sslprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of sslprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = sslprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ sslprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ sslprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the sslprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = sslprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = sslprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [sslprofile() for _ in range(len(name))]
						obj = [sslprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = sslprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of sslprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the sslprofile resources configured on NetScaler.
		"""
		try :
			obj = sslprofile()
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
		r""" Use this API to count filtered the set of sslprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = sslprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Denysslreneg:
		NO = "NO"
		FRONTEND_CLIENT = "FRONTEND_CLIENT"
		FRONTEND_CLIENTSERVER = "FRONTEND_CLIENTSERVER"
		ALL = "ALL"
		NONSECURE = "NONSECURE"

	class Sessionticketkeyrefresh:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Quantumsize:
		_4096 = "4096"
		_8192 = "8192"
		_16384 = "16384"

	class Tls1:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dh:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Hsts:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Nonfipsciphers:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Serverauth:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Tls13:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sslinterception:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Snienable:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cipherredirect:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Labeltype:
		vserver = "vserver"
		service = "service"
		policylabel = "policylabel"

	class Strictsigdigestcheck:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Clientcert:
		Mandatory = "Mandatory"
		Optional = "Optional"

	class Crlcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

	class Ocspcheck:
		Mandatory = "Mandatory"
		Optional = "Optional"

	class Ssliverifyservercertforreuse:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Insertionencoding:
		Unicode = "Unicode"
		UTF_8 = "UTF-8"

	class Sslredirect:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ersa:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Strictcachecks:
		YES = "YES"
		NO = "NO"

	class Sslireneg:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Redirectportrewrite:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

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

	class Sessreuse:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ssl3:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sessionticket:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

	class Clientauthuseboundcachain:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dhekeyexchangewithpsk:
		YES = "YES"
		NO = "NO"

	class Ocspstapling:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Preload:
		YES = "YES"
		NO = "NO"

	class Sendclosenotify:
		YES = "YES"
		NO = "NO"

	class Tls11:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Skipclientcertpolicycheck:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dropreqwithnohostheader:
		YES = "YES"
		NO = "NO"

	class Tls12:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Includesubdomains:
		YES = "YES"
		NO = "NO"

	class Ssliocspcheck:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dhkeyexpsizelimit:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Pushenctrigger:
		Always = "Always"
		Merge = "Merge"
		Ignore = "Ignore"
		Timer = "Timer"

	class Clientauth:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Zerorttearlydata:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sslprofiletype:
		BackEnd = "BackEnd"
		FrontEnd = "FrontEnd"

class sslprofile_response(base_response) :
	def __init__(self, length=1) :
		self.sslprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.sslprofile = [sslprofile() for _ in range(length)]

