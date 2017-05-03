# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *

class StartResult:

    def __init__(self):
        self.__dict__['processId'] = 0

    def __getattr__(self, name):
        if name == 'processId':
            return self.__dict__['processId']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'processId':
            self.__dict__['processId'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_RESULT_START_PROCESS_ID, self.__dict__['processId'])
        mmsg.AddMessage(MSG_KEY_RESULT_START, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_START, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['processId'] = submsg.FindU64(MSG_KEY_RESULT_START_PROCESS_ID)


class OutputResult:

    def __init__(self):
        self.__dict__['processId'] = 0
        self.__dict__['output'] = ''

    def __getattr__(self, name):
        if name == 'processId':
            return self.__dict__['processId']
        if name == 'output':
            return self.__dict__['output']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'processId':
            self.__dict__['processId'] = value
        elif name == 'output':
            self.__dict__['output'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_RESULT_OUTPUT_PROCESS_ID, self.__dict__['processId'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_OUTPUT_OUTPUT, self.__dict__['output'])
        mmsg.AddMessage(MSG_KEY_RESULT_OUTPUT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_OUTPUT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['processId'] = submsg.FindU64(MSG_KEY_RESULT_OUTPUT_PROCESS_ID)
        self.__dict__['output'] = submsg.FindString(MSG_KEY_RESULT_OUTPUT_OUTPUT)


class EndResult:

    def __init__(self):
        self.__dict__['normalExit'] = False
        self.__dict__['exitStatus'] = 0
        self.__dict__['processId'] = 0

    def __getattr__(self, name):
        if name == 'normalExit':
            return self.__dict__['normalExit']
        if name == 'exitStatus':
            return self.__dict__['exitStatus']
        if name == 'processId':
            return self.__dict__['processId']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'normalExit':
            self.__dict__['normalExit'] = value
        elif name == 'exitStatus':
            self.__dict__['exitStatus'] = value
        elif name == 'processId':
            self.__dict__['processId'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddBool(MSG_KEY_RESULT_END_NORMAL_EXIT, self.__dict__['normalExit'])
        submsg.AddU64(MSG_KEY_RESULT_END_EXIT_STATUS, self.__dict__['exitStatus'])
        submsg.AddU64(MSG_KEY_RESULT_END_PROCESS_ID, self.__dict__['processId'])
        mmsg.AddMessage(MSG_KEY_RESULT_END, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_END, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['normalExit'] = submsg.FindBool(MSG_KEY_RESULT_END_NORMAL_EXIT)
        self.__dict__['exitStatus'] = submsg.FindU64(MSG_KEY_RESULT_END_EXIT_STATUS)
        self.__dict__['processId'] = submsg.FindU64(MSG_KEY_RESULT_END_PROCESS_ID)