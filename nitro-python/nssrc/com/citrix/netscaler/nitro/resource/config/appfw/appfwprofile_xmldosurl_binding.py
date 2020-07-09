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

class appfwprofile_xmldosurl_binding(base_resource) :
	""" Binding class showing the xmldosurl that can be bound to appfwprofile.
	"""
	def __init__(self) :
		self._xmldosurl = None
		self._xmlmaxelementdepthcheck = None
		self._xmlmaxelementdepth = None
		self._xmlmaxelementnamelengthcheck = None
		self._xmlmaxelementnamelength = None
		self._xmlmaxelementscheck = None
		self._xmlmaxelements = None
		self._xmlmaxelementchildrencheck = None
		self._xmlmaxelementchildren = None
		self._xmlmaxnodescheck = None
		self._xmlmaxnodes = None
		self._xmlmaxentityexpansionscheck = None
		self._xmlmaxentityexpansions = None
		self._xmlmaxentityexpansiondepthcheck = None
		self._xmlmaxentityexpansiondepth = None
		self._xmlmaxattributescheck = None
		self._xmlmaxattributes = None
		self._xmlmaxattributenamelengthcheck = None
		self._xmlmaxattributenamelength = None
		self._xmlmaxattributevaluelengthcheck = None
		self._xmlmaxattributevaluelength = None
		self._xmlmaxnamespacescheck = None
		self._xmlmaxnamespaces = None
		self._xmlmaxnamespaceurilengthcheck = None
		self._xmlmaxnamespaceurilength = None
		self._xmlmaxchardatalengthcheck = None
		self._xmlmaxchardatalength = None
		self._xmlmaxfilesizecheck = None
		self._xmlmaxfilesize = None
		self._xmlminfilesizecheck = None
		self._xmlminfilesize = None
		self._xmlblockpi = None
		self._xmlblockdtd = None
		self._xmlblockexternalentities = None
		self._xmlsoaparraycheck = None
		self._xmlmaxsoaparraysize = None
		self._xmlmaxsoaparrayrank = None
		self._state = None
		self._comment = None
		self._isautodeployed = None
		self._name = None
		self.___count = None

	@property
	def xmlmaxelementdepthcheck(self) :
		r"""State if XML Max element depth check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxelementdepthcheck
		except Exception as e:
			raise e

	@xmlmaxelementdepthcheck.setter
	def xmlmaxelementdepthcheck(self, xmlmaxelementdepthcheck) :
		r"""State if XML Max element depth check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxelementdepthcheck = xmlmaxelementdepthcheck
		except Exception as e:
			raise e

	@property
	def xmlmaxfilesize(self) :
		r"""Specify the maximum size of XML messages. Protects against overflow attacks.
		"""
		try :
			return self._xmlmaxfilesize
		except Exception as e:
			raise e

	@xmlmaxfilesize.setter
	def xmlmaxfilesize(self, xmlmaxfilesize) :
		r"""Specify the maximum size of XML messages. Protects against overflow attacks.
		"""
		try :
			self._xmlmaxfilesize = xmlmaxfilesize
		except Exception as e:
			raise e

	@property
	def xmlmaxnamespaceurilength(self) :
		r"""Specify the longest URI of any XML namespace. Protects against overflow attacks.
		"""
		try :
			return self._xmlmaxnamespaceurilength
		except Exception as e:
			raise e

	@xmlmaxnamespaceurilength.setter
	def xmlmaxnamespaceurilength(self, xmlmaxnamespaceurilength) :
		r"""Specify the longest URI of any XML namespace. Protects against overflow attacks.
		"""
		try :
			self._xmlmaxnamespaceurilength = xmlmaxnamespaceurilength
		except Exception as e:
			raise e

	@property
	def xmldosurl(self) :
		r"""XML DoS URL regular expression length.
		"""
		try :
			return self._xmldosurl
		except Exception as e:
			raise e

	@xmldosurl.setter
	def xmldosurl(self, xmldosurl) :
		r"""XML DoS URL regular expression length.
		"""
		try :
			self._xmldosurl = xmldosurl
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Enabled.<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""Enabled.<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def xmlsoaparraycheck(self) :
		r"""State if XML SOAP Array check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlsoaparraycheck
		except Exception as e:
			raise e

	@xmlsoaparraycheck.setter
	def xmlsoaparraycheck(self, xmlsoaparraycheck) :
		r"""State if XML SOAP Array check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlsoaparraycheck = xmlsoaparraycheck
		except Exception as e:
			raise e

	@property
	def xmlmaxelementnamelengthcheck(self) :
		r"""State if XML Max element name length check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxelementnamelengthcheck
		except Exception as e:
			raise e

	@xmlmaxelementnamelengthcheck.setter
	def xmlmaxelementnamelengthcheck(self, xmlmaxelementnamelengthcheck) :
		r"""State if XML Max element name length check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxelementnamelengthcheck = xmlmaxelementnamelengthcheck
		except Exception as e:
			raise e

	@property
	def xmlmaxelementscheck(self) :
		r"""State if XML Max elements check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxelementscheck
		except Exception as e:
			raise e

	@xmlmaxelementscheck.setter
	def xmlmaxelementscheck(self, xmlmaxelementscheck) :
		r"""State if XML Max elements check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxelementscheck = xmlmaxelementscheck
		except Exception as e:
			raise e

	@property
	def xmlmaxentityexpansions(self) :
		r"""Specify maximum allowed number of entity expansions. Protects aganist Entity Expansion Attack.
		"""
		try :
			return self._xmlmaxentityexpansions
		except Exception as e:
			raise e

	@xmlmaxentityexpansions.setter
	def xmlmaxentityexpansions(self, xmlmaxentityexpansions) :
		r"""Specify maximum allowed number of entity expansions. Protects aganist Entity Expansion Attack.
		"""
		try :
			self._xmlmaxentityexpansions = xmlmaxentityexpansions
		except Exception as e:
			raise e

	@property
	def xmlmaxattributes(self) :
		r"""Specify maximum number of attributes per XML element. Protects against overflow attacks.
		"""
		try :
			return self._xmlmaxattributes
		except Exception as e:
			raise e

	@xmlmaxattributes.setter
	def xmlmaxattributes(self, xmlmaxattributes) :
		r"""Specify maximum number of attributes per XML element. Protects against overflow attacks.
		"""
		try :
			self._xmlmaxattributes = xmlmaxattributes
		except Exception as e:
			raise e

	@property
	def xmlmaxfilesizecheck(self) :
		r"""State if XML Max file size check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxfilesizecheck
		except Exception as e:
			raise e

	@xmlmaxfilesizecheck.setter
	def xmlmaxfilesizecheck(self, xmlmaxfilesizecheck) :
		r"""State if XML Max file size check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxfilesizecheck = xmlmaxfilesizecheck
		except Exception as e:
			raise e

	@property
	def xmlmaxchardatalength(self) :
		r"""Specify the maximum size of CDATA. Protects against overflow attacks and large quantities of unparsed data within XML messages.
		"""
		try :
			return self._xmlmaxchardatalength
		except Exception as e:
			raise e

	@xmlmaxchardatalength.setter
	def xmlmaxchardatalength(self, xmlmaxchardatalength) :
		r"""Specify the maximum size of CDATA. Protects against overflow attacks and large quantities of unparsed data within XML messages.
		"""
		try :
			self._xmlmaxchardatalength = xmlmaxchardatalength
		except Exception as e:
			raise e

	@property
	def xmlmaxnamespacescheck(self) :
		r"""State if XML Max namespaces check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxnamespacescheck
		except Exception as e:
			raise e

	@xmlmaxnamespacescheck.setter
	def xmlmaxnamespacescheck(self, xmlmaxnamespacescheck) :
		r"""State if XML Max namespaces check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxnamespacescheck = xmlmaxnamespacescheck
		except Exception as e:
			raise e

	@property
	def xmlmaxnamespaces(self) :
		r"""Specify maximum number of active namespaces. Protects against overflow attacks.
		"""
		try :
			return self._xmlmaxnamespaces
		except Exception as e:
			raise e

	@xmlmaxnamespaces.setter
	def xmlmaxnamespaces(self, xmlmaxnamespaces) :
		r"""Specify maximum number of active namespaces. Protects against overflow attacks.
		"""
		try :
			self._xmlmaxnamespaces = xmlmaxnamespaces
		except Exception as e:
			raise e

	@property
	def xmlmaxattributenamelengthcheck(self) :
		r"""State if XML Max attribute name length check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxattributenamelengthcheck
		except Exception as e:
			raise e

	@xmlmaxattributenamelengthcheck.setter
	def xmlmaxattributenamelengthcheck(self, xmlmaxattributenamelengthcheck) :
		r"""State if XML Max attribute name length check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxattributenamelengthcheck = xmlmaxattributenamelengthcheck
		except Exception as e:
			raise e

	@property
	def xmlblockdtd(self) :
		r"""State if XML DTD is ON or OFF. Protects against recursive Document Type Declaration (DTD) entity expansion attacks. Also, SOAP messages cannot have DTDs in messages. .<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlblockdtd
		except Exception as e:
			raise e

	@xmlblockdtd.setter
	def xmlblockdtd(self, xmlblockdtd) :
		r"""State if XML DTD is ON or OFF. Protects against recursive Document Type Declaration (DTD) entity expansion attacks. Also, SOAP messages cannot have DTDs in messages. .<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlblockdtd = xmlblockdtd
		except Exception as e:
			raise e

	@property
	def xmlmaxattributevaluelength(self) :
		r"""Specify the longest value of any XML attribute. Protects against overflow attacks.
		"""
		try :
			return self._xmlmaxattributevaluelength
		except Exception as e:
			raise e

	@xmlmaxattributevaluelength.setter
	def xmlmaxattributevaluelength(self, xmlmaxattributevaluelength) :
		r"""Specify the longest value of any XML attribute. Protects against overflow attacks.
		"""
		try :
			self._xmlmaxattributevaluelength = xmlmaxattributevaluelength
		except Exception as e:
			raise e

	@property
	def xmlmaxelementdepth(self) :
		r"""Maximum nesting (depth) of XML elements. This check protects against documents that have excessive hierarchy depths.
		"""
		try :
			return self._xmlmaxelementdepth
		except Exception as e:
			raise e

	@xmlmaxelementdepth.setter
	def xmlmaxelementdepth(self, xmlmaxelementdepth) :
		r"""Maximum nesting (depth) of XML elements. This check protects against documents that have excessive hierarchy depths.
		"""
		try :
			self._xmlmaxelementdepth = xmlmaxelementdepth
		except Exception as e:
			raise e

	@property
	def xmlmaxelementnamelength(self) :
		r"""Specify the longest name of any element (including the expanded namespace) to protect against overflow attacks.
		"""
		try :
			return self._xmlmaxelementnamelength
		except Exception as e:
			raise e

	@xmlmaxelementnamelength.setter
	def xmlmaxelementnamelength(self, xmlmaxelementnamelength) :
		r"""Specify the longest name of any element (including the expanded namespace) to protect against overflow attacks.
		"""
		try :
			self._xmlmaxelementnamelength = xmlmaxelementnamelength
		except Exception as e:
			raise e

	@property
	def name(self) :
		r"""Name of the profile to which to bind an exemption or rule.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name of the profile to which to bind an exemption or rule.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def xmlblockpi(self) :
		r"""State if XML Block PI is ON or OFF. Protects resources from denial of service attacks as SOAP messages cannot have processing instructions (PI) in messages.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlblockpi
		except Exception as e:
			raise e

	@xmlblockpi.setter
	def xmlblockpi(self, xmlblockpi) :
		r"""State if XML Block PI is ON or OFF. Protects resources from denial of service attacks as SOAP messages cannot have processing instructions (PI) in messages.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlblockpi = xmlblockpi
		except Exception as e:
			raise e

	@property
	def xmlmaxelementchildrencheck(self) :
		r"""State if XML Max element children check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxelementchildrencheck
		except Exception as e:
			raise e

	@xmlmaxelementchildrencheck.setter
	def xmlmaxelementchildrencheck(self, xmlmaxelementchildrencheck) :
		r"""State if XML Max element children check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxelementchildrencheck = xmlmaxelementchildrencheck
		except Exception as e:
			raise e

	@property
	def xmlmaxelements(self) :
		r"""Specify the maximum number of XML elements allowed. Protects against overflow attacks.
		"""
		try :
			return self._xmlmaxelements
		except Exception as e:
			raise e

	@xmlmaxelements.setter
	def xmlmaxelements(self, xmlmaxelements) :
		r"""Specify the maximum number of XML elements allowed. Protects against overflow attacks.
		"""
		try :
			self._xmlmaxelements = xmlmaxelements
		except Exception as e:
			raise e

	@property
	def xmlmaxentityexpansionscheck(self) :
		r"""State if XML Max Entity Expansions Check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxentityexpansionscheck
		except Exception as e:
			raise e

	@xmlmaxentityexpansionscheck.setter
	def xmlmaxentityexpansionscheck(self, xmlmaxentityexpansionscheck) :
		r"""State if XML Max Entity Expansions Check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxentityexpansionscheck = xmlmaxentityexpansionscheck
		except Exception as e:
			raise e

	@property
	def xmlmaxnamespaceurilengthcheck(self) :
		r"""State if XML Max namespace URI length check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxnamespaceurilengthcheck
		except Exception as e:
			raise e

	@xmlmaxnamespaceurilengthcheck.setter
	def xmlmaxnamespaceurilengthcheck(self, xmlmaxnamespaceurilengthcheck) :
		r"""State if XML Max namespace URI length check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxnamespaceurilengthcheck = xmlmaxnamespaceurilengthcheck
		except Exception as e:
			raise e

	@property
	def xmlmaxentityexpansiondepthcheck(self) :
		r"""State if XML Max Entity Expansions Depth Check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxentityexpansiondepthcheck
		except Exception as e:
			raise e

	@xmlmaxentityexpansiondepthcheck.setter
	def xmlmaxentityexpansiondepthcheck(self, xmlmaxentityexpansiondepthcheck) :
		r"""State if XML Max Entity Expansions Depth Check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxentityexpansiondepthcheck = xmlmaxentityexpansiondepthcheck
		except Exception as e:
			raise e

	@property
	def xmlmaxattributevaluelengthcheck(self) :
		r"""State if XML Max atribute value length is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxattributevaluelengthcheck
		except Exception as e:
			raise e

	@xmlmaxattributevaluelengthcheck.setter
	def xmlmaxattributevaluelengthcheck(self, xmlmaxattributevaluelengthcheck) :
		r"""State if XML Max atribute value length is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxattributevaluelengthcheck = xmlmaxattributevaluelengthcheck
		except Exception as e:
			raise e

	@property
	def xmlmaxsoaparraysize(self) :
		r"""XML Max Total SOAP Array Size. Protects against SOAP Array Abuse attack.
		"""
		try :
			return self._xmlmaxsoaparraysize
		except Exception as e:
			raise e

	@xmlmaxsoaparraysize.setter
	def xmlmaxsoaparraysize(self, xmlmaxsoaparraysize) :
		r"""XML Max Total SOAP Array Size. Protects against SOAP Array Abuse attack.
		"""
		try :
			self._xmlmaxsoaparraysize = xmlmaxsoaparraysize
		except Exception as e:
			raise e

	@property
	def xmlmaxentityexpansiondepth(self) :
		r"""Specify maximum entity expansion depth. Protects aganist Entity Expansion Attack.
		"""
		try :
			return self._xmlmaxentityexpansiondepth
		except Exception as e:
			raise e

	@xmlmaxentityexpansiondepth.setter
	def xmlmaxentityexpansiondepth(self, xmlmaxentityexpansiondepth) :
		r"""Specify maximum entity expansion depth. Protects aganist Entity Expansion Attack.
		"""
		try :
			self._xmlmaxentityexpansiondepth = xmlmaxentityexpansiondepth
		except Exception as e:
			raise e

	@property
	def xmlmaxnodescheck(self) :
		r"""State if XML Max nodes check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxnodescheck
		except Exception as e:
			raise e

	@xmlmaxnodescheck.setter
	def xmlmaxnodescheck(self, xmlmaxnodescheck) :
		r"""State if XML Max nodes check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxnodescheck = xmlmaxnodescheck
		except Exception as e:
			raise e

	@property
	def xmlmaxattributenamelength(self) :
		r"""Specify the longest name of any XML attribute. Protects against overflow attacks.
		"""
		try :
			return self._xmlmaxattributenamelength
		except Exception as e:
			raise e

	@xmlmaxattributenamelength.setter
	def xmlmaxattributenamelength(self, xmlmaxattributenamelength) :
		r"""Specify the longest name of any XML attribute. Protects against overflow attacks.
		"""
		try :
			self._xmlmaxattributenamelength = xmlmaxattributenamelength
		except Exception as e:
			raise e

	@property
	def xmlmaxchardatalengthcheck(self) :
		r"""State if XML Max CDATA length check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxchardatalengthcheck
		except Exception as e:
			raise e

	@xmlmaxchardatalengthcheck.setter
	def xmlmaxchardatalengthcheck(self, xmlmaxchardatalengthcheck) :
		r"""State if XML Max CDATA length check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxchardatalengthcheck = xmlmaxchardatalengthcheck
		except Exception as e:
			raise e

	@property
	def xmlminfilesizecheck(self) :
		r"""State if XML Min file size check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlminfilesizecheck
		except Exception as e:
			raise e

	@xmlminfilesizecheck.setter
	def xmlminfilesizecheck(self, xmlminfilesizecheck) :
		r"""State if XML Min file size check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlminfilesizecheck = xmlminfilesizecheck
		except Exception as e:
			raise e

	@property
	def xmlmaxelementchildren(self) :
		r"""Specify the maximum number of children allowed per XML element. Protects against overflow attacks.
		"""
		try :
			return self._xmlmaxelementchildren
		except Exception as e:
			raise e

	@xmlmaxelementchildren.setter
	def xmlmaxelementchildren(self, xmlmaxelementchildren) :
		r"""Specify the maximum number of children allowed per XML element. Protects against overflow attacks.
		"""
		try :
			self._xmlmaxelementchildren = xmlmaxelementchildren
		except Exception as e:
			raise e

	@property
	def xmlminfilesize(self) :
		r"""Enforces minimum message size.
		"""
		try :
			return self._xmlminfilesize
		except Exception as e:
			raise e

	@xmlminfilesize.setter
	def xmlminfilesize(self, xmlminfilesize) :
		r"""Enforces minimum message size.
		"""
		try :
			self._xmlminfilesize = xmlminfilesize
		except Exception as e:
			raise e

	@property
	def xmlmaxnodes(self) :
		r"""Specify the maximum number of XML nodes. Protects against overflow attacks.
		"""
		try :
			return self._xmlmaxnodes
		except Exception as e:
			raise e

	@xmlmaxnodes.setter
	def xmlmaxnodes(self, xmlmaxnodes) :
		r"""Specify the maximum number of XML nodes. Protects against overflow attacks.
		"""
		try :
			self._xmlmaxnodes = xmlmaxnodes
		except Exception as e:
			raise e

	@property
	def isautodeployed(self) :
		r"""Is the rule auto deployed by dynamic profile ?.<br/>Possible values = AUTODEPLOYED, NOTAUTODEPLOYED.
		"""
		try :
			return self._isautodeployed
		except Exception as e:
			raise e

	@isautodeployed.setter
	def isautodeployed(self, isautodeployed) :
		r"""Is the rule auto deployed by dynamic profile ?.<br/>Possible values = AUTODEPLOYED, NOTAUTODEPLOYED
		"""
		try :
			self._isautodeployed = isautodeployed
		except Exception as e:
			raise e

	@property
	def comment(self) :
		r"""Any comments about the purpose of profile, or other useful information about the profile.
		"""
		try :
			return self._comment
		except Exception as e:
			raise e

	@comment.setter
	def comment(self, comment) :
		r"""Any comments about the purpose of profile, or other useful information about the profile.
		"""
		try :
			self._comment = comment
		except Exception as e:
			raise e

	@property
	def xmlmaxattributescheck(self) :
		r"""State if XML Max attributes check is ON or OFF.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlmaxattributescheck
		except Exception as e:
			raise e

	@xmlmaxattributescheck.setter
	def xmlmaxattributescheck(self, xmlmaxattributescheck) :
		r"""State if XML Max attributes check is ON or OFF.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlmaxattributescheck = xmlmaxattributescheck
		except Exception as e:
			raise e

	@property
	def xmlmaxsoaparrayrank(self) :
		r"""XML Max Individual SOAP Array Rank. This is the dimension of the SOAP array.
		"""
		try :
			return self._xmlmaxsoaparrayrank
		except Exception as e:
			raise e

	@xmlmaxsoaparrayrank.setter
	def xmlmaxsoaparrayrank(self, xmlmaxsoaparrayrank) :
		r"""XML Max Individual SOAP Array Rank. This is the dimension of the SOAP array.
		"""
		try :
			self._xmlmaxsoaparrayrank = xmlmaxsoaparrayrank
		except Exception as e:
			raise e

	@property
	def xmlblockexternalentities(self) :
		r"""State if XML Block External Entities Check is ON or OFF. Protects against XML External Entity (XXE) attacks that force applications to parse untrusted external entities (sources) in XML documents.<br/>Possible values = ON, OFF.
		"""
		try :
			return self._xmlblockexternalentities
		except Exception as e:
			raise e

	@xmlblockexternalentities.setter
	def xmlblockexternalentities(self, xmlblockexternalentities) :
		r"""State if XML Block External Entities Check is ON or OFF. Protects against XML External Entity (XXE) attacks that force applications to parse untrusted external entities (sources) in XML documents.<br/>Possible values = ON, OFF
		"""
		try :
			self._xmlblockexternalentities = xmlblockexternalentities
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(appfwprofile_xmldosurl_binding_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.appfwprofile_xmldosurl_binding
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
		addresource = appfwprofile_xmldosurl_binding()
		addresource.name = resource.name
		addresource.comment = resource.comment
		addresource.state = resource.state
		addresource.xmldosurl = resource.xmldosurl
		addresource.xmlmaxelementdepthcheck = resource.xmlmaxelementdepthcheck
		addresource.xmlmaxelementdepth = resource.xmlmaxelementdepth
		addresource.xmlmaxelementnamelengthcheck = resource.xmlmaxelementnamelengthcheck
		addresource.xmlmaxelementnamelength = resource.xmlmaxelementnamelength
		addresource.xmlmaxelementscheck = resource.xmlmaxelementscheck
		addresource.xmlmaxelements = resource.xmlmaxelements
		addresource.xmlmaxelementchildrencheck = resource.xmlmaxelementchildrencheck
		addresource.xmlmaxelementchildren = resource.xmlmaxelementchildren
		addresource.xmlmaxattributescheck = resource.xmlmaxattributescheck
		addresource.xmlmaxattributes = resource.xmlmaxattributes
		addresource.xmlmaxattributenamelengthcheck = resource.xmlmaxattributenamelengthcheck
		addresource.xmlmaxattributenamelength = resource.xmlmaxattributenamelength
		addresource.xmlmaxattributevaluelengthcheck = resource.xmlmaxattributevaluelengthcheck
		addresource.xmlmaxattributevaluelength = resource.xmlmaxattributevaluelength
		addresource.xmlmaxchardatalengthcheck = resource.xmlmaxchardatalengthcheck
		addresource.xmlmaxchardatalength = resource.xmlmaxchardatalength
		addresource.xmlmaxfilesizecheck = resource.xmlmaxfilesizecheck
		addresource.xmlmaxfilesize = resource.xmlmaxfilesize
		addresource.xmlminfilesizecheck = resource.xmlminfilesizecheck
		addresource.xmlminfilesize = resource.xmlminfilesize
		addresource.xmlblockpi = resource.xmlblockpi
		addresource.xmlblockdtd = resource.xmlblockdtd
		addresource.xmlblockexternalentities = resource.xmlblockexternalentities
		addresource.xmlmaxentityexpansionscheck = resource.xmlmaxentityexpansionscheck
		addresource.xmlmaxentityexpansions = resource.xmlmaxentityexpansions
		addresource.xmlmaxentityexpansiondepthcheck = resource.xmlmaxentityexpansiondepthcheck
		addresource.xmlmaxentityexpansiondepth = resource.xmlmaxentityexpansiondepth
		addresource.xmlmaxnamespacescheck = resource.xmlmaxnamespacescheck
		addresource.xmlmaxnamespaces = resource.xmlmaxnamespaces
		addresource.xmlmaxnamespaceurilengthcheck = resource.xmlmaxnamespaceurilengthcheck
		addresource.xmlmaxnamespaceurilength = resource.xmlmaxnamespaceurilength
		addresource.xmlsoaparraycheck = resource.xmlsoaparraycheck
		addresource.xmlmaxsoaparraysize = resource.xmlmaxsoaparraysize
		addresource.xmlmaxsoaparrayrank = resource.xmlmaxsoaparrayrank
		addresource.isautodeployed = resource.isautodeployed
		return addresource

	@classmethod
	def add(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				updateresource = cls.filter_add_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if resource and len(resource) > 0 :
					updateresources = [appfwprofile_xmldosurl_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_add_parameters(resource[i])
				return cls.update_bulk_request(client, updateresources)
		except Exception as e :
			raise e

	@classmethod
	def filter_delete_parameters(cls, resource) :
		r""" Use this function to create a resource with only delete operation specific parameters.
		"""
		deleteresource = appfwprofile_xmldosurl_binding()
		deleteresource.name = resource.name
		deleteresource.xmldosurl = resource.xmldosurl
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		try :
			if resource and type(resource) is not list :
				deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if resource and len(resource) > 0 :
					deleteresources = [appfwprofile_xmldosurl_binding() for _ in range(len(resource))]
					for i in range(len(resource)) :
						deleteresources[i] = cls.filter_delete_parameters(resource[i])
				return cls.delete_bulk_request(client, deleteresources)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, service, name="", option_="") :
		r""" Use this API to fetch appfwprofile_xmldosurl_binding resources.
		"""
		try :
			if not name :
				obj = appfwprofile_xmldosurl_binding()
				response = obj.get_resources(service, option_)
			else :
				obj = appfwprofile_xmldosurl_binding()
				obj.name = name
				response = obj.get_resources(service)
			return response
		except Exception as e:
			raise e

	@classmethod
	def get_filtered(cls, service, name, filter_) :
		r""" Use this API to fetch filtered set of appfwprofile_xmldosurl_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwprofile_xmldosurl_binding()
			obj.name = name
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			return response
		except Exception as e:
			raise e

	@classmethod
	def count(cls, service, name) :
		r""" Use this API to count appfwprofile_xmldosurl_binding resources configued on NetScaler.
		"""
		try :
			obj = appfwprofile_xmldosurl_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			response = obj.get_resources(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	@classmethod
	def count_filtered(cls, service, name, filter_) :
		r""" Use this API to count the filtered set of appfwprofile_xmldosurl_binding resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = appfwprofile_xmldosurl_binding()
			obj.name = name
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(service, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e:
			raise e

	class As_scan_location_xmlsql:
		ELEMENT = "ELEMENT"
		ATTRIBUTE = "ATTRIBUTE"

	class Jsonmaxarraylengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxelementdepthcheck:
		ON = "ON"
		OFF = "OFF"

	class Jsonmaxdocumentlengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxattachmentsizecheck:
		ON = "ON"
		OFF = "OFF"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Xmlsoaparraycheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex_ff:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlmaxelementnamelengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxelementscheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlendpointcheck:
		ABSOLUTE = "ABSOLUTE"
		RELATIVE = "RELATIVE"

	class Xmlmaxfilesizecheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxnamespacescheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxattributenamelengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Isvalueregex_xss:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlblockdtd:
		ON = "ON"
		OFF = "OFF"

	class Isregex_sql:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlblockpi:
		ON = "ON"
		OFF = "OFF"

	class Xmlvalidateresponse:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxelementchildrencheck:
		ON = "ON"
		OFF = "OFF"

	class Jsonmaxobjectkeylengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlmaxentityexpansionscheck:
		ON = "ON"
		OFF = "OFF"

	class As_scan_location_xss:
		FORMFIELD = "FORMFIELD"
		HEADER = "HEADER"
		COOKIE = "COOKIE"

	class Xmlmaxnamespaceurilengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxentityexpansiondepthcheck:
		ON = "ON"
		OFF = "OFF"

	class As_scan_location_xmlxss:
		ELEMENT = "ELEMENT"
		ATTRIBUTE = "ATTRIBUTE"

	class Isvalueregex_sql:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class As_scan_location_sql:
		FORMFIELD = "FORMFIELD"
		HEADER = "HEADER"
		COOKIE = "COOKIE"

	class Isregex_ffc:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlmaxattributevaluelengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Filetype:
		pdf = "pdf"
		msdoc = "msdoc"
		text = "text"
		image = "image"
		any = "any"

	class Jsonmaxobjectkeycountcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlattachmentcontenttypecheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex_xmlsql:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmlvalidatesoapenvelope:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxnodescheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxchardatalengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlminfilesizecheck:
		ON = "ON"
		OFF = "OFF"

	class Jsonmaxstringlengthcheck:
		ON = "ON"
		OFF = "OFF"

	class Isregex_xss:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class As_value_type_sql:
		Keyword = "Keyword"
		SpecialString = "SpecialString"
		Wildchar = "Wildchar"

	class Isregex_fileuploadtypes_url:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Isregex_xmlxss:
		REGEX = "REGEX"
		NOTREGEX = "NOTREGEX"

	class Xmladditionalsoapheaders:
		ON = "ON"
		OFF = "OFF"

	class Isautodeployed:
		AUTODEPLOYED = "AUTODEPLOYED"
		NOTAUTODEPLOYED = "NOTAUTODEPLOYED"

	class Jsonmaxcontainerdepthcheck:
		ON = "ON"
		OFF = "OFF"

	class Xmlmaxattributescheck:
		ON = "ON"
		OFF = "OFF"

	class Action:
		none = "none"
		block = "block"
		log = "log"
		remove = "remove"
		stats = "stats"
		xout = "xout"

	class As_value_type_xss:
		Tag = "Tag"
		Attribute = "Attribute"
		Pattern = "Pattern"

	class Xmlblockexternalentities:
		ON = "ON"
		OFF = "OFF"

class appfwprofile_xmldosurl_binding_response(base_response) :
	def __init__(self, length=1) :
		self.appfwprofile_xmldosurl_binding = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.appfwprofile_xmldosurl_binding = [appfwprofile_xmldosurl_binding() for _ in range(length)]

