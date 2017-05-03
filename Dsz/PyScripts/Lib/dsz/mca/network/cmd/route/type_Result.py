# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.IpAddr
RESULT_FLAG_LOOPBACK = 1
RESULT_FLAG_AUTOCONFIG = 2
RESULT_FLAG_PERMANENT = 4
RESULT_FLAG_PUBLISH = 8
RESULT_ORIGIN_UNKNOWN = 0
RESULT_ORIGIN_MANUAL = 1
RESULT_ORIGIN_WELLKNOWN = 2
RESULT_ORIGIN_DHCP = 3
RESULT_ORIGIN_ROUTER_AD = 4
RESULT_ORIGIN_6_TO_4 = 5

class Result:

    def __init__(self):
        self.__dict__['dest'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['netmask'] = 0
        self.__dict__['gateway'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['metric'] = 0
        self.__dict__['iface'] = ''
        self.__dict__['flags'] = 0
        self.__dict__['origin'] = RESULT_ORIGIN_UNKNOWN

    def __getattr__(self, name):
        if name == 'dest':
            return self.__dict__['dest']
        if name == 'netmask':
            return self.__dict__['netmask']
        if name == 'gateway':
            return self.__dict__['gateway']
        if name == 'metric':
            return self.__dict__['metric']
        if name == 'iface':
            return self.__dict__['iface']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'origin':
            return self.__dict__['origin']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'dest':
            self.__dict__['dest'] = value
        elif name == 'netmask':
            self.__dict__['netmask'] = value
        elif name == 'gateway':
            self.__dict__['gateway'] = value
        elif name == 'metric':
            self.__dict__['metric'] = value
        elif name == 'iface':
            self.__dict__['iface'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'origin':
            self.__dict__['origin'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddIpAddr(MSG_KEY_RESULT_DESTINATION, self.__dict__['dest'])
        submsg.AddU32(MSG_KEY_RESULT_NETMASK, self.__dict__['netmask'])
        submsg.AddIpAddr(MSG_KEY_RESULT_GATEWAY, self.__dict__['gateway'])
        submsg.AddU32(MSG_KEY_RESULT_METRIC, self.__dict__['metric'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_INTERFACE, self.__dict__['iface'])
        submsg.AddU32(MSG_KEY_RESULT_FLAGS, self.__dict__['flags'])
        submsg.AddU8(MSG_KEY_RESULT_ORIGIN, self.__dict__['origin'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['dest'] = submsg.FindIpAddr(MSG_KEY_RESULT_DESTINATION)
        self.__dict__['netmask'] = submsg.FindU32(MSG_KEY_RESULT_NETMASK)
        self.__dict__['gateway'] = submsg.FindIpAddr(MSG_KEY_RESULT_GATEWAY)
        self.__dict__['metric'] = submsg.FindU32(MSG_KEY_RESULT_METRIC)
        self.__dict__['iface'] = submsg.FindString(MSG_KEY_RESULT_INTERFACE)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_RESULT_FLAGS)
        self.__dict__['origin'] = submsg.FindU8(MSG_KEY_RESULT_ORIGIN)