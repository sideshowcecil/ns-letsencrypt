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

class nslicenseserver(base_resource) :
	""" Configuration for licenseserver resource. """
	def __init__(self) :
		self._licenseserverip = None
		self._servername = None
		self._port = None
		self._nodeid = None
		self._status = None
		self._grace = None
		self._gptimeleft = None
		self.___count = None

	@property
	def licenseserverip(self) :
		r"""IP address of the License server.<br/>Minimum length =  1.
		"""
		try :
			return self._licenseserverip
		except Exception as e:
			raise e

	@licenseserverip.setter
	def licenseserverip(self, licenseserverip) :
		r"""IP address of the License server.<br/>Minimum length =  1
		"""
		try :
			self._licenseserverip = licenseserverip
		except Exception as e:
			raise e

	@property
	def servername(self) :
		r"""Fully qualified domain name of the License server.
		"""
		try :
			return self._servername
		except Exception as e:
			raise e

	@servername.setter
	def servername(self, servername) :
		r"""Fully qualified domain name of the License server.
		"""
		try :
			self._servername = servername
		except Exception as e:
			raise e

	@property
	def port(self) :
		r"""License server port.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		r"""License server port.
		"""
		try :
			self._port = port
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
	def status(self) :
		r"""Status of license server.
		"""
		try :
			return self._status
		except Exception as e:
			raise e

	@property
	def grace(self) :
		r"""Grace status of server.
		"""
		try :
			return self._grace
		except Exception as e:
			raise e

	@property
	def gptimeleft(self) :
		r"""Grace time left.
		"""
		try :
			return self._gptimeleft
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nslicenseserver_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nslicenseserver
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.licenseserverip is not None :
				return str(self.licenseserverip)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = nslicenseserver()
		addresource.licenseserverip = resource.licenseserverip
		addresource.servername = resource.servername
		addresource.port = resource.port
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add nslicenseserver.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nslicenseserver() for _ in range(len(resource))]
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
		deleteresource = nslicenseserver()
		deleteresource.licenseserverip = resource.licenseserverip
		deleteresource.servername = resource.servername
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete nslicenseserver.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nslicenseserver()
				if type(resource) !=  type(deleteresource):
					deleteresource.licenseserverip = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nslicenseserver() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].licenseserverip = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nslicenseserver() for _ in range(len(resource))]
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
		updateresource = nslicenseserver()
		updateresource.licenseserverip = resource.licenseserverip
		updateresource.servername = resource.servername
		updateresource.port = resource.port
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nslicenseserver.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nslicenseserver() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nslicenseserver resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nslicenseserver()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) != cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					option_ = options()
					option_.args = nitro_util.object_to_string_withoutquotes(name)
					response = name.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) != cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [nslicenseserver() for _ in range(len(name))]
						for i in range(len(name)) :
							option_ = options()
							option_.args = nitro_util.object_to_string_withoutquotes(name[i])
							response[i] = name[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the nslicenseserver resources that are configured on netscaler.
	# This uses nslicenseserver_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = nslicenseserver()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of nslicenseserver resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nslicenseserver()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the nslicenseserver resources configured on NetScaler.
		"""
		try :
			obj = nslicenseserver()
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
		r""" Use this API to count filtered the set of nslicenseserver resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nslicenseserver()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class nslicenseserver_response(base_response) :
	def __init__(self, length=1) :
		self.nslicenseserver = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nslicenseserver = [nslicenseserver() for _ in range(length)]

