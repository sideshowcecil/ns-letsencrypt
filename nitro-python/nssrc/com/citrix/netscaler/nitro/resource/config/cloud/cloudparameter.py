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

class cloudparameter(base_resource) :
	""" Configuration for cloud parameter resource. """
	def __init__(self) :
		self._controllerfqdn = None
		self._controllerport = None
		self._instanceid = None
		self._customerid = None
		self._resourcelocation = None
		self._activationcode = None
		self._deployment = None
		self._connectorresidence = None
		self._controlconnectionstatus = None

	@property
	def controllerfqdn(self) :
		r"""FQDN of the controller to which the Citrix ADC SDProxy Connects.<br/>Minimum length =  1.
		"""
		try :
			return self._controllerfqdn
		except Exception as e:
			raise e

	@controllerfqdn.setter
	def controllerfqdn(self, controllerfqdn) :
		r"""FQDN of the controller to which the Citrix ADC SDProxy Connects.<br/>Minimum length =  1
		"""
		try :
			self._controllerfqdn = controllerfqdn
		except Exception as e:
			raise e

	@property
	def controllerport(self) :
		r"""Port number of the controller to which the Citrix ADC SDProxy connects.<br/>Minimum length =  1<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API.
		"""
		try :
			return self._controllerport
		except Exception as e:
			raise e

	@controllerport.setter
	def controllerport(self, controllerport) :
		r"""Port number of the controller to which the Citrix ADC SDProxy connects.<br/>Minimum length =  1<br/>Range 1 - 65535<br/>* in CLI is represented as 65535 in NITRO API
		"""
		try :
			self._controllerport = controllerport
		except Exception as e:
			raise e

	@property
	def instanceid(self) :
		r"""Instance ID of the customer provided by Trust.<br/>Minimum length =  1.
		"""
		try :
			return self._instanceid
		except Exception as e:
			raise e

	@instanceid.setter
	def instanceid(self, instanceid) :
		r"""Instance ID of the customer provided by Trust.<br/>Minimum length =  1
		"""
		try :
			self._instanceid = instanceid
		except Exception as e:
			raise e

	@property
	def customerid(self) :
		r"""Customer ID of the citrix cloud customer.<br/>Minimum length =  1.
		"""
		try :
			return self._customerid
		except Exception as e:
			raise e

	@customerid.setter
	def customerid(self, customerid) :
		r"""Customer ID of the citrix cloud customer.<br/>Minimum length =  1
		"""
		try :
			self._customerid = customerid
		except Exception as e:
			raise e

	@property
	def resourcelocation(self) :
		r"""Resource Location of the customer provided by Trust.<br/>Minimum length =  1.
		"""
		try :
			return self._resourcelocation
		except Exception as e:
			raise e

	@resourcelocation.setter
	def resourcelocation(self, resourcelocation) :
		r"""Resource Location of the customer provided by Trust.<br/>Minimum length =  1
		"""
		try :
			self._resourcelocation = resourcelocation
		except Exception as e:
			raise e

	@property
	def activationcode(self) :
		r"""Activation code for the NGS Connector instance.
		"""
		try :
			return self._activationcode
		except Exception as e:
			raise e

	@activationcode.setter
	def activationcode(self, activationcode) :
		r"""Activation code for the NGS Connector instance.
		"""
		try :
			self._activationcode = activationcode
		except Exception as e:
			raise e

	@property
	def deployment(self) :
		r"""Describes if the customer is a Staging/Production or Dev Citrix Cloud customer.<br/>Possible values = , Production, Staging, Dev.
		"""
		try :
			return self._deployment
		except Exception as e:
			raise e

	@deployment.setter
	def deployment(self, deployment) :
		r"""Describes if the customer is a Staging/Production or Dev Citrix Cloud customer.<br/>Possible values = , Production, Staging, Dev
		"""
		try :
			self._deployment = deployment
		except Exception as e:
			raise e

	@property
	def connectorresidence(self) :
		r"""Identifies whether the connector is located Onprem, Aws or Azure.<br/>Possible values = None, Onprem, Aws, Azure, Cpx.
		"""
		try :
			return self._connectorresidence
		except Exception as e:
			raise e

	@connectorresidence.setter
	def connectorresidence(self, connectorresidence) :
		r"""Identifies whether the connector is located Onprem, Aws or Azure.<br/>Possible values = None, Onprem, Aws, Azure, Cpx
		"""
		try :
			self._connectorresidence = connectorresidence
		except Exception as e:
			raise e

	@property
	def controlconnectionstatus(self) :
		r"""Status of the control connection: In case of successful registration to the controller, connection status will be shown as "Registered" else "Unregistered".
		"""
		try :
			return self._controlconnectionstatus
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(cloudparameter_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.cloudparameter
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
		updateresource = cloudparameter()
		updateresource.controllerfqdn = resource.controllerfqdn
		updateresource.controllerport = resource.controllerport
		updateresource.instanceid = resource.instanceid
		updateresource.customerid = resource.customerid
		updateresource.resourcelocation = resource.resourcelocation
		updateresource.activationcode = resource.activationcode
		updateresource.deployment = resource.deployment
		updateresource.connectorresidence = resource.connectorresidence
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update cloudparameter.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of cloudparameter resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = cloudparameter()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the cloudparameter resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = cloudparameter()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Deployment:
		_ = ""
		Production = "Production"
		Staging = "Staging"
		Dev = "Dev"

	class Connectorresidence:
		NONE = "None"
		Onprem = "Onprem"
		Aws = "Aws"
		Azure = "Azure"
		Cpx = "Cpx"

class cloudparameter_response(base_response) :
	def __init__(self, length=1) :
		self.cloudparameter = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.cloudparameter = [cloudparameter() for _ in range(length)]

