
# Copyright (c) 2008-2015 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use self file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

class MasContext(object):
    _mas_ip = ""
    _sessionid = ""
    _target_ip = ""

    def __init__(self, mas_ip, sessionid, target_ip):
        """ 
        @param mas_ip Ipaddress of the MAS
        @param sessionid of MAS
        @param target_ip Ipadress of the netscaler on which configuration is to be run.
        """
        self._mas_ip = mas_ip
        self._sessionid = sessionid
        self._target_ip = target_ip
            
    @property
    def sessionid(self):
        """ Gets the sessionId.
        @return sessionId.
        """
        return self._sessionid

    @property    
    def target_nsip(self):
        """ Gets the Ipaddress of the target netscaler.
        @return Ipadress.
        """
        return self._target_ip

    @target_nsip.setter
    def target_nsip(self, target_ip):
        """ set target nsip
        """
        self._target_ip = target_ip
            
    @property
    def mas_ip(self):
        """ Gets the Ipaddress of MAS
        @return MASIP
        """
        return self._mas_ip
