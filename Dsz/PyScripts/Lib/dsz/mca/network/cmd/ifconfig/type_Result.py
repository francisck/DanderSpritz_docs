# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.MclTime
import array
import mcl.object.IpAddr
RESULT_FIXED_TYPE_NOT_SPECIFIED = 0
RESULT_FIXED_TYPE_BROADCAST = 1
RESULT_FIXED_TYPE_PEER_TO_PEER = 2
RESULT_FIXED_TYPE_MIXED = 3
RESULT_FIXED_TYPE_HYBRID = 4
RESULT_ADAPTER_TYPE_NOT_SPECIFIED = 1
RESULT_ADAPTER_TYPE_ETHERNET = 1
RESULT_ADAPTER_TYPE_TOKENRING = 2
RESULT_ADAPTER_TYPE_FDDI = 3
RESULT_ADAPTER_TYPE_PPP = 4
RESULT_ADAPTER_TYPE_LOCAL = 5
RESULT_ADAPTER_TYPE_IP6INIP4 = 6
RESULT_ADAPTER_TYPE_SLIP = 7
RESULT_ADAPTER_TYPE_OTHER = 8
RESULT_ADAPTER_TYPE_ATM = 9
RESULT_ADAPTER_TYPE_802_11 = 10
RESULT_ADAPTER_TYPE_TUNNEL = 11
RESULT_ADAPTER_TYPE_1394 = 12
RESULT_MAX_ADAPTER_ADDRESS_SIZE = 8
RESULT_MEDIA_STATE_NOT_KNOWN = 0
RESULT_MEDIA_STATE_UP = 1
RESULT_MEDIA_STATE_DOWN = 2
RESULT_MEDIA_STATE_TESTING = 3
RESULT_MEDIA_STATE_UNKNOWN = 4
RESULT_MEDIA_STATE_DORMANT = 5
RESULT_MEDIA_STATE_NOT_PRESENT = 6
RESULT_MEDIA_STATE_LOWER_LAYER_DOWN = 7

