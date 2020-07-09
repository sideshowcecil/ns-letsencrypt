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

class lsnpool_lsnip_binding(base_resource) :
	""" Binding class showing the lsnip that can be bound to lsnpool.
	"""
	def __init__(self) :
		self._lsnip = None
		self._ownernode = None
		self._poolname = None
		self.___count = None

	@property
	def poolname(self) :
		r"""Name for the LSN pool. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN pool is created. The following requirement applies only to the Citrix ADC CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn pool1" or 'lsn pool1').<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._poolname
		except Exception as e:
			raise e

	@poolname.setter
	def poolname(self, poolname) :
		r"""Name for the LSN pool. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN pool is created. The following requirement applies only to the Citrix ADC CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn pool1" or 'lsn pool1').<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._poolname = poolname
		except Exception as e:
			raise e

	@property
	def ownernode(self) :
		r"""ID(s) of cluster node(s) on which command is to be executed.<br/>Minimum value =  0<br/>Maximum value =  31.
		"""
		try :
			return self._ownernode
		except Exception as e:
			raise e

	@ownernode.setter
	def ownernode(self, ownernode) :
		r"""ID(s) of cluster node(s) on which command is to be executed.<br/>Minimum value =  0<br/>Maximum value =  31
		"""
		try :
			self._ownernode = ownernode
		except Exception as e:
			raise e

	@property
	def lsnip(self) :
		r"""IPv4 address or a range of IPv4 addresses to be used as NAT IP address(es) for LSN.
		After the pool is created, these IPv4 addresses are added to the Citrix ADC as Citrix ADC owned IP address of type LSN. A maximum of 4096 IP addresses can be bound to an LSN pool. An LSN IP address associated with an LSN pool cannot be shared with other LSN pools. IP addresses specified for this parameter must not already exist on the Citrix ADC as any Citrix ADC owned IP addresses. In the command line interface, separate the range with a hyphen. For example: 10.102.29.30-10.102.29.189. You can later remove some or all the LSN IP addresses from the pool, and add IP addresses to the LSN pool.
		By default , arp is enabled on LSN IP address but, you can disable it using command - "set ns ip"
		.<br/>Minimum length =  1.
		"""
		try :
			return self._lsnip
		except Exception as e:
			raise e

	@lsnip.setter
	def lsnip(self, lsnip) :
		r"""IPv4 address or a range of IPv4 addresses to be used as NAT IP address(es) for LSN.
		After the pool is created, these IPv4 addresses are added to the Citrix ADC as Citrix ADC owned IP address of type LSN. A maximum of 4096 IP addresses can be bound to an LSN pool. An LSN IP address associated with an LSN pool cannot be shared with other LSN pools. IP addresses specified for this parameter must not already exist on the Citrix ADC as any Citrix ADC owned IP addresses. In the command line interface, separate the range with a hyphen. For example: 10.102.29.30-10.102.29.189. You can later remove some or all the LSN IP addresses from the pool, and add IP addresses to the LSN pool.
		By default , arp is enabled on LSN IP address but, you can disable it using command - "set ns ip"
		.<br/>Minimum length =  1
		"""
		try :
			self._lsnip = lsnip
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(lsnpool_lsnip_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.lsnpool_lsnip_binding
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.poolname is not None :
				return str(self.poolname)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_add_parameters(cls, resource) :
		r""" Use this function to create a resource with only add operation specific parameters.
		"""
		addresource = lsnpool_lsnip_binding()
		addresource.poolname = resource.poolname
		addresource.ownernode = resource.ownernode
		addresource.lsnip = resource.lsnip
		return addresource

	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = cls.filter_add_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [lsnpool_lsnip_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_add_parameters(resource[i])
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = lsnpool_lsnip_binding()
		deleteresource.poolname = resource.poolname
		deleteresource.ownernode = resource.ownernode
		deleteresource.lsnip = resource.lsnip
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [lsnpool_lsnip_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i] = cls.filter_delete_parameters(resource[i])
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, poolname="", option_="") :
		r""" Use this API to fetch lsnpool_lsnip_binding resources.
		"""
		try :
			if not poolname :
				obj = lsnpool_lsnip_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = lsnpool_lsnip_binding()
				obj.poolname = poolname
				response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, poolname, filter_) :
		r""" Use this API to fetch filtered set of lsnpool_lsnip_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnpool_lsnip_binding()
			obj.poolname = poolname
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, poolname) :
		r""" Use this API to count lsnpool_lsnip_binding resources configued on NetScaler.
		"""
		try :
			obj = lsnpool_lsnip_binding()
			obj.poolname = poolname
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, poolname, filter_) :
		r""" Use this API to count the filtered set of lsnpool_lsnip_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = lsnpool_lsnip_binding()
			obj.poolname = poolname
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

class lsnpool_lsnip_binding_response(base_response) :
	def __init__(self, length=1) :
		self.lsnpool_lsnip_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.lsnpool_lsnip_binding = [lsnpool_lsnip_binding() for _ in range(length)]

