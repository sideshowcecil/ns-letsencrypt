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

class xmdeployment(base_resource) :
	""" Configuration for XenMobile Deployment resource. """
	def __init__(self) :
		self._name = None
		self._frompackage = None
		self._config = None
		self._meta = None
		self.___count = None

	@property
	def name(self) :
		r"""XenMobile deployment name.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""XenMobile deployment name.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def frompackage(self) :
		r"""XenMobile package name.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._frompackage
		except Exception as e:
			raise e

	@frompackage.setter
	def frompackage(self, frompackage) :
		r"""XenMobile package name.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._frompackage = frompackage
		except Exception as e:
			raise e

	@property
	def config(self) :
		r"""XenMobile deployment config data.<br/>Minimum length =  1<br/>Maximum length =  4095.
		"""
		try :
			return self._config
		except Exception as e:
			raise e

	@config.setter
	def config(self, config) :
		r"""XenMobile deployment config data.<br/>Minimum length =  1<br/>Maximum length =  4095
		"""
		try :
			self._config = config
		except Exception as e:
			raise e

	@property
	def meta(self) :
		r"""XenMobile deployment meta data.<br/>Minimum length =  1<br/>Maximum length =  16383.
		"""
		try :
			return self._meta
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(xmdeployment_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.xmdeployment
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
		addresource = xmdeployment()
		addresource.name = resource.name
		addresource.frompackage = resource.frompackage
		addresource.config = resource.config
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add xmdeployment.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ xmdeployment() for _ in range(len(resource))]
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
		deleteresource = xmdeployment()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete xmdeployment.
		"""
		try :
			if type(resource) is not list :
				deleteresource = xmdeployment()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ xmdeployment() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ xmdeployment() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i] = cls.filter_delete_parameters(resource)
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the xmdeployment resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = xmdeployment()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = xmdeployment()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [xmdeployment() for _ in range(len(name))]
						obj = [xmdeployment() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = xmdeployment()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of xmdeployment resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = xmdeployment()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the xmdeployment resources configured on NetScaler.
		"""
		try :
			obj = xmdeployment()
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
		r""" Use this API to count filtered the set of xmdeployment resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = xmdeployment()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class xmdeployment_response(base_response) :
	def __init__(self, length=1) :
		self.xmdeployment = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.xmdeployment = [xmdeployment() for _ in range(length)]

