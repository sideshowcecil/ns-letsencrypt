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

class contentinspectionprofile(base_resource) :
	""" Configuration for ContentInspection profile resource. """
	def __init__(self) :
		self._name = None
		self._type = None
		self._ingressinterface = None
		self._ingressvlan = None
		self._egressinterface = None
		self._iptunnel = None
		self._egressvlan = None
		self.___count = None

	@property
	def name(self) :
		r"""Name of a ContentInspection profile. Must begin with a letter, number, or the underscore \(_\) character. Other characters allowed, after the first character, are the hyphen \(-\), period \(.\), hash \(\#\), space \( \), at \(@\), colon \(:\), and equal \(=\) characters. The name of a IPS profile cannot be changed after it is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks \(for example, "my ips profile" or 'my ips profile'\).<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of a ContentInspection profile. Must begin with a letter, number, or the underscore \(_\) character. Other characters allowed, after the first character, are the hyphen \(-\), period \(.\), hash \(\#\), space \( \), at \(@\), colon \(:\), and equal \(=\) characters. The name of a IPS profile cannot be changed after it is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks \(for example, "my ips profile" or 'my ips profile'\).<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def type(self) :
		r"""Type of ContentInspection profile. Following types are available to configure:
		INLINEINSPECTION : To inspect the packets/requests using IPS.
		MIRROR : To forward cloned packets.<br/>Possible values = InlineInspection, Mirror.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""Type of ContentInspection profile. Following types are available to configure:
		INLINEINSPECTION : To inspect the packets/requests using IPS.
		MIRROR : To forward cloned packets.<br/>Possible values = InlineInspection, Mirror
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	@property
	def ingressinterface(self) :
		r"""Ingress interface for CI profile.It is a mandatory argument while creating an ContentInspection profile of IPS type.
		"""
		try :
			return self._ingressinterface
		except Exception as e:
			raise e

	@ingressinterface.setter
	def ingressinterface(self, ingressinterface) :
		r"""Ingress interface for CI profile.It is a mandatory argument while creating an ContentInspection profile of IPS type.
		"""
		try :
			self._ingressinterface = ingressinterface
		except Exception as e:
			raise e

	@property
	def ingressvlan(self) :
		r"""Ingress Vlan for CI.
		"""
		try :
			return self._ingressvlan
		except Exception as e:
			raise e

	@ingressvlan.setter
	def ingressvlan(self, ingressvlan) :
		r"""Ingress Vlan for CI.
		"""
		try :
			self._ingressvlan = ingressvlan
		except Exception as e:
			raise e

	@property
	def egressinterface(self) :
		r"""Egress interface for CI profile.It is a mandatory argument while creating an ContentInspection profile of type INLINEINSPECTION or MIRROR.
		"""
		try :
			return self._egressinterface
		except Exception as e:
			raise e

	@egressinterface.setter
	def egressinterface(self, egressinterface) :
		r"""Egress interface for CI profile.It is a mandatory argument while creating an ContentInspection profile of type INLINEINSPECTION or MIRROR.
		"""
		try :
			self._egressinterface = egressinterface
		except Exception as e:
			raise e

	@property
	def iptunnel(self) :
		r"""IP Tunnel for CI profile. It is used while creating a ContentInspection profile of type MIRROR when the IDS device is in a different network.<br/>Minimum length =  1<br/>Maximum length =  31.
		"""
		try :
			return self._iptunnel
		except Exception as e:
			raise e

	@iptunnel.setter
	def iptunnel(self, iptunnel) :
		r"""IP Tunnel for CI profile. It is used while creating a ContentInspection profile of type MIRROR when the IDS device is in a different network.<br/>Minimum length =  1<br/>Maximum length =  31
		"""
		try :
			self._iptunnel = iptunnel
		except Exception as e:
			raise e

	@property
	def egressvlan(self) :
		r"""Egress Vlan for CI.
		"""
		try :
			return self._egressvlan
		except Exception as e:
			raise e

	@egressvlan.setter
	def egressvlan(self, egressvlan) :
		r"""Egress Vlan for CI.
		"""
		try :
			self._egressvlan = egressvlan
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(contentinspectionprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.contentinspectionprofile
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
		addresource = contentinspectionprofile()
		addresource.name = resource.name
		addresource.type = resource.type
		addresource.ingressinterface = resource.ingressinterface
		addresource.ingressvlan = resource.ingressvlan
		addresource.egressinterface = resource.egressinterface
		addresource.iptunnel = resource.iptunnel
		addresource.egressvlan = resource.egressvlan
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add contentinspectionprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ contentinspectionprofile() for _ in range(len(resource))]
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
		deleteresource = contentinspectionprofile()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete contentinspectionprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = contentinspectionprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ contentinspectionprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ contentinspectionprofile() for _ in range(len(resource))]
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
		updateresource = contentinspectionprofile()
		updateresource.name = resource.name
		updateresource.egressinterface = resource.egressinterface
		updateresource.ingressinterface = resource.ingressinterface
		updateresource.egressvlan = resource.egressvlan
		updateresource.ingressvlan = resource.ingressvlan
		updateresource.iptunnel = resource.iptunnel
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update contentinspectionprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ contentinspectionprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of contentinspectionprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = contentinspectionprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ contentinspectionprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ contentinspectionprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the contentinspectionprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = contentinspectionprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = contentinspectionprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [contentinspectionprofile() for _ in range(len(name))]
						obj = [contentinspectionprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = contentinspectionprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of contentinspectionprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = contentinspectionprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the contentinspectionprofile resources configured on NetScaler.
		"""
		try :
			obj = contentinspectionprofile()
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
		r""" Use this API to count filtered the set of contentinspectionprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = contentinspectionprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Type:
		InlineInspection = "InlineInspection"
		Mirror = "Mirror"

class contentinspectionprofile_response(base_response) :
	def __init__(self, length=1) :
		self.contentinspectionprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.contentinspectionprofile = [contentinspectionprofile() for _ in range(length)]

