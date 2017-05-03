# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Item.py
from types import *
RESULT_TYPE_BOOL = 1
RESULT_TYPE_STR = 2
RESULT_TYPE_INT = 3
RESULT_TYPE_TIME = 4
RESULT_TYPE_HEX = 5
RESULT_TYPE_LARGEINT = 6
RESULT_TYPE_UNKNOWN = 7
RESULT_TYPE_EXCEPTION = 8

class Result:

    def __init__(self):
        self.__dict__['numAttributes'] = 0
        self.__dict__['attrType'] = ''
        self.__dict__['osDataType'] = 0
        self.__dict__['dataType'] = 0

    def __getattr__(self, name):
        if name == 'numAttributes':
            return self.__dict__['numAttributes']
        if name == 'attrType':
            return self.__dict__['attrType']
        if name == 'osDataType':
            return self.__dict__['osDataType']
        if name == 'dataType':
            return self.__dict__['dataType']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'numAttributes':
            self.__dict__['numAttributes'] = value
        elif name == 'attrType':
            self.__dict__['attrType'] = value
        elif name == 'osDataType':
            self.__dict__['osDataType'] = value
        elif name == 'dataType':
            self.__dict__['dataType'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddS32(MSG_KEY_RESULT_INFO_NUM_ATTRIBUTES, self.__dict__['numAttributes'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_INFO_ATTRIBUTE_TYPE, self.__dict__['attrType'])
        submsg.AddU32(MSG_KEY_RESULT_INFO_OS_DATA_TYPE, self.__dict__['osDataType'])
        submsg.AddU32(MSG_KEY_RESULT_INFO_DATA_TYPE, self.__dict__['dataType'])
        mmsg.AddMessage(MSG_KEY_RESULT_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['numAttributes'] = submsg.FindS32(MSG_KEY_RESULT_INFO_NUM_ATTRIBUTES)
        self.__dict__['attrType'] = submsg.FindString(MSG_KEY_RESULT_INFO_ATTRIBUTE_TYPE)
        self.__dict__['osDataType'] = submsg.FindU32(MSG_KEY_RESULT_INFO_OS_DATA_TYPE)
        self.__dict__['dataType'] = submsg.FindU32(MSG_KEY_RESULT_INFO_DATA_TYPE)