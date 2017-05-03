# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.IpAddr
import array
RESULT_MAX_PHYSICAL_ADDR_LEN = 32
RESULT_ENTRY_TYPE_NO_TYPE = 0
RESULT_ENTRY_TYPE_OTHER = 1
RESULT_ENTRY_TYPE_INVALID = 2
RESULT_ENTRY_TYPE_DYNAMIC = 3
RESULT_ENTRY_TYPE_STATIC = 4
RESULT_STATE_UNKNOWN = 0
RESULT_STATE_UNREACHABLE = 1
RESULT_STATE_INCOMPLETE = 2
RESULT_STATE_PROBE = 3
RESULT_STATE_DELAY = 4
RESULT_STATE_STALE = 5
RESULT_STATE_REACHABLE = 6
RESULT_STATE_PERMANENT = 7
RESULT_INITIAL_LIST = 0
RESULT_NORMAL_LIST = 1
RESULT_FLAGS_IS_ROUTER = 1
RESULT_FLAGS_IS_UNREACHABLE = 2

class Result:

    def __init__(self):
        self.__dict__['ipAddr'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['physicalAddr'] = array.array('B')
        i = 0
        while i < RESULT_MAX_PHYSICAL_ADDR_LEN:
            self.__dict__['physicalAddr'].append(0)
            i = i + 1

        self.__dict__['physicalAddrLen'] = 0
        self.__dict__['type'] = RESULT_ENTRY_TYPE_NO_TYPE
        self.__dict__['state'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['listType'] = 0
        self.__dict__['moreData'] = False
        self.__dict__['adapter'] = ''

    def __getattr__(self, name):
        if name == 'ipAddr':
            return self.__dict__['ipAddr']
        if name == 'physicalAddr':
            return self.__dict__['physicalAddr']
        if name == 'physicalAddrLen':
            return self.__dict__['physicalAddrLen']
        if name == 'type':
            return self.__dict__['type']
        if name == 'state':
            return self.__dict__['state']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'listType':
            return self.__dict__['listType']
        if name == 'moreData':
            return self.__dict__['moreData']
        if name == 'adapter':
            return self.__dict__['adapter']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'ipAddr':
            self.__dict__['ipAddr'] = value
        elif name == 'physicalAddr':
            self.__dict__['physicalAddr'] = value
        elif name == 'physicalAddrLen':
            self.__dict__['physicalAddrLen'] = value
        elif name == 'type':
            self.__dict__['type'] = value
        elif name == 'state':
            self.__dict__['state'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'listType':
            self.__dict__['listType'] = value
        elif name == 'moreData':
            self.__dict__['moreData'] = value
        elif name == 'adapter':
            self.__dict__['adapter'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddIpAddr(MSG_KEY_RESULT_IP_ADDRESS, self.__dict__['ipAddr'])
        submsg.AddData(MSG_KEY_RESULT_PHYSICAL_ADDRESS, self.__dict__['physicalAddr'])
        submsg.AddU8(MSG_KEY_RESULT_PHYSICAL_ADDRESS_LENGTH, self.__dict__['physicalAddrLen'])
        submsg.AddU8(MSG_KEY_RESULT_TYPE, self.__dict__['type'])
        submsg.AddU8(MSG_KEY_RESULT_STATE, self.__dict__['state'])
        submsg.AddU32(MSG_KEY_RESULT_FLAGS, self.__dict__['flags'])
        submsg.AddU8(MSG_KEY_RESULT_LIST_TYPE, self.__dict__['listType'])
        submsg.AddBool(MSG_KEY_RESULT_MORE_DATA, self.__dict__['moreData'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_ADAPTER, self.__dict__['adapter'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['ipAddr'] = submsg.FindIpAddr(MSG_KEY_RESULT_IP_ADDRESS)
        self.__dict__['physicalAddr'] = submsg.FindData(MSG_KEY_RESULT_PHYSICAL_ADDRESS)
        self.__dict__['physicalAddrLen'] = submsg.FindU8(MSG_KEY_RESULT_PHYSICAL_ADDRESS_LENGTH)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_RESULT_TYPE)
        self.__dict__['state'] = submsg.FindU8(MSG_KEY_RESULT_STATE)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_RESULT_FLAGS)
        self.__dict__['listType'] = submsg.FindU8(MSG_KEY_RESULT_LIST_TYPE)
        self.__dict__['moreData'] = submsg.FindBool(MSG_KEY_RESULT_MORE_DATA)
        self.__dict__['adapter'] = submsg.FindString(MSG_KEY_RESULT_ADAPTER)