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

class systemrestorepoint(base_resource) :
	""" Configuration for Setting restorepoints for auto restore resource. """
	def __init__(self) :
		self._filename = None
		self._backupfilename = None
		self._techsuprtname = None
		self._creationtime = None
		self._version = None
		self._createdby = None
		self._ipaddress = None
		self.___count = None

	@property
	def filename(self) :
		r"""Name of the restore point.<br/>Minimum length =  1.
		"""
		try :
			return self._filename
		except Exception as e:
			raise e

	@filename.setter
	def filename(self, filename) :
		r"""Name of the restore point.<br/>Minimum length =  1
		"""
		try :
			self._filename = filename
		except Exception as e:
			raise e

	@property
	def backupfilename(self) :
		r"""backup file name of the restore points created internally.
		"""
		try :
			return self._backupfilename
		except Exception as e:
			raise e

	@property
	def techsuprtname(self) :
		r"""Tech support bundle name created during creation of restore points.
		"""
		try :
			return self._techsuprtname
		except Exception as e:
			raise e

	@property
	def creationtime(self) :
		r"""Creation time of the restore points.
		"""
		try :
			return self._creationtime
		except Exception as e:
			raise e

	@property
	def version(self) :
		r"""Build version of the restore points.
		"""
		try :
			return self._version
		except Exception as e:
			raise e

	@property
	def createdby(self) :
		r"""Name of user who created the restore points.
		"""
		try :
			return self._createdby
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		r"""Ip of Netscaler box where the restore point was created.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(systemrestorepoint_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.systemrestorepoint
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.filename is not None :
				return str(self.filename)
			return None
		except Exception as e :
			raise e



	@classmethod
	def create(cls, client, resource) :
		r""" Use this API to create systemrestorepoint.
		"""
		try :
			if type(resource) is not list :
				createresource = systemrestorepoint()
				createresource.filename = resource.filename
				return createresource.perform_operation(client,"create")
			else :
				if (resource and len(resource) > 0) :
					createresources = [ systemrestorepoint() for _ in range(len(resource))]
					for i in range(len(resource)) :
						createresources[i].filename = resource[i].filename
				result = cls.perform_operation_bulk_request(client, createresources,"create")
			return result
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = systemrestorepoint()
		deleteresource.filename = resource.filename
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete systemrestorepoint.
		"""
		try :
			if type(resource) is not list :
				deleteresource = systemrestorepoint()
				if type(resource) !=  type(deleteresource):
					deleteresource.filename = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ systemrestorepoint() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].filename = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ systemrestorepoint() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i] = cls.filter_delete_parameters(resource)
				result = cls.delete_bulk_request(client, deleteresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the systemrestorepoint resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = systemrestorepoint()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = systemrestorepoint()
					obj.filename = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [systemrestorepoint() for _ in range(len(name))]
						obj = [systemrestorepoint() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = systemrestorepoint()
							obj[i].filename = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of systemrestorepoint resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = systemrestorepoint()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the systemrestorepoint resources configured on NetScaler.
		"""
		try :
			obj = systemrestorepoint()
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
		r""" Use this API to count filtered the set of systemrestorepoint resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = systemrestorepoint()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


class systemrestorepoint_response(base_response) :
	def __init__(self, length=1) :
		self.systemrestorepoint = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.systemrestorepoint = [systemrestorepoint() for _ in range(length)]

