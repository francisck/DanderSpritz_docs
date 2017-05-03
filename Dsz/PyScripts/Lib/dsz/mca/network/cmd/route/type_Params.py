# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *

class Params:

    def __init__(self):
        self.__dict__['dest'] = ''
        self.__dict__['netmask'] = ''
        self.__dict__['gateway'] = ''
        self.__dict__['iface'] = ''
        self.__dict__['metric'] = 0

    def __getattr__(self, name):
        if name == 'dest':
            return self.__dict__['dest']
        if name == 'netmask':
            return self.__dict__['netmask']
        if name == 'gateway':
            return self.__dict__['gateway']
        if name == 'iface':
            return self.__dict__['iface']
        if name == 'metric':
            return self.__dict__['metric']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'dest':
            self.__dict__['dest'] = value
        elif name == 'netmask':
            self.__dict__['netmask'] = value
        elif name == 'gateway':
            self.__dict__['gateway'] = value
        elif name == 'iface':
            self.__dict__['iface'] = value
        elif name == 'metric':
            self.__dict__['metric'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_PARAMS_DESTINATION, self.__dict__['dest'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_NETMASK, self.__dict__['netmask'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_GATEWAY, self.__dict__['gateway'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_INTERFACE, self.__dict__['iface'])
        submsg.AddU32(MSG_KEY_PARAMS_METRIC, self.__dict__['metric'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['dest'] = submsg.FindString(MSG_KEY_PARAMS_DESTINATION)
        self.__dict__['netmask'] = submsg.FindString(MSG_KEY_PARAMS_NETMASK)
        self.__dict__['gateway'] = submsg.FindString(MSG_KEY_PARAMS_GATEWAY)
        self.__dict__['iface'] = submsg.FindString(MSG_KEY_PARAMS_INTERFACE)
        self.__dict__['metric'] = submsg.FindU32(MSG_KEY_PARAMS_METRIC)