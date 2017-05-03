# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
import mcl.object.IpAddr
PARAMS_TYPE_QUERY = 0
PARAMS_TYPE_REVERSE_QUERY = 1
PARAMS_TYPE_ZONE_TRANSFER = 2
PARAMS_TYPE_CACHE_QUERY = 3
PARAMS_TYPE_CACHE_FLUSH = 4
PARAMS_PROTOCOL_DEFAULT = 0
PARAMS_PROTOCOL_DNS_QUERY_A = 1
PARAMS_PROTOCOL_DNS_QUERY_AAAA = 2

class Params:

    def __init__(self):
        self.__dict__['type'] = 0
        self.__dict__['dnsServer'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['queryInfo'] = ''
        self.__dict__['protocol'] = PARAMS_PROTOCOL_DEFAULT

    def __getattr__(self, name):
        if name == 'type':
            return self.__dict__['type']
        if name == 'dnsServer':
            return self.__dict__['dnsServer']
        if name == 'queryInfo':
            return self.__dict__['queryInfo']
        if name == 'protocol':
            return self.__dict__['protocol']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'type':
            self.__dict__['type'] = value
        elif name == 'dnsServer':
            self.__dict__['dnsServer'] = value
        elif name == 'queryInfo':
            self.__dict__['queryInfo'] = value
        elif name == 'protocol':
            self.__dict__['protocol'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_TYPE, self.__dict__['type'])
        submsg.AddIpAddr(MSG_KEY_PARAMS_DNS_SERVER, self.__dict__['dnsServer'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_QUERY_INFO, self.__dict__['queryInfo'])
        submsg.AddU8(MSG_KEY_PARAMS_PROTOCOL, self.__dict__['protocol'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_PARAMS_TYPE)
        self.__dict__['dnsServer'] = submsg.FindIpAddr(MSG_KEY_PARAMS_DNS_SERVER)
        self.__dict__['queryInfo'] = submsg.FindString(MSG_KEY_PARAMS_QUERY_INFO)
        try:
            self.__dict__['protocol'] = submsg.FindU8(MSG_KEY_PARAMS_PROTOCOL)
        except:
            pass