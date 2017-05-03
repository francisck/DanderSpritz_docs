# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Value.py
from types import *
import array
VALUE_TYPE_REG_UNKNOWN = 0
VALUE_TYPE_REG_NONE = 1
VALUE_TYPE_REG_SZ = 2
VALUE_TYPE_REG_EXPAND_SZ = 3
VALUE_TYPE_REG_BINARY = 4
VALUE_TYPE_REG_DWORD = 5
VALUE_TYPE_REG_DWORD_BIG_ENDIAN = 6
VALUE_TYPE_REG_LINK = 7
VALUE_TYPE_REG_MULTI_SZ = 8
VALUE_TYPE_REG_RESOURCE_LIST = 9
VALUE_TYPE_REG_FULL_RESOURCE_DESCRIPTOR = 10
VALUE_TYPE_REG_RESOURCE_REQUIREMENTS_LIST = 11
VALUE_TYPE_REG_QWORD = 12

class Value:

    def __init__(self):
        self.__dict__['type'] = 0
        self.__dict__['nativeType'] = 0
        self.__dict__['name'] = ''
        self.__dict__['data'] = array.array('B')

    def __getattr__(self, name):
        if name == 'type':
            return self.__dict__['type']
        if name == 'nativeType':
            return self.__dict__['nativeType']
        if name == 'name':
            return self.__dict__['name']
        if name == 'data':
            return self.__dict__['data']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'type':
            self.__dict__['type'] = value
        elif name == 'nativeType':
            self.__dict__['nativeType'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        elif name == 'data':
            self.__dict__['data'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_VALUE_TYPE, self.__dict__['type'])
        submsg.AddU32(MSG_KEY_RESULT_VALUE_NATIVE_TYPE, self.__dict__['nativeType'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_VALUE_NAME, self.__dict__['name'])
        submsg.AddData(MSG_KEY_RESULT_VALUE_DATA, self.__dict__['data'])
        mmsg.AddMessage(MSG_KEY_RESULT_VALUE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_VALUE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_RESULT_VALUE_TYPE)
        self.__dict__['nativeType'] = submsg.FindU32(MSG_KEY_RESULT_VALUE_NATIVE_TYPE)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_VALUE_NAME)
        self.__dict__['data'] = submsg.FindData(MSG_KEY_RESULT_VALUE_DATA)