# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *

class Result:

    def __init__(self):
        self.__dict__['physicalTotal'] = 0
        self.__dict__['physicalAvail'] = 0
        self.__dict__['pageTotal'] = 0
        self.__dict__['pageAvail'] = 0
        self.__dict__['virtualTotal'] = 0
        self.__dict__['virtualAvail'] = 0

    def __getattr__(self, name):
        if name == 'physicalTotal':
            return self.__dict__['physicalTotal']
        if name == 'physicalAvail':
            return self.__dict__['physicalAvail']
        if name == 'pageTotal':
            return self.__dict__['pageTotal']
        if name == 'pageAvail':
            return self.__dict__['pageAvail']
        if name == 'virtualTotal':
            return self.__dict__['virtualTotal']
        if name == 'virtualAvail':
            return self.__dict__['virtualAvail']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'physicalTotal':
            self.__dict__['physicalTotal'] = value
        elif name == 'physicalAvail':
            self.__dict__['physicalAvail'] = value
        elif name == 'pageTotal':
            self.__dict__['pageTotal'] = value
        elif name == 'pageAvail':
            self.__dict__['pageAvail'] = value
        elif name == 'virtualTotal':
            self.__dict__['virtualTotal'] = value
        elif name == 'virtualAvail':
            self.__dict__['virtualAvail'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_RESULT_PHYSICAL_TOTAL, self.__dict__['physicalTotal'])
        submsg.AddU64(MSG_KEY_RESULT_PHYSICAL_AVAILABLE, self.__dict__['physicalAvail'])
        submsg.AddU64(MSG_KEY_RESULT_PAGE_TOTAL, self.__dict__['pageTotal'])
        submsg.AddU64(MSG_KEY_RESULT_PAGE_AVAILABLE, self.__dict__['pageAvail'])
        submsg.AddU64(MSG_KEY_RESULT_VIRTUAL_TOTAL, self.__dict__['virtualTotal'])
        submsg.AddU64(MSG_KEY_RESULT_VIRTUAL_AVAILABLE, self.__dict__['virtualAvail'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['physicalTotal'] = submsg.FindU64(MSG_KEY_RESULT_PHYSICAL_TOTAL)
        self.__dict__['physicalAvail'] = submsg.FindU64(MSG_KEY_RESULT_PHYSICAL_AVAILABLE)
        self.__dict__['pageTotal'] = submsg.FindU64(MSG_KEY_RESULT_PAGE_TOTAL)
        self.__dict__['pageAvail'] = submsg.FindU64(MSG_KEY_RESULT_PAGE_AVAILABLE)
        self.__dict__['virtualTotal'] = submsg.FindU64(MSG_KEY_RESULT_VIRTUAL_TOTAL)
        self.__dict__['virtualAvail'] = submsg.FindU64(MSG_KEY_RESULT_VIRTUAL_AVAILABLE)