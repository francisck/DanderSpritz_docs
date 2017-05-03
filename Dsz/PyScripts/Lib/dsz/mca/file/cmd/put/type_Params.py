# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
import array
PARAMS_CREATE_FLAG_PERMANENT = 1

class CreateParams:

    def __init__(self):
        self.__dict__['flags'] = 0
        self.__dict__['writeOffset'] = 0
        self.__dict__['filePath'] = ''
        self.__dict__['provider'] = 0

    def __getattr__(self, name):
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'writeOffset':
            return self.__dict__['writeOffset']
        if name == 'filePath':
            return self.__dict__['filePath']
        if name == 'provider':
            return self.__dict__['provider']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'writeOffset':
            self.__dict__['writeOffset'] = value
        elif name == 'filePath':
            self.__dict__['filePath'] = value
        elif name == 'provider':
            self.__dict__['provider'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU16(MSG_KEY_PARAMS_CREATE_FLAGS, self.__dict__['flags'])
        submsg.AddU64(MSG_KEY_PARAMS_CREATE_WRITE_OFFSET, self.__dict__['writeOffset'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_CREATE_FILE_PATH, self.__dict__['filePath'])
        submsg.AddU32(MSG_KEY_PARAMS_CREATE_PROVIDER, self.__dict__['provider'])
        mmsg.AddMessage(MSG_KEY_PARAMS_CREATE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_CREATE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['flags'] = submsg.FindU16(MSG_KEY_PARAMS_CREATE_FLAGS)
        try:
            self.__dict__['writeOffset'] = submsg.FindU64(MSG_KEY_PARAMS_CREATE_WRITE_OFFSET)
        except:
            pass

        self.__dict__['filePath'] = submsg.FindString(MSG_KEY_PARAMS_CREATE_FILE_PATH)
        try:
            self.__dict__['provider'] = submsg.FindU32(MSG_KEY_PARAMS_CREATE_PROVIDER)
        except:
            pass


class WriteParams:

    def __init__(self):
        self.__dict__['lastData'] = False
        self.__dict__['chunkIndex'] = 0
        self.__dict__['data'] = array.array('B')

    def __getattr__(self, name):
        if name == 'lastData':
            return self.__dict__['lastData']
        if name == 'chunkIndex':
            return self.__dict__['chunkIndex']
        if name == 'data':
            return self.__dict__['data']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'lastData':
            self.__dict__['lastData'] = value
        elif name == 'chunkIndex':
            self.__dict__['chunkIndex'] = value
        elif name == 'data':
            self.__dict__['data'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddBool(MSG_KEY_PARAMS_WRITE_LAST_DATA, self.__dict__['lastData'])
        submsg.AddU32(MSG_KEY_PARAMS_WRITE_CHUNK_INDEX, self.__dict__['chunkIndex'])
        submsg.AddData(MSG_KEY_PARAMS_WRITE_DATA, self.__dict__['data'])
        mmsg.AddMessage(MSG_KEY_PARAMS_WRITE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_WRITE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['lastData'] = submsg.FindBool(MSG_KEY_PARAMS_WRITE_LAST_DATA)
        self.__dict__['chunkIndex'] = submsg.FindU32(MSG_KEY_PARAMS_WRITE_CHUNK_INDEX)
        self.__dict__['data'] = submsg.FindData(MSG_KEY_PARAMS_WRITE_DATA)