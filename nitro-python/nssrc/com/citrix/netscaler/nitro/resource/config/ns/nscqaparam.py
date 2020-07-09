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

class nscqaparam(base_resource) :
	""" Configuration for cqaparam resource. """
	def __init__(self) :
		self._harqretxdelay = None
		self._net1label = None
		self._minrttnet1 = None
		self._lr1coeflist = None
		self._lr1probthresh = None
		self._net1cclscale = None
		self._net1csqscale = None
		self._net1logcoef = None
		self._net2label = None
		self._minrttnet2 = None
		self._lr2coeflist = None
		self._lr2probthresh = None
		self._net2cclscale = None
		self._net2csqscale = None
		self._net2logcoef = None
		self._net3label = None
		self._minrttnet3 = None
		self._net3cclscale = None
		self._net3csqscale = None
		self._net3logcoef = None

	@property
	def harqretxdelay(self) :
		r"""HARQ retransmission delay (in ms).<br/>Default value: 0<br/>Minimum length =  1<br/>Maximum length =  64000.
		"""
		try :
			return self._harqretxdelay
		except Exception as e:
			raise e

	@harqretxdelay.setter
	def harqretxdelay(self, harqretxdelay) :
		r"""HARQ retransmission delay (in ms).<br/>Default value: 0<br/>Minimum length =  1<br/>Maximum length =  64000
		"""
		try :
			self._harqretxdelay = harqretxdelay
		except Exception as e:
			raise e

	@property
	def net1label(self) :
		r"""Name of the network label.<br/>Maximum length =  15.
		"""
		try :
			return self._net1label
		except Exception as e:
			raise e

	@net1label.setter
	def net1label(self, net1label) :
		r"""Name of the network label.<br/>Maximum length =  15
		"""
		try :
			self._net1label = net1label
		except Exception as e:
			raise e

	@property
	def minrttnet1(self) :
		r"""MIN RTT (in ms) for the first network.<br/>Default value: 0<br/>Maximum length =  6400.
		"""
		try :
			return self._minrttnet1
		except Exception as e:
			raise e

	@minrttnet1.setter
	def minrttnet1(self, minrttnet1) :
		r"""MIN RTT (in ms) for the first network.<br/>Default value: 0<br/>Maximum length =  6400
		"""
		try :
			self._minrttnet1 = minrttnet1
		except Exception as e:
			raise e

	@property
	def lr1coeflist(self) :
		r"""coefficients values for Label1.
		"""
		try :
			return self._lr1coeflist
		except Exception as e:
			raise e

	@lr1coeflist.setter
	def lr1coeflist(self, lr1coeflist) :
		r"""coefficients values for Label1.
		"""
		try :
			self._lr1coeflist = lr1coeflist
		except Exception as e:
			raise e

	@property
	def lr1probthresh(self) :
		r"""Probability threshold values for LR model to differentiate between NET1 and reset(NET2 and NET3).<br/>Default value: 0<br/>Maximum length =  1.
		"""
		try :
			return self._lr1probthresh
		except Exception as e:
			raise e

	@lr1probthresh.setter
	def lr1probthresh(self, lr1probthresh) :
		r"""Probability threshold values for LR model to differentiate between NET1 and reset(NET2 and NET3).<br/>Default value: 0<br/>Maximum length =  1
		"""
		try :
			self._lr1probthresh = lr1probthresh
		except Exception as e:
			raise e

	@property
	def net1cclscale(self) :
		r"""Three congestion level scores limits corresponding to None, Low, Medium.
		"""
		try :
			return self._net1cclscale
		except Exception as e:
			raise e

	@net1cclscale.setter
	def net1cclscale(self, net1cclscale) :
		r"""Three congestion level scores limits corresponding to None, Low, Medium.
		"""
		try :
			self._net1cclscale = net1cclscale
		except Exception as e:
			raise e

	@property
	def net1csqscale(self) :
		r"""Three signal quality level scores limits corresponding to Excellent, Good, Fair.
		"""
		try :
			return self._net1csqscale
		except Exception as e:
			raise e

	@net1csqscale.setter
	def net1csqscale(self, net1csqscale) :
		r"""Three signal quality level scores limits corresponding to Excellent, Good, Fair.
		"""
		try :
			self._net1csqscale = net1csqscale
		except Exception as e:
			raise e

	@property
	def net1logcoef(self) :
		r"""Connection quality ranking Log coefficients of network 1.
		"""
		try :
			return self._net1logcoef
		except Exception as e:
			raise e

	@net1logcoef.setter
	def net1logcoef(self, net1logcoef) :
		r"""Connection quality ranking Log coefficients of network 1.
		"""
		try :
			self._net1logcoef = net1logcoef
		except Exception as e:
			raise e

	@property
	def net2label(self) :
		r"""Name of the network label 2.<br/>Maximum length =  15.
		"""
		try :
			return self._net2label
		except Exception as e:
			raise e

	@net2label.setter
	def net2label(self, net2label) :
		r"""Name of the network label 2.<br/>Maximum length =  15
		"""
		try :
			self._net2label = net2label
		except Exception as e:
			raise e

	@property
	def minrttnet2(self) :
		r"""MIN RTT (in ms) for the second network.<br/>Default value: 0<br/>Maximum length =  6400.
		"""
		try :
			return self._minrttnet2
		except Exception as e:
			raise e

	@minrttnet2.setter
	def minrttnet2(self, minrttnet2) :
		r"""MIN RTT (in ms) for the second network.<br/>Default value: 0<br/>Maximum length =  6400
		"""
		try :
			self._minrttnet2 = minrttnet2
		except Exception as e:
			raise e

	@property
	def lr2coeflist(self) :
		r"""coefficients values for Label 2.
		"""
		try :
			return self._lr2coeflist
		except Exception as e:
			raise e

	@lr2coeflist.setter
	def lr2coeflist(self, lr2coeflist) :
		r"""coefficients values for Label 2.
		"""
		try :
			self._lr2coeflist = lr2coeflist
		except Exception as e:
			raise e

	@property
	def lr2probthresh(self) :
		r"""Probability threshold values for LR model to differentiate between NET2 and NET3.<br/>Default value: 0<br/>Maximum length =  1.
		"""
		try :
			return self._lr2probthresh
		except Exception as e:
			raise e

	@lr2probthresh.setter
	def lr2probthresh(self, lr2probthresh) :
		r"""Probability threshold values for LR model to differentiate between NET2 and NET3.<br/>Default value: 0<br/>Maximum length =  1
		"""
		try :
			self._lr2probthresh = lr2probthresh
		except Exception as e:
			raise e

	@property
	def net2cclscale(self) :
		r"""Three congestion level scores limits corresponding to None, Low, Medium.
		"""
		try :
			return self._net2cclscale
		except Exception as e:
			raise e

	@net2cclscale.setter
	def net2cclscale(self, net2cclscale) :
		r"""Three congestion level scores limits corresponding to None, Low, Medium.
		"""
		try :
			self._net2cclscale = net2cclscale
		except Exception as e:
			raise e

	@property
	def net2csqscale(self) :
		r"""Three signal quality level scores limits corresponding to Excellent, Good, Fair.
		"""
		try :
			return self._net2csqscale
		except Exception as e:
			raise e

	@net2csqscale.setter
	def net2csqscale(self, net2csqscale) :
		r"""Three signal quality level scores limits corresponding to Excellent, Good, Fair.
		"""
		try :
			self._net2csqscale = net2csqscale
		except Exception as e:
			raise e

	@property
	def net2logcoef(self) :
		r"""Connnection quality ranking Log coefficients of network 2.
		"""
		try :
			return self._net2logcoef
		except Exception as e:
			raise e

	@net2logcoef.setter
	def net2logcoef(self, net2logcoef) :
		r"""Connnection quality ranking Log coefficients of network 2.
		"""
		try :
			self._net2logcoef = net2logcoef
		except Exception as e:
			raise e

	@property
	def net3label(self) :
		r"""Name of the network label 3.<br/>Maximum length =  15.
		"""
		try :
			return self._net3label
		except Exception as e:
			raise e

	@net3label.setter
	def net3label(self, net3label) :
		r"""Name of the network label 3.<br/>Maximum length =  15
		"""
		try :
			self._net3label = net3label
		except Exception as e:
			raise e

	@property
	def minrttnet3(self) :
		r"""MIN RTT (in ms) for the third network.<br/>Default value: 0<br/>Maximum length =  6400.
		"""
		try :
			return self._minrttnet3
		except Exception as e:
			raise e

	@minrttnet3.setter
	def minrttnet3(self, minrttnet3) :
		r"""MIN RTT (in ms) for the third network.<br/>Default value: 0<br/>Maximum length =  6400
		"""
		try :
			self._minrttnet3 = minrttnet3
		except Exception as e:
			raise e

	@property
	def net3cclscale(self) :
		r"""Three congestion level scores limits corresponding to None, Low, Medium.
		"""
		try :
			return self._net3cclscale
		except Exception as e:
			raise e

	@net3cclscale.setter
	def net3cclscale(self, net3cclscale) :
		r"""Three congestion level scores limits corresponding to None, Low, Medium.
		"""
		try :
			self._net3cclscale = net3cclscale
		except Exception as e:
			raise e

	@property
	def net3csqscale(self) :
		r"""Three signal quality level scores limits corresponding to Excellent, Good, Fair.
		"""
		try :
			return self._net3csqscale
		except Exception as e:
			raise e

	@net3csqscale.setter
	def net3csqscale(self, net3csqscale) :
		r"""Three signal quality level scores limits corresponding to Excellent, Good, Fair.
		"""
		try :
			self._net3csqscale = net3csqscale
		except Exception as e:
			raise e

	@property
	def net3logcoef(self) :
		r"""Connection quality ranking Log coefficients of network 3.
		"""
		try :
			return self._net3logcoef
		except Exception as e:
			raise e

	@net3logcoef.setter
	def net3logcoef(self, net3logcoef) :
		r"""Connection quality ranking Log coefficients of network 3.
		"""
		try :
			self._net3logcoef = net3logcoef
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nscqaparam_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nscqaparam
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
		updateresource = nscqaparam()
		updateresource.harqretxdelay = resource.harqretxdelay
		updateresource.net1label = resource.net1label
		updateresource.minrttnet1 = resource.minrttnet1
		updateresource.lr1coeflist = resource.lr1coeflist
		updateresource.lr1probthresh = resource.lr1probthresh
		updateresource.net1cclscale = resource.net1cclscale
		updateresource.net1csqscale = resource.net1csqscale
		updateresource.net1logcoef = resource.net1logcoef
		updateresource.net2label = resource.net2label
		updateresource.minrttnet2 = resource.minrttnet2
		updateresource.lr2coeflist = resource.lr2coeflist
		updateresource.lr2probthresh = resource.lr2probthresh
		updateresource.net2cclscale = resource.net2cclscale
		updateresource.net2csqscale = resource.net2csqscale
		updateresource.net2logcoef = resource.net2logcoef
		updateresource.net3label = resource.net3label
		updateresource.minrttnet3 = resource.minrttnet3
		updateresource.net3cclscale = resource.net3cclscale
		updateresource.net3csqscale = resource.net3csqscale
		updateresource.net3logcoef = resource.net3logcoef
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nscqaparam.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nscqaparam resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nscqaparam()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nscqaparam resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nscqaparam()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


class nscqaparam_response(base_response) :
	def __init__(self, length=1) :
		self.nscqaparam = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nscqaparam = [nscqaparam() for _ in range(length)]

