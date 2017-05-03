# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *

class ResultHandle:

    def __init__(self):
        self.__dict__['processId'] = 0
        self.__dict__['handle'] = 0
        self.__dict__['rights'] = 0
        self.__dict__['type'] = ''
        self.__dict__['metadata'] = ''

    def __getattr__(self, name):
        if name == 'processId':
            return self.__dict__['processId']
        if name == 'handle':
            return self.__dict__['handle']
        if name == 'rights':
            return self.__dict__['rights']
        if name == 'type':
            return self.__dict__['type']
        if name == 'metadata':
            return self.__dict__['metadata']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'processId':
            self.__dict__['processId'] = value
        elif name == 'handle':
            self.__dict__['handle'] = value
        elif name == 'rights':
            self.__dict__['rights'] = value
        elif name == 'type':
            self.__dict__['type'] = value
        elif name == 'metadata':
            self.__dict__['metadata'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_HANDLE_PROCESS_ID, self.__dict__['processId'])
        submsg.AddU64(MSG_KEY_RESULT_HANDLE_HANDLE, self.__dict__['handle'])
        submsg.AddU32(MSG_KEY_RESULT_HANDLE_RIGHTS, self.__dict__['rights'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_HANDLE_TYPE, self.__dict__['type'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_HANDLE_METADATA, self.__dict__['metadata'])
        mmsg.AddMessage(MSG_KEY_RESULT_HANDLE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_HANDLE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['processId'] = submsg.FindU32(MSG_KEY_RESULT_HANDLE_PROCESS_ID)
        self.__dict__['handle'] = submsg.FindU64(MSG_KEY_RESULT_HANDLE_HANDLE)
        self.__dict__['rights'] = submsg.FindU32(MSG_KEY_RESULT_HANDLE_RIGHTS)
        self.__dict__['type'] = submsg.FindString(MSG_KEY_RESULT_HANDLE_TYPE)
        self.__dict__['metadata'] = submsg.FindString(MSG_KEY_RESULT_HANDLE_METADATA)


class ResultDuplicate:

    def __init__(self):
        self.__dict__['origProcessId'] = 0
        self.__dict__['origHandle'] = 0
        self.__dict__['newProcessId'] = 0
        self.__dict__['newHandle'] = 0

    def __getattr__(self, name):
        if name == 'origProcessId':
            return self.__dict__['origProcessId']
        if name == 'origHandle':
            return self.__dict__['origHandle']
        if name == 'newProcessId':
            return self.__dict__['newProcessId']
        if name == 'newHandle':
            return self.__dict__['newHandle']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'origProcessId':
            self.__dict__['origProcessId'] = value
        elif name == 'origHandle':
            self.__dict__['origHandle'] = value
        elif name == 'newProcessId':
            self.__dict__['newProcessId'] = value
        elif name == 'newHandle':
            self.__dict__['newHandle'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_DUPLICATE_ORIG_PROCESS_ID, self.__dict__['origProcessId'])
        submsg.AddU64(MSG_KEY_RESULT_DUPLICATE_ORIG_HANDLE, self.__dict__['origHandle'])
        submsg.AddU32(MSG_KEY_RESULT_DUPLICATE_NEW_PROCESS_ID, self.__dict__['newProcessId'])
        submsg.AddU64(MSG_KEY_RESULT_DUPLICATE_NEW_HANDLE, self.__dict__['newHandle'])
        mmsg.AddMessage(MSG_KEY_RESULT_DUPLICATE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_DUPLICATE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['origProcessId'] = submsg.FindU32(MSG_KEY_RESULT_DUPLICATE_ORIG_PROCESS_ID)
        self.__dict__['origHandle'] = submsg.FindU64(MSG_KEY_RESULT_DUPLICATE_ORIG_HANDLE)
        self.__dict__['newProcessId'] = submsg.FindU32(MSG_KEY_RESULT_DUPLICATE_NEW_PROCESS_ID)
        self.__dict__['newHandle'] = submsg.FindU64(MSG_KEY_RESULT_DUPLICATE_NEW_HANDLE)


class ResultClose:

    def __init__(self):
        self.__dict__['processId'] = 0
        self.__dict__['handleValue'] = 0

    def __getattr__(self, name):
        if name == 'processId':
            return self.__dict__['processId']
        if name == 'handleValue':
            return self.__dict__['handleValue']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'processId':
            self.__dict__['processId'] = value
        elif name == 'handleValue':
            self.__dict__['handleValue'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_CLOSE_PROCESS_ID, self.__dict__['processId'])
        submsg.AddU64(MSG_KEY_RESULT_CLOSE_HANDLE, self.__dict__['handleValue'])
        mmsg.AddMessage(MSG_KEY_RESULT_CLOSE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_CLOSE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['processId'] = submsg.FindU32(MSG_KEY_RESULT_CLOSE_PROCESS_ID)
        self.__dict__['handleValue'] = submsg.FindU64(MSG_KEY_RESULT_CLOSE_HANDLE)