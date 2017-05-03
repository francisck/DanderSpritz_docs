# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *

class ResultHeader:

    def __init__(self):
        self.__dict__['perfCount'] = 0
        self.__dict__['perfCountsPerSecond'] = 0
        self.__dict__['perfTime100nSec'] = 0
        self.__dict__['sysName'] = ''

    def __getattr__(self, name):
        if name == 'perfCount':
            return self.__dict__['perfCount']
        if name == 'perfCountsPerSecond':
            return self.__dict__['perfCountsPerSecond']
        if name == 'perfTime100nSec':
            return self.__dict__['perfTime100nSec']
        if name == 'sysName':
            return self.__dict__['sysName']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'perfCount':
            self.__dict__['perfCount'] = value
        elif name == 'perfCountsPerSecond':
            self.__dict__['perfCountsPerSecond'] = value
        elif name == 'perfTime100nSec':
            self.__dict__['perfTime100nSec'] = value
        elif name == 'sysName':
            self.__dict__['sysName'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_RESULT_HEADER_PERF_COUNT, self.__dict__['perfCount'])
        submsg.AddU64(MSG_KEY_RESULT_HEADER_PERF_COUNTS_PER_SECOND, self.__dict__['perfCountsPerSecond'])
        submsg.AddU64(MSG_KEY_RESULT_HEADER_PERF_TIME_100NANOSECONDS, self.__dict__['perfTime100nSec'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_HEADER_SYSTEM_NAME, self.__dict__['sysName'])
        mmsg.AddMessage(MSG_KEY_RESULT_HEADER, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_HEADER, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['perfCount'] = submsg.FindU64(MSG_KEY_RESULT_HEADER_PERF_COUNT)
        self.__dict__['perfCountsPerSecond'] = submsg.FindU64(MSG_KEY_RESULT_HEADER_PERF_COUNTS_PER_SECOND)
        self.__dict__['perfTime100nSec'] = submsg.FindU64(MSG_KEY_RESULT_HEADER_PERF_TIME_100NANOSECONDS)
        self.__dict__['sysName'] = submsg.FindString(MSG_KEY_RESULT_HEADER_SYSTEM_NAME)


class ResultObjectHeader:

    def __init__(self):
        self.__dict__['helpTitleIndex'] = 0
        self.__dict__['nameTitleIndex'] = 0

    def __getattr__(self, name):
        if name == 'helpTitleIndex':
            return self.__dict__['helpTitleIndex']
        if name == 'nameTitleIndex':
            return self.__dict__['nameTitleIndex']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'helpTitleIndex':
            self.__dict__['helpTitleIndex'] = value
        elif name == 'nameTitleIndex':
            self.__dict__['nameTitleIndex'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_OBJECT_HEADER_HELP_TITLE_INDEX, self.__dict__['helpTitleIndex'])
        submsg.AddU32(MSG_KEY_RESULT_OBJECT_HEADER_NAME_TITLE_INDEX, self.__dict__['nameTitleIndex'])
        mmsg.AddMessage(MSG_KEY_RESULT_OBJECT_HEADER, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_OBJECT_HEADER, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['helpTitleIndex'] = submsg.FindU32(MSG_KEY_RESULT_OBJECT_HEADER_HELP_TITLE_INDEX)
        self.__dict__['nameTitleIndex'] = submsg.FindU32(MSG_KEY_RESULT_OBJECT_HEADER_NAME_TITLE_INDEX)


class ResultInstance:

    def __init__(self):
        self.__dict__['id'] = 0
        self.__dict__['parent'] = 0
        self.__dict__['name'] = ''

    def __getattr__(self, name):
        if name == 'id':
            return self.__dict__['id']
        if name == 'parent':
            return self.__dict__['parent']
        if name == 'name':
            return self.__dict__['name']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'id':
            self.__dict__['id'] = value
        elif name == 'parent':
            self.__dict__['parent'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_INSTANCE_ID, self.__dict__['id'])
        submsg.AddU32(MSG_KEY_RESULT_INSTANCE_PARENT, self.__dict__['parent'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_INSTANCE_NAME, self.__dict__['name'])
        mmsg.AddMessage(MSG_KEY_RESULT_INSTANCE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_INSTANCE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['id'] = submsg.FindU32(MSG_KEY_RESULT_INSTANCE_ID)
        self.__dict__['parent'] = submsg.FindU32(MSG_KEY_RESULT_INSTANCE_PARENT)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_INSTANCE_NAME)


class ResultCount:

    def __init__(self):
        self.__dict__['type'] = 0
        self.__dict__['nameIndex'] = 0
        self.__dict__['helpIndex'] = 0
        self.__dict__['value'] = 0
        self.__dict__['valueStr'] = ''

    def __getattr__(self, name):
        if name == 'type':
            return self.__dict__['type']
        if name == 'nameIndex':
            return self.__dict__['nameIndex']
        if name == 'helpIndex':
            return self.__dict__['helpIndex']
        if name == 'value':
            return self.__dict__['value']
        if name == 'valueStr':
            return self.__dict__['valueStr']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'type':
            self.__dict__['type'] = value
        elif name == 'nameIndex':
            self.__dict__['nameIndex'] = value
        elif name == 'helpIndex':
            self.__dict__['helpIndex'] = value
        elif name == 'value':
            self.__dict__['value'] = value
        elif name == 'valueStr':
            self.__dict__['valueStr'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_COUNT_TYPE, self.__dict__['type'])
        submsg.AddU32(MSG_KEY_RESULT_COUNT_NAME_INDEX, self.__dict__['nameIndex'])
        submsg.AddU32(MSG_KEY_RESULT_COUNT_HELP_INDEX, self.__dict__['helpIndex'])
        submsg.AddU64(MSG_KEY_RESULT_COUNT_VALUE, self.__dict__['value'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_COUNT_VALUE_STRING, self.__dict__['valueStr'])
        mmsg.AddMessage(MSG_KEY_RESULT_COUNT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_COUNT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['type'] = submsg.FindU32(MSG_KEY_RESULT_COUNT_TYPE)
        self.__dict__['nameIndex'] = submsg.FindU32(MSG_KEY_RESULT_COUNT_NAME_INDEX)
        self.__dict__['helpIndex'] = submsg.FindU32(MSG_KEY_RESULT_COUNT_HELP_INDEX)
        self.__dict__['value'] = submsg.FindU64(MSG_KEY_RESULT_COUNT_VALUE)
        self.__dict__['valueStr'] = submsg.FindString(MSG_KEY_RESULT_COUNT_VALUE_STRING)


class ResultString:

    def __init__(self):
        self.__dict__['id'] = 0
        self.__dict__['str'] = ''

    def __getattr__(self, name):
        if name == 'id':
            return self.__dict__['id']
        if name == 'str':
            return self.__dict__['str']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'id':
            self.__dict__['id'] = value
        elif name == 'str':
            self.__dict__['str'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_STRING_ID, self.__dict__['id'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_STRING_STRING, self.__dict__['str'])
        mmsg.AddMessage(MSG_KEY_RESULT_STRING, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_STRING, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['id'] = submsg.FindU32(MSG_KEY_RESULT_STRING_ID)
        self.__dict__['str'] = submsg.FindString(MSG_KEY_RESULT_STRING_STRING)