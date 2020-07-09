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

class ssllogprofile(base_resource) :
	""" Configuration for SSL logging Profile resource. """
	def __init__(self) :
		self._name = None
		self._ssllogclauth = None
		self._ssllogclauthfailures = None
		self._sslloghs = None
		self._sslloghsfailures = None
		self.___count = None

	@property
	def name(self) :
		r"""The name of the ssllogprofile.<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""The name of the ssllogprofile.<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def ssllogclauth(self) :
		r"""log all SSL ClAuth events.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ssllogclauth
		except Exception as e:
			raise e

	@ssllogclauth.setter
	def ssllogclauth(self, ssllogclauth) :
		r"""log all SSL ClAuth events.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ssllogclauth = ssllogclauth
		except Exception as e:
			raise e

	@property
	def ssllogclauthfailures(self) :
		r"""log all SSL ClAuth error events.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._ssllogclauthfailures
		except Exception as e:
			raise e

	@ssllogclauthfailures.setter
	def ssllogclauthfailures(self, ssllogclauthfailures) :
		r"""log all SSL ClAuth error events.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._ssllogclauthfailures = ssllogclauthfailures
		except Exception as e:
			raise e

	@property
	def sslloghs(self) :
		r"""log all SSL HS events.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sslloghs
		except Exception as e:
			raise e

	@sslloghs.setter
	def sslloghs(self, sslloghs) :
		r"""log all SSL HS events.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sslloghs = sslloghs
		except Exception as e:
			raise e

	@property
	def sslloghsfailures(self) :
		r"""log all SSL HS error events.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._sslloghsfailures
		except Exception as e:
			raise e

	@sslloghsfailures.setter
	def sslloghsfailures(self, sslloghsfailures) :
		r"""log all SSL HS error events.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._sslloghsfailures = sslloghsfailures
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(ssllogprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.ssllogprofile
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
		addresource = ssllogprofile()
		addresource.name = resource.name
		addresource.ssllogclauth = resource.ssllogclauth
		addresource.ssllogclauthfailures = resource.ssllogclauthfailures
		addresource.sslloghs = resource.sslloghs
		addresource.sslloghsfailures = resource.sslloghsfailures
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add ssllogprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ ssllogprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						addresources[i] = cls.filter_add_parameters(resource[i])
				result = cls.add_bulk_request(client, addresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = ssllogprofile()
		updateresource.name = resource.name
		updateresource.ssllogclauth = resource.ssllogclauth
		updateresource.ssllogclauthfailures = resource.ssllogclauthfailures
		updateresource.sslloghs = resource.sslloghs
		updateresource.sslloghsfailures = resource.sslloghsfailures
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update ssllogprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ ssllogprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of ssllogprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = ssllogprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ ssllogprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ ssllogprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = ssllogprofile()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete ssllogprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = ssllogprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ ssllogprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ ssllogprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i] = cls.filter_delete_parameters(resource)
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the ssllogprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = ssllogprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = ssllogprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [ssllogprofile() for _ in range(len(name))]
						obj = [ssllogprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = ssllogprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of ssllogprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = ssllogprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the ssllogprofile resources configured on NetScaler.
		"""
		try :
			obj = ssllogprofile()
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
		r""" Use this API to count filtered the set of ssllogprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = ssllogprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Ssllogclauthfailures:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sslloghs:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Sslloghsfailures:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Ssllogclauth:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class ssllogprofile_response(base_response) :
	def __init__(self, length=1) :
		self.ssllogprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.ssllogprofile = [ssllogprofile() for _ in range(length)]

