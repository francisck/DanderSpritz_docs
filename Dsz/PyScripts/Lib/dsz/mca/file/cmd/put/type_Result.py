# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *

class Result:

    def __init__(self):
        self.__dict__['bytesWritten'] = 0
        self.__dict__['filePath'] = ''

    def __getattr__(self, name):
        if name == 'bytesWritten':
            return self.__dict__['bytesWritten']
        if name == 'filePath':
            return self.__dict__['filePath']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'bytesWritten':
            self.__dict__['bytesWritten'] = value
        elif name == 'filePath':
            self.__dict__['filePath'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_RESULT_BYTES_WRITTEN, self.__dict__['bytesWritten'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_RESULT_FILE_PATH, self.__dict__['filePath'])
        mmsg.AddMessage(MSG_KEY_PARAMS_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['bytesWritten'] = submsg.FindU32(MSG_KEY_PARAMS_RESULT_BYTES_WRITTEN)
        self.__dict__['filePath'] = submsg.FindString(MSG_KEY_PARAMS_RESULT_FILE_PATH)