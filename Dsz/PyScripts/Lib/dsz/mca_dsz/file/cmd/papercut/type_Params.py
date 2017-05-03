# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
import mcl.object.MclTime
PARAMS_FLAG_ELEVATE = 1
PARAMS_TAIL_OFFSET = -1
PARAMS_DATE_TYPE_NONE = 0
PARAMS_DATE_TYPE_CREATE = 1
PARAMS_DATE_TYPE_WRITE = 2
PARAMS_DATE_TYPE_ACCESS = 3

class ParamsGet:

    def __init__(self):
        self.__dict__['procId'] = 0
        self.__dict__['handle'] = 0
        self.__dict__['chunksize'] = 131070
        self.__dict__['flags'] = 0

    def __getattr__(self, name):
        if name == 'procId':
            return self.__dict__['procId']
        if name == 'handle':
            return self.__dict__['handle']
        if name == 'chunksize':
            return self.__dict__['chunksize']
        if name == 'flags':
            return self.__dict__['flags']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'procId':
            self.__dict__['procId'] = value
        elif name == 'handle':
            self.__dict__['handle'] = value
        elif name == 'chunksize':
            self.__dict__['chunksize'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_GET_PROCESS_ID, self.__dict__['procId'])
        submsg.AddU64(MSG_KEY_PARAMS_GET_HANDLE, self.__dict__['handle'])
        submsg.AddU32(MSG_KEY_PARAMS_GET_CHUNK_SIZE, self.__dict__['chunksize'])
        submsg.AddU16(MSG_KEY_PARAMS_GET_FLAGS, self.__dict__['flags'])
        mmsg.AddMessage(MSG_KEY_PARAMS_GET, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_GET, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['procId'] = submsg.FindU32(MSG_KEY_PARAMS_GET_PROCESS_ID)
        except:
            pass

        try:
            self.__dict__['handle'] = submsg.FindU64(MSG_KEY_PARAMS_GET_HANDLE)
        except:
            pass

        try:
            self.__dict__['chunksize'] = submsg.FindU32(MSG_KEY_PARAMS_GET_CHUNK_SIZE)
        except:
            pass

        try:
            self.__dict__['flags'] = submsg.FindU16(MSG_KEY_PARAMS_GET_FLAGS)
        except:
            pass


class ParamsLock:

    def __init__(self):
        self.__dict__['procId'] = 0
        self.__dict__['handle'] = 0
        self.__dict__['locktime'] = mcl.object.MclTime.MclTime()
        self.__dict__['flags'] = 0

    def __getattr__(self, name):
        if name == 'procId':
            return self.__dict__['procId']
        if name == 'handle':
            return self.__dict__['handle']
        if name == 'locktime':
            return self.__dict__['locktime']
        if name == 'flags':
            return self.__dict__['flags']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'procId':
            self.__dict__['procId'] = value
        elif name == 'handle':
            self.__dict__['handle'] = value
        elif name == 'locktime':
            self.__dict__['locktime'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_LOCK_PROCESS_ID, self.__dict__['procId'])
        submsg.AddU64(MSG_KEY_PARAMS_LOCK_HANDLE, self.__dict__['handle'])
        submsg.AddTime(MSG_KEY_PARAMS_LOCK_LOCK_TIME, self.__dict__['locktime'])
        submsg.AddU16(MSG_KEY_PARAMS_LOCK_FLAGS, self.__dict__['flags'])
        mmsg.AddMessage(MSG_KEY_PARAMS_LOCK, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_LOCK, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['procId'] = submsg.FindU32(MSG_KEY_PARAMS_LOCK_PROCESS_ID)
        except:
            pass

        try:
            self.__dict__['handle'] = submsg.FindU64(MSG_KEY_PARAMS_LOCK_HANDLE)
        except:
            pass

        try:
            self.__dict__['locktime'] = submsg.FindTime(MSG_KEY_PARAMS_LOCK_LOCK_TIME)
        except:
            pass

        try:
            self.__dict__['flags'] = submsg.FindU16(MSG_KEY_PARAMS_LOCK_FLAGS)
        except:
            pass


class ParamsTrim:

    def __init__(self):
        self.__dict__['procId'] = 0
        self.__dict__['handle'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['startOffset'] = 0
        self.__dict__['endOffset'] = 0

    def __getattr__(self, name):
        if name == 'procId':
            return self.__dict__['procId']
        if name == 'handle':
            return self.__dict__['handle']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'startOffset':
            return self.__dict__['startOffset']
        if name == 'endOffset':
            return self.__dict__['endOffset']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'procId':
            self.__dict__['procId'] = value
        elif name == 'handle':
            self.__dict__['handle'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'startOffset':
            self.__dict__['startOffset'] = value
        elif name == 'endOffset':
            self.__dict__['endOffset'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_TRIM_PROCESS_ID, self.__dict__['procId'])
        submsg.AddU64(MSG_KEY_PARAMS_TRIM_HANDLE, self.__dict__['handle'])
        submsg.AddU16(MSG_KEY_PARAMS_TRIM_FLAGS, self.__dict__['flags'])
        submsg.AddU64(MSG_KEY_PARAMS_TRIM_START_OFFSET, self.__dict__['startOffset'])
        submsg.AddU64(MSG_KEY_PARAMS_TRIM_END_OFFSET, self.__dict__['endOffset'])
        mmsg.AddMessage(MSG_KEY_PARAMS_TRIM, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_TRIM, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['procId'] = submsg.FindU32(MSG_KEY_PARAMS_TRIM_PROCESS_ID)
        except:
            pass

        try:
            self.__dict__['handle'] = submsg.FindU64(MSG_KEY_PARAMS_TRIM_HANDLE)
        except:
            pass

        try:
            self.__dict__['flags'] = submsg.FindU16(MSG_KEY_PARAMS_TRIM_FLAGS)
        except:
            pass

        try:
            self.__dict__['startOffset'] = submsg.FindU64(MSG_KEY_PARAMS_TRIM_START_OFFSET)
        except:
            pass

        try:
            self.__dict__['endOffset'] = submsg.FindU64(MSG_KEY_PARAMS_TRIM_END_OFFSET)
        except:
            pass


class ParamsMap:

    def __init__(self):
        self.__dict__['procId'] = 0
        self.__dict__['handle'] = 0
        self.__dict__['flags'] = 0

    def __getattr__(self, name):
        if name == 'procId':
            return self.__dict__['procId']
        if name == 'handle':
            return self.__dict__['handle']
        if name == 'flags':
            return self.__dict__['flags']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'procId':
            self.__dict__['procId'] = value
        elif name == 'handle':
            self.__dict__['handle'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_MAP_PROCESS_ID, self.__dict__['procId'])
        submsg.AddU64(MSG_KEY_PARAMS_MAP_HANDLE, self.__dict__['handle'])
        submsg.AddU16(MSG_KEY_PARAMS_MAP_FLAGS, self.__dict__['flags'])
        mmsg.AddMessage(MSG_KEY_PARAMS_MAP, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_MAP, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['procId'] = submsg.FindU32(MSG_KEY_PARAMS_MAP_PROCESS_ID)
        except:
            pass

        try:
            self.__dict__['handle'] = submsg.FindU64(MSG_KEY_PARAMS_MAP_HANDLE)
        except:
            pass

        try:
            self.__dict__['flags'] = submsg.FindU16(MSG_KEY_PARAMS_MAP_FLAGS)
        except:
            pass