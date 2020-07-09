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


class nsversion_args :
	r""" Provides additional arguments required for fetching the nsversion resource.
	"""
	def __init__(self) :
		self._installedversion = None

	@property
	def installedversion(self) :
		r"""Installed version.
		"""
		try :
			return self._installedversion
		except Exception as e:
			raise e

	@installedversion.setter
	def installedversion(self, installedversion) :
		r"""Installed version.
		"""
		try :
			self._installedversion = installedversion
		except Exception as e:
			raise e

