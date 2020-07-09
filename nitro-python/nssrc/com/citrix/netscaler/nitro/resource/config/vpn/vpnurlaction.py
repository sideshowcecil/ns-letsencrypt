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

class vpnurlaction(base_resource) :
	""" Configuration for VPN url action resource. """
	def __init__(self) :
		self._name = None
		self._linkname = None
		self._actualurl = None
		self._vservername = None
		self._clientlessaccess = None
		self._comment = None
		self._iconurl = None
		self._ssotype = None
		self._applicationtype = None
		self._samlssoprofile = None
		self._newname = None
		self.___count = None

	@property
	def name(self) :
		r"""Name of the bookmark link.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the bookmark link.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def linkname(self) :
		r"""Description of the bookmark link. The description appears in the Access Interface.<br/>Minimum length =  1.
		"""
		try :
			return self._linkname
		except Exception as e:
			raise e

	@linkname.setter
	def linkname(self, linkname) :
		r"""Description of the bookmark link. The description appears in the Access Interface.<br/>Minimum length =  1
		"""
		try :
			self._linkname = linkname
		except Exception as e:
			raise e

	@property
	def actualurl(self) :
		r"""Web address for the bookmark link.<br/>Minimum length =  1.
		"""
		try :
			return self._actualurl
		except Exception as e:
			raise e

	@actualurl.setter
	def actualurl(self, actualurl) :
		r"""Web address for the bookmark link.<br/>Minimum length =  1
		"""
		try :
			self._actualurl = actualurl
		except Exception as e:
			raise e

	@property
	def vservername(self) :
		r"""Name of the associated vserver to handle selfAuth SSO.
		"""
		try :
			return self._vservername
		except Exception as e:
			raise e

	@vservername.setter
	def vservername(self, vservername) :
		r"""Name of the associated vserver to handle selfAuth SSO.
		"""
		try :
			self._vservername = vservername
		except Exception as e:
			raise e

	@property
	def clientlessaccess(self) :
		r"""If clientless access to the resource hosting the link is allowed, also use clientless access for the bookmarked web address in the Secure Client Access based session. Allows single sign-on and other HTTP processing on NetScaler Gateway for HTTPS resources.<br/>Default value: OFF<br/>Possible values = ON, OFF.
		"""
		try :
			return self._clientlessaccess
		except Exception as e:
			raise e

	@clientlessaccess.setter
	def clientlessaccess(self, clientlessaccess) :
		r"""If clientless access to the resource hosting the link is allowed, also use clientless access for the bookmarked web address in the Secure Client Access based session. Allows single sign-on and other HTTP processing on NetScaler Gateway for HTTPS resources.<br/>Default value: OFF<br/>Possible values = ON, OFF
		"""
		try :
			self._clientlessaccess = clientlessaccess
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Any comments associated with the bookmark link.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Any comments associated with the bookmark link.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def iconurl(self) :
		r"""URL to fetch icon file for displaying this resource.
		"""
		try :
			return self._iconurl
		except Exception as e:
			raise e

	@iconurl.setter
	def iconurl(self, iconurl) :
		r"""URL to fetch icon file for displaying this resource.
		"""
		try :
			self._iconurl = iconurl
		except Exception as e:
			raise e

	@property
	def ssotype(self) :
		r"""Single sign on type for unified gateway.<br/>Possible values = unifiedgateway, selfauth, samlauth.
		"""
		try :
			return self._ssotype
		except Exception as e:
			raise e

	@ssotype.setter
	def ssotype(self, ssotype) :
		r"""Single sign on type for unified gateway.<br/>Possible values = unifiedgateway, selfauth, samlauth
		"""
		try :
			self._ssotype = ssotype
		except Exception as e:
			raise e

	@property
	def applicationtype(self) :
		r"""The type of application this VPN URL represents. Possible values are CVPN/SaaS/VPN.<br/>Possible values = CVPN, VPN, SaaS.
		"""
		try :
			return self._applicationtype
		except Exception as e:
			raise e

	@applicationtype.setter
	def applicationtype(self, applicationtype) :
		r"""The type of application this VPN URL represents. Possible values are CVPN/SaaS/VPN.<br/>Possible values = CVPN, VPN, SaaS
		"""
		try :
			self._applicationtype = applicationtype
		except Exception as e:
			raise e

	@property
	def samlssoprofile(self) :
		r"""Profile to be used for doing SAML SSO.
		"""
		try :
			return self._samlssoprofile
		except Exception as e:
			raise e

	@samlssoprofile.setter
	def samlssoprofile(self, samlssoprofile) :
		r"""Profile to be used for doing SAML SSO.
		"""
		try :
			self._samlssoprofile = samlssoprofile
		except Exception as e:
			raise e

	@property
	def newname(self) :
		r"""New name for the vpn urlAction.
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my vpnurl action" or 'my vpnurl action').<br/>Minimum length =  1.
		"""
		try :
			return self._newname
		except Exception as e:
			raise e

	@newname.setter
	def newname(self, newname) :
		r"""New name for the vpn urlAction.
		Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
		The following requirement applies only to the NetScaler CLI:
		If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my vpnurl action" or 'my vpnurl action').<br/>Minimum length =  1
		"""
		try :
			self._newname = newname
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(vpnurlaction_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.vpnurlaction
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
		addresource = vpnurlaction()
		addresource.name = resource.name
		addresource.linkname = resource.linkname
		addresource.actualurl = resource.actualurl
		addresource.vservername = resource.vservername
		addresource.clientlessaccess = resource.clientlessaccess
		addresource.comment = resource.comment
		addresource.iconurl = resource.iconurl
		addresource.ssotype = resource.ssotype
		addresource.applicationtype = resource.applicationtype
		addresource.samlssoprofile = resource.samlssoprofile
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add vpnurlaction.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ vpnurlaction() for _ in range(len(resource))]
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
		deleteresource = vpnurlaction()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete vpnurlaction.
		"""
		try :
			if type(resource) is not list :
				deleteresource = vpnurlaction()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpnurlaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ vpnurlaction() for _ in range(len(resource))]
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
		updateresource = vpnurlaction()
		updateresource.name = resource.name
		updateresource.linkname = resource.linkname
		updateresource.actualurl = resource.actualurl
		updateresource.vservername = resource.vservername
		updateresource.clientlessaccess = resource.clientlessaccess
		updateresource.comment = resource.comment
		updateresource.iconurl = resource.iconurl
		updateresource.ssotype = resource.ssotype
		updateresource.applicationtype = resource.applicationtype
		updateresource.samlssoprofile = resource.samlssoprofile
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update vpnurlaction.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ vpnurlaction() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of vpnurlaction resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = vpnurlaction()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ vpnurlaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ vpnurlaction() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def rename(cls, client, resource, new_name) :
		r""" Use this API to rename a vpnurlaction resource.
		"""
		try :
			renameresource = vpnurlaction()
			if type(resource) == cls :
				renameresource.name = resource.name
			else :
				renameresource.name = resource
			return renameresource.rename_resource(client,new_name)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the vpnurlaction resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = vpnurlaction()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = vpnurlaction()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [vpnurlaction() for _ in range(len(name))]
						obj = [vpnurlaction() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = vpnurlaction()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of vpnurlaction resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnurlaction()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the vpnurlaction resources configured on NetScaler.
		"""
		try :
			obj = vpnurlaction()
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
		r""" Use this API to count filtered the set of vpnurlaction resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = vpnurlaction()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Applicationtype:
		CVPN = "CVPN"
		VPN = "VPN"
		SaaS = "SaaS"

	class Clientlessaccess:
		ON = "ON"
		OFF = "OFF"

	class Ssotype:
		unifiedgateway = "unifiedgateway"
		selfauth = "selfauth"
		samlauth = "samlauth"

class vpnurlaction_response(base_response) :
	def __init__(self, length=1) :
		self.vpnurlaction = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.vpnurlaction = [vpnurlaction() for _ in range(length)]

