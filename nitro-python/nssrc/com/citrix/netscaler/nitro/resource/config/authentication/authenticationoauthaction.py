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

class authenticationoauthaction(base_resource) :
	""" Configuration for OAuth authentication action resource. """
	def __init__(self) :
		self._name = None
		self._oauthtype = None
		self._authorizationendpoint = None
		self._tokenendpoint = None
		self._idtokendecryptendpoint = None
		self._clientid = None
		self._clientsecret = None
		self._defaultauthenticationgroup = None
		self._attribute1 = None
		self._attribute2 = None
		self._attribute3 = None
		self._attribute4 = None
		self._attribute5 = None
		self._attribute6 = None
		self._attribute7 = None
		self._attribute8 = None
		self._attribute9 = None
		self._attribute10 = None
		self._attribute11 = None
		self._attribute12 = None
		self._attribute13 = None
		self._attribute14 = None
		self._attribute15 = None
		self._attribute16 = None
		self._attributes = None
		self._tenantid = None
		self._graphendpoint = None
		self._refreshinterval = None
		self._certendpoint = None
		self._audience = None
		self._usernamefield = None
		self._skewtime = None
		self._issuer = None
		self._userinfourl = None
		self._certfilepath = None
		self._granttype = None
		self._authentication = None
		self._oauthstatus = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the OAuth Authentication action. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the profile is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication action" or 'my authentication action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the OAuth Authentication action. 
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the profile is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication action" or 'my authentication action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def oauthtype(self) :
		r"""Type of the OAuth implementation. Default value is generic implementation that is applicable for most deployments.<br/>Default value: GENERIC<br/>Possible values = GENERIC, INTUNE, ATHENA.
		"""
		try :
			return self._oauthtype
		except Exception as e:
			raise e

	@oauthtype.setter
	def oauthtype(self, oauthtype) :
		r"""Type of the OAuth implementation. Default value is generic implementation that is applicable for most deployments.<br/>Default value: GENERIC<br/>Possible values = GENERIC, INTUNE, ATHENA
		"""
		try :
			self._oauthtype = oauthtype
		except Exception as e:
			raise e

	@property
	def authorizationendpoint(self) :
		r"""Authorization endpoint/url to which unauthenticated user will be redirected. Citrix ADC redirects user to this endpoint by adding query parameters including clientid. If this parameter not specified then as default value we take Token Endpoint/URL value. Please note that Authorization Endpoint or Token Endpoint is mandatory for oauthAction.
		"""
		try :
			return self._authorizationendpoint
		except Exception as e:
			raise e

	@authorizationendpoint.setter
	def authorizationendpoint(self, authorizationendpoint) :
		r"""Authorization endpoint/url to which unauthenticated user will be redirected. Citrix ADC redirects user to this endpoint by adding query parameters including clientid. If this parameter not specified then as default value we take Token Endpoint/URL value. Please note that Authorization Endpoint or Token Endpoint is mandatory for oauthAction.
		"""
		try :
			self._authorizationendpoint = authorizationendpoint
		except Exception as e:
			raise e

	@property
	def tokenendpoint(self) :
		r"""URL to which OAuth token will be posted to verify its authenticity. User obtains this token from Authorization server upon successful authentication. Citrix ADC will validate presented token by posting it to the URL configured.
		"""
		try :
			return self._tokenendpoint
		except Exception as e:
			raise e

	@tokenendpoint.setter
	def tokenendpoint(self, tokenendpoint) :
		r"""URL to which OAuth token will be posted to verify its authenticity. User obtains this token from Authorization server upon successful authentication. Citrix ADC will validate presented token by posting it to the URL configured.
		"""
		try :
			self._tokenendpoint = tokenendpoint
		except Exception as e:
			raise e

	@property
	def idtokendecryptendpoint(self) :
		r"""URL to which obtained idtoken will be posted to get a decrypted user identity. Encrypted idtoken will be obtained by posting OAuth token to token endpoint. In order to decrypt idtoken, Citrix ADC posts request to the URL configured.
		"""
		try :
			return self._idtokendecryptendpoint
		except Exception as e:
			raise e

	@idtokendecryptendpoint.setter
	def idtokendecryptendpoint(self, idtokendecryptendpoint) :
		r"""URL to which obtained idtoken will be posted to get a decrypted user identity. Encrypted idtoken will be obtained by posting OAuth token to token endpoint. In order to decrypt idtoken, Citrix ADC posts request to the URL configured.
		"""
		try :
			self._idtokendecryptendpoint = idtokendecryptendpoint
		except Exception as e:
			raise e

	@property
	def clientid(self) :
		r"""Unique identity of the client/user who is getting authenticated. Authorization server infers client configuration using this ID.<br/>Minimum length =  1.
		"""
		try :
			return self._clientid
		except Exception as e:
			raise e

	@clientid.setter
	def clientid(self, clientid) :
		r"""Unique identity of the client/user who is getting authenticated. Authorization server infers client configuration using this ID.<br/>Minimum length =  1
		"""
		try :
			self._clientid = clientid
		except Exception as e:
			raise e

	@property
	def clientsecret(self) :
		r"""Secret string established by user and authorization server.<br/>Minimum length =  1.
		"""
		try :
			return self._clientsecret
		except Exception as e:
			raise e

	@clientsecret.setter
	def clientsecret(self, clientsecret) :
		r"""Secret string established by user and authorization server.<br/>Minimum length =  1
		"""
		try :
			self._clientsecret = clientsecret
		except Exception as e:
			raise e

	@property
	def defaultauthenticationgroup(self) :
		r"""This is the default group that is chosen when the authentication succeeds in addition to extracted groups.
		"""
		try :
			return self._defaultauthenticationgroup
		except Exception as e:
			raise e

	@defaultauthenticationgroup.setter
	def defaultauthenticationgroup(self, defaultauthenticationgroup) :
		r"""This is the default group that is chosen when the authentication succeeds in addition to extracted groups.
		"""
		try :
			self._defaultauthenticationgroup = defaultauthenticationgroup
		except Exception as e:
			raise e

	@property
	def attribute1(self) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute1.
		"""
		try :
			return self._attribute1
		except Exception as e:
			raise e

	@attribute1.setter
	def attribute1(self, attribute1) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute1.
		"""
		try :
			self._attribute1 = attribute1
		except Exception as e:
			raise e

	@property
	def attribute2(self) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute2.
		"""
		try :
			return self._attribute2
		except Exception as e:
			raise e

	@attribute2.setter
	def attribute2(self, attribute2) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute2.
		"""
		try :
			self._attribute2 = attribute2
		except Exception as e:
			raise e

	@property
	def attribute3(self) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute3.
		"""
		try :
			return self._attribute3
		except Exception as e:
			raise e

	@attribute3.setter
	def attribute3(self, attribute3) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute3.
		"""
		try :
			self._attribute3 = attribute3
		except Exception as e:
			raise e

	@property
	def attribute4(self) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute4.
		"""
		try :
			return self._attribute4
		except Exception as e:
			raise e

	@attribute4.setter
	def attribute4(self, attribute4) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute4.
		"""
		try :
			self._attribute4 = attribute4
		except Exception as e:
			raise e

	@property
	def attribute5(self) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute5.
		"""
		try :
			return self._attribute5
		except Exception as e:
			raise e

	@attribute5.setter
	def attribute5(self, attribute5) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute5.
		"""
		try :
			self._attribute5 = attribute5
		except Exception as e:
			raise e

	@property
	def attribute6(self) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute6.
		"""
		try :
			return self._attribute6
		except Exception as e:
			raise e

	@attribute6.setter
	def attribute6(self, attribute6) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute6.
		"""
		try :
			self._attribute6 = attribute6
		except Exception as e:
			raise e

	@property
	def attribute7(self) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute7.
		"""
		try :
			return self._attribute7
		except Exception as e:
			raise e

	@attribute7.setter
	def attribute7(self, attribute7) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute7.
		"""
		try :
			self._attribute7 = attribute7
		except Exception as e:
			raise e

	@property
	def attribute8(self) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute8.
		"""
		try :
			return self._attribute8
		except Exception as e:
			raise e

	@attribute8.setter
	def attribute8(self, attribute8) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute8.
		"""
		try :
			self._attribute8 = attribute8
		except Exception as e:
			raise e

	@property
	def attribute9(self) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute9.
		"""
		try :
			return self._attribute9
		except Exception as e:
			raise e

	@attribute9.setter
	def attribute9(self, attribute9) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute9.
		"""
		try :
			self._attribute9 = attribute9
		except Exception as e:
			raise e

	@property
	def attribute10(self) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute10.
		"""
		try :
			return self._attribute10
		except Exception as e:
			raise e

	@attribute10.setter
	def attribute10(self, attribute10) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute10.
		"""
		try :
			self._attribute10 = attribute10
		except Exception as e:
			raise e

	@property
	def attribute11(self) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute11.
		"""
		try :
			return self._attribute11
		except Exception as e:
			raise e

	@attribute11.setter
	def attribute11(self, attribute11) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute11.
		"""
		try :
			self._attribute11 = attribute11
		except Exception as e:
			raise e

	@property
	def attribute12(self) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute12.
		"""
		try :
			return self._attribute12
		except Exception as e:
			raise e

	@attribute12.setter
	def attribute12(self, attribute12) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute12.
		"""
		try :
			self._attribute12 = attribute12
		except Exception as e:
			raise e

	@property
	def attribute13(self) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute13.
		"""
		try :
			return self._attribute13
		except Exception as e:
			raise e

	@attribute13.setter
	def attribute13(self, attribute13) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute13.
		"""
		try :
			self._attribute13 = attribute13
		except Exception as e:
			raise e

	@property
	def attribute14(self) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute14.
		"""
		try :
			return self._attribute14
		except Exception as e:
			raise e

	@attribute14.setter
	def attribute14(self, attribute14) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute14.
		"""
		try :
			self._attribute14 = attribute14
		except Exception as e:
			raise e

	@property
	def attribute15(self) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute15.
		"""
		try :
			return self._attribute15
		except Exception as e:
			raise e

	@attribute15.setter
	def attribute15(self, attribute15) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute15.
		"""
		try :
			self._attribute15 = attribute15
		except Exception as e:
			raise e

	@property
	def attribute16(self) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute16.
		"""
		try :
			return self._attribute16
		except Exception as e:
			raise e

	@attribute16.setter
	def attribute16(self, attribute16) :
		r"""Name of the attribute to be extracted from OAuth Token and to be stored in the attribute16.
		"""
		try :
			self._attribute16 = attribute16
		except Exception as e:
			raise e

	@property
	def attributes(self) :
		r"""List of attribute names separated by ',' which needs to be extracted.
		Note that preceding and trailing spaces will be removed.
		Attribute name can be 127 bytes and total length of this string should not cross 1023 bytes.
		These attributes have multi-value support separated by ',' and stored as key-value pair in AAA session.
		"""
		try :
			return self._attributes
		except Exception as e:
			raise e

	@attributes.setter
	def attributes(self, attributes) :
		r"""List of attribute names separated by ',' which needs to be extracted.
		Note that preceding and trailing spaces will be removed.
		Attribute name can be 127 bytes and total length of this string should not cross 1023 bytes.
		These attributes have multi-value support separated by ',' and stored as key-value pair in AAA session.
		"""
		try :
			self._attributes = attributes
		except Exception as e:
			raise e

	@property
	def tenantid(self) :
		r"""TenantID of the application. This is usually specific to providers such as Microsoft and usually refers to the deployment identifier.
		"""
		try :
			return self._tenantid
		except Exception as e:
			raise e

	@tenantid.setter
	def tenantid(self, tenantid) :
		r"""TenantID of the application. This is usually specific to providers such as Microsoft and usually refers to the deployment identifier.
		"""
		try :
			self._tenantid = tenantid
		except Exception as e:
			raise e

	@property
	def graphendpoint(self) :
		r"""URL of the Graph API service to learn Enterprise Mobility Services (EMS) endpoints.
		"""
		try :
			return self._graphendpoint
		except Exception as e:
			raise e

	@graphendpoint.setter
	def graphendpoint(self, graphendpoint) :
		r"""URL of the Graph API service to learn Enterprise Mobility Services (EMS) endpoints.
		"""
		try :
			self._graphendpoint = graphendpoint
		except Exception as e:
			raise e

	@property
	def refreshinterval(self) :
		r"""Interval at which services are monitored for necessary configuration.<br/>Default value: 1440.
		"""
		try :
			return self._refreshinterval
		except Exception as e:
			raise e

	@refreshinterval.setter
	def refreshinterval(self, refreshinterval) :
		r"""Interval at which services are monitored for necessary configuration.<br/>Default value: 1440
		"""
		try :
			self._refreshinterval = refreshinterval
		except Exception as e:
			raise e

	@property
	def certendpoint(self) :
		r"""URL of the endpoint that contains JWKs (Json Web Key) for JWT (Json Web Token) verification.
		"""
		try :
			return self._certendpoint
		except Exception as e:
			raise e

	@certendpoint.setter
	def certendpoint(self, certendpoint) :
		r"""URL of the endpoint that contains JWKs (Json Web Key) for JWT (Json Web Token) verification.
		"""
		try :
			self._certendpoint = certendpoint
		except Exception as e:
			raise e

	@property
	def audience(self) :
		r"""Audience for which token sent by Authorization server is applicable. This is typically entity name or url that represents the recipient.
		"""
		try :
			return self._audience
		except Exception as e:
			raise e

	@audience.setter
	def audience(self, audience) :
		r"""Audience for which token sent by Authorization server is applicable. This is typically entity name or url that represents the recipient.
		"""
		try :
			self._audience = audience
		except Exception as e:
			raise e

	@property
	def usernamefield(self) :
		r"""Attribute in the token from which username should be extracted.<br/>Minimum length =  1.
		"""
		try :
			return self._usernamefield
		except Exception as e:
			raise e

	@usernamefield.setter
	def usernamefield(self, usernamefield) :
		r"""Attribute in the token from which username should be extracted.<br/>Minimum length =  1
		"""
		try :
			self._usernamefield = usernamefield
		except Exception as e:
			raise e

	@property
	def skewtime(self) :
		r"""This option specifies the allowed clock skew in number of minutes that Citrix ADC allows on an incoming token. For example, if skewTime is 10, then token would be valid from (current time - 10) min to (current time + 10) min, ie 20min in all.<br/>Default value: 5.
		"""
		try :
			return self._skewtime
		except Exception as e:
			raise e

	@skewtime.setter
	def skewtime(self, skewtime) :
		r"""This option specifies the allowed clock skew in number of minutes that Citrix ADC allows on an incoming token. For example, if skewTime is 10, then token would be valid from (current time - 10) min to (current time + 10) min, ie 20min in all.<br/>Default value: 5
		"""
		try :
			self._skewtime = skewtime
		except Exception as e:
			raise e

	@property
	def issuer(self) :
		r"""Identity of the server whose tokens are to be accepted.
		"""
		try :
			return self._issuer
		except Exception as e:
			raise e

	@issuer.setter
	def issuer(self, issuer) :
		r"""Identity of the server whose tokens are to be accepted.
		"""
		try :
			self._issuer = issuer
		except Exception as e:
			raise e

	@property
	def userinfourl(self) :
		r"""URL to which OAuth access token will be posted to obtain user information.
		"""
		try :
			return self._userinfourl
		except Exception as e:
			raise e

	@userinfourl.setter
	def userinfourl(self, userinfourl) :
		r"""URL to which OAuth access token will be posted to obtain user information.
		"""
		try :
			self._userinfourl = userinfourl
		except Exception as e:
			raise e

	@property
	def certfilepath(self) :
		r"""Path to the file that contains JWKs (Json Web Key) for JWT (Json Web Token) verification.
		"""
		try :
			return self._certfilepath
		except Exception as e:
			raise e

	@certfilepath.setter
	def certfilepath(self, certfilepath) :
		r"""Path to the file that contains JWKs (Json Web Key) for JWT (Json Web Token) verification.
		"""
		try :
			self._certfilepath = certfilepath
		except Exception as e:
			raise e

	@property
	def granttype(self) :
		r"""Grant type support. value can be code or password.<br/>Default value: CODE<br/>Possible values = CODE, PASSWORD.
		"""
		try :
			return self._granttype
		except Exception as e:
			raise e

	@granttype.setter
	def granttype(self, granttype) :
		r"""Grant type support. value can be code or password.<br/>Default value: CODE<br/>Possible values = CODE, PASSWORD
		"""
		try :
			self._granttype = granttype
		except Exception as e:
			raise e

	@property
	def authentication(self) :
		r"""If authentication is disabled, password is not sent in the request. .<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._authentication
		except Exception as e:
			raise e

	@authentication.setter
	def authentication(self, authentication) :
		r"""If authentication is disabled, password is not sent in the request. .<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._authentication = authentication
		except Exception as e:
			raise e

	@property
	def oauthstatus(self) :
		r"""Describes status information of oauth server.<br/>Default value: INIT<br/>Possible values = INIT, CERTFETCH, AADFORGRAPH, GRAPH, AADFORMDM, MDMINFO, COMPLETE.
		"""
		try :
			return self._oauthstatus
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(authenticationoauthaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationoauthaction
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
		addresource = authenticationoauthaction()
		addresource.name = resource.name
		addresource.oauthtype = resource.oauthtype
		addresource.authorizationendpoint = resource.authorizationendpoint
		addresource.tokenendpoint = resource.tokenendpoint
		addresource.idtokendecryptendpoint = resource.idtokendecryptendpoint
		addresource.clientid = resource.clientid
		addresource.clientsecret = resource.clientsecret
		addresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
		addresource.attribute1 = resource.attribute1
		addresource.attribute2 = resource.attribute2
		addresource.attribute3 = resource.attribute3
		addresource.attribute4 = resource.attribute4
		addresource.attribute5 = resource.attribute5
		addresource.attribute6 = resource.attribute6
		addresource.attribute7 = resource.attribute7
		addresource.attribute8 = resource.attribute8
		addresource.attribute9 = resource.attribute9
		addresource.attribute10 = resource.attribute10
		addresource.attribute11 = resource.attribute11
		addresource.attribute12 = resource.attribute12
		addresource.attribute13 = resource.attribute13
		addresource.attribute14 = resource.attribute14
		addresource.attribute15 = resource.attribute15
		addresource.attribute16 = resource.attribute16
		addresource.attributes = resource.attributes
		addresource.tenantid = resource.tenantid
		addresource.graphendpoint = resource.graphendpoint
		addresource.refreshinterval = resource.refreshinterval
		addresource.certendpoint = resource.certendpoint
		addresource.audience = resource.audience
		addresource.usernamefield = resource.usernamefield
		addresource.skewtime = resource.skewtime
		addresource.issuer = resource.issuer
		addresource.userinfourl = resource.userinfourl
		addresource.certfilepath = resource.certfilepath
		addresource.granttype = resource.granttype
		addresource.authentication = resource.authentication
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add authenticationoauthaction.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ authenticationoauthaction() for _ in range(len(resource))]
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
		deleteresource = authenticationoauthaction()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete authenticationoauthaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = authenticationoauthaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationoauthaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationoauthaction() for _ in range(len(resource))]
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
		updateresource = authenticationoauthaction()
		updateresource.name = resource.name
		updateresource.oauthtype = resource.oauthtype
		updateresource.authorizationendpoint = resource.authorizationendpoint
		updateresource.tokenendpoint = resource.tokenendpoint
		updateresource.idtokendecryptendpoint = resource.idtokendecryptendpoint
		updateresource.clientid = resource.clientid
		updateresource.clientsecret = resource.clientsecret
		updateresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
		updateresource.attribute1 = resource.attribute1
		updateresource.attribute2 = resource.attribute2
		updateresource.attribute3 = resource.attribute3
		updateresource.attribute4 = resource.attribute4
		updateresource.attribute5 = resource.attribute5
		updateresource.attribute6 = resource.attribute6
		updateresource.attribute7 = resource.attribute7
		updateresource.attribute8 = resource.attribute8
		updateresource.attribute9 = resource.attribute9
		updateresource.attribute10 = resource.attribute10
		updateresource.attribute11 = resource.attribute11
		updateresource.attribute12 = resource.attribute12
		updateresource.attribute13 = resource.attribute13
		updateresource.attribute14 = resource.attribute14
		updateresource.attribute15 = resource.attribute15
		updateresource.attribute16 = resource.attribute16
		updateresource.attributes = resource.attributes
		updateresource.tenantid = resource.tenantid
		updateresource.graphendpoint = resource.graphendpoint
		updateresource.refreshinterval = resource.refreshinterval
		updateresource.certendpoint = resource.certendpoint
		updateresource.audience = resource.audience
		updateresource.usernamefield = resource.usernamefield
		updateresource.skewtime = resource.skewtime
		updateresource.issuer = resource.issuer
		updateresource.userinfourl = resource.userinfourl
		updateresource.certfilepath = resource.certfilepath
		updateresource.granttype = resource.granttype
		updateresource.authentication = resource.authentication
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update authenticationoauthaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ authenticationoauthaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of authenticationoauthaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = authenticationoauthaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationoauthaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationoauthaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the authenticationoauthaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = authenticationoauthaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = authenticationoauthaction()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [authenticationoauthaction() for _ in range(len(name))]
						obj = [authenticationoauthaction() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = authenticationoauthaction()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of authenticationoauthaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationoauthaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the authenticationoauthaction resources configured on NetScaler.
		"""
		try :
			obj = authenticationoauthaction()
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
		r""" Use this API to count filtered the set of authenticationoauthaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationoauthaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Authentication:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Oauthstatus:
		INIT = "INIT"
		CERTFETCH = "CERTFETCH"
		AADFORGRAPH = "AADFORGRAPH"
		GRAPH = "GRAPH"
		AADFORMDM = "AADFORMDM"
		MDMINFO = "MDMINFO"
		COMPLETE = "COMPLETE"

	class Granttype:
		CODE = "CODE"
		PASSWORD = "PASSWORD"

	class Oauthtype:
		GENERIC = "GENERIC"
		INTUNE = "INTUNE"
		ATHENA = "ATHENA"

class authenticationoauthaction_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationoauthaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationoauthaction = [authenticationoauthaction() for _ in range(length)]

