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

class nspbr(base_resource) :
	""" Configuration for Policy Based Routing(PBR) entry resource. """
	def __init__(self) :
		self._name = None
		self._action = None
		self._td = None
		self._srcip = None
		self._srcipop = None
		self._srcipval = None
		self._srcport = None
		self._srcportop = None
		self._srcportval = None
		self._destip = None
		self._destipop = None
		self._destipval = None
		self._destport = None
		self._destportop = None
		self._destportval = None
		self._nexthop = None
		self._nexthopval = None
		self._iptunnel = None
		self._iptunnelname = None
		self._vxlanvlanmap = None
		self._srcmac = None
		self._srcmacmask = None
		self._protocol = None
		self._protocolnumber = None
		self._vlan = None
		self._vxlan = None
		self._Interface = None
		self._priority = None
		self._msr = None
		self._monitor = None
		self._state = None
		self._ownergroup = None
		self._detail = None
		self._hits = None
		self._kernelstate = None
		self._curstate = None
		self._totalprobes = None
		self._totalfailedprobes = None
		self._failedprobes = None
		self._monstatcode = None
		self._monstatparam1 = None
		self._monstatparam2 = None
		self._monstatparam3 = None
		self._data = None
		self.___count = None

	@property
	def name(self) :
		r"""Name for the PBR. Must begin with an ASCII alphabetic or underscore \(_\) character, and must contain only ASCII alphanumeric, underscore, hash \(\#\), period \(.\), space, colon \(:\), at \(@\), equals \(=\), and hyphen \(-\) characters. Cannot be changed after the PBR is created.<br/>Minimum length =  1.
		"""
		try :
			return self._name
		except Exception as e:
			raise e

	@name.setter
	def name(self, name) :
		r"""Name for the PBR. Must begin with an ASCII alphabetic or underscore \(_\) character, and must contain only ASCII alphanumeric, underscore, hash \(\#\), period \(.\), space, colon \(:\), at \(@\), equals \(=\), and hyphen \(-\) characters. Cannot be changed after the PBR is created.<br/>Minimum length =  1
		"""
		try :
			self._name = name
		except Exception as e:
			raise e

	@property
	def action(self) :
		r"""Action to perform on the outgoing IPv4 packets that match the PBR.
		Available settings function as follows:
		* ALLOW - The Citrix ADC sends the packet to the designated next-hop router.
		* DENY - The Citrix ADC applies the routing table for normal destination-based routing.<br/>Possible values = ALLOW, DENY.
		"""
		try :
			return self._action
		except Exception as e:
			raise e

	@action.setter
	def action(self, action) :
		r"""Action to perform on the outgoing IPv4 packets that match the PBR.
		Available settings function as follows:
		* ALLOW - The Citrix ADC sends the packet to the designated next-hop router.
		* DENY - The Citrix ADC applies the routing table for normal destination-based routing.<br/>Possible values = ALLOW, DENY
		"""
		try :
			self._action = action
		except Exception as e:
			raise e

	@property
	def td(self) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094.
		"""
		try :
			return self._td
		except Exception as e:
			raise e

	@td.setter
	def td(self, td) :
		r"""Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094
		"""
		try :
			self._td = td
		except Exception as e:
			raise e

	@property
	def srcip(self) :
		r"""IP address or range of IP addresses to match against the source IP address of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 10.102.29.30-10.102.29.189.
		"""
		try :
			return self._srcip
		except Exception as e:
			raise e

	@srcip.setter
	def srcip(self, srcip) :
		r"""IP address or range of IP addresses to match against the source IP address of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 10.102.29.30-10.102.29.189.
		"""
		try :
			self._srcip = srcip
		except Exception as e:
			raise e

	@property
	def srcipop(self) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ.
		"""
		try :
			return self._srcipop
		except Exception as e:
			raise e

	@srcipop.setter
	def srcipop(self, srcipop) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ
		"""
		try :
			self._srcipop = srcipop
		except Exception as e:
			raise e

	@property
	def srcipval(self) :
		r"""IP address or range of IP addresses to match against the source IP address of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 10.102.29.30-10.102.29.189.
		"""
		try :
			return self._srcipval
		except Exception as e:
			raise e

	@srcipval.setter
	def srcipval(self, srcipval) :
		r"""IP address or range of IP addresses to match against the source IP address of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 10.102.29.30-10.102.29.189.
		"""
		try :
			self._srcipval = srcipval
		except Exception as e:
			raise e

	@property
	def srcport(self) :
		r"""Port number or range of port numbers to match against the source port number of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 40-90.
		Note: The destination port can be specified only for TCP and UDP protocols.
		"""
		try :
			return self._srcport
		except Exception as e:
			raise e

	@srcport.setter
	def srcport(self, srcport) :
		r"""Port number or range of port numbers to match against the source port number of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 40-90.
		Note: The destination port can be specified only for TCP and UDP protocols.
		"""
		try :
			self._srcport = srcport
		except Exception as e:
			raise e

	@property
	def srcportop(self) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ.
		"""
		try :
			return self._srcportop
		except Exception as e:
			raise e

	@srcportop.setter
	def srcportop(self, srcportop) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ
		"""
		try :
			self._srcportop = srcportop
		except Exception as e:
			raise e

	@property
	def srcportval(self) :
		r"""Port number or range of port numbers to match against the source port number of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 40-90.
		Note: The destination port can be specified only for TCP and UDP protocols.<br/>Maximum length =  65535.
		"""
		try :
			return self._srcportval
		except Exception as e:
			raise e

	@srcportval.setter
	def srcportval(self, srcportval) :
		r"""Port number or range of port numbers to match against the source port number of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 40-90.
		Note: The destination port can be specified only for TCP and UDP protocols.<br/>Maximum length =  65535
		"""
		try :
			self._srcportval = srcportval
		except Exception as e:
			raise e

	@property
	def destip(self) :
		r"""IP address or range of IP addresses to match against the destination IP address of an outgoing IPv4 packet.  In the command line interface, separate the range with a hyphen. For example: 10.102.29.30-10.102.29.189.
		"""
		try :
			return self._destip
		except Exception as e:
			raise e

	@destip.setter
	def destip(self, destip) :
		r"""IP address or range of IP addresses to match against the destination IP address of an outgoing IPv4 packet.  In the command line interface, separate the range with a hyphen. For example: 10.102.29.30-10.102.29.189.
		"""
		try :
			self._destip = destip
		except Exception as e:
			raise e

	@property
	def destipop(self) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ.
		"""
		try :
			return self._destipop
		except Exception as e:
			raise e

	@destipop.setter
	def destipop(self, destipop) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ
		"""
		try :
			self._destipop = destipop
		except Exception as e:
			raise e

	@property
	def destipval(self) :
		r"""IP address or range of IP addresses to match against the destination IP address of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 10.102.29.30-10.102.29.189.
		"""
		try :
			return self._destipval
		except Exception as e:
			raise e

	@destipval.setter
	def destipval(self, destipval) :
		r"""IP address or range of IP addresses to match against the destination IP address of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 10.102.29.30-10.102.29.189.
		"""
		try :
			self._destipval = destipval
		except Exception as e:
			raise e

	@property
	def destport(self) :
		r"""Port number or range of port numbers to match against the destination port number of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 40-90.
		Note: The destination port can be specified only for TCP and UDP protocols.
		"""
		try :
			return self._destport
		except Exception as e:
			raise e

	@destport.setter
	def destport(self, destport) :
		r"""Port number or range of port numbers to match against the destination port number of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 40-90.
		Note: The destination port can be specified only for TCP and UDP protocols.
		"""
		try :
			self._destport = destport
		except Exception as e:
			raise e

	@property
	def destportop(self) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ.
		"""
		try :
			return self._destportop
		except Exception as e:
			raise e

	@destportop.setter
	def destportop(self, destportop) :
		r"""Either the equals (=) or does not equal (!=) logical operator.<br/>Possible values = =, !=, EQ, NEQ
		"""
		try :
			self._destportop = destportop
		except Exception as e:
			raise e

	@property
	def destportval(self) :
		r"""Port number or range of port numbers to match against the destination port number of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 40-90.
		Note: The destination port can be specified only for TCP and UDP protocols.<br/>Maximum length =  65535.
		"""
		try :
			return self._destportval
		except Exception as e:
			raise e

	@destportval.setter
	def destportval(self, destportval) :
		r"""Port number or range of port numbers to match against the destination port number of an outgoing IPv4 packet. In the command line interface, separate the range with a hyphen. For example: 40-90.
		Note: The destination port can be specified only for TCP and UDP protocols.<br/>Maximum length =  65535
		"""
		try :
			self._destportval = destportval
		except Exception as e:
			raise e

	@property
	def nexthop(self) :
		r"""IP address of the next hop router or the name of the link load balancing virtual server to which to send matching packets if action is set to ALLOW.
		If you specify a link load balancing (LLB) virtual server, which can provide a backup if a next hop link fails, first make sure that the next hops bound to the LLB virtual server are actually next hops that are directly connected to the Citrix ADC. Otherwise, the Citrix ADC throws an error when you attempt to create the PBR. The next hop can be null to represent null routes.
		"""
		try :
			return self._nexthop
		except Exception as e:
			raise e

	@nexthop.setter
	def nexthop(self, nexthop) :
		r"""IP address of the next hop router or the name of the link load balancing virtual server to which to send matching packets if action is set to ALLOW.
		If you specify a link load balancing (LLB) virtual server, which can provide a backup if a next hop link fails, first make sure that the next hops bound to the LLB virtual server are actually next hops that are directly connected to the Citrix ADC. Otherwise, the Citrix ADC throws an error when you attempt to create the PBR. The next hop can be null to represent null routes.
		"""
		try :
			self._nexthop = nexthop
		except Exception as e:
			raise e

	@property
	def nexthopval(self) :
		r"""The Next Hop IP address or gateway name.
		"""
		try :
			return self._nexthopval
		except Exception as e:
			raise e

	@nexthopval.setter
	def nexthopval(self, nexthopval) :
		r"""The Next Hop IP address or gateway name.
		"""
		try :
			self._nexthopval = nexthopval
		except Exception as e:
			raise e

	@property
	def iptunnel(self) :
		r"""The Tunnel name.
		"""
		try :
			return self._iptunnel
		except Exception as e:
			raise e

	@iptunnel.setter
	def iptunnel(self, iptunnel) :
		r"""The Tunnel name.
		"""
		try :
			self._iptunnel = iptunnel
		except Exception as e:
			raise e

	@property
	def iptunnelname(self) :
		r"""The iptunnel name where packets need to be forwarded upon.
		"""
		try :
			return self._iptunnelname
		except Exception as e:
			raise e

	@iptunnelname.setter
	def iptunnelname(self, iptunnelname) :
		r"""The iptunnel name where packets need to be forwarded upon.
		"""
		try :
			self._iptunnelname = iptunnelname
		except Exception as e:
			raise e

	@property
	def vxlanvlanmap(self) :
		r"""The vlan to vxlan mapping to be applied for incoming packets over this pbr tunnel.
		"""
		try :
			return self._vxlanvlanmap
		except Exception as e:
			raise e

	@vxlanvlanmap.setter
	def vxlanvlanmap(self, vxlanvlanmap) :
		r"""The vlan to vxlan mapping to be applied for incoming packets over this pbr tunnel.
		"""
		try :
			self._vxlanvlanmap = vxlanvlanmap
		except Exception as e:
			raise e

	@property
	def srcmac(self) :
		r"""MAC address to match against the source MAC address of an outgoing IPv4 packet.
		"""
		try :
			return self._srcmac
		except Exception as e:
			raise e

	@srcmac.setter
	def srcmac(self, srcmac) :
		r"""MAC address to match against the source MAC address of an outgoing IPv4 packet.
		"""
		try :
			self._srcmac = srcmac
		except Exception as e:
			raise e

	@property
	def srcmacmask(self) :
		r""" Used to define range of Source MAC address. It takes string of 0 and 1, 0s are for exact match and 1s for wildcard. For matching first 3 bytes of MAC address, srcMacMask value "000000111111". .<br/>Default value: "000000000000".
		"""
		try :
			return self._srcmacmask
		except Exception as e:
			raise e

	@srcmacmask.setter
	def srcmacmask(self, srcmacmask) :
		r""" Used to define range of Source MAC address. It takes string of 0 and 1, 0s are for exact match and 1s for wildcard. For matching first 3 bytes of MAC address, srcMacMask value "000000111111". .<br/>Default value: "000000000000"
		"""
		try :
			self._srcmacmask = srcmacmask
		except Exception as e:
			raise e

	@property
	def protocol(self) :
		r"""Protocol, identified by protocol name, to match against the protocol of an outgoing IPv4 packet.<br/>Possible values = ICMP, IGMP, TCP, EGP, IGP, ARGUS, UDP, RDP, RSVP, EIGRP, L2TP, ISIS, GGP, IPoverIP, ST, CBT, BBN-RCC-M, NVP-II, PUP, EMCON, XNET, CHAOS, MUX, DCN-MEAS, HMP, PRM, XNS-IDP, TRUNK-1, TRUNK-2, LEAF-1, LEAF-2, IRTP, ISO-TP4, NETBLT, MFE-NSP, MERIT-INP, SEP, 3PC, IDPR, XTP, DDP, IDPR-CMTP, TP++, IL, IPv6, SDRP, IPv6-Route, IPv6-Frag, IDRP, GRE, MHRP, BNA, ESP, AH, I-NLSP, SWIPE, NARP, MOBILE, TLSP, SKIP, ICMPV6, IPv6-NoNx, IPv6-Opts, Any-Host-Internal-Protocol, CFTP, Any-Local-Network, SAT-EXPAK, KRYPTOLAN, RVD, IPPC, Any-Distributed-File-System, TFTP, VISA, IPCV, CPNX, CPHB, WSN, PVP, BR-SAT-MO, SUN-ND, WB-MON, WB-EXPAK, ISO-IP, VMTP, SECURE-VM, VINES, TTP, NSFNET-IG, DGP, TCF, OSPFIGP, Sprite-RP, LARP, MTP, AX.25, IPIP, MICP, SCC-SP, ETHERIP, Any-Private-Encryption-Scheme, GMTP, IFMP, PNNI, PIM, ARIS, SCPS, QNX, A/N, IPComp, SNP, Compaq-Pe, IPX-in-IP, VRRP, PGM, Any-0-Hop-Protocol, ENCAP, DDX, IATP, STP, SRP, UTI, SMP, SM, PTP, FIRE, CRTP, CRUDP, SSCOPMCE, IPLT, SPS, PIPE, SCTP, FC, RSVP-E2E-IGNORE, Mobility-Header, UDPLite.
		"""
		try :
			return self._protocol
		except Exception as e:
			raise e

	@protocol.setter
	def protocol(self, protocol) :
		r"""Protocol, identified by protocol name, to match against the protocol of an outgoing IPv4 packet.<br/>Possible values = ICMP, IGMP, TCP, EGP, IGP, ARGUS, UDP, RDP, RSVP, EIGRP, L2TP, ISIS, GGP, IPoverIP, ST, CBT, BBN-RCC-M, NVP-II, PUP, EMCON, XNET, CHAOS, MUX, DCN-MEAS, HMP, PRM, XNS-IDP, TRUNK-1, TRUNK-2, LEAF-1, LEAF-2, IRTP, ISO-TP4, NETBLT, MFE-NSP, MERIT-INP, SEP, 3PC, IDPR, XTP, DDP, IDPR-CMTP, TP++, IL, IPv6, SDRP, IPv6-Route, IPv6-Frag, IDRP, GRE, MHRP, BNA, ESP, AH, I-NLSP, SWIPE, NARP, MOBILE, TLSP, SKIP, ICMPV6, IPv6-NoNx, IPv6-Opts, Any-Host-Internal-Protocol, CFTP, Any-Local-Network, SAT-EXPAK, KRYPTOLAN, RVD, IPPC, Any-Distributed-File-System, TFTP, VISA, IPCV, CPNX, CPHB, WSN, PVP, BR-SAT-MO, SUN-ND, WB-MON, WB-EXPAK, ISO-IP, VMTP, SECURE-VM, VINES, TTP, NSFNET-IG, DGP, TCF, OSPFIGP, Sprite-RP, LARP, MTP, AX.25, IPIP, MICP, SCC-SP, ETHERIP, Any-Private-Encryption-Scheme, GMTP, IFMP, PNNI, PIM, ARIS, SCPS, QNX, A/N, IPComp, SNP, Compaq-Pe, IPX-in-IP, VRRP, PGM, Any-0-Hop-Protocol, ENCAP, DDX, IATP, STP, SRP, UTI, SMP, SM, PTP, FIRE, CRTP, CRUDP, SSCOPMCE, IPLT, SPS, PIPE, SCTP, FC, RSVP-E2E-IGNORE, Mobility-Header, UDPLite
		"""
		try :
			self._protocol = protocol
		except Exception as e:
			raise e

	@property
	def protocolnumber(self) :
		r"""Protocol, identified by protocol number, to match against the protocol of an outgoing IPv4 packet.<br/>Minimum length =  1<br/>Maximum length =  255.
		"""
		try :
			return self._protocolnumber
		except Exception as e:
			raise e

	@protocolnumber.setter
	def protocolnumber(self, protocolnumber) :
		r"""Protocol, identified by protocol number, to match against the protocol of an outgoing IPv4 packet.<br/>Minimum length =  1<br/>Maximum length =  255
		"""
		try :
			self._protocolnumber = protocolnumber
		except Exception as e:
			raise e

	@property
	def vlan(self) :
		r"""ID of the VLAN. The Citrix ADC compares the PBR only to the outgoing packets on the specified VLAN. If you do not specify any interface ID, the appliance compares the PBR to the outgoing packets on all VLANs.<br/>Minimum length =  1<br/>Maximum length =  4094.
		"""
		try :
			return self._vlan
		except Exception as e:
			raise e

	@vlan.setter
	def vlan(self, vlan) :
		r"""ID of the VLAN. The Citrix ADC compares the PBR only to the outgoing packets on the specified VLAN. If you do not specify any interface ID, the appliance compares the PBR to the outgoing packets on all VLANs.<br/>Minimum length =  1<br/>Maximum length =  4094
		"""
		try :
			self._vlan = vlan
		except Exception as e:
			raise e

	@property
	def vxlan(self) :
		r"""ID of the VXLAN. The Citrix ADC compares the PBR only to the outgoing packets on the specified VXLAN. If you do not specify any interface ID, the appliance compares the PBR to the outgoing packets on all VXLANs.<br/>Minimum length =  1<br/>Maximum length =  16777215.
		"""
		try :
			return self._vxlan
		except Exception as e:
			raise e

	@vxlan.setter
	def vxlan(self, vxlan) :
		r"""ID of the VXLAN. The Citrix ADC compares the PBR only to the outgoing packets on the specified VXLAN. If you do not specify any interface ID, the appliance compares the PBR to the outgoing packets on all VXLANs.<br/>Minimum length =  1<br/>Maximum length =  16777215
		"""
		try :
			self._vxlan = vxlan
		except Exception as e:
			raise e

	@property
	def Interface(self) :
		r"""ID of an interface. The Citrix ADC compares the PBR only to the outgoing packets on the specified interface. If you do not specify any value, the appliance compares the PBR to the outgoing packets on all interfaces.
		"""
		try :
			return self._Interface
		except Exception as e:
			raise e

	@Interface.setter
	def Interface(self, Interface) :
		r"""ID of an interface. The Citrix ADC compares the PBR only to the outgoing packets on the specified interface. If you do not specify any value, the appliance compares the PBR to the outgoing packets on all interfaces.
		"""
		try :
			self._Interface = Interface
		except Exception as e:
			raise e

	@property
	def priority(self) :
		r"""Priority of the PBR, which determines the order in which it is evaluated relative to the other PBRs. If you do not specify priorities while creating PBRs, the PBRs are evaluated in the order in which they are created.<br/>Minimum length =  1<br/>Maximum length =  81920.
		"""
		try :
			return self._priority
		except Exception as e:
			raise e

	@priority.setter
	def priority(self, priority) :
		r"""Priority of the PBR, which determines the order in which it is evaluated relative to the other PBRs. If you do not specify priorities while creating PBRs, the PBRs are evaluated in the order in which they are created.<br/>Minimum length =  1<br/>Maximum length =  81920
		"""
		try :
			self._priority = priority
		except Exception as e:
			raise e

	@property
	def msr(self) :
		r"""Monitor the route specified byte Next Hop parameter. This parameter is not applicable if you specify a link load balancing (LLB) virtual server name with the Next Hop parameter.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._msr
		except Exception as e:
			raise e

	@msr.setter
	def msr(self, msr) :
		r"""Monitor the route specified byte Next Hop parameter. This parameter is not applicable if you specify a link load balancing (LLB) virtual server name with the Next Hop parameter.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._msr = msr
		except Exception as e:
			raise e

	@property
	def monitor(self) :
		r"""The name of the monitor.(Can be only of type ping or ARP ).<br/>Minimum length =  1.
		"""
		try :
			return self._monitor
		except Exception as e:
			raise e

	@monitor.setter
	def monitor(self, monitor) :
		r"""The name of the monitor.(Can be only of type ping or ARP ).<br/>Minimum length =  1
		"""
		try :
			self._monitor = monitor
		except Exception as e:
			raise e

	@property
	def state(self) :
		r"""Enable or disable the PBR. After you apply the PBRs, the Citrix ADC compares outgoing packets to the enabled PBRs.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.
		"""
		try :
			return self._state
		except Exception as e:
			raise e

	@state.setter
	def state(self, state) :
		r"""Enable or disable the PBR. After you apply the PBRs, the Citrix ADC compares outgoing packets to the enabled PBRs.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED
		"""
		try :
			self._state = state
		except Exception as e:
			raise e

	@property
	def ownergroup(self) :
		r"""The owner node group in a Cluster for this pbr rule. If ownernode is not specified then the pbr rule is treated as Striped pbr rule.<br/>Default value: DEFAULT_NG<br/>Minimum length =  1.
		"""
		try :
			return self._ownergroup
		except Exception as e:
			raise e

	@ownergroup.setter
	def ownergroup(self, ownergroup) :
		r"""The owner node group in a Cluster for this pbr rule. If ownernode is not specified then the pbr rule is treated as Striped pbr rule.<br/>Default value: DEFAULT_NG<br/>Minimum length =  1
		"""
		try :
			self._ownergroup = ownergroup
		except Exception as e:
			raise e

	@property
	def detail(self) :
		r"""To get a detailed view.
		"""
		try :
			return self._detail
		except Exception as e:
			raise e

	@detail.setter
	def detail(self, detail) :
		r"""To get a detailed view.
		"""
		try :
			self._detail = detail
		except Exception as e:
			raise e

	@property
	def hits(self) :
		r"""The hits of this PBR.
		"""
		try :
			return self._hits
		except Exception as e:
			raise e

	@property
	def kernelstate(self) :
		r"""The commit status of the PBR.<br/>Default value: NOTAPPLIED<br/>Possible values = APPLIED, NOTAPPLIED, RE-APPLY, SFAPPLIED, SFNOTAPPLIED, SFAPPLIED61, SFNOTAPPLIED61.
		"""
		try :
			return self._kernelstate
		except Exception as e:
			raise e

	@property
	def curstate(self) :
		r"""If this route is UP/DOWN.
		"""
		try :
			return self._curstate
		except Exception as e:
			raise e

	@property
	def totalprobes(self) :
		r"""The total number of probes sent.
		"""
		try :
			return self._totalprobes
		except Exception as e:
			raise e

	@property
	def totalfailedprobes(self) :
		r"""The total number of failed probes.
		"""
		try :
			return self._totalfailedprobes
		except Exception as e:
			raise e

	@property
	def failedprobes(self) :
		r"""Number of the current failed monitoring probes.
		"""
		try :
			return self._failedprobes
		except Exception as e:
			raise e

	@property
	def monstatcode(self) :
		r"""The code indicating the monitor response.
		"""
		try :
			return self._monstatcode
		except Exception as e:
			raise e

	@property
	def monstatparam1(self) :
		r"""First parameter for use with message code.
		"""
		try :
			return self._monstatparam1
		except Exception as e:
			raise e

	@property
	def monstatparam2(self) :
		r"""Second parameter for use with message code.
		"""
		try :
			return self._monstatparam2
		except Exception as e:
			raise e

	@property
	def monstatparam3(self) :
		r"""Third parameter for use with message code.
		"""
		try :
			return self._monstatparam3
		except Exception as e:
			raise e

	@property
	def data(self) :
		r"""Internal data of this route.
		"""
		try :
			return self._data
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(nspbr_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.nspbr
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
		addresource = nspbr()
		addresource.name = resource.name
		addresource.action = resource.action
		addresource.td = resource.td
		addresource.srcip = resource.srcip
		addresource.srcipop = resource.srcipop
		addresource.srcipval = resource.srcipval
		addresource.srcport = resource.srcport
		addresource.srcportop = resource.srcportop
		addresource.srcportval = resource.srcportval
		addresource.destip = resource.destip
		addresource.destipop = resource.destipop
		addresource.destipval = resource.destipval
		addresource.destport = resource.destport
		addresource.destportop = resource.destportop
		addresource.destportval = resource.destportval
		addresource.nexthop = resource.nexthop
		addresource.nexthopval = resource.nexthopval
		addresource.iptunnel = resource.iptunnel
		addresource.iptunnelname = resource.iptunnelname
		addresource.vxlanvlanmap = resource.vxlanvlanmap
		addresource.srcmac = resource.srcmac
		addresource.srcmacmask = resource.srcmacmask
		addresource.protocol = resource.protocol
		addresource.protocolnumber = resource.protocolnumber
		addresource.vlan = resource.vlan
		addresource.vxlan = resource.vxlan
		addresource.Interface = resource.Interface
		addresource.priority = resource.priority
		addresource.msr = resource.msr
		addresource.monitor = resource.monitor
		addresource.state = resource.state
		addresource.ownergroup = resource.ownergroup
		return addresource

	@classmethod
	def add(cls, client, resource) :
		r""" Use this API to add nspbr.
		"""
		try :
			if type(resource) is not list :
				addresource = cls.filter_add_parameters(resource)
				return addresource.add_resource(client)
			else :
				if (resource and len(resource) > 0) :
					addresources = [ nspbr() for _ in range(len(resource))]
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
		deleteresource = nspbr()
		deleteresource.name = resource.name
		return deleteresource

	@classmethod
	def delete(cls, client, resource) :
		r""" Use this API to delete nspbr.
		"""
		try :
			if type(resource) is not list :
				deleteresource = nspbr()
				if type(resource) !=  type(deleteresource):
					deleteresource.name = resource
				else :
					deleteresource = cls.filter_delete_parameters(resource)
				return deleteresource.delete_resource(client)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						deleteresources = [ nspbr() for _ in range(len(resource))]
						for i in range(len(resource)) :
							deleteresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						deleteresources = [ nspbr() for _ in range(len(resource))]
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
		updateresource = nspbr()
		updateresource.name = resource.name
		updateresource.action = resource.action
		updateresource.srcip = resource.srcip
		updateresource.srcipop = resource.srcipop
		updateresource.srcipval = resource.srcipval
		updateresource.srcport = resource.srcport
		updateresource.srcportop = resource.srcportop
		updateresource.srcportval = resource.srcportval
		updateresource.destip = resource.destip
		updateresource.destipop = resource.destipop
		updateresource.destipval = resource.destipval
		updateresource.destport = resource.destport
		updateresource.destportop = resource.destportop
		updateresource.destportval = resource.destportval
		updateresource.nexthop = resource.nexthop
		updateresource.nexthopval = resource.nexthopval
		updateresource.iptunnel = resource.iptunnel
		updateresource.iptunnelname = resource.iptunnelname
		updateresource.vxlanvlanmap = resource.vxlanvlanmap
		updateresource.srcmac = resource.srcmac
		updateresource.srcmacmask = resource.srcmacmask
		updateresource.protocol = resource.protocol
		updateresource.protocolnumber = resource.protocolnumber
		updateresource.vlan = resource.vlan
		updateresource.vxlan = resource.vxlan
		updateresource.Interface = resource.Interface
		updateresource.priority = resource.priority
		updateresource.msr = resource.msr
		updateresource.monitor = resource.monitor
		return updateresource

	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update nspbr.
		"""
		try :
			if type(resource) is not list :
				updateresource = cls.filter_update_parameters(resource)
				return updateresource.update_resource(client)
			else :
				if (resource and len(resource) > 0) :
					updateresources = [ nspbr() for _ in range(len(resource))]
					for i in range(len(resource)) :
						updateresources[i] = cls.filter_update_parameters(resource[i])
				result = cls.update_bulk_request(client, updateresources)
			return result
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of nspbr resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = nspbr()
				if type(resource) !=  type(unsetresource):
					unsetresource.name = resource
				else :
					unsetresource.name = resource.name
				return unsetresource.unset_resource(client, args)
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						unsetresources = [ nspbr() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						unsetresources = [ nspbr() for _ in range(len(resource))]
						for i in range(len(resource)) :
							unsetresources[i].name = resource[i].name
				result = cls.unset_bulk_request(client, unsetresources, args)
			return result
		except Exception as e :
			raise e

	@classmethod
	def enable(cls, client, resource) :
		r""" Use this API to enable nspbr.
		"""
		try :
			if type(resource) is not list :
				enableresource = nspbr()
				if type(resource) !=  type(enableresource):
					enableresource.name = resource
				else :
					enableresource.name = resource.name
				return enableresource.perform_operation(client,"enable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						enableresources = [ nspbr() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						enableresources = [ nspbr() for _ in range(len(resource))]
						for i in range(len(resource)) :
							enableresources[i].name = resource[i].name
				result = cls.perform_operation_bulk_request(client, enableresources,"enable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def disable(cls, client, resource) :
		r""" Use this API to disable nspbr.
		"""
		try :
			if type(resource) is not list :
				disableresource = nspbr()
				if type(resource) !=  type(disableresource):
					disableresource.name = resource
				else :
					disableresource.name = resource.name
				return disableresource.perform_operation(client,"disable")
			else :
				if type(resource[0]) != cls :
					if (resource and len(resource) > 0) :
						disableresources = [ nspbr() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].name = resource[i]
				else :
					if (resource and len(resource) > 0) :
						disableresources = [ nspbr() for _ in range(len(resource))]
						for i in range(len(resource)) :
							disableresources[i].name = resource[i].name
				result = cls.perform_operation_bulk_request(client, disableresources,"disable")
			return result
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the nspbr resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = nspbr()
				response = obj.get_resources(client, option_)
			else :
				if type(name) is not list :
					if type(name) == cls :
						raise Exception('Invalid parameter name:{0}'.format(type(name)))
					obj = nspbr()
					obj.name = name
					response = obj.get_resource(client, option_)
				else :
					if name and len(name) > 0 :
						if type(name[0]) == cls :
							raise Exception('Invalid parameter name:{0}'.format(type(name[0])))
						response = [nspbr() for _ in range(len(name))]
						obj = [nspbr() for _ in range(len(name))]
						for i in range(len(name)) :
							obj[i] = nspbr()
							obj[i].name = name[i]
							response[i] = obj[i].get_resource(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_args(cls, client, args) :
		r""" Use this API to fetch all the nspbr resources that are configured on netscaler.
	# This uses nspbr_args which is a way to provide additional arguments while fetching the resources.
		"""
		try :
			obj = nspbr()
			option_ = options()
			option_.args = nitro_util.object_to_string_withoutquotes(args)
			response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def get_filtered(cls, client, filter_) :
		r""" Use this API to fetch filtered set of nspbr resources.
		filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nspbr()
			option_ = options()
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			return response
		except Exception as e :
			raise e


	@classmethod
	def count(cls, client) :
		r""" Use this API to count the nspbr resources configured on NetScaler.
		"""
		try :
			obj = nspbr()
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
		r""" Use this API to count filtered the set of nspbr resources.
		Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".
		"""
		try :
			obj = nspbr()
			option_ = options()
			option_.count = True
			option_.filter = filter_
			response = obj.getfiltered(client, option_)
			if response :
				return response[0].__dict__['___count']
			return 0
		except Exception as e :
			raise e


	class Protocol:
		ICMP = "ICMP"
		IGMP = "IGMP"
		TCP = "TCP"
		EGP = "EGP"
		IGP = "IGP"
		ARGUS = "ARGUS"
		UDP = "UDP"
		RDP = "RDP"
		RSVP = "RSVP"
		EIGRP = "EIGRP"
		L2TP = "L2TP"
		ISIS = "ISIS"
		GGP = "GGP"
		IPoverIP = "IPoverIP"
		ST = "ST"
		CBT = "CBT"
		BBN_RCC_M = "BBN-RCC-M"
		NVP_II = "NVP-II"
		PUP = "PUP"
		EMCON = "EMCON"
		XNET = "XNET"
		CHAOS = "CHAOS"
		MUX = "MUX"
		DCN_MEAS = "DCN-MEAS"
		HMP = "HMP"
		PRM = "PRM"
		XNS_IDP = "XNS-IDP"
		TRUNK_1 = "TRUNK-1"
		TRUNK_2 = "TRUNK-2"
		LEAF_1 = "LEAF-1"
		LEAF_2 = "LEAF-2"
		IRTP = "IRTP"
		ISO_TP4 = "ISO-TP4"
		NETBLT = "NETBLT"
		MFE_NSP = "MFE-NSP"
		MERIT_INP = "MERIT-INP"
		SEP = "SEP"
		_3PC = "3PC"
		IDPR = "IDPR"
		XTP = "XTP"
		DDP = "DDP"
		IDPR_CMTP = "IDPR-CMTP"
		TP__ = "TP++"
		IL = "IL"
		IPv6 = "IPv6"
		SDRP = "SDRP"
		IPv6_Route = "IPv6-Route"
		IPv6_Frag = "IPv6-Frag"
		IDRP = "IDRP"
		GRE = "GRE"
		MHRP = "MHRP"
		BNA = "BNA"
		ESP = "ESP"
		AH = "AH"
		I_NLSP = "I-NLSP"
		SWIPE = "SWIPE"
		NARP = "NARP"
		MOBILE = "MOBILE"
		TLSP = "TLSP"
		SKIP = "SKIP"
		ICMPV6 = "ICMPV6"
		IPv6_NoNx = "IPv6-NoNx"
		IPv6_Opts = "IPv6-Opts"
		Any_Host_Internal_Protocol = "Any-Host-Internal-Protocol"
		CFTP = "CFTP"
		Any_Local_Network = "Any-Local-Network"
		SAT_EXPAK = "SAT-EXPAK"
		KRYPTOLAN = "KRYPTOLAN"
		RVD = "RVD"
		IPPC = "IPPC"
		Any_Distributed_File_System = "Any-Distributed-File-System"
		TFTP = "TFTP"
		VISA = "VISA"
		IPCV = "IPCV"
		CPNX = "CPNX"
		CPHB = "CPHB"
		WSN = "WSN"
		PVP = "PVP"
		BR_SAT_MO = "BR-SAT-MO"
		SUN_ND = "SUN-ND"
		WB_MON = "WB-MON"
		WB_EXPAK = "WB-EXPAK"
		ISO_IP = "ISO-IP"
		VMTP = "VMTP"
		SECURE_VM = "SECURE-VM"
		VINES = "VINES"
		TTP = "TTP"
		NSFNET_IG = "NSFNET-IG"
		DGP = "DGP"
		TCF = "TCF"
		OSPFIGP = "OSPFIGP"
		Sprite_RP = "Sprite-RP"
		LARP = "LARP"
		MTP = "MTP"
		AX_25 = "AX.25"
		IPIP = "IPIP"
		MICP = "MICP"
		SCC_SP = "SCC-SP"
		ETHERIP = "ETHERIP"
		Any_Private_Encryption_Scheme = "Any-Private-Encryption-Scheme"
		GMTP = "GMTP"
		IFMP = "IFMP"
		PNNI = "PNNI"
		PIM = "PIM"
		ARIS = "ARIS"
		SCPS = "SCPS"
		QNX = "QNX"
		A_N = "A/N"
		IPComp = "IPComp"
		SNP = "SNP"
		Compaq_Pe = "Compaq-Pe"
		IPX_in_IP = "IPX-in-IP"
		VRRP = "VRRP"
		PGM = "PGM"
		Any_0_Hop_Protocol = "Any-0-Hop-Protocol"
		ENCAP = "ENCAP"
		DDX = "DDX"
		IATP = "IATP"
		STP = "STP"
		SRP = "SRP"
		UTI = "UTI"
		SMP = "SMP"
		SM = "SM"
		PTP = "PTP"
		FIRE = "FIRE"
		CRTP = "CRTP"
		CRUDP = "CRUDP"
		SSCOPMCE = "SSCOPMCE"
		IPLT = "IPLT"
		SPS = "SPS"
		PIPE = "PIPE"
		SCTP = "SCTP"
		FC = "FC"
		RSVP_E2E_IGNORE = "RSVP-E2E-IGNORE"
		Mobility_Header = "Mobility-Header"
		UDPLite = "UDPLite"

	class Srcipop:
		_EQ = "="
		_NEQ = "!="
		EQ = "EQ"
		NEQ = "NEQ"

	class Destipop:
		_EQ = "="
		_NEQ = "!="
		EQ = "EQ"
		NEQ = "NEQ"

	class State:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Kernelstate:
		APPLIED = "APPLIED"
		NOTAPPLIED = "NOTAPPLIED"
		RE_APPLY = "RE-APPLY"
		SFAPPLIED = "SFAPPLIED"
		SFNOTAPPLIED = "SFNOTAPPLIED"
		SFAPPLIED61 = "SFAPPLIED61"
		SFNOTAPPLIED61 = "SFNOTAPPLIED61"

	class Msr:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"

	class Destportop:
		_EQ = "="
		_NEQ = "!="
		EQ = "EQ"
		NEQ = "NEQ"

	class Action:
		ALLOW = "ALLOW"
		DENY = "DENY"

	class Srcportop:
		_EQ = "="
		_NEQ = "!="
		EQ = "EQ"
		NEQ = "NEQ"

class nspbr_response(base_response) :
	def __init__(self, length=1) :
		self.nspbr = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.nspbr = [nspbr() for _ in range(length)]

