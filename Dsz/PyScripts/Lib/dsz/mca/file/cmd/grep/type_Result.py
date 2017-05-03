# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *

class ResultFileInfo:

    def __init__(self):
        self.__dict__['openStatus'] = 0
        self.__dict__['file'] = ''

    def __getattr__(self, name):
        if name == 'openStatus':
            return self.__dict__['openStatus']
        if name == 'file':
            return self.__dict__['file']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'openStatus':
            self.__dict__['openStatus'] = value
        elif name == 'file':
            self.__dict__['file'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_FILE_INFO_OPEN_STATUS, self.__dict__['openStatus'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_FILE_INFO_FILE, self.__dict__['file'])
        mmsg.AddMessage(MSG_KEY_RESULT_FILE_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_FILE_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['openStatus'] = submsg.FindU32(MSG_KEY_RESULT_FILE_INFO_OPEN_STATUS)
        self.__dict__['file'] = submsg.FindString(MSG_KEY_RESULT_FILE_INFO_FILE)


class ResultLine:

    def __init__(self):
        self.__dict__['position'] = 0
        self.__dict__['line'] = ''

    def __getattr__(self, name):
        if name == 'position':
            return self.__dict__['position']
        if name == 'line':
            return self.__dict__['line']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'position':
            self.__dict__['position'] = value
        elif name == 'line':
            self.__dict__['line'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_RESULT_LINE_POSITION, self.__dict__['position'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_LINE_LINE, self.__dict__['line'])
        mmsg.AddMessage(MSG_KEY_RESULT_LINE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_LINE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['position'] = submsg.FindU64(MSG_KEY_RESULT_LINE_POSITION)
        self.__dict__['line'] = submsg.FindString(MSG_KEY_RESULT_LINE_LINE)