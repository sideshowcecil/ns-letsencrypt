# Copyright (c) 2008-2015 Citrix Systems, Inc.
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

from nssrc.com.citrix.netscaler.nitro.resource.base.base_response import base_response
from nssrc.com.citrix.netscaler.nitro.resource.base.base_responses import base_responses
from nssrc.com.citrix.netscaler.nitro.resource.base.constants import *
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
from nssrc.com.citrix.netscaler.nitro.util.nitro_util import nitro_util
from nssrc.com.citrix.netscaler.nitro.service.options import options
from collections import OrderedDict

import requests
import json
import abc
import inspect
import re
try:
    import urllib2
except ImportError:
    import urllib.request as urllib2

class base_resource:
    __metaclass__ = abc.ABCMeta
    # Idempotent flag can't be added for these resources
    idempotent_invalid_resources = ["login", "logout", "reboot", "shutdown", "ping", "ping6", "traceroute", "traceroute6", "install"]
    # Regex string for extracting text inside <h4> tag from html page
    regex_for_h4_tag = r'<(h4)>(.+?)</(h4)>'
    @abc.abstractmethod
    def _get_nitro_response(self, service, string):
        pass

    @abc.abstractmethod
    def _get_object_name(self):
        pass

    @classmethod
    def get_object_type(cls):
        """ Gets the resource type.

        Returns:
            Resource Type. eg:lbvserver, csvserver.
        """
        return cls.__name__

    def resource_to_string(self, service):
        """ Converts netscaler resource to Json string.

        Parameters:
            service - nitro_service object.
            id - sessionId.

        Returns:
            string in Json format.
        """
        try:
            result = service.payload_formatter.resource_to_string(self)
            return result
        except Exception as e:
            raise e

    def resource_to_string(self, service):
        """ Converts netscaler resource to Json string.

        Parameters:
            service - nitro_service object

        Returns:
            string in Json format.
        """
        result = service.payload_formatter.resource_to_string(self)
        return result


    def unset_string(self, service, args):
        """ forms a String for unset operation on a resource.

        Parameters:
            service - nitro_service object.
            id - session id.
            args - Array of args that are to be unset.

        Returns:
            string in Json format.

        Throws:
            Exception if invalid input is given.
        """
        try:
            result = "{\"" + self.__class__.get_object_type() + "\":"
            result = result + service.payload_formatter.unset_string(self, args) + "}"
            return result
        except Exception as e:
            raise e

    @staticmethod
    def construct_url_queryparams_str(url_params_dict):
        """
        Constructs url parameter string from the dict
        @param url_params_dict Dictionary of parameters
        @return Constructed url parameter string
        """
        url_params = ""
        for idx, (key, val) in enumerate(url_params_dict.items()):
            if idx == 0:
                url_params += "?"
            else:
                url_params += "&"
            url_params += (key + "=" + val)
        return url_params

    def post_requestEx(self, service, opt):
        """ Use this method to perform a POST operation on netscaler resource.

        Parameters:
            service - nitro_service object.
            opt - Options class object.

        Returns:
            requested resource.

        Throws:
            Exception if invalid input is given.
        """
        try:
            request = self.resource_to_string(service)
            return self.post_dataEx(service, request, opt)
        except Exception as e:
            raise e


    def post_request(self, service, opt):
        """ Use this method to perform a Add operation on netscaler resource.

        Parameters:
            service - nitro_service object.
            opt - Options class object.

        Returns:
            status of the operation performed.

        Throws:
            Exception if invalid input is given.
        """
        try:
            request = self.resource_to_string(service)
            return self.post_data(service, request, opt)
        except Exception as e:
            raise e


    def unset_request(self, service, opt, args):
        """ Use this method to perform an Unset operation on netscaler resource.

        Parameters:
            service - nitro_service object.
            opt - options class object.
            args - string.

        Returns:
            status of the operation performed.

        Throws:
            Exception
        """
        try:
            request = self.unset_string(service, args)
            return self.post_data(service, request, opt)
        except Exception as e:
            raise e

    def add_resource(self, service, opt=""):
        """ Use this method to perform a add operation on netscaler resource.

        Parameters:
            service - nitro_service object.
            opt - options class object.

        Returns:
            status of the operation performed.

        Throws:
            Exception
        """
        try:
            if not service.isLogin():
                service.login()
            request = self.resource_to_string(service)
            return self.post_data(service, request, opt)
        except Exception as e:
            raise e


    def update_resource(self, service):
        """ Use this method to perform a modify operation on netscaler resource.

        Parameters:
            service - nitro_service object.
            opt - options class object.

        Returns:
            status of the operation performed.

        Throws:
            Exception
        """
        try:
            if not service.isLogin():
                service.login()
            request = self.resource_to_string(service)
            return self.put_data(service, request)
        except Exception as e:
            raise e


    def delete_resource(self, service):
        """ Use this method to perform a delete operation on netscaler resource.

        Parameters:
            service - nitro_service object

        Returns:
            status of the operation performed.

        Throws:
            Exception of the type nitro_exception is thrown.
        """
        try:
            if not service.isLogin() :
                service.login()
            str_ = nitro_util.object_to_string_withoutquotes(self)
            response = self.delete_request(service, str_)
            return response
        except Exception as e:
            raise e


    def getfiltered(self, service, opt):
        """ Use this method to perform a filtered get operation on netscaler resource.

        Parameters:
            service - nitro_service object.
            opt - options class object.

        Returns:
            Array of nitro resources of given resource type.

        Throws:
            Exception of the type nitro_exception is thrown.
        """
        try:
            if (not service.isLogin()):
                service.login()
            response = self.get_request(service, opt)
            return response
        except Exception as e:
            raise e

    def get_resources(self, service, opt=""):
        """ Use this method to perform a get operation on netscaler resource.

        Parameters:
            service - nitro_service object.
            opt - options class object.

        Returns:
            Array of nitro resources of specified type.

        Throws:
            Exception of the type nitro_exception is thrown.
        """
        try:
            if (not service.isLogin()):
                service.login()
            response = self.get_request(service, opt)
            return response
        except Exception as e:
            raise e


    def get_resource(self, service, opt=""):
        """ Use this method to perform a get operation on netscaler resource.

        Parameters:
            service - nitro_service object.
            opt - options class object.

        Returns:
            Array of nitro resources of specified type.

        Throws:
            Exception of the type nitro_exception is thrown.
        """
        try:
            if (not service.isLogin()):
                service.login()
            response = self.get_request(service, opt)
            if type(response) is list:
                return response[0]
            else :
                return response
            return None
        except Exception as e:
            raise e


    def stat_resources(self, service, opt="") :
        """ Use this method to perform a stat operation on netscaler resources.

        Parameters:
            service - nitro_service object.
            opt - options class object.

        Returns:
            Array of nitro stat resources of specified type.

        Throws:
            Exception of the type nitro_exception is thrown.
        """
        try:
            if not service.isLogin() :
                service.login()
            response = self.stat_request(service, opt)
            return response
        except Exception as e:
            raise e


    def stat_resource(self, service, opt=""):
        """ Use this method to perform a stat operation on a netscaler resource.

        Parameters:
            service - nitro_service object.
            opt - options class object.

        Returns:
            Requested Nitro stat resource.

        Throws:
            Exception of the type nitro_exception is thrown.
        """
        try:
            if (not service.isLogin()):
                service.login()
            response = self.stat_request(service, opt)
            if (response and len(response) > 0) :
                return response[0]
            return None
        except Exception as e:
            raise e


    def perform_operation(self, service, action="", opt=""):
        """ Use this method to perform a clear/sync/link/unlink/save ...etc
        operation on netscaler resource.

        Parameters:
            service - nitro_service object.
            action - action needs to be taken on resource.
            opt - options object with action that is to be performed set.

        Returns:
            status of the operation performed.

        Throws:
            Exception of the type nitro_exception is thrown.
        """
        try:
            if (not service.isLogin() and self.__class__.get_object_type()!="login"):
                service.login()
            if not opt and not action:
                return self.post_request(service, None)
            elif not opt :
                opt = options()
                opt.action = action
            response = self.post_request(service, opt)
            return response
        except Exception as e:
            raise e


    def perform_operationEx(self, service, action=""):
        """ Use this method to perform a POST operation that returns a resource ...etc
        operation on netscaler resource.

        Parameters:
            service - nitro_service object.
            action - action needs to be taken on resource.

        Returns:
            requested resource

        Throws:
            Exception of the type nitro_exception is thrown.
        """
        try:
            if (not service.isLogin() and self.__class__.get_object_type() != "login"):
                service.login()
            opt = options()
            opt.action = action
            response = self.post_requestEx(service, opt)
            return response
        except Exception as e:
            raise e


    @classmethod
    def perform_operation_bulk_request(cls, service, resources, action ):
        """ Use this method to perform a clear/sync/link/unlink/save ...etc
        operation on netscaler resources.

        Parameters:
            service - nitro_service object.
            resources - Array of Nitro resources on which the specified action to be performed.
            opt - options object with action that is to be performed set.

        Returns:
            status of the operation performed.

        Throws:
            Exception of the type nitro_exception is thrown.
        """
        try:
            if (not service.isLogin()):
                service.login()

            opt = options()
            opt.action = action
            resource_name = cls.__name__
            if resource_name == "macroapi":
                request = service.payload_formatter.resource_to_string_macroapi(resources)
            else:
                request = service.payload_formatter.resource_to_string_bulk(resources)
            result = cls.post_bulk_data(service, request, opt)
            return result
        except Exception as e:
            raise e


    def rename_resource(self, service, newname):
        """ Use this method to perform a rename operation on netscaler resource.

        Parameters:
            service - nitro_service object.
            newname - new name to be set to the specified resource.

        Returns:
            status of the operation performed.

        Throws:
            Exception of the type nitro_exception is thrown.
        """
        try:
            if not service.isLogin():
                service.login()

            if '_newname' in self.__dict__ :
                self.newname = newname
            else :
                raise nitro_exception(-1,str("Rename is not supported for this resource"),)
            opt = options()
            opt.action = "rename"
            response = self.post_request(service, opt)
            return response
        except Exception as e:
            raise e


    def unset_resource(self, service, args):
        """ Use this method to perform an Unset operation on netscaler resource.

        Parameters:
            service - nitro_service object.
            args - Array of args that are to be unset.

        Returns:
            status of the operation performed.

        Throws:
            Exception of the type nitro_exception is thrown.
        """
        try:
            if not service.isLogin():
                service.login()
            opt = options()
            opt.action = "unset"
            response = self.unset_request(service, opt, args)
            return response
        except Exception as e:
            raise e


    @classmethod
    def update_bulk_request(cls, service, resources):
        """ Use this method to perform an update operation on netscaler resources.

        Parameters:
            service - nitro_service object.
            resources - Array of nitro resources to be updated.

        Returns:
            status of the operation performed.

        Throws:
            Exception of the type nitro_exception is thrown.
        """
        try:
            if (not service.isLogin()):
                service.login()
            resource_name = cls.__name__
            if resource_name == "macroapi":
                request = service.payload_formatter.resource_to_string_macroapi(resources)
            else:
                request = service.payload_formatter.resource_to_string_bulk(resources)
            result = cls.put_bulk_data(service, request)
            return result
        except Exception as e:
            raise e


    @classmethod
    def unset_bulk_request(cls, service, resources, args):
        try:
            if (not service.isLogin()):
                service.login()

            opt = options()
            opt.action = "unset"
            request = service.payload_formatter.unset_string_bulk(resources, args)
            return cls.post_bulk_data(service, request, opt)
        except Exception as e:
            raise e


    @classmethod
    def add_bulk_request(cls, service, resources, opt=""):
        """ Use this method to perform a add operation on netscaler resources.

        Parameters:
            service - nitro_service object.
            resources - Nitro resources to be added on netscaler.
            opt - options class object.

        Returns:
            status of the performed operation.

        Throws:
            Exception  Nitro exception is thrown.
        """
        try:
            if not service.isLogin():
                service.login()
            resource_name = cls.__name__
            if resource_name == "macroapi":
                request = service.payload_formatter.resource_to_string_macroapi(resources)
            else:
                request = service.payload_formatter.resource_to_string_bulk(resources)
            result = cls.post_bulk_data(service, request, opt)
            return result
        except Exception as e:
            raise e


    @classmethod
    def delete_bulk_request(cls, service, resources, opt=""):
        """ Use this method to perform a delete operation on netscaler resources.

        Parameters:
            service - nitro_service object.
            resources - Nitro resources to be deleted on netscaler.
            opt - options class object.

        Returns:
            status of the performed operation.

        Throws:
            Exception  Nitro exception is thrown.
        """
        try:
            if (not service.isLogin()):
                service.login()
            opt = options()
            opt.action = "rm"
            resource_name = cls.__name__
            if resource_name == "macroapi":
                request = service.payload_formatter.resource_to_string_macroapi(resources)
            else:
                type_ = resources[0].__class__.get_object_type()
                if (type_.find("_binding") > 0):
                    opt.action = "unbind"
                request = service.payload_formatter.resource_to_string_bulk(resources)
            result = cls.post_bulk_data(service, request, opt)
            return result
        except Exception as e:
            raise e


    @staticmethod
    def _put(resourcetype, service, request, bulk=""):
        """ This method, forms the http PUT request, applies on the netscaler.
        Reads the response from the netscaler and converts it to base response.

        Parameters:
            service - nitro_service object.
            request - Json request.

        Returns:
            status of the operation performed.

        Throws:
            Exception of the type nitro_exception is thrown.
        """
        try :
            if (service.isMasContext):
                ipaddress = service.mas_ipaddress
            else :
                ipaddress = service.ipaddress
            version = service.version
            protocol = service.protocol
            if inspect.isclass(resourcetype) :
                resrc_type = resourcetype.get_object_type()
                urlstr = protocol+"://" + ipaddress + "/nitro/" + version + "/config/" + resrc_type
            else :
                resrc_type = resourcetype.__class__.get_object_type()
                urlstr = protocol+"://" + ipaddress + "/nitro/" + version + "/config/" + resrc_type
                name = str(resourcetype._get_object_name())
                if (name and len(name) > 0):
                    urlstr = urlstr+"/"+ str(nitro_util.encode(nitro_util.encode(name)))
            warning = service.warning
            onerror = service.onerror
            skipinvalidarg = service.skipinvalidarg
            idempotent = service.idempotent

            url_params_dict = OrderedDict()
            if warning and warning==True :
                url_params_dict["warning"]= "yes"
            if skipinvalidarg:
                url_params_dict["skipinvalidarg"] = "yes"
            # Add idempotent flag if resource-name doesn't have "_binding" and is not one of idempotent_invalid_resources
            if idempotent and ("_binding" not in resrc_type) and (resrc_type not in base_resource.idempotent_invalid_resources):
                url_params_dict["idempotent"] = "yes"

            urlstr += base_resource.construct_url_queryparams_str(url_params_dict)
            if bulk :
                headers = {'Content-type': 'application/vnd.com.citrix.netscaler.'+ resrc_type +'_list+json','Connection': 'keep-alive'}
            else :
                headers = {'Content-type': 'application/vnd.com.citrix.netscaler.'+ resrc_type +'+json','Connection': 'keep-alive'}
            if onerror:
                headers['X-NITRO-ONERROR'] = onerror

            retry = True
            retries = 0
            while retry:
                # set sessionid in headers
                if service.isMasContext:
                    headers['Cookie'] = 'SESSID='+service.mas_sessionid
                    headers['_MPS_API_PROXY_MANAGED_INSTANCE_IP'] = service.mas_target_nsip
                elif service.basic_auth:
                    headers['Authorization'] = service.get_basic_auth_str()
                else :
                    headers['Set-Cookie'] = 'NITRO_AUTH_TOKEN='+ service.sessionid

                response = requests.put(urlstr, data=request, headers=headers, verify = service.certvalidation, timeout=(service.connection_timeout,service.read_timeout))
                if not response.ok:
               	    #return '{"errorcode":0,"severitnc:"Done","message":"DONEXXX"}'
               	    #return '{"errorcode":123,"severity":"ERROR","message":"ERROR-INJCTED"}'
               	    #return '{"errorcode":777,"severity":"None","message":"some member bindings failed", "servicegroup_servicegroupmemberlist_binding":[{"failed_member_list":[{"ip":"1.2.3.4","port":80},{"ip":"5.6.7.8","port":81}]}]}'
               	    #return '{ "errorcode": 1243, "message": "Bulk operation failed", "severity": "ERROR", "response": [ { "errorcode": 273, "message": "Resource already exists", "severity": "ERROR" , "servicegroup_servicegroupmemberlist_binding":[{"failed_member_list":[{"ip":"1.1.1.1","port":88}]}]}, { "errorcode": 1265, "message": "command not attempted for configuration", "severity": "WARNING" } ] }'
                    # in case of "bulk request" - '200' Ok is returned as statuscode for session expiry error,
                    # hence it will not be handled in above if block
                    response = json.loads(response.text)
                    if not service.isMasContext and response["errorcode"] in [NSERR_SESSION_EXPIRED, NSERR_AUTHTIMEOUT] and retries < MAX_LOGIN_RETRIES_ALLOWED:
                        retries += 1
                        # Re-Login
                        service.clear_session()
                        service.login()
                    else:
                        #response returned by MAS in case of error does not have severity..
                        try:
                            response["severity"]
                        except KeyError:
                            response["severity"] = "ERROR"
                        raise nitro_exception((response['errorcode']), str(response['message']), str(response['severity']))
                elif bulk:
                    response_json = json.loads(response.text)
                    if not service.isMasContext and response_json["errorcode"] in [NSERR_SESSION_EXPIRED, NSERR_AUTHTIMEOUT] and retries < MAX_LOGIN_RETRIES_ALLOWED:
                        retries += 1
                        # Re-Login
                        service.clear_session()
                        service.login()
                    else:
                        return response.text
                else:
                    if response.text:
                        return response.text
                    nitro_response = {}
                    nitro_response['errorcode'] = 0
                    nitro_response['message'] = "Done"
                    nitro_response['severity']= ""
                    return json.dumps(nitro_response)
        except Exception as e:
            raise e

    def put_data(self, service, request):
        try:
            response = self._put(self, service, request)
            if self.is_desiredstate_api(self):
                return self._get_nitro_response(service, response)
            result = service.payload_formatter.string_to_resource(base_response, response, self.__class__.__name__)
            if (result.errorcode != 0):
                if (result.severity):
                    if(result.severity  == "ERROR"):
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result
        except Exception as e:
            raise e

    @classmethod
    def put_bulk_data(cls, service, request):
        try:
            is_bulk_request = True
            if cls.__name__ == "macroapi":
                is_bulk_request = False
            response = cls._put(cls, service, request, is_bulk_request)
