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

class authenticationoauthidpprofile(base_resource) :
	""" Configuration for OAuth Identity Provider (IdP) profile resource. """
	def __init__(self) :
		self._name = None
		self._clientid = None
		self._clientsecret = None
		self._redirecturl = None
		self._issuer = None
		self._configservice = None
		self._audience = None
		self._skewtime = None
		self._defaultauthenticationgroup = None
		self._relyingpartymetadataurl = None
		self._refreshinterval = None
		self._encrypttoken = None
		self._signatureservice = None
		self._signaturealg = None
		self._attributes = None
		self._sendpassword = None
		self._oauthstatus = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the new OAuth Identity Provider (IdP) single sign-on profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after an action is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the new OAuth Identity Provider (IdP) single sign-on profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after an action is created.
		The following requirement applies only to the Citrix ADC CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def clientid(self) :
		r"""Unique identity of the relying party requesting for authentication.<br/>Minimum length =  1.
		"""
		try :
			return self._clientid
		except Exception as e:
			raise e

	@clientid.setter
	def clientid(self, clientid) :
		r"""Unique identity of the relying party requesting for authentication.<br/>Minimum length =  1
		"""
		try :
			self._clientid = clientid
		except Exception as e:
			raise e

	@property
	def clientsecret(self) :
		r"""Unique secret string to authorize relying party at authorization server.<br/>Minimum length =  1.
		"""
		try :
			return self._clientsecret
		except Exception as e:
			raise e

	@clientsecret.setter
	def clientsecret(self, clientsecret) :
		r"""Unique secret string to authorize relying party at authorization server.<br/>Minimum length =  1
		"""
		try :
			self._clientsecret = clientsecret
		except Exception as e:
			raise e

	@property
	def redirecturl(self) :
		r"""URL endpoint on relying party to which the OAuth token is to be sent.<br/>Minimum length =  1.
		"""
		try :
			return self._redirecturl
		except Exception as e:
			raise e

	@redirecturl.setter
	def redirecturl(self, redirecturl) :
		r"""URL endpoint on relying party to which the OAuth token is to be sent.<br/>Minimum length =  1
		"""
		try :
			self._redirecturl = redirecturl
		except Exception as e:
			raise e

	@property
	def issuer(self) :
		r"""The name to be used in requests sent from	Citrix ADC to IdP to uniquely identify Citrix ADC.<br/>Minimum length =  1.
		"""
		try :
			return self._issuer
		except Exception as e:
			raise e

	@issuer.setter
	def issuer(self, issuer) :
		r"""The name to be used in requests sent from	Citrix ADC to IdP to uniquely identify Citrix ADC.<br/>Minimum length =  1
		"""
		try :
			self._issuer = issuer
		except Exception as e:
			raise e

	@property
	def configservice(self) :
		r"""Name of the entity that is used to obtain configuration for the current authentication request. It is used only in Citrix Cloud.<br/>Minimum length =  1.
		"""
		try :
			return self._configservice
		except Exception as e:
			raise e

	@configservice.setter
	def configservice(self, configservice) :
		r"""Name of the entity that is used to obtain configuration for the current authentication request. It is used only in Citrix Cloud.<br/>Minimum length =  1
		"""
		try :
			self._configservice = configservice
		except Exception as e:
			raise e

	@property
	def audience(self) :
		r"""Audience for which token is being sent by Citrix ADC IdP. This is typically entity name or url that represents the recipient.
		"""
		try :
			return self._audience
		except Exception as e:
			raise e

	@audience.setter
	def audience(self, audience) :
		r"""Audience for which token is being sent by Citrix ADC IdP. This is typically entity name or url that represents the recipient.
		"""
		try :
			self._audience = audience
		except Exception as e:
			raise e

	@property
	def skewtime(self) :
		r"""This option specifies the duration for which the token sent by Citrix ADC IdP is valid. For example, if skewTime is 10, then token would be valid from (current time - 10) min to (current time + 10) min, ie 20min in all.<br/>Default value: 5.
		"""
		try :
			return self._skewtime
		except Exception as e:
			raise e

	@skewtime.setter
	def skewtime(self, skewtime) :
		r"""This option specifies the duration for which the token sent by Citrix ADC IdP is valid. For example, if skewTime is 10, then token would be valid from (current time - 10) min to (current time + 10) min, ie 20min in all.<br/>Default value: 5
		"""
		try :
			self._skewtime = skewtime
		except Exception as e:
			raise e

	@property
	def defaultauthenticationgroup(self) :
		r"""This is the group that is added to user sessions that match current IdP policy. It can be used in policies to identify relying party trust.
		"""
		try :
			return self._defaultauthenticationgroup
		except Exception as e:
			raise e

	@defaultauthenticationgroup.setter
	def defaultauthenticationgroup(self, defaultauthenticationgroup) :
		r"""This is the group that is added to user sessions that match current IdP policy. It can be used in policies to identify relying party trust.
		"""
		try :
			self._defaultauthenticationgroup = defaultauthenticationgroup
		except Exception as e:
			raise e

	@property
	def relyingpartymetadataurl(self) :
		r"""This is the endpoint at which Citrix ADC IdP can get details about Relying Party (RP) being configured. Metadata response should include endpoints for jwks_uri for RP public key(s).
		"""
		try :
			return self._relyingpartymetadataurl
		except Exception as e:
			raise e

	@relyingpartymetadataurl.setter
	def relyingpartymetadataurl(self, relyingpartymetadataurl) :
		r"""This is the endpoint at which Citrix ADC IdP can get details about Relying Party (RP) being configured. Metadata response should include endpoints for jwks_uri for RP public key(s).
		"""
		try :
			self._relyingpartymetadataurl = relyingpartymetadataurl
		except Exception as e:
			raise e

	@property
	def refreshinterval(self) :
		r"""Interval at which Relying Party metadata is refreshed.<br/>Default value: 50.
		"""
		try :
			return self._refreshinterval
		except Exception as e:
			raise e

	@refreshinterval.setter
	def refreshinterval(self, refreshinterval) :
		r"""Interval at which Relying Party metadata is refreshed.<br/>Default value: 50
		"""
		try :
			self._refreshinterval = refreshinterval
		except Exception as e:
			raise e

	@property
	def encrypttoken(self) :
		r"""Option to encrypt token when Citrix ADC IDP sends one.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._encrypttoken
		except Exception as e:
			raise e

	@encrypttoken.setter
	def encrypttoken(self, encrypttoken) :
		r"""Option to encrypt token when Citrix ADC IDP sends one.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._encrypttoken = encrypttoken
		except Exception as e:
			raise e

	@property
	def signatureservice(self) :
		r"""Name of the service in cloud used to sign the data. This is applicable only if signature if offloaded to cloud.<br/>Minimum length =  1.
		"""
		try :
			return self._signatureservice
		except Exception as e:
			raise e

	@signatureservice.setter
	def signatureservice(self, signatureservice) :
		r"""Name of the service in cloud used to sign the data. This is applicable only if signature if offloaded to cloud.<br/>Minimum length =  1
		"""
		try :
			self._signatureservice = signatureservice
		except Exception as e:
			raise e

	@property
	def signaturealg(self) :
		r"""Algorithm to be used to sign OpenID tokens.<br/>Default value: RS256<br/>Possible values = RS256, RS512.
		"""
		try :
			return self._signaturealg
		except Exception as e:
			raise e

	@signaturealg.setter
	def signaturealg(self, signaturealg) :
		r"""Algorithm to be used to sign OpenID tokens.<br/>Default value: RS256<br/>Possible values = RS256, RS512
		"""
		try :
			self._signaturealg = signaturealg
		except Exception as e:
			raise e

	@property
	def attributes(self) :
		r"""Name-Value pairs of attributes to be inserted in idtoken. Configuration format is name=value_expr@@@name2=value2_expr@@@.
		'@@@' is used as delimiter between Name-Value pairs. name is a literal string whose value is 127 characters and does not contain '=' character.
		Value is advanced policy expression terminated by @@@ delimiter. Last value need not contain the delimiter.
		"""
		try :
			return self._attributes
		except Exception as e:
			raise e

	@attributes.setter
	def attributes(self, attributes) :
		r"""Name-Value pairs of attributes to be inserted in idtoken. Configuration format is name=value_expr@@@name2=value2_expr@@@.
		'@@@' is used as delimiter between Name-Value pairs. name is a literal string whose value is 127 characters and does not contain '=' character.
		Value is advanced policy expression terminated by @@@ delimiter. Last value need not contain the delimiter.
		"""
		try :
			self._attributes = attributes
		except Exception as e:
			raise e

	@property
	def sendpassword(self) :
		r"""Option to send encrypted password in idtoken.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._sendpassword
		except Exception as e:
			raise e

	@sendpassword.setter
	def sendpassword(self, sendpassword) :
		r"""Option to send encrypted password in idtoken.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._sendpassword = sendpassword
		except Exception as e:
			raise e

	@property
	def oauthstatus(self) :
		r"""Describes status information of oauth idp metadata fetch process.<br/>Default value: INIT<br/>Possible values = INIT, CERTFETCH, AADFORGRAPH, GRAPH, AADFORMDM, MDMINFO, COMPLETE.
		"""
		try :
			return self._oauthstatus
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(authenticationoauthidpprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.authenticationoauthidpprofile
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
		addresource = authenticationoauthidpprofile()
		addresource.name = resource.name
		addresource.clientid = resource.clientid
		addresource.clientsecret = resource.clientsecret
		addresource.redirecturl = resource.redirecturl
		addresource.issuer = resource.issuer
		addresource.configservice = resource.configservice
		addresource.audience = resource.audience
		addresource.skewtime = resource.skewtime
		addresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
		addresource.relyingpartymetadataurl = resource.relyingpartymetadataurl
		addresource.refreshinterval = resource.refreshinterval
		addresource.encrypttoken = resource.encrypttoken
		addresource.signatureservice = resource.signatureservice
		addresource.signaturealg = resource.signaturealg
		addresource.attributes = resource.attributes
		addresource.sendpassword = resource.sendpassword
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add authenticationoauthidpprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ authenticationoauthidpprofile() for _ in range(len(resource))]
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
		deleteresource = authenticationoauthidpprofile()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete authenticationoauthidpprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = authenticationoauthidpprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationoauthidpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ authenticationoauthidpprofile() for _ in range(len(resource))]
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
		updateresource = authenticationoauthidpprofile()
		updateresource.name = resource.name
		updateresource.clientid = resource.clientid
		updateresource.clientsecret = resource.clientsecret
		updateresource.redirecturl = resource.redirecturl
		updateresource.issuer = resource.issuer
		updateresource.configservice = resource.configservice
		updateresource.audience = resource.audience
		updateresource.skewtime = resource.skewtime
		updateresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
		updateresource.relyingpartymetadataurl = resource.relyingpartymetadataurl
		updateresource.refreshinterval = resource.refreshinterval
		updateresource.encrypttoken = resource.encrypttoken
		updateresource.signatureservice = resource.signatureservice
		updateresource.signaturealg = resource.signaturealg
		updateresource.attributes = resource.attributes
		updateresource.sendpassword = resource.sendpassword
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update authenticationoauthidpprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ authenticationoauthidpprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of authenticationoauthidpprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = authenticationoauthidpprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationoauthidpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ authenticationoauthidpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the authenticationoauthidpprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = authenticationoauthidpprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = authenticationoauthidpprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [authenticationoauthidpprofile() for _ in range(len(name))]
						obj = [authenticationoauthidpprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = authenticationoauthidpprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of authenticationoauthidpprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationoauthidpprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the authenticationoauthidpprofile resources configured on NetScaler.
		"""
		try :
			obj = authenticationoauthidpprofile()
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
		r""" Use this API to count filtered the set of authenticationoauthidpprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = authenticationoauthidpprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Sendpassword:
		ON = "ON"
		OFF = "OFF"

	class Oauthstatus:
		INIT = "INIT"
		CERTFETCH = "CERTFETCH"
		AADFORGRAPH = "AADFORGRAPH"
		GRAPH = "GRAPH"
		AADFORMDM = "AADFORMDM"
		MDMINFO = "MDMINFO"
		COMPLETE = "COMPLETE"

	class Encrypttoken:
		ON = "ON"
		OFF = "OFF"

	class Signaturealg:
		RS256 = "RS256"
		RS512 = "RS512"

class authenticationoauthidpprofile_response(base_response) :
	def __init__(self, length=1) :
		self.authenticationoauthidpprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.authenticationoauthidpprofile = [authenticationoauthidpprofile() for _ in range(length)]

