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

class subscribersessions(base_resource) :
	""" Configuration for subscriber sesions resource. """
	def __init__(self) :
		self._ip = None
		self._vlan = None
		self._nodeid = None
		self._subscriptionidtype = None
		self._subscriptionidvalue = None
		self._subscriberrules = None
		self._flags = None
		self._ttl = None
		self._idlettl = None
		self._avpdisplaybuffer = None
		self._servicepath = None
		self.___count = None

	@property
	def ip(self) :
		r"""Subscriber IP Address.<br/>Default value: 0.
		"""
		try :
			return self._ip
		except Exception as e:
			raise e

	@ip.setter
	def ip(self, ip) :
		r"""Subscriber IP Address.<br/>Default value: 0
		"""
		try :
			self._ip = ip
		except Exception as e:
			raise e

	@property
	def vlan(self) :
		r"""The vlan number on which the subscriber is located.<br/>Default value: 0<br/>Maximum length =  4096.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@vlan.setter
	def vlan(self, vlan) :
		r"""The vlan number on which the subscriber is located.<br/>Default value: 0<br/>Maximum length =  4096
		"""
		try :
			self._vlan = vlan
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
	def subscriptionidtype(self) :
		r"""Subscription-Id type.<br/>Possible values = E164, IMSI, SIP_URI, NAI, PRIVATE.
		"""
		try :
			return self._subscriptionidtype
		except Exception as e:
			raise e

	@property
	def subscriptionidvalue(self) :
		r"""Subscription-Id value.
		"""
		try :
			return self._subscriptionidvalue
		except Exception as e:
			raise e

	@property
	def subscriberrules(self) :
		r"""Rules stored in this session for this subscriber. When PCRF sends Charging-Rule-Name or Charging-Rule-Base-Name AVP for a subscriber, Citrix ADC stores these AVPs in the subscriber session. These Rules can be retreived using 'Subscriber.Rule_Active(<rule name>)' expression. For static subscriber profiles, these rules are configured using '-subscriberRules <list of rules>'.
		"""
		try :
			return self._subscriberrules
		except Exception as e:
			raise e

	@property
	def flags(self) :
		r"""Subscriber Session flags.
		"""
		try :
			return self._flags
		except Exception as e:
			raise e

	@property
	def ttl(self) :
		r"""Subscriber Session revalidation Timeout remaining. This TTL gets refreshed when a radius or CCA or RAR message is received for this subscriber session.
		Citrix ADC will send a CCR-U after revalidation timer expires.
		If subscriber sessions is a negative session, then Citrix ADC will send a CCR-I after TTL expires. Negative Sessions are sessions which have not been resolved by PCRF and instead of polling PCRF continously, Citrix ADC has installed a negative session. If default subscriber is configued, then Negative Sessions inherits default subscriber profile. .
		"""
		try :
			return self._ttl
		except Exception as e:
			raise e

	@property
	def idlettl(self) :
		r"""Subscriber Session Activity Timeout remaining. Citrix ADC will take an idleAction after ttl expires. idleaction could be -->
		1. ccrTerminate: (default) send CCR-T to inform PCRF about session termination and delete the session.  
		2. delete: Just delete the subscriber session without informing PCRF.
		3. ccrUpdate: Do not delete the session and instead send a CCR-U to PCRF requesting for an updated session.
		But if this is a negative session and idleaction is ccrUpdate then Citrix ADC won't take any action. Also on negative sessions ccrTerminate translates to delete.
		"""
		try :
			return self._idlettl
		except Exception as e:
			raise e

	@property
	def avpdisplaybuffer(self) :
		r"""Subscriber Attributes Display.
		"""
		try :
			return self._avpdisplaybuffer
		except Exception as e:
			raise e

	@property
	def servicepath(self) :
		r""" Name of the servicepath to be taken for this subscriber.
		"""
		try :
			return self._servicepath
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(subscribersessions_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.subscribersessions
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			if self.ip is not None :
				return str(self.ip)
			return None
		except Exception as e :
			raise e



	@classmethod
	def clear(cls, client, resource) :
		r""" Use this API to clear subscribersessions.
		"""
		try :
			if type(resource) is not list :
				clearresource = subscribersessions()
				clearresource.ip = resource.ip
				clearresource.vlan = resource.vlan
				return clearresource.perform_operation(client,"clear")
			else :
				if (resource and len(resource) > 0) :
					clearresources = [ subscribersessions() for _ in range(len(resource))]
					for i in range(len(resource)) :
						clearresources[i].ip = resource[i].ip
						clearresources[i].vlan = resource[i].vlan
				result = cls.perform_operation_bulk_request(client, clearresources,"clear")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the subscribersessions resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = subscribersessions()
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
						response = [subscribersessions() for _ in range(len(name))]
						for i in range(len(name)) :
							option_ = options()
							option_.args = nitro_util.object_to_string_withoutquotes(name[i])
							response[i] = name[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the subscribersessions resources that are configured on netscaler.
	# This uses subscribersessions_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = subscribersessions()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of subscribersessions resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = subscribersessions()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the subscribersessions resources configured on NetScaler.
		"""
		try :
			obj = subscribersessions()
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
		r""" Use this API to count filtered the set of subscribersessions resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = subscribersessions()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Subscriptionidtype:
		E164 = "E164"
		IMSI = "IMSI"
		SIP_URI = "SIP_URI"
		NAI = "NAI"
		PRIVATE = "PRIVATE"

class subscribersessions_response(base_response) :
	def __init__(self, length=1) :
		self.subscribersessions = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.subscribersessions = [subscribersessions() for _ in range(length)]