#             if cls.is_desiredstate_api(cls):
#                 return cls._get_nitro_response_bulk(cls, service, response)
            result =service.payload_formatter.string_to_resource(base_responses, response, cls.__name__)
            if (result.errorcode != 0):
                if(result.severity):
                    if(result.severity == "ERROR"):
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity), result.response)
                else:
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity), result.response)
            return result
        except Exception as e:
            raise e


    @staticmethod
    def _post(resourcetype, service, request, opt, bulk=""):
        """ This method, forms the http POST request, applies on the netscaler.
        Reads the response from the netscaler and converts it to base response.

        Parameters:
            service - nitro_service object.
            request - Json request.

        Returns:
            status of the operation performed.

        Throws:
            Exception
        """
        try:
            if (service.isMasContext):
                ipaddress = service.mas_ipaddress
            else :
                ipaddress = service.ipaddress
            version = service.version
            protocol = service.protocol
            if inspect.isclass(resourcetype) :
                resrc_type = resourcetype.get_object_type()
            else :
                resrc_type = resourcetype.__class__.get_object_type()

            urlstr = protocol+"://" + ipaddress + "/nitro/" + version + "/config/" + resrc_type
            warning = service.warning
            onerror = service.onerror
            skipinvalidarg = service.skipinvalidarg
            idempotent = service.idempotent
            url_params_dict = OrderedDict()
            if opt :
                if opt.action :
                    url_params_dict["action"] = opt.action
            if warning and warning==True :
                url_params_dict["warning"] = "yes"
            if skipinvalidarg :
                url_params_dict["skipinvalidarg"] = "yes"
            # Add idempotent flag only if action is empty and resource-name doesn't have "_binding" and is not one of idempotent_invalid_resources
            if idempotent and not (opt and opt.action) and ("_binding" not in resrc_type) and (resrc_type not in base_resource.idempotent_invalid_resources):
                url_params_dict["idempotent"] = "yes"

            urlstr += base_resource.construct_url_queryparams_str(url_params_dict)

            if bulk :
                headers = {'Content-type': 'application/vnd.com.citrix.netscaler.'+ resrc_type +'_list+json','Connection': 'keep-alive'}
            else :
                headers = {'Content-type': 'application/vnd.com.citrix.netscaler.'+ resrc_type +'+json','Connection': 'keep-alive'}
            if onerror:
                headers["X-NITRO-ONERROR"] = onerror

            retry = True
            retries = 0
            while retry:
                # set sessionid in headers
                if service.isMasContext:
                    headers['Cookie'] = 'SESSID='+service.mas_sessionid
                    headers['_MPS_API_PROXY_MANAGED_INSTANCE_IP'] = service.mas_target_nsip
                elif service.basic_auth:
                    headers['Authorization'] = service.get_basic_auth_str()
                elif service.sessionid:
                    headers['Set-Cookie'] = 'NITRO_AUTH_TOKEN='+ service.sessionid
                response = requests.post(urlstr, data=request, headers=headers, verify = service.certvalidation, timeout=(service.connection_timeout,service.read_timeout))
                if not response.ok:
                    # in case of "bulk request" - '200' Ok is returned as statuscode for session expiry error,
                    # hence it will not be handled in above if block
                    response = json.loads(response.text)
                    if not service.isMasContext and response["errorcode"] in [NSERR_SESSION_EXPIRED, NSERR_AUTHTIMEOUT] and retries < MAX_LOGIN_RETRIES_ALLOWED:
                        retries += 1
                        # Re-Login
                        service.clear_session()
                        service.login()
                    else:
                        #response returned by MAS in case of error does not have severity..
                        try:
                            response["severity"]
                        except KeyError:
                            response["severity"] = "ERROR"
                        raise nitro_exception((response['errorcode']), str(response['message']), str(response['severity']))
                elif bulk and  response.text :
                    response_json = json.loads(response.text)
                    if not service.isMasContext and response_json["errorcode"] in [NSERR_SESSION_EXPIRED, NSERR_AUTHTIMEOUT] and retries < MAX_LOGIN_RETRIES_ALLOWED:
                        retries += 1
                        # Re-Login
                        service.clear_session()
                        service.login()
                    else:
                        return response.text
                else:
                    response_needed = resourcetype.is_responseneeded(resrc_type,opt)
                    if response_needed and response.text :
                        return response.text
                    nitro_response = {}
                    if resrc_type == "login" :
                        nitro_response['sessionid']=urllib2.unquote(response.cookies['NITRO_AUTH_TOKEN'])
                    nitro_response['errorcode'] = 0
                    nitro_response['message'] = "Done"
                    nitro_response['severity']= ""
                    return json.dumps(nitro_response)
        except Exception as e:
            raise e

    def post_dataEx(self, service, request, opt=""):
        try:
            response = self._post(self, service, request, opt)
            result = self._get_nitro_response(service, response)
            return result[0]
        except Exception as e:
            raise e


    def post_data(self, service, request, opt):
        try :
            response = self._post(self, service, request, opt)
            result = service.payload_formatter.string_to_resource(base_response, response, self.__class__.__name__)
            if (result.errorcode != 0 and result.errorcode != 1034):
                if result.severity:
                    if (result.severity == "ERROR"):
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else:
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result
        except Exception as e:
            raise e

    @classmethod
    def post_bulk_data(cls, service, request, opt=""):
        try:
            is_bulk_request = True
            if cls.__name__ == "macroapi":
                is_bulk_request = False
            response = cls._post(cls, service, request, opt, is_bulk_request)
            result = service.payload_formatter.string_to_resource(base_responses, response, cls.__name__)
            if (result.errorcode != 0):
                if (result.severity):
                    if (result.severity == "ERROR"):
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity), result.response)
                else:
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity), result.response)
            return result
        except Exception as e:
            raise e


    def get_request(self, service, opt):
        """ This method, forms the http GET request, applies on the netscaler.
        Reads the response from the netscaler and converts it to corresponding
        resource type.

        Parameters:
            service - nitro_service object.
            opt - Options class object

        Returns:
            Array of requested resources.
        """
        try:
            if (service.isMasContext):
                ipaddress = service.mas_ipaddress
            else :
                ipaddress = service.ipaddress

            version = service.version
            sessionid = service.sessionid
            objtype = self.__class__.get_object_type()
            protocol = service.protocol

            # build URL
            urlstr = protocol + "://" + ipaddress + "/nitro/" + version + "/config/" + objtype;

            name = self._get_object_name();
            if (name and len(name) > 0):
                urlstr = urlstr+"/"+ str(nitro_util.encode(nitro_util.encode(name)))

            if (opt or (service.warning)):
                optionstr = ""
                if (opt):
                    optionstr = opt.to_string()
                    if (len(optionstr) > 0):
                        urlstr = urlstr +"?"
                        urlstr = urlstr + optionstr
                if (service.warning):
                    if (opt and len(optionstr) > 0):
                        urlstr = urlstr+"&"
                    else:
                        urlstr = urlstr+"?"
                    urlstr = urlstr+"warning=yes"

            headers = {'Content-type': 'application/vnd.com.citrix.netscaler.'+ objtype +'+json','Connection': 'keep-alive'}

            retry = True
            retries = 0
            while retry:
                # set sessionid in headers
                if service.isMasContext:
                    headers['Cookie'] = 'SESSID='+service.mas_sessionid
                    headers['_MPS_API_PROXY_MANAGED_INSTANCE_IP'] = service.mas_target_nsip
                elif service.basic_auth:
                    headers['Authorization'] = service.get_basic_auth_str()
                else:
                    headers['Set-Cookie'] = 'NITRO_AUTH_TOKEN='+ service.sessionid

                response = requests.get(urlstr, headers=headers, verify = service.certvalidation, timeout=(service.connection_timeout,service.read_timeout))
                if not response.ok:
                    try:
                        response = json.loads(response.text)
                    except Exception as e:
                        # HTML page is returned for Basic Auth Failure
                        error_msg = ""
                        # find the text-message inside h4 tag using regex
                        r = re.compile(base_resource.regex_for_h4_tag, re.IGNORECASE | re.DOTALL)
                        x = re.findall(r, response.text)
                        if len(x):
                            error_msg = x[0][1]
                        raise nitro_exception(NSERR_NOUSER, error_msg, "ERROR")
                    if not service.isMasContext and response["errorcode"] in [NSERR_SESSION_EXPIRED, NSERR_AUTHTIMEOUT] and retries < MAX_LOGIN_RETRIES_ALLOWED:
                        retries += 1
                        # Re-Login
                        service.clear_session()
                        service.login()
                    else:
                        try:
                            response["severity"]
                        except KeyError:
                            response["severity"] = "ERROR"
                        raise nitro_exception((response['errorcode']), str(response['message']), str(response['severity']))
                else:
                    result = self._get_nitro_response(service, response.text)
                    return result
        except Exception as e:
            raise e



    def stat_request(self, service,opt):
        """ This method, forms the http GET request, applies on the netscaler.
        Reads the response from the netscaler and converts it to corresponding stat resource type.

        Parameters:
            service
            opt - Options class object

        Returns:
            Array of requested resources.
        """
        try:
            if (service.isMasContext):
                ipaddress = service.mas_ipaddress
            else:
                ipaddress = service.ipaddress
            version = service.version
            sessionid = service.sessionid
            objtype = self.__class__.get_object_type()
            objtype = objtype.split('_stats')
            objtype = objtype[0]
            protocol = service.protocol

            # build URL
            urlstr = protocol + "://" + ipaddress + "/nitro/" + version + "/stat/" + objtype;

            name = self._get_object_name();
            if (name and len(name) > 0):
                urlstr = urlstr+"/"+ str(nitro_util.encode(nitro_util.encode(name)))

            if (opt or service.warning):
                optionstr = ""
                if (opt):
                    optionstr = opt.to_string()
                    if (len(optionstr) > 0):
                        urlstr = urlstr +"?"
                        urlstr = urlstr + optionstr
                if (service.warning):
                    if (opt and len(optionstr) > 0):
                        urlstr = urlstr+"&"
                    else:
                        urlstr = urlstr+"?"
                    urlstr = urlstr+"warning=yes"
            headers = {'Content-type': 'application/vnd.com.citrix.netscaler.'+ objtype +'+json','Connection': 'keep-alive'}

            retry = True
            retries = 0
            while retry:
                # set sessionid in headers
                if service.isMasContext:
                    headers['Cookie'] = 'SESSID='+service.mas_sessionid
                    headers['_MPS_API_PROXY_MANAGED_INSTANCE_IP'] = service.mas_target_nsip
                elif service.basic_auth:
                    headers['Authorization'] = service.get_basic_auth_str()
                else:
                    headers['Set-Cookie'] = 'NITRO_AUTH_TOKEN='+ service.sessionid

                response = requests.get(urlstr, headers=headers, verify = service.certvalidation, timeout=(service.connection_timeout,service.read_timeout))
                if not response.ok:
                    try:
                        response = json.loads(response.text)
                    except Exception as e:
                        # HTML page is returned for Basic Auth Failure
                        error_msg = ""
                        # find the text-message inside h4 tag using regex
                        r = re.compile(base_resource.regex_for_h4_tag, re.IGNORECASE | re.DOTALL)
                        x = re.findall(r, response.text)
                        if len(x):
                            error_msg = x[0][1]
                        raise nitro_exception(NSERR_NOUSER, error_msg, "ERROR")
                    if not service.isMasContext and (response["errorcode"] == NSERR_SESSION_EXPIRED or response["errorcode"] == NSERR_AUTHTIMEOUT) and retries < MAX_LOGIN_RETRIES_ALLOWED:
                        retries += 1
                        # Re-Login
                        service.clear_session()
                        service.login()
                    else:
                        #response returned by MAS in case of error does not have severity..
                        try:
                            response["severity"]
                        except KeyError:
                            response["severity"] = "ERROR"
                        raise nitro_exception((response['errorcode']), str(response['message']), str(response['severity']))
                else:
                    result = self._get_nitro_response(service, response.text)
                    return result
        except Exception as e:
            raise e


    def delete_request(self, service, req_args):
        """ This method, forms the http DELETE request, applies on the netscaler.
        Reads the response from the netscaler and converts it to base response.

        Parameters:
            service - nitro_service object.
            req_args

        Returns:
            Array of requested resources.

        Throws:
            Exception
        """
        try:
            if (service.isMasContext):
                ipaddress = service.mas_ipaddress
            else:
                ipaddress = service.ipaddress
            version = service.version
            sessionid = service.sessionid
            objtype = self.__class__.get_object_type()
            protocol = service.protocol

            # build URL
            urlstr = protocol + "://" + ipaddress + "/nitro/" + version + "/config/" + objtype

            name = self._get_object_name()
            if (name and len(name) > 0):
                urlstr = urlstr+"/"+nitro_util.encode(nitro_util.encode(name))

            url_params_dict = OrderedDict()
            if (service.skipinvalidarg):
                url_params_dict["skipinvalidarg"] = "yes"
            if(req_args):
                url_params_dict["args"] = req_args
            if(service.warning):
                url_params_dict["warning"] = "yes"

            urlstr += base_resource.construct_url_queryparams_str(url_params_dict)

            headers = {'Content-type': 'application/vnd.com.citrix.netscaler.'+ objtype +'+json','Connection': 'keep-alive'}

            retry = True
            retries = 0
            while retry:
                # set sessionid in headers
                if service.isMasContext:
                    headers['Cookie'] = 'SESSID='+service.mas_sessionid
                    headers['_MPS_API_PROXY_MANAGED_INSTANCE_IP'] = service.mas_target_nsip
                elif service.basic_auth:
                    headers['Authorization'] = service.get_basic_auth_str()
                else:
                    headers['Set-Cookie'] = 'NITRO_AUTH_TOKEN='+ service.sessionid
                response = requests.delete(urlstr, headers=headers, verify = service.certvalidation, timeout=(service.connection_timeout,service.read_timeout))
                if not response.ok:
                    try:
                        response = json.loads(response.text)
                    except Exception as e:
                        # HTML page is returned for Basic Auth Failure
                        error_msg = ""
                        # find the text-message inside h4 tag using regex
                        r = re.compile(base_resource.regex_for_h4_tag, re.IGNORECASE | re.DOTALL)
                        x = re.findall(r, response.text)
                        if len(x):
                            error_msg = x[0][1]
                        raise nitro_exception(NSERR_NOUSER, error_msg, "ERROR")
                    if not service.isMasContext and response["errorcode"] in [NSERR_SESSION_EXPIRED, NSERR_AUTHTIMEOUT] and retries < MAX_LOGIN_RETRIES_ALLOWED:
                        retries += 1
                        service.clear_session()
                        service.login()
                    else:
                        #response returned by MAS in case of error does not have severity..
                        try:
                            response["severity"]
                        except KeyError:
                            response["severity"] = "ERROR"
                        raise nitro_exception((response['errorcode']), str(response['message']), str(response['severity']))
                else:
                    result = service.payload_formatter.string_to_resource(base_response, response.text, self.__class__.__name__)
                    return result
        except Exception as e:
            raise e

    @staticmethod
    def is_desiredstate_api(resourcetype):
        if inspect.isclass(resourcetype):
            if (resourcetype.get_object_type() == "servicegroup_servicegroupmemberlist_binding"):
                return True
        else:
            if (resourcetype.__class__.get_object_type() == "servicegroup_servicegroupmemberlist_binding"):
                return True
        return False

    @staticmethod
    def is_responseneeded(resrc_name, opt):
        resources_list = ["techsupport", "ping", "ping6", "traceroute", "traceroute6", "macroapi"]
        if resrc_name in resources_list:
            return True
        elif (resrc_name == "nsconfig" and hasattr(opt,'action')):
            if (opt.action == "diff"):
                return True
            else:
                return False
        else:
            return False
