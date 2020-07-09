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

class nscapacity(base_resource) :
	""" Configuration for capacity resource. """
	def __init__(self) :
		self._bandwidth = None
		self._platform = None
		self._vcpu = None
		self._edition = None
		self._unit = None
		self._nodeid = None
		self._actualbandwidth = None
		self._vcpucount = None
		self._maxvcpucount = None
		self._maxbandwidth = None
		self._minbandwidth = None
		self._instancecount = None

	@property
	def bandwidth(self) :
		r"""System bandwidth limit.
		"""
		try :
			return self._bandwidth
		except Exception as e:
			raise e

	@bandwidth.setter
	def bandwidth(self, bandwidth) :
		r"""System bandwidth limit.
		"""
		try :
			self._bandwidth = bandwidth
		except Exception as e:
			raise e

	@property
	def platform(self) :
		r"""appliance platform type.<br/>Possible values = VS10, VE10, VP10, VS25, VE25, VP25, VS200, VE200, VP200, VS1000, VE1000, VP1000, VS3000, VE3000, VP3000, VS5000, VE5000, VP5000, VS8000, VE8000, VP8000, VS10000, VE10000, VP10000, VS15000, VE15000, VP15000, VS25000, VE25000, VP25000, VS40000, VE40000, VP40000, VS100000, VE100000, VP100000, CP1000.
		"""
		try :
			return self._platform
		except Exception as e:
			raise e

	@platform.setter
	def platform(self, platform) :
		r"""appliance platform type.<br/>Possible values = VS10, VE10, VP10, VS25, VE25, VP25, VS200, VE200, VP200, VS1000, VE1000, VP1000, VS3000, VE3000, VP3000, VS5000, VE5000, VP5000, VS8000, VE8000, VP8000, VS10000, VE10000, VP10000, VS15000, VE15000, VP15000, VS25000, VE25000, VP25000, VS40000, VE40000, VP40000, VS100000, VE100000, VP100000, CP1000
		"""
		try :
			self._platform = platform
		except Exception as e:
			raise e

	@property
	def vcpu(self) :
		r"""licensed using vcpu pool.
		"""
		try :
			return self._vcpu
		except Exception as e:
			raise e

	@vcpu.setter
	def vcpu(self, vcpu) :
		r"""licensed using vcpu pool.
		"""
		try :
			self._vcpu = vcpu
		except Exception as e:
			raise e

	@property
	def edition(self) :
		r"""Product edition.<br/>Possible values = Standard, Enterprise, Platinum.
		"""
		try :
			return self._edition
		except Exception as e:
			raise e

	@edition.setter
	def edition(self, edition) :
		r"""Product edition.<br/>Possible values = Standard, Enterprise, Platinum
		"""
		try :
			self._edition = edition
		except Exception as e:
			raise e

	@property
	def unit(self) :
		r"""Bandwidth unit.<br/>Possible values = Gbps, Mbps.
		"""
		try :
			return self._unit
		except Exception as e:
			raise e

	@unit.setter
	def unit(self, unit) :
		r"""Bandwidth unit.<br/>Possible values = Gbps, Mbps
		"""
		try :
			self._unit = unit
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
	def actualbandwidth(self) :
		r"""Bandwith in MBPS.
		"""
		try :
			return self._actualbandwidth
		except Exception as e:
			raise e

	@property
	def vcpucount(self) :
		r"""number of vCPUs licensed.<br/>Minimum value =  1<br/>Maximum value =  20.
		"""
		try :
			return self._vcpucount
		except Exception as e:
			raise e

	@property
	def maxvcpucount(self) :
		r"""number of max vCPUs.<br/>Minimum value =  1<br/>Maximum value =  20.
		"""
		try :
			return self._maxvcpucount
		except Exception as e:
			raise e

	@property
	def maxbandwidth(self) :
		r"""Maximum Bandwidth.
		"""
		try :
			return self._maxbandwidth
		except Exception as e:
			raise e

	@property
	def minbandwidth(self) :
		r"""Minimum Bandwidth.
		"""
		try :
			return self._minbandwidth
		except Exception as e:
			raise e

	@property
	def instancecount(self) :
		r"""VPX will consume one instance and MPX will consume zero instance.
		"""
		try :
			return self._instancecount
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nscapacity_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nscapacity
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def filter_update_parameters(cls, resource) :
		r""" Use this function to create a resource with only update operation specific parameters.
		"""
		updateresource = nscapacity()
		updateresource.bandwidth = resource.bandwidth
		updateresource.platform = resource.platform
		updateresource.vcpu = resource.vcpu
		updateresource.edition = resource.edition
		updateresource.unit = resource.unit
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nscapacity.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nscapacity resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nscapacity()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nscapacity resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nscapacity()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the nscapacity resources that are configured on netscaler.
	# This uses nscapacity_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = nscapacity()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Edition:
		Standard = "Standard"
		Enterprise = "Enterprise"
		Platinum = "Platinum"

	class Platform:
		VS10 = "VS10"
		VE10 = "VE10"
		VP10 = "VP10"
		VS25 = "VS25"
		VE25 = "VE25"
		VP25 = "VP25"
		VS200 = "VS200"
		VE200 = "VE200"
		VP200 = "VP200"
		VS1000 = "VS1000"
		VE1000 = "VE1000"
		VP1000 = "VP1000"
		VS3000 = "VS3000"
		VE3000 = "VE3000"
		VP3000 = "VP3000"
		VS5000 = "VS5000"
		VE5000 = "VE5000"
		VP5000 = "VP5000"
		VS8000 = "VS8000"
		VE8000 = "VE8000"
		VP8000 = "VP8000"
		VS10000 = "VS10000"
		VE10000 = "VE10000"
		VP10000 = "VP10000"
		VS15000 = "VS15000"
		VE15000 = "VE15000"
		VP15000 = "VP15000"
		VS25000 = "VS25000"
		VE25000 = "VE25000"
		VP25000 = "VP25000"
		VS40000 = "VS40000"
		VE40000 = "VE40000"
		VP40000 = "VP40000"
		VS100000 = "VS100000"
		VE100000 = "VE100000"
		VP100000 = "VP100000"
		CP1000 = "CP1000"

	class Unit:
		Gbps = "Gbps"
		Mbps = "Mbps"

class nscapacity_response(base_response) :
	def __init__(self, length=1) :
		self.nscapacity = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nscapacity = [nscapacity() for _ in range(length)]

