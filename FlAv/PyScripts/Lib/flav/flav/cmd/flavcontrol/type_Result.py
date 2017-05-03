# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *

class AvailableResult:

    def __init__(self):
        self.__dict__['available'] = False

    def __getattr__(self, name):
        if name == 'available':
            return self.__dict__['available']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'available':
            self.__dict__['available'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddBool(MSG_KEY_RESULT_AVAILABLE_AVAILABLE, self.__dict__['available'])
        mmsg.AddMessage(MSG_KEY_RESULT_AVAILABLE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_AVAILABLE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['available'] = submsg.FindBool(MSG_KEY_RESULT_AVAILABLE_AVAILABLE)


class StatusResult:

    def __init__(self):
        self.__dict__['major'] = 0
        self.__dict__['minor'] = 0
        self.__dict__['fix'] = 0
        self.__dict__['build'] = 0
        self.__dict__['available'] = False

    def __getattr__(self, name):
        if name == 'major':
            return self.__dict__['major']
        if name == 'minor':
            return self.__dict__['minor']
        if name == 'fix':
            return self.__dict__['fix']
        if name == 'build':
            return self.__dict__['build']
        if name == 'available':
            return self.__dict__['available']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'major':
            self.__dict__['major'] = value
        elif name == 'minor':
            self.__dict__['minor'] = value
        elif name == 'fix':
            self.__dict__['fix'] = value
        elif name == 'build':
            self.__dict__['build'] = value
        elif name == 'available':
            self.__dict__['available'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_STATUS_MAJOR, self.__dict__['major'])
        submsg.AddU32(MSG_KEY_RESULT_STATUS_MINOR, self.__dict__['minor'])
        submsg.AddU32(MSG_KEY_RESULT_STATUS_FIX, self.__dict__['fix'])
        submsg.AddU32(MSG_KEY_RESULT_STATUS_BUILD, self.__dict__['build'])
        submsg.AddBool(MSG_KEY_RESULT_STATUS_AVAILABLE, self.__dict__['available'])
        mmsg.AddMessage(MSG_KEY_RESULT_STATUS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_STATUS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['major'] = submsg.FindU32(MSG_KEY_RESULT_STATUS_MAJOR)
        self.__dict__['minor'] = submsg.FindU32(MSG_KEY_RESULT_STATUS_MINOR)
        self.__dict__['fix'] = submsg.FindU32(MSG_KEY_RESULT_STATUS_FIX)
        self.__dict__['build'] = submsg.FindU32(MSG_KEY_RESULT_STATUS_BUILD)
        self.__dict__['available'] = submsg.FindBool(MSG_KEY_RESULT_STATUS_AVAILABLE)


class StringResult:

    def __init__(self):
        self.__dict__['str'] = ''

    def __getattr__(self, name):
        if name == 'str':
            return self.__dict__['str']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'str':
            self.__dict__['str'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_STRING_VALUE, self.__dict__['str'])
        mmsg.AddMessage(MSG_KEY_RESULT_STRING, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_STRING, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['str'] = submsg.FindString(MSG_KEY_RESULT_STRING_VALUE)