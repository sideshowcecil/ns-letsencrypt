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

class nsvpxparam(base_resource) :
	""" Configuration for "VPX" resource. """
	def __init__(self) :
		self._cpuyield = None
		self._ownernode = None
		self.___count = None

	@property
	def cpuyield(self) :
		r"""This setting applicable in virtual appliances, is to affect the cpu yield(relinquishing the cpu resources) in any hypervised environment.
		* There are 3 options for the behavior:
		1. YES - Allow the Virtual Appliance to yield its vCPUs periodically, if there is no data traffic.
		2. NO - Virtual Appliance will not yield the vCPU.
		3. DEFAULT - Restores the default behaviour, according to the license.
		* Its behavior in different scenarios:
		1. As this setting is node specific only, it will not be propagated to other nodes, when executed on Cluster(CLIP) and HA(Primary).
		2. In cluster setup, use '-ownerNode' to specify ID of the cluster node.
		3. This setting is a system wide implementation and not granular to vCPUs.
		4. No effect on the management PE.<br/>Possible values = DEFAULT, YES, NO.
		"""
		try :
			return self._cpuyield
		except Exception as e:
			raise e

	@cpuyield.setter
	def cpuyield(self, cpuyield) :
		r"""This setting applicable in virtual appliances, is to affect the cpu yield(relinquishing the cpu resources) in any hypervised environment.
		* There are 3 options for the behavior:
		1. YES - Allow the Virtual Appliance to yield its vCPUs periodically, if there is no data traffic.
		2. NO - Virtual Appliance will not yield the vCPU.
		3. DEFAULT - Restores the default behaviour, according to the license.
		* Its behavior in different scenarios:
		1. As this setting is node specific only, it will not be propagated to other nodes, when executed on Cluster(CLIP) and HA(Primary).
		2. In cluster setup, use '-ownerNode' to specify ID of the cluster node.
		3. This setting is a system wide implementation and not granular to vCPUs.
		4. No effect on the management PE.<br/>Possible values = DEFAULT, YES, NO
		"""
		try :
			self._cpuyield = cpuyield
		except Exception as e:
			raise e

	@property
	def ownernode(self) :
		r"""ID of the cluster node for which you are setting the cpuyield. It can be configured only through the cluster IP address.<br/>Default value: 255<br/>Maximum length =  31.
		"""
		try :
			return self._ownernode
		except Exception as e:
			raise e

	@ownernode.setter
	def ownernode(self, ownernode) :
		r"""ID of the cluster node for which you are setting the cpuyield. It can be configured only through the cluster IP address.<br/>Default value: 255<br/>Maximum length =  31
		"""
		try :
			self._ownernode = ownernode
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nsvpxparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nsvpxparam
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.ownernode is not None :
				return str(self.ownernode)
			return None
		except Exception as e :
			raise e



	@classmethod
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = nsvpxparam()
		updateresource.cpuyield = resource.cpuyield
		updateresource.ownernode = resource.ownernode
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nsvpxparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nsvpxparam() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nsvpxparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nsvpxparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of nsvpxparam resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsvpxparam()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the nsvpxparam resources configured on NetScaler.
		"""
		try :
			obj = nsvpxparam()
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
		r""" Use this API to count filtered the set of nsvpxparam resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nsvpxparam()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Cpuyield:
		DEFAULT = "DEFAULT"
		YES = "YES"
		NO = "NO"

class nsvpxparam_response(base_response) :
	def __init__(self, length=1) :
		self.nsvpxparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nsvpxparam = [nsvpxparam() for _ in range(length)]