class FixedResult:

    def __init__(self):
        self.__dict__['type'] = RESULT_FIXED_TYPE_NOT_SPECIFIED
        self.__dict__['enableDns'] = False
        self.__dict__['enableProxy'] = False
        self.__dict__['enableRouting'] = False
        self.__dict__['hostName'] = ''
        self.__dict__['domainName'] = ''
        self.__dict__['scopeId'] = ''

    def __getattr__(self, name):
        if name == 'type':
            return self.__dict__['type']
        if name == 'enableDns':
            return self.__dict__['enableDns']
        if name == 'enableProxy':
            return self.__dict__['enableProxy']
        if name == 'enableRouting':
            return self.__dict__['enableRouting']
        if name == 'hostName':
            return self.__dict__['hostName']
        if name == 'domainName':
            return self.__dict__['domainName']
        if name == 'scopeId':
            return self.__dict__['scopeId']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'type':
            self.__dict__['type'] = value
        elif name == 'enableDns':
            self.__dict__['enableDns'] = value
        elif name == 'enableProxy':
            self.__dict__['enableProxy'] = value
        elif name == 'enableRouting':
            self.__dict__['enableRouting'] = value
        elif name == 'hostName':
            self.__dict__['hostName'] = value
        elif name == 'domainName':
            self.__dict__['domainName'] = value
        elif name == 'scopeId':
            self.__dict__['scopeId'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_FIXED_INFO_TYPE, self.__dict__['type'])
        submsg.AddBool(MSG_KEY_RESULT_FIXED_INFO_ENABLE_DNS, self.__dict__['enableDns'])
        submsg.AddBool(MSG_KEY_RESULT_FIXED_INFO_ENABLE_PROXY, self.__dict__['enableProxy'])
        submsg.AddBool(MSG_KEY_RESULT_FIXED_INFO_ENABLE_ROUTING, self.__dict__['enableRouting'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_FIXED_INFO_HOST_NAME, self.__dict__['hostName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_FIXED_INFO_DOMAIN_NAME, self.__dict__['domainName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_FIXED_INFO_SCOPE_ID, self.__dict__['scopeId'])
        mmsg.AddMessage(MSG_KEY_RESULT_FIXED_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_FIXED_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_RESULT_FIXED_INFO_TYPE)
        self.__dict__['enableDns'] = submsg.FindBool(MSG_KEY_RESULT_FIXED_INFO_ENABLE_DNS)
        self.__dict__['enableProxy'] = submsg.FindBool(MSG_KEY_RESULT_FIXED_INFO_ENABLE_PROXY)
        self.__dict__['enableRouting'] = submsg.FindBool(MSG_KEY_RESULT_FIXED_INFO_ENABLE_ROUTING)
        self.__dict__['hostName'] = submsg.FindString(MSG_KEY_RESULT_FIXED_INFO_HOST_NAME)
        self.__dict__['domainName'] = submsg.FindString(MSG_KEY_RESULT_FIXED_INFO_DOMAIN_NAME)
        self.__dict__['scopeId'] = submsg.FindString(MSG_KEY_RESULT_FIXED_INFO_SCOPE_ID)


class AdapterResult:

    def __init__(self):
        self.__dict__['index'] = 0
        self.__dict__['enabled'] = False
        self.__dict__['type'] = RESULT_ADAPTER_TYPE_NOT_SPECIFIED
        self.__dict__['status'] = RESULT_MEDIA_STATE_NOT_KNOWN
        self.__dict__['dhcpEnabled'] = False
        self.__dict__['haveWins'] = False
        self.__dict__['leaseObtained'] = mcl.object.MclTime.MclTime()
        self.__dict__['leaseExpires'] = mcl.object.MclTime.MclTime()
        self.__dict__['physicalAddress'] = array.array('B')
        i = 0
        while i < RESULT_MAX_ADAPTER_ADDRESS_SIZE:
            self.__dict__['physicalAddress'].append(0)
            i = i + 1

        self.__dict__['physicalAddressLength'] = 6
        self.__dict__['mtu'] = 0
        self.__dict__['arpEnabled'] = False
        self.__dict__['name'] = ''
        self.__dict__['description'] = ''
        self.__dict__['dnsSuffix'] = ''
        self.__dict__['subnetMask'] = ''
        self.__dict__['primaryWins'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['secondaryWins'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['dhcp'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['gateway'] = mcl.object.IpAddr.IpAddr()

    def __getattr__(self, name):
        if name == 'index':
            return self.__dict__['index']
        if name == 'enabled':
            return self.__dict__['enabled']
        if name == 'type':
            return self.__dict__['type']
        if name == 'status':
            return self.__dict__['status']
        if name == 'dhcpEnabled':
            return self.__dict__['dhcpEnabled']
        if name == 'haveWins':
            return self.__dict__['haveWins']
        if name == 'leaseObtained':
            return self.__dict__['leaseObtained']
        if name == 'leaseExpires':
            return self.__dict__['leaseExpires']
        if name == 'physicalAddress':
            return self.__dict__['physicalAddress']
        if name == 'physicalAddressLength':
            return self.__dict__['physicalAddressLength']
        if name == 'mtu':
            return self.__dict__['mtu']
        if name == 'arpEnabled':
            return self.__dict__['arpEnabled']
        if name == 'name':
            return self.__dict__['name']
        if name == 'description':
            return self.__dict__['description']
        if name == 'dnsSuffix':
            return self.__dict__['dnsSuffix']
        if name == 'subnetMask':
            return self.__dict__['subnetMask']
        if name == 'primaryWins':
            return self.__dict__['primaryWins']
        if name == 'secondaryWins':
            return self.__dict__['secondaryWins']
        if name == 'dhcp':
            return self.__dict__['dhcp']
        if name == 'gateway':
            return self.__dict__['gateway']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'index':
            self.__dict__['index'] = value
        elif name == 'enabled':
            self.__dict__['enabled'] = value
        elif name == 'type':
            self.__dict__['type'] = value
        elif name == 'status':
            self.__dict__['status'] = value
        elif name == 'dhcpEnabled':
            self.__dict__['dhcpEnabled'] = value
        elif name == 'haveWins':
            self.__dict__['haveWins'] = value
        elif name == 'leaseObtained':
            self.__dict__['leaseObtained'] = value
        elif name == 'leaseExpires':
            self.__dict__['leaseExpires'] = value
        elif name == 'physicalAddress':
            self.__dict__['physicalAddress'] = value
        elif name == 'physicalAddressLength':
            self.__dict__['physicalAddressLength'] = value
        elif name == 'mtu':
            self.__dict__['mtu'] = value
        elif name == 'arpEnabled':
            self.__dict__['arpEnabled'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        elif name == 'description':
            self.__dict__['description'] = value
        elif name == 'dnsSuffix':
            self.__dict__['dnsSuffix'] = value
        elif name == 'subnetMask':
            self.__dict__['subnetMask'] = value
        elif name == 'primaryWins':
            self.__dict__['primaryWins'] = value
        elif name == 'secondaryWins':
            self.__dict__['secondaryWins'] = value
        elif name == 'dhcp':
            self.__dict__['dhcp'] = value
        elif name == 'gateway':
            self.__dict__['gateway'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_ADAPTER_INFO_INDEX, self.__dict__['index'])
        submsg.AddBool(MSG_KEY_RESULT_ADAPTER_INFO_ENABLED, self.__dict__['enabled'])
        submsg.AddU8(MSG_KEY_RESULT_ADAPTER_INFO_TYPE, self.__dict__['type'])
        submsg.AddU8(MSG_KEY_RESULT_ADAPTER_INFO_STATUS, self.__dict__['status'])
        submsg.AddBool(MSG_KEY_RESULT_ADAPTER_INFO_DHCP_ENABLED, self.__dict__['dhcpEnabled'])
        submsg.AddBool(MSG_KEY_RESULT_ADAPTER_INFO_HAVE_WINS, self.__dict__['haveWins'])
        submsg.AddTime(MSG_KEY_RESULT_ADAPTER_INFO_LEASE_OBTAINED, self.__dict__['leaseObtained'])
        submsg.AddTime(MSG_KEY_RESULT_ADAPTER_INFO_LEASE_EXPIRES, self.__dict__['leaseExpires'])
        submsg.AddData(MSG_KEY_RESULT_ADAPTER_INFO_PHYSICAL_ADDRESS, self.__dict__['physicalAddress'])
        submsg.AddU8(MSG_KEY_RESULT_ADAPTER_INFO_PHYSICAL_ADDRESS_LENGTH, self.__dict__['physicalAddressLength'])
        submsg.AddU32(MSG_KEY_RESULT_ADAPTER_INFO_MTU, self.__dict__['mtu'])
        submsg.AddBool(MSG_KEY_RESULT_ADAPTER_INFO_ARP_ENABLED, self.__dict__['arpEnabled'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_ADAPTER_INFO_NAME, self.__dict__['name'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_ADAPTER_INFO_DESCRIPTION, self.__dict__['description'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_ADAPTER_INFO_DNS_SUFFIX, self.__dict__['dnsSuffix'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_ADAPTER_INFO_SUBNET_MASK, self.__dict__['subnetMask'])
        submsg.AddIpAddr(MSG_KEY_RESULT_ADAPTER_INFO_PRIMARY_WINS, self.__dict__['primaryWins'])
        submsg.AddIpAddr(MSG_KEY_RESULT_ADAPTER_INFO_SECONDAY_WINS, self.__dict__['secondaryWins'])
        submsg.AddIpAddr(MSG_KEY_RESULT_ADAPTER_INFO_DHCP, self.__dict__['dhcp'])
        submsg.AddIpAddr(MSG_KEY_RESULT_ADAPTER_INFO_GATEWAY, self.__dict__['gateway'])
        mmsg.AddMessage(MSG_KEY_RESULT_ADAPTER_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_ADAPTER_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['index'] = submsg.FindU32(MSG_KEY_RESULT_ADAPTER_INFO_INDEX)
        self.__dict__['enabled'] = submsg.FindBool(MSG_KEY_RESULT_ADAPTER_INFO_ENABLED)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_RESULT_ADAPTER_INFO_TYPE)
        self.__dict__['status'] = submsg.FindU8(MSG_KEY_RESULT_ADAPTER_INFO_STATUS)
        self.__dict__['dhcpEnabled'] = submsg.FindBool(MSG_KEY_RESULT_ADAPTER_INFO_DHCP_ENABLED)
        self.__dict__['haveWins'] = submsg.FindBool(MSG_KEY_RESULT_ADAPTER_INFO_HAVE_WINS)
        self.__dict__['leaseObtained'] = submsg.FindTime(MSG_KEY_RESULT_ADAPTER_INFO_LEASE_OBTAINED)
        self.__dict__['leaseExpires'] = submsg.FindTime(MSG_KEY_RESULT_ADAPTER_INFO_LEASE_EXPIRES)
        self.__dict__['physicalAddress'] = submsg.FindData(MSG_KEY_RESULT_ADAPTER_INFO_PHYSICAL_ADDRESS)
        self.__dict__['physicalAddressLength'] = submsg.FindU8(MSG_KEY_RESULT_ADAPTER_INFO_PHYSICAL_ADDRESS_LENGTH)
        self.__dict__['mtu'] = submsg.FindU32(MSG_KEY_RESULT_ADAPTER_INFO_MTU)
        self.__dict__['arpEnabled'] = submsg.FindBool(MSG_KEY_RESULT_ADAPTER_INFO_ARP_ENABLED)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_ADAPTER_INFO_NAME)
        self.__dict__['description'] = submsg.FindString(MSG_KEY_RESULT_ADAPTER_INFO_DESCRIPTION)
        self.__dict__['dnsSuffix'] = submsg.FindString(MSG_KEY_RESULT_ADAPTER_INFO_DNS_SUFFIX)
        self.__dict__['subnetMask'] = submsg.FindString(MSG_KEY_RESULT_ADAPTER_INFO_SUBNET_MASK)
        self.__dict__['primaryWins'] = submsg.FindIpAddr(MSG_KEY_RESULT_ADAPTER_INFO_PRIMARY_WINS)
        self.__dict__['secondaryWins'] = submsg.FindIpAddr(MSG_KEY_RESULT_ADAPTER_INFO_SECONDAY_WINS)
        self.__dict__['dhcp'] = submsg.FindIpAddr(MSG_KEY_RESULT_ADAPTER_INFO_DHCP)
        self.__dict__['gateway'] = submsg.FindIpAddr(MSG_KEY_RESULT_ADAPTER_INFO_GATEWAY)