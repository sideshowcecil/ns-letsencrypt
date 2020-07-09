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


class nsacl6_args :
	r""" Provides additional arguments required for fetching the nsacl6 resource.
	"""
	def __init__(self) :
		self._type = None

	@property
	def type(self) :
		r"""default will display both CLASSIC and DFD.<br/>Possible values = CLASSIC, DFD.
		"""
		try :
			return self._type
		except Exception as e:
			raise e

	@type.setter
	def type(self, type) :
		r"""default will display both CLASSIC and DFD.<br/>Possible values = CLASSIC, DFD
		"""
		try :
			self._type = type
		except Exception as e:
			raise e

	class Type:
		CLASSIC = "CLASSIC"
		DFD = "DFD"

