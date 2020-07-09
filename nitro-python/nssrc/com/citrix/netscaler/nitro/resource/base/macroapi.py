# Copyright (c) 2008-2019 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
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

from nssrc.com.citrix.netscaler.nitro.resource.base.base_resource import base_resource
from nssrc.com.citrix.netscaler.nitro.resource.base.base_responses import base_responses
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver import lbvserver
from nssrc.com.citrix.netscaler.nitro.resource.config.cs.csvserver import csvserver
from nssrc.com.citrix.netscaler.nitro.service.nitro_service import nitro_service
from nssrc.com.citrix.netscaler.nitro.service.options import options
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception

import abc
class macroapi(base_resource):
    """ Class to perform macroapi operations. Macroapi is used to
        add, update and delete multiple resources simuntaneously.
    """
    __metaclass__ = abc.ABCMeta

    @classmethod
    def add(cls, service, resources):
        """ Use this method to perform add operation on netscaler resources

        Parameters:
            service - nitro_service object.
            resources - list of netscaler resources.

        Returns:
            status of the operation performed.
        """
        resources = [resource.filter_add_parameters(resource) for resource in resources]
        return cls.add_bulk_request(service, resources)

    @classmethod
    def update(cls, service, resources):
        """ Use this method to perform update operation on netscaler resources

        Parameters:
            service - nitro_service object.
            resources - list of netscaler resources.

        Returns:
            status of the operation performed.
        """
        resources = [resource.filter_update_parameters(resource) for resource in resources]
        return cls.update_bulk_request(service, resources)

    @classmethod
    def delete(cls, service, resources):
        """ Use this method to perform delete operation on netscaler resources

        Parameters:
            service - nitro_service object.
            resources - list of netscaler resources.

        Returns:
            status of the operation performed.
        """
        resources = [resource.filter_delete_parameters(resource) for resource in resources]
        return cls.delete_bulk_request(service, resources)

    @classmethod
    def unbind(cls, service, resources):
        """ Use this method to perform unbind operation on netscaler resources

        Parameters:
            service - nitro_service object.
            resources - list of netscaler resources.

        Returns:
            status of the operation performed.
        """
        action = "unbind"
        return cls.perform_operation(service, resources, action)

    @classmethod
    def perform_operation(cls, service, resources, action):
        """ Use this method to perform a clear/sync/link/unlink/save ...etc
        operation on netscaler resources.

        Parameters:
            service - nitro_service object.
            resources - list of netscaler resources.
            action - action to be performed

        Returns:
            status of the operation performed.
        """
        return cls.perform_operation_bulk_request(service, resources, action)
