# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.MclTime
RESULT_STATE_INITIAL = 1
RESULT_STATE_STARTED = 2
RESULT_STATE_STOPPED = 3
RESULT_STATE_LIST = 4
RESULT_PROCESS_FLAG_64_BIT = 1
RESULT_PROCESS_FLAG_32_BIT = 2

class Result:

    def __init__(self):
        self.__dict__['state'] = 0
        self.__dict__['processId'] = 0
        self.__dict__['parentProcessId'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['createTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['processorTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['user'] = ''
        self.__dict__['displayLocation'] = ''
        self.__dict__['name'] = ''
        self.__dict__['executablePath'] = ''
        self.__dict__['description'] = ''

    def __getattr__(self, name):
        if name == 'state':
            return self.__dict__['state']
        if name == 'processId':
            return self.__dict__['processId']
        if name == 'parentProcessId':
            return self.__dict__['parentProcessId']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'createTime':
            return self.__dict__['createTime']
        if name == 'processorTime':
            return self.__dict__['processorTime']
        if name == 'user':
            return self.__dict__['user']
        if name == 'displayLocation':
            return self.__dict__['displayLocation']
        if name == 'name':
            return self.__dict__['name']
        if name == 'executablePath':
            return self.__dict__['executablePath']
        if name == 'description':
            return self.__dict__['description']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'state':
            self.__dict__['state'] = value
        elif name == 'processId':
            self.__dict__['processId'] = value
        elif name == 'parentProcessId':
            self.__dict__['parentProcessId'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'createTime':
            self.__dict__['createTime'] = value
        elif name == 'processorTime':
            self.__dict__['processorTime'] = value
        elif name == 'user':
            self.__dict__['user'] = value
        elif name == 'displayLocation':
            self.__dict__['displayLocation'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        elif name == 'executablePath':
            self.__dict__['executablePath'] = value
        elif name == 'description':
            self.__dict__['description'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_STATE, self.__dict__['state'])
        submsg.AddU32(MSG_KEY_RESULT_PROCESS_ID, self.__dict__['processId'])
        submsg.AddU32(MSG_KEY_RESULT_PARENT_PROCESS_ID, self.__dict__['parentProcessId'])
        submsg.AddU32(MSG_KEY_RESULT_FLAGS, self.__dict__['flags'])
        submsg.AddTime(MSG_KEY_RESULT_CREATE_TIME, self.__dict__['createTime'])
        submsg.AddTime(MSG_KEY_RESULT_PROCESSOR_TIME, self.__dict__['processorTime'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_USER, self.__dict__['user'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DISPLAY_LOCATION, self.__dict__['displayLocation'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_NAME, self.__dict__['name'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_EXECUTABLE_PATH, self.__dict__['executablePath'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DESCRIPTION, self.__dict__['description'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['state'] = submsg.FindU8(MSG_KEY_RESULT_STATE)
        self.__dict__['processId'] = submsg.FindU32(MSG_KEY_RESULT_PROCESS_ID)
        self.__dict__['parentProcessId'] = submsg.FindU32(MSG_KEY_RESULT_PARENT_PROCESS_ID)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_RESULT_FLAGS)
        self.__dict__['createTime'] = submsg.FindTime(MSG_KEY_RESULT_CREATE_TIME)
        self.__dict__['processorTime'] = submsg.FindTime(MSG_KEY_RESULT_PROCESSOR_TIME)
        self.__dict__['user'] = submsg.FindString(MSG_KEY_RESULT_USER)
        self.__dict__['displayLocation'] = submsg.FindString(MSG_KEY_RESULT_DISPLAY_LOCATION)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_NAME)
        self.__dict__['executablePath'] = submsg.FindString(MSG_KEY_RESULT_EXECUTABLE_PATH)
        self.__dict__['description'] = submsg.FindString(MSG_KEY_RESULT_DESCRIPTION)