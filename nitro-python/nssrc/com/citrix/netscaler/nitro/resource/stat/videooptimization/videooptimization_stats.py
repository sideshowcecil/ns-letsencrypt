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

class videooptimization_stats(base_resource) :
	def __init__(self) :
		self._clearstats = None
		self._voctpdvideo = 0
		self._voctpdvideorate = 0
		self._voctabvideo = 0
		self._voctabvideorate = 0
		self._voeabvideo = 0
		self._voeabvideorate = 0
		self._voquicvideo = 0
		self._voquicvideorate = 0
		self._vovideooptother = 0
		self._vovideoopherrate = 0
		self._voctabvideoses = 0
		self._voctabvideosesrate = 0
		self._voeabvideoses = 0
		self._voeabvideosesrate = 0
		self._voquicvideoses = 0
		self._voquicvideosesrate = 0
		self._voctpdvideobytes = 0
		self._voctpdvideobytesrate = 0
		self._voctabvideobytes = 0
		self._voctabvideobytesrate = 0
		self._voeabvideobytes = 0
		self._voeabvideobytesrate = 0
		self._voquicvideobytes = 0
		self._voquicvideobytesrate = 0
		self._vovideooptotherbytes = 0
		self._vovideoopherbytesrate = 0

	@property
	def clearstats(self) :
		r"""Clear the statsistics / counters.<br/>Possible values = basic, full.
		"""
		try :
			return self._clearstats
		except Exception as e:
			raise e

	@clearstats.setter
	def clearstats(self, clearstats) :
		r"""Clear the statsistics / counters
		"""
		try :
			self._clearstats = clearstats
		except Exception as e:
			raise e

	@property
	def voctpdvideobytesrate(self) :
		r"""Rate (/s) counter for voctpdvideobytes.
		"""
		try :
			return self._voctpdvideobytesrate
		except Exception as e:
			raise e

	@property
	def voquicvideoses(self) :
		r"""Total number of sessions with QUIC videos.
		"""
		try :
			return self._voquicvideoses
		except Exception as e:
			raise e

	@property
	def voctabvideobytesrate(self) :
		r"""Rate (/s) counter for voctabvideobytes.
		"""
		try :
			return self._voctabvideobytesrate
		except Exception as e:
			raise e

	@property
	def vovideooptother(self) :
		r"""Non video traffic.
		"""
		try :
			return self._vovideooptother
		except Exception as e:
			raise e

	@property
	def voctpdvideobytes(self) :
		r"""Total number of bytes for progressive download HTTP videos.
		"""
		try :
			return self._voctpdvideobytes
		except Exception as e:
			raise e

	@property
	def voctabvideorate(self) :
		r"""Rate (/s) counter for voctabvideo.
		"""
		try :
			return self._voctabvideorate
		except Exception as e:
			raise e

	@property
	def voquicvideobytes(self) :
		r"""Total number of bytes for QUIC videos.
		"""
		try :
			return self._voquicvideobytes
		except Exception as e:
			raise e

	@property
	def voctabvideobytes(self) :
		r"""Total number of bytes for adaptive bitrate HTTP videos.
		"""
		try :
			return self._voctabvideobytes
		except Exception as e:
			raise e

	@property
	def voeabvideosesrate(self) :
		r"""Rate (/s) counter for voeabvideoses.
		"""
		try :
			return self._voeabvideosesrate
		except Exception as e:
			raise e

	@property
	def voctabvideoses(self) :
		r"""Total number of adaptive bitrate HTTP video sessions.
		"""
		try :
			return self._voctabvideoses
		except Exception as e:
			raise e

	@property
	def voeabvideoses(self) :
		r"""Total number of adaptive bitrate HTTPS videos.
		"""
		try :
			return self._voeabvideoses
		except Exception as e:
			raise e

	@property
	def vovideoopherbytesrate(self) :
		r"""Rate (/s) counter for vovideooptotherbytes.
		"""
		try :
			return self._vovideoopherbytesrate
		except Exception as e:
			raise e

	@property
	def voquicvideo(self) :
		r"""Total number of QUIC videos.
		"""
		try :
			return self._voquicvideo
		except Exception as e:
			raise e

	@property
	def voeabvideorate(self) :
		r"""Rate (/s) counter for voeabvideo.
		"""
		try :
			return self._voeabvideorate
		except Exception as e:
			raise e

	@property
	def voctpdvideo(self) :
		r"""Total number of progressive download HTTP videos.
		"""
		try :
			return self._voctpdvideo
		except Exception as e:
			raise e

	@property
	def voeabvideo(self) :
		r"""Total number of adaptive bitrate HTTPS videos.
		"""
		try :
			return self._voeabvideo
		except Exception as e:
			raise e

	@property
	def voquicvideosesrate(self) :
		r"""Rate (/s) counter for voquicvideoses.
		"""
		try :
			return self._voquicvideosesrate
		except Exception as e:
			raise e

	@property
	def voeabvideobytesrate(self) :
		r"""Rate (/s) counter for voeabvideobytes.
		"""
		try :
			return self._voeabvideobytesrate
		except Exception as e:
			raise e

	@property
	def vovideoopherrate(self) :
		r"""Rate (/s) counter for vovideooptother.
		"""
		try :
			return self._vovideoopherrate
		except Exception as e:
			raise e

	@property
	def voctabvideo(self) :
		r"""Total number of adaptive bitrate HTTP videos.
		"""
		try :
			return self._voctabvideo
		except Exception as e:
			raise e

	@property
	def voquicvideobytesrate(self) :
		r"""Rate (/s) counter for voquicvideobytes.
		"""
		try :
			return self._voquicvideobytesrate
		except Exception as e:
			raise e

	@property
	def voctpdvideorate(self) :
		r"""Rate (/s) counter for voctpdvideo.
		"""
		try :
			return self._voctpdvideorate
		except Exception as e:
			raise e

	@property
	def voctabvideosesrate(self) :
		r"""Rate (/s) counter for voctabvideoses.
		"""
		try :
			return self._voctabvideosesrate
		except Exception as e:
			raise e

	@property
	def voquicvideorate(self) :
		r"""Rate (/s) counter for voquicvideo.
		"""
		try :
			return self._voquicvideorate
		except Exception as e:
			raise e

	@property
	def vovideooptotherbytes(self) :
		r"""Total number of bytes for non video traffic.
		"""
		try :
			return self._vovideooptotherbytes
		except Exception as e:
			raise e

	@property
	def voeabvideobytes(self) :
		r"""Total number of bytes for adaptive bitrate HTTPS videos.
		"""
		try :
			return self._voeabvideobytes
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(videooptimization_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.videooptimization
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
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all videooptimization_stats resources that are configured on netscaler.
		 set statbindings=True in options to retrieve bindings.
		"""
		try :
			obj = videooptimization_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class videooptimization_response(base_response) :
	def __init__(self, length=1) :
		self.videooptimization = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.videooptimization = [videooptimization_stats() for _ in range(length)]

