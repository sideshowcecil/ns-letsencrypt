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


class urlfilteringcategories_args :
	r""" Provides additional arguments required for fetching the urlfilteringcategories resource.
	"""
	def __init__(self) :
		self._group = None

	@property
	def group(self) :
		r"""URL Filtering SDK Category per Group.<br/>Minimum length =  1.
		"""
		try :
			return self._group
		except Exception as e:
			raise e

	@group.setter
	def group(self, group) :
		r"""URL Filtering SDK Category per Group.<br/>Minimum length =  1
		"""
		try :
			self._group = group
		except Exception as e:
			raise e

