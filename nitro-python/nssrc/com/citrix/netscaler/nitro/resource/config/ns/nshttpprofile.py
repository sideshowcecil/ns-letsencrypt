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

class nshttpprofile(base_resource) :
	""" Configuration for HTTP profile resource. """
	def __init__(self) :
		self._name = None
		self._dropinvalreqs = None
		self._markhttp09inval = None
		self._markconnreqinval = None
		self._marktracereqinval = None
		self._cmponpush = None
		self._conmultiplex = None
		self._maxreusepool = None
		self._dropextracrlf = None
		self._incomphdrdelay = None
		self._websocket = None
		self._rtsptunnel = None
		self._reqtimeout = None
		self._adpttimeout = None
		self._reqtimeoutaction = None
		self._dropextradata = None
		self._weblog = None
		self._clientiphdrexpr = None
		self._maxreq = None
		self._persistentetag = None
		self._spdy = None
		self._http2 = None
		self._http2direct = None
		self._http2strictcipher = None
		self._altsvc = None
		self._reusepooltimeout = None
		self._maxheaderlen = None
		self._minreusepool = None
		self._http2maxheaderlistsize = None
		self._http2maxframesize = None
		self._http2maxconcurrentstreams = None
		self._http2initialwindowsize = None
		self._http2headertablesize = None
		self._http2minseverconn = None
		self._apdexcltresptimethreshold = None
		self._refcnt = None
		self._builtin = None
		self._feature = None
		self._apdexsvrresptimethreshold = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for an HTTP profile. Must begin with a letter, number, or the underscore \(_\) character. Other characters allowed, after the first character, are the hyphen \(-\), period \(.\), hash \(\#\), space \( \), at \(@\), colon \(:\), and equal \(=\) characters. The name of a HTTP profile cannot be changed after it is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks \(for example, "my http profile" or 'my http profile'\).<br/>Minimum length =  1<br/>Maximum length =  127.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for an HTTP profile. Must begin with a letter, number, or the underscore \(_\) character. Other characters allowed, after the first character, are the hyphen \(-\), period \(.\), hash \(\#\), space \( \), at \(@\), colon \(:\), and equal \(=\) characters. The name of a HTTP profile cannot be changed after it is created.
		CLI Users: If the name includes one or more spaces, enclose the name in double or single quotation marks \(for example, "my http profile" or 'my http profile'\).<br/>Minimum length =  1<br/>Maximum length =  127
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def dropinvalreqs(self) :
		r"""Drop invalid HTTP requests or responses.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dropinvalreqs
		except Exception as e:
			raise e

	@dropinvalreqs.setter
	def dropinvalreqs(self, dropinvalreqs) :
		r"""Drop invalid HTTP requests or responses.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dropinvalreqs = dropinvalreqs
		except Exception as e:
			raise e

	@property
	def markhttp09inval(self) :
		r"""Mark HTTP/0.9 requests as invalid.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._markhttp09inval
		except Exception as e:
			raise e

	@markhttp09inval.setter
	def markhttp09inval(self, markhttp09inval) :
		r"""Mark HTTP/0.9 requests as invalid.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._markhttp09inval = markhttp09inval
		except Exception as e:
			raise e

	@property
	def markconnreqinval(self) :
		r"""Mark CONNECT requests as invalid.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._markconnreqinval
		except Exception as e:
			raise e

	@markconnreqinval.setter
	def markconnreqinval(self, markconnreqinval) :
		r"""Mark CONNECT requests as invalid.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._markconnreqinval = markconnreqinval
		except Exception as e:
			raise e

	@property
	def marktracereqinval(self) :
		r"""Mark TRACE requests as invalid.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._marktracereqinval
		except Exception as e:
			raise e

	@marktracereqinval.setter
	def marktracereqinval(self, marktracereqinval) :
		r"""Mark TRACE requests as invalid.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._marktracereqinval = marktracereqinval
		except Exception as e:
			raise e

	@property
	def cmponpush(self) :
		r"""Start data compression on receiving a TCP packet with PUSH flag set.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._cmponpush
		except Exception as e:
			raise e

	@cmponpush.setter
	def cmponpush(self, cmponpush) :
		r"""Start data compression on receiving a TCP packet with PUSH flag set.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._cmponpush = cmponpush
		except Exception as e:
			raise e

	@property
	def conmultiplex(self) :
		r"""Reuse server connections for requests from more than one client connections.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._conmultiplex
		except Exception as e:
			raise e

	@conmultiplex.setter
	def conmultiplex(self, conmultiplex) :
		r"""Reuse server connections for requests from more than one client connections.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._conmultiplex = conmultiplex
		except Exception as e:
			raise e

	@property
	def maxreusepool(self) :
		r"""Maximum limit on the number of connections, from the Citrix ADC to a particular server that are kept in the reuse pool. This setting is helpful for optimal memory utilization and for reducing the idle connections to the server just after the peak time. Zero implies no limit on reuse pool size. If non-zero value is given, it has to be greater than or equal to the number of running Packet Engines.<br/>Default value: 0<br/>Maximum length =  360000.
		"""
		try :
			return self._maxreusepool
		except Exception as e:
			raise e

	@maxreusepool.setter
	def maxreusepool(self, maxreusepool) :
		r"""Maximum limit on the number of connections, from the Citrix ADC to a particular server that are kept in the reuse pool. This setting is helpful for optimal memory utilization and for reducing the idle connections to the server just after the peak time. Zero implies no limit on reuse pool size. If non-zero value is given, it has to be greater than or equal to the number of running Packet Engines.<br/>Default value: 0<br/>Maximum length =  360000
		"""
		try :
			self._maxreusepool = maxreusepool
		except Exception as e:
			raise e

	@property
	def dropextracrlf(self) :
		r"""Drop any extra 'CR' and 'LF' characters present after the header.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dropextracrlf
		except Exception as e:
			raise e

	@dropextracrlf.setter
	def dropextracrlf(self, dropextracrlf) :
		r"""Drop any extra 'CR' and 'LF' characters present after the header.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dropextracrlf = dropextracrlf
		except Exception as e:
			raise e

	@property
	def incomphdrdelay(self) :
		r"""Maximum time to wait, in milliseconds, between incomplete header packets. If the header packets take longer to arrive at Citrix ADC, the connection is silently dropped.<br/>Default value: 7000<br/>Minimum length =  1<br/>Maximum length =  360000.
		"""
		try :
			return self._incomphdrdelay
		except Exception as e:
			raise e

	@incomphdrdelay.setter
	def incomphdrdelay(self, incomphdrdelay) :
		r"""Maximum time to wait, in milliseconds, between incomplete header packets. If the header packets take longer to arrive at Citrix ADC, the connection is silently dropped.<br/>Default value: 7000<br/>Minimum length =  1<br/>Maximum length =  360000
		"""
		try :
			self._incomphdrdelay = incomphdrdelay
		except Exception as e:
			raise e

	@property
	def websocket(self) :
		r"""HTTP connection to be upgraded to a web socket connection. Once upgraded, Citrix ADC does not process Layer 7 traffic on this connection.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._websocket
		except Exception as e:
			raise e

	@websocket.setter
	def websocket(self, websocket) :
		r"""HTTP connection to be upgraded to a web socket connection. Once upgraded, Citrix ADC does not process Layer 7 traffic on this connection.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._websocket = websocket
		except Exception as e:
			raise e

	@property
	def rtsptunnel(self) :
		r"""Allow RTSP tunnel in HTTP. Once application/x-rtsp-tunnelled is seen in Accept or Content-Type header, Citrix ADC does not process Layer 7 traffic on this connection.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._rtsptunnel
		except Exception as e:
			raise e

	@rtsptunnel.setter
	def rtsptunnel(self, rtsptunnel) :
		r"""Allow RTSP tunnel in HTTP. Once application/x-rtsp-tunnelled is seen in Accept or Content-Type header, Citrix ADC does not process Layer 7 traffic on this connection.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._rtsptunnel = rtsptunnel
		except Exception as e:
			raise e

	@property
	def reqtimeout(self) :
		r"""Time, in seconds, within which the HTTP request must complete. If the request does not complete within this time, the specified request timeout action is executed. Zero disables the timeout.<br/>Default value: 0<br/>Maximum length =  86400.
		"""
		try :
			return self._reqtimeout
		except Exception as e:
			raise e

	@reqtimeout.setter
	def reqtimeout(self, reqtimeout) :
		r"""Time, in seconds, within which the HTTP request must complete. If the request does not complete within this time, the specified request timeout action is executed. Zero disables the timeout.<br/>Default value: 0<br/>Maximum length =  86400
		"""
		try :
			self._reqtimeout = reqtimeout
		except Exception as e:
			raise e

	@property
	def adpttimeout(self) :
		r"""Adapts the configured request timeout based on flow conditions. The timeout is increased or decreased internally and applied on the flow.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._adpttimeout
		except Exception as e:
			raise e

	@adpttimeout.setter
	def adpttimeout(self, adpttimeout) :
		r"""Adapts the configured request timeout based on flow conditions. The timeout is increased or decreased internally and applied on the flow.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._adpttimeout = adpttimeout
		except Exception as e:
			raise e

	@property
	def reqtimeoutaction(self) :
		r"""Action to take when the HTTP request does not complete within the specified request timeout duration. You can configure the following actions:
		* RESET - Send RST (reset) to client when timeout occurs.
		* DROP - Drop silently when timeout occurs.
		* Custom responder action - Name of the responder action to trigger when timeout occurs, used to send custom message.
		"""
		try :
			return self._reqtimeoutaction
		except Exception as e:
			raise e

	@reqtimeoutaction.setter
	def reqtimeoutaction(self, reqtimeoutaction) :
		r"""Action to take when the HTTP request does not complete within the specified request timeout duration. You can configure the following actions:
		* RESET - Send RST (reset) to client when timeout occurs.
		* DROP - Drop silently when timeout occurs.
		* Custom responder action - Name of the responder action to trigger when timeout occurs, used to send custom message.
		"""
		try :
			self._reqtimeoutaction = reqtimeoutaction
		except Exception as e:
			raise e

	@property
	def dropextradata(self) :
		r"""Drop any extra data when server sends more data than the specified content-length.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._dropextradata
		except Exception as e:
			raise e

	@dropextradata.setter
	def dropextradata(self, dropextradata) :
		r"""Drop any extra data when server sends more data than the specified content-length.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._dropextradata = dropextradata
		except Exception as e:
			raise e

	@property
	def weblog(self) :
		r"""Enable or disable web logging.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._weblog
		except Exception as e:
			raise e

	@weblog.setter
	def weblog(self, weblog) :
		r"""Enable or disable web logging.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._weblog = weblog
		except Exception as e:
			raise e

	@property
	def clientiphdrexpr(self) :
		r"""Name of the header that contains the real client IP address.
		"""
		try :
			return self._clientiphdrexpr
		except Exception as e:
			raise e

	@clientiphdrexpr.setter
	def clientiphdrexpr(self, clientiphdrexpr) :
		r"""Name of the header that contains the real client IP address.
		"""
		try :
			self._clientiphdrexpr = clientiphdrexpr
		except Exception as e:
			raise e

	@property
	def maxreq(self) :
		r"""Maximum number of requests allowed on a single connection. Zero implies no limit on the number of requests.<br/>Default value: 0<br/>Maximum length =  65534.
		"""
		try :
			return self._maxreq
		except Exception as e:
			raise e

	@maxreq.setter
	def maxreq(self, maxreq) :
		r"""Maximum number of requests allowed on a single connection. Zero implies no limit on the number of requests.<br/>Default value: 0<br/>Maximum length =  65534
		"""
		try :
			self._maxreq = maxreq
		except Exception as e:
			raise e

	@property
	def persistentetag(self) :
		r"""Generate the persistent Citrix ADC specific ETag for the HTTP response with ETag header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._persistentetag
		except Exception as e:
			raise e

	@persistentetag.setter
	def persistentetag(self, persistentetag) :
		r"""Generate the persistent Citrix ADC specific ETag for the HTTP response with ETag header.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._persistentetag = persistentetag
		except Exception as e:
			raise e

	@property
	def spdy(self) :
		r"""Enable SPDYv2 or SPDYv3 or both over SSL vserver. SSL will advertise SPDY support either during NPN Handshake or when client will advertises SPDY support during ALPN handshake. Both SPDY versions are enabled when this parameter is set to ENABLED.<br/>Default value: DISABLED<br/>Possible values = DISABLED, ENABLED, V2, V3.
		"""
		try :
			return self._spdy
		except Exception as e:
			raise e

	@spdy.setter
	def spdy(self, spdy) :
		r"""Enable SPDYv2 or SPDYv3 or both over SSL vserver. SSL will advertise SPDY support either during NPN Handshake or when client will advertises SPDY support during ALPN handshake. Both SPDY versions are enabled when this parameter is set to ENABLED.<br/>Default value: DISABLED<br/>Possible values = DISABLED, ENABLED, V2, V3
		"""
		try :
			self._spdy = spdy
		except Exception as e:
			raise e

	@property
	def http2(self) :
		r"""Choose whether to enable support for HTTP/2.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._http2
		except Exception as e:
			raise e

	@http2.setter
	def http2(self, http2) :
		r"""Choose whether to enable support for HTTP/2.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._http2 = http2
		except Exception as e:
			raise e

	@property
	def http2direct(self) :
		r"""Choose whether to enable support for Direct HTTP/2.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._http2direct
		except Exception as e:
			raise e

	@http2direct.setter
	def http2direct(self, http2direct) :
		r"""Choose whether to enable support for Direct HTTP/2.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._http2direct = http2direct
		except Exception as e:
			raise e

	@property
	def http2strictcipher(self) :
		r"""Choose whether to enable strict HTTP/2 cipher selection.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._http2strictcipher
		except Exception as e:
			raise e

	@http2strictcipher.setter
	def http2strictcipher(self, http2strictcipher) :
		r"""Choose whether to enable strict HTTP/2 cipher selection.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._http2strictcipher = http2strictcipher
		except Exception as e:
			raise e

	@property
	def altsvc(self) :
		r"""Choose whether to enable support for Alternative Service.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._altsvc
		except Exception as e:
			raise e

	@altsvc.setter
	def altsvc(self, altsvc) :
		r"""Choose whether to enable support for Alternative Service.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._altsvc = altsvc
		except Exception as e:
			raise e

	@property
	def reusepooltimeout(self) :
		r"""Idle timeout (in seconds) for server connections in re-use pool. Connections in the re-use pool are flushed, if they remain idle for the configured timeout.<br/>Default value: 0<br/>Maximum length =  31536000.
		"""
		try :
			return self._reusepooltimeout
		except Exception as e:
			raise e

	@reusepooltimeout.setter
	def reusepooltimeout(self, reusepooltimeout) :
		r"""Idle timeout (in seconds) for server connections in re-use pool. Connections in the re-use pool are flushed, if they remain idle for the configured timeout.<br/>Default value: 0<br/>Maximum length =  31536000
		"""
		try :
			self._reusepooltimeout = reusepooltimeout
		except Exception as e:
			raise e

	@property
	def maxheaderlen(self) :
		r"""Number of bytes to be queued to look for complete header before returning error. If complete header is not obtained after queuing these many bytes, request will be marked as invalid and no L7 processing will be done for that TCP connection.<br/>Default value: 24820<br/>Minimum length =  2048<br/>Maximum length =  61440.
		"""
		try :
			return self._maxheaderlen
		except Exception as e:
			raise e

	@maxheaderlen.setter
	def maxheaderlen(self, maxheaderlen) :
		r"""Number of bytes to be queued to look for complete header before returning error. If complete header is not obtained after queuing these many bytes, request will be marked as invalid and no L7 processing will be done for that TCP connection.<br/>Default value: 24820<br/>Minimum length =  2048<br/>Maximum length =  61440
		"""
		try :
			self._maxheaderlen = maxheaderlen
		except Exception as e:
			raise e

	@property
	def minreusepool(self) :
		r"""Minimum limit on the number of connections, from the Citrix ADC to a particular server that are kept in the reuse pool. This setting is helpful for optimal memory utilization and for reducing the idle connections to the server just after the peak time. Zero implies no limit on reuse pool size.<br/>Default value: 0<br/>Maximum length =  360000.
		"""
		try :
			return self._minreusepool
		except Exception as e:
			raise e

	@minreusepool.setter
	def minreusepool(self, minreusepool) :
		r"""Minimum limit on the number of connections, from the Citrix ADC to a particular server that are kept in the reuse pool. This setting is helpful for optimal memory utilization and for reducing the idle connections to the server just after the peak time. Zero implies no limit on reuse pool size.<br/>Default value: 0<br/>Maximum length =  360000
		"""
		try :
			self._minreusepool = minreusepool
		except Exception as e:
			raise e

	@property
	def http2maxheaderlistsize(self) :
		r"""Maximum size of header list that the Citrix ADC is prepared to accept, in bytes. NOTE: The actual plain text header size that the Citrix ADC accepts is limited by maxHeaderLen. Please change maxHeaderLen parameter as well when modifying http2MaxHeaderListSize.<br/>Default value: 24576<br/>Minimum length =  8192<br/>Maximum length =  65535.
		"""
		try :
			return self._http2maxheaderlistsize
		except Exception as e:
			raise e

	@http2maxheaderlistsize.setter
	def http2maxheaderlistsize(self, http2maxheaderlistsize) :
		r"""Maximum size of header list that the Citrix ADC is prepared to accept, in bytes. NOTE: The actual plain text header size that the Citrix ADC accepts is limited by maxHeaderLen. Please change maxHeaderLen parameter as well when modifying http2MaxHeaderListSize.<br/>Default value: 24576<br/>Minimum length =  8192<br/>Maximum length =  65535
		"""
		try :
			self._http2maxheaderlistsize = http2maxheaderlistsize
		except Exception as e:
			raise e

	@property
	def http2maxframesize(self) :
		r"""Maximum size of the frame payload that the Citrix ADC is willing to receive, in bytes.<br/>Default value: 16384<br/>Minimum length =  16384<br/>Maximum length =  32768.
		"""
		try :
			return self._http2maxframesize
		except Exception as e:
			raise e

	@http2maxframesize.setter
	def http2maxframesize(self, http2maxframesize) :
		r"""Maximum size of the frame payload that the Citrix ADC is willing to receive, in bytes.<br/>Default value: 16384<br/>Minimum length =  16384<br/>Maximum length =  32768
		"""
		try :
			self._http2maxframesize = http2maxframesize
		except Exception as e:
			raise e

	@property
	def http2maxconcurrentstreams(self) :
		r"""Maximum number of concurrent streams that is allowed per connection.<br/>Default value: 100<br/>Maximum length =  1000.
		"""
		try :
			return self._http2maxconcurrentstreams
		except Exception as e:
			raise e

	@http2maxconcurrentstreams.setter
	def http2maxconcurrentstreams(self, http2maxconcurrentstreams) :
		r"""Maximum number of concurrent streams that is allowed per connection.<br/>Default value: 100<br/>Maximum length =  1000
		"""
		try :
			self._http2maxconcurrentstreams = http2maxconcurrentstreams
		except Exception as e:
			raise e

	@property
	def http2initialwindowsize(self) :
		r"""Initial window size for stream level flow control, in bytes.<br/>Default value: 65535<br/>Minimum length =  8192<br/>Maximum length =  20971520.
		"""
		try :
			return self._http2initialwindowsize
		except Exception as e:
			raise e

	@http2initialwindowsize.setter
	def http2initialwindowsize(self, http2initialwindowsize) :
		r"""Initial window size for stream level flow control, in bytes.<br/>Default value: 65535<br/>Minimum length =  8192<br/>Maximum length =  20971520
		"""
		try :
			self._http2initialwindowsize = http2initialwindowsize
		except Exception as e:
			raise e

	@property
	def http2headertablesize(self) :
		r"""Maximum size of the header compression table used to decode header blocks, in bytes.<br/>Default value: 4096<br/>Maximum length =  16384.
		"""
		try :
			return self._http2headertablesize
		except Exception as e:
			raise e

	@http2headertablesize.setter
	def http2headertablesize(self, http2headertablesize) :
		r"""Maximum size of the header compression table used to decode header blocks, in bytes.<br/>Default value: 4096<br/>Maximum length =  16384
		"""
		try :
			self._http2headertablesize = http2headertablesize
		except Exception as e:
			raise e

	@property
	def http2minseverconn(self) :
		r"""Minimum number of HTTP2 connections established to backend server, on receiving HTTP requests from client before multiplexing the streams into the available HTTP/2 connections.<br/>Default value: 20<br/>Minimum length =  1<br/>Maximum length =  360000.
		"""
		try :
			return self._http2minseverconn
		except Exception as e:
			raise e

	@http2minseverconn.setter
	def http2minseverconn(self, http2minseverconn) :
		r"""Minimum number of HTTP2 connections established to backend server, on receiving HTTP requests from client before multiplexing the streams into the available HTTP/2 connections.<br/>Default value: 20<br/>Minimum length =  1<br/>Maximum length =  360000
		"""
		try :
			self._http2minseverconn = http2minseverconn
		except Exception as e:
			raise e

	@property
	def apdexcltresptimethreshold(self) :
		r"""This option sets the satisfactory threshold (T) for client response time in milliseconds to be used for APDEX calculations. This means a transaction responding in less than this threshold is considered satisfactory. Transaction responding between T and 4*T is considered tolerable. Any transaction responding in more than 4*T time is considered frustrating. Citrix ADC maintains stats for such tolerable and frustrating transcations. And client response time related apdex counters are only updated on a vserver which receives clients traffic.<br/>Default value: 500<br/>Minimum length =  1<br/>Maximum length =  3600000.
		"""
		try :
			return self._apdexcltresptimethreshold
		except Exception as e:
			raise e

	@apdexcltresptimethreshold.setter
	def apdexcltresptimethreshold(self, apdexcltresptimethreshold) :
		r"""This option sets the satisfactory threshold (T) for client response time in milliseconds to be used for APDEX calculations. This means a transaction responding in less than this threshold is considered satisfactory. Transaction responding between T and 4*T is considered tolerable. Any transaction responding in more than 4*T time is considered frustrating. Citrix ADC maintains stats for such tolerable and frustrating transcations. And client response time related apdex counters are only updated on a vserver which receives clients traffic.<br/>Default value: 500<br/>Minimum length =  1<br/>Maximum length =  3600000
		"""
		try :
			self._apdexcltresptimethreshold = apdexcltresptimethreshold
		except Exception as e:
			raise e

	@property
	def refcnt(self) :
		r"""Number of entities using this profile.
		"""
		try :
			return self._refcnt
		except Exception as e:
			raise e

	@property
	def builtin(self) :
		r"""Flag to determine if http profile is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL.
		"""
		try :
			return self._builtin
		except Exception as e:
			raise e

	@property
	def feature(self) :
		r"""The feature to be checked while applying this config.
		"""
		try :
			return self._feature
		except Exception as e:
			raise e

	@property
	def apdexsvrresptimethreshold(self) :
		r"""This option sets the satisfactory threshold (T) for server response time in milliseconds to be used for APDEX calculations. This means a transaction responding in less than this threshold is considered satisfactory. Transaction responding between T and 4*T is considered tolerable. Any transaction responding in more than 4*T time is considered frustrating. Citrix ADC maintains stats for such tolerable and frustrating transcations. Server Response time related apdex counters are only updated on backend services or a backend vserver which is not accepting client traffic.<br/>Default value: 400<br/>Minimum value =  1<br/>Maximum value =  3600000.
		"""
		try :
			return self._apdexsvrresptimethreshold
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nshttpprofile_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nshttpprofile
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
		addresource = nshttpprofile()
		addresource.name = resource.name
		addresource.dropinvalreqs = resource.dropinvalreqs
		addresource.markhttp09inval = resource.markhttp09inval
		addresource.markconnreqinval = resource.markconnreqinval
		addresource.marktracereqinval = resource.marktracereqinval
		addresource.cmponpush = resource.cmponpush
		addresource.conmultiplex = resource.conmultiplex
		addresource.maxreusepool = resource.maxreusepool
		addresource.dropextracrlf = resource.dropextracrlf
		addresource.incomphdrdelay = resource.incomphdrdelay
		addresource.websocket = resource.websocket
		addresource.rtsptunnel = resource.rtsptunnel
		addresource.reqtimeout = resource.reqtimeout
		addresource.adpttimeout = resource.adpttimeout
		addresource.reqtimeoutaction = resource.reqtimeoutaction
		addresource.dropextradata = resource.dropextradata
		addresource.weblog = resource.weblog
		addresource.clientiphdrexpr = resource.clientiphdrexpr
		addresource.maxreq = resource.maxreq
		addresource.persistentetag = resource.persistentetag
		addresource.spdy = resource.spdy
		addresource.http2 = resource.http2
		addresource.http2direct = resource.http2direct
		addresource.http2strictcipher = resource.http2strictcipher
		addresource.altsvc = resource.altsvc
		addresource.reusepooltimeout = resource.reusepooltimeout
		addresource.maxheaderlen = resource.maxheaderlen
		addresource.minreusepool = resource.minreusepool
		addresource.http2maxheaderlistsize = resource.http2maxheaderlistsize
		addresource.http2maxframesize = resource.http2maxframesize
		addresource.http2maxconcurrentstreams = resource.http2maxconcurrentstreams
		addresource.http2initialwindowsize = resource.http2initialwindowsize
		addresource.http2headertablesize = resource.http2headertablesize
		addresource.http2minseverconn = resource.http2minseverconn
		addresource.apdexcltresptimethreshold = resource.apdexcltresptimethreshold
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add nshttpprofile.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nshttpprofile() for _ in range(len(resource))]
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
		deleteresource = nshttpprofile()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete nshttpprofile.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nshttpprofile()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nshttpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nshttpprofile() for _ in range(len(resource))]
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
		updateresource = nshttpprofile()
		updateresource.name = resource.name
		updateresource.dropinvalreqs = resource.dropinvalreqs
		updateresource.markhttp09inval = resource.markhttp09inval
		updateresource.markconnreqinval = resource.markconnreqinval
		updateresource.marktracereqinval = resource.marktracereqinval
		updateresource.cmponpush = resource.cmponpush
		updateresource.conmultiplex = resource.conmultiplex
		updateresource.maxreusepool = resource.maxreusepool
		updateresource.dropextracrlf = resource.dropextracrlf
		updateresource.incomphdrdelay = resource.incomphdrdelay
		updateresource.websocket = resource.websocket
		updateresource.rtsptunnel = resource.rtsptunnel
		updateresource.reqtimeout = resource.reqtimeout
		updateresource.adpttimeout = resource.adpttimeout
		updateresource.reqtimeoutaction = resource.reqtimeoutaction
		updateresource.dropextradata = resource.dropextradata
		updateresource.weblog = resource.weblog
		updateresource.clientiphdrexpr = resource.clientiphdrexpr
		updateresource.maxreq = resource.maxreq
		updateresource.persistentetag = resource.persistentetag
		updateresource.spdy = resource.spdy
		updateresource.http2 = resource.http2
		updateresource.http2direct = resource.http2direct
		updateresource.http2strictcipher = resource.http2strictcipher
		updateresource.altsvc = resource.altsvc
		updateresource.http2maxheaderlistsize = resource.http2maxheaderlistsize
		updateresource.http2maxframesize = resource.http2maxframesize
		updateresource.http2maxconcurrentstreams = resource.http2maxconcurrentstreams
		updateresource.http2initialwindowsize = resource.http2initialwindowsize
		updateresource.http2headertablesize = resource.http2headertablesize
		updateresource.http2minseverconn = resource.http2minseverconn
		updateresource.reusepooltimeout = resource.reusepooltimeout
		updateresource.maxheaderlen = resource.maxheaderlen
		updateresource.minreusepool = resource.minreusepool
		updateresource.apdexcltresptimethreshold = resource.apdexcltresptimethreshold
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nshttpprofile.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nshttpprofile() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nshttpprofile resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nshttpprofile()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ nshttpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ nshttpprofile() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nshttpprofile resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nshttpprofile()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = nshttpprofile()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [nshttpprofile() for _ in range(len(name))]
						obj = [nshttpprofile() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = nshttpprofile()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of nshttpprofile resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nshttpprofile()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the nshttpprofile resources configured on NetScaler.
		"""
		try :
			obj = nshttpprofile()
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
		r""" Use this API to count filtered the set of nshttpprofile resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nshttpprofile()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Conmultiplex:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Markhttp09inval:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Http2direct:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Adpttimeout:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Feature:
		WL = "WL"
		WebLogging = "WebLogging"
		SP = "SP"
		SurgeProtection = "SurgeProtection"
		LB = "LB"
		LoadBalancing = "LoadBalancing"
		CS = "CS"
		ContentSwitching = "ContentSwitching"
		CR = "CR"
		CacheRedirection = "CacheRedirection"
		SC = "SC"
		SureConnect = "SureConnect"
		CMP = "CMP"
		CMPcntl = "CMPcntl"
		CompressionControl = "CompressionControl"
		PQ = "PQ"
		PriorityQueuing = "PriorityQueuing"
		HDOSP = "HDOSP"
		HttpDoSProtection = "HttpDoSProtection"
		SSLVPN = "SSLVPN"
		AAA = "AAA"
		GSLB = "GSLB"
		GlobalServerLoadBalancing = "GlobalServerLoadBalancing"
		SSL = "SSL"
		SSLOffload = "SSLOffload"
		SSLOffloading = "SSLOffloading"
		CF = "CF"
		ContentFiltering = "ContentFiltering"
		IC = "IC"
		IntegratedCaching = "IntegratedCaching"
		OSPF = "OSPF"
		OSPFRouting = "OSPFRouting"
		RIP = "RIP"
		RIPRouting = "RIPRouting"
		BGP = "BGP"
		BGPRouting = "BGPRouting"
		REWRITE = "REWRITE"
		IPv6PT = "IPv6PT"
		IPv6protocoltranslation = "IPv6protocoltranslation"
		AppFw = "AppFw"
		ApplicationFirewall = "ApplicationFirewall"
		RESPONDER = "RESPONDER"
		HTMLInjection = "HTMLInjection"
		push = "push"
		NSPush = "NSPush"
		NetScalerPush = "NetScalerPush"
		AppFlow = "AppFlow"
		CloudBridge = "CloudBridge"
		ISIS = "ISIS"
		ISISRouting = "ISISRouting"
		CH = "CH"
		CallHome = "CallHome"
		AppQoE = "AppQoE"
		ContentAccelerator = "ContentAccelerator"
		SYSTEM = "SYSTEM"
		RISE = "RISE"
		FEO = "FEO"
		LSN = "LSN"
		LargeScaleNAT = "LargeScaleNAT"
		RDPProxy = "RDPProxy"
		Rep = "Rep"
		Reputation = "Reputation"
		URLFiltering = "URLFiltering"
		VideoOptimization = "VideoOptimization"
		ForwardProxy = "ForwardProxy"
		SSLInterception = "SSLInterception"
		AdaptiveTCP = "AdaptiveTCP"
		CQA = "CQA"
		CI = "CI"
		ContentInspection = "ContentInspection"
		Bot = "Bot"

	class Http2strictcipher:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Builtin:
		MODIFIABLE = "MODIFIABLE"
		DELETABLE = "DELETABLE"
		IMMUTABLE = "IMMUTABLE"
		PARTITION_ALL = "PARTITION_ALL"

	class Markconnreqinval:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Spdy:
		DISABLED = "DISABLED"
		ENABLED = "ENABLED"
		V2 = "V2"
		V3 = "V3"

	class Persistentetag:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Rtsptunnel:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Altsvc:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dropinvalreqs:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dropextracrlf:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Http2:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Dropextradata:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Websocket:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Cmponpush:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Weblog:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Marktracereqinval:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

class nshttpprofile_response(base_response) :
	def __init__(self, length=1) :
		self.nshttpprofile = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nshttpprofile = [nshttpprofile() for _ in range(length)]

