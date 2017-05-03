# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
import mcl.object.MclTime
PARAMS_FLAG_RECURSIVE = 1
PARAMS_TAIL_OFFSET = -1
PARAMS_DATE_TYPE_NONE = 0
PARAMS_DATE_TYPE_CREATE = 1
PARAMS_DATE_TYPE_WRITE = 2
PARAMS_DATE_TYPE_ACCESS = 3

class Params:

    def __init__(self):
        self.__dict__['rawIndex'] = 0
        self.__dict__['offset'] = 0
        self.__dict__['bytesToRead'] = 0
        self.__dict__['maxFiles'] = 0
        self.__dict__['chunkSize'] = 131070
        self.__dict__['flags'] = 0
        self.__dict__['dateType'] = PARAMS_DATE_TYPE_NONE
        self.__dict__['age'] = mcl.object.MclTime.MclTime()
        self.__dict__['afterTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['beforeTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['mask'] = ''
        self.__dict__['path'] = ''
        self.__dict__['minSize'] = 0
        self.__dict__['maxSize'] = 0
        self.__dict__['provider'] = 0

    def __getattr__(self, name):
        if name == 'rawIndex':
            return self.__dict__['rawIndex']
        if name == 'offset':
            return self.__dict__['offset']
        if name == 'bytesToRead':
            return self.__dict__['bytesToRead']
        if name == 'maxFiles':
            return self.__dict__['maxFiles']
        if name == 'chunkSize':
            return self.__dict__['chunkSize']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'dateType':
            return self.__dict__['dateType']
        if name == 'age':
            return self.__dict__['age']
        if name == 'afterTime':
            return self.__dict__['afterTime']
        if name == 'beforeTime':
            return self.__dict__['beforeTime']
        if name == 'mask':
            return self.__dict__['mask']
        if name == 'path':
            return self.__dict__['path']
        if name == 'minSize':
            return self.__dict__['minSize']
        if name == 'maxSize':
            return self.__dict__['maxSize']
        if name == 'provider':
            return self.__dict__['provider']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'rawIndex':
            self.__dict__['rawIndex'] = value
        elif name == 'offset':
            self.__dict__['offset'] = value
        elif name == 'bytesToRead':
            self.__dict__['bytesToRead'] = value
        elif name == 'maxFiles':
            self.__dict__['maxFiles'] = value
        elif name == 'chunkSize':
            self.__dict__['chunkSize'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'dateType':
            self.__dict__['dateType'] = value
        elif name == 'age':
            self.__dict__['age'] = value
        elif name == 'afterTime':
            self.__dict__['afterTime'] = value
        elif name == 'beforeTime':
            self.__dict__['beforeTime'] = value
        elif name == 'mask':
            self.__dict__['mask'] = value
        elif name == 'path':
            self.__dict__['path'] = value
        elif name == 'minSize':
            self.__dict__['minSize'] = value
        elif name == 'maxSize':
            self.__dict__['maxSize'] = value
        elif name == 'provider':
            self.__dict__['provider'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_PARAMS_RAW_INDEX, self.__dict__['rawIndex'])
        submsg.AddS64(MSG_KEY_PARAMS_OFFSET, self.__dict__['offset'])
        submsg.AddU64(MSG_KEY_PARAMS_BYTES_TO_READ, self.__dict__['bytesToRead'])
        submsg.AddU16(MSG_KEY_PARAMS_MAX_FILES, self.__dict__['maxFiles'])
        submsg.AddU32(MSG_KEY_PARAMS_CHUNK_SIZE, self.__dict__['chunkSize'])
        submsg.AddU16(MSG_KEY_PARAMS_FLAGS, self.__dict__['flags'])
        submsg.AddU8(MSG_KEY_PARAMS_DATE_TYPE, self.__dict__['dateType'])
        submsg.AddTime(MSG_KEY_PARAMS_AGE, self.__dict__['age'])
        submsg.AddTime(MSG_KEY_PARAMS_AFTER_TIME, self.__dict__['afterTime'])
        submsg.AddTime(MSG_KEY_PARAMS_BEFORE_TIME, self.__dict__['beforeTime'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_MASK, self.__dict__['mask'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_PATH, self.__dict__['path'])
        submsg.AddU64(MSG_KEY_PARAMS_MINIMUM_SIZE, self.__dict__['minSize'])
        submsg.AddU64(MSG_KEY_PARAMS_MAXIMUM_SIZE, self.__dict__['maxSize'])
        submsg.AddU32(MSG_KEY_PARAMS_FILE_PROVIDER, self.__dict__['provider'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['rawIndex'] = submsg.FindU64(MSG_KEY_PARAMS_RAW_INDEX)
        except:
            pass

        try:
            self.__dict__['offset'] = submsg.FindS64(MSG_KEY_PARAMS_OFFSET)
        except:
            pass

        try:
            self.__dict__['bytesToRead'] = submsg.FindU64(MSG_KEY_PARAMS_BYTES_TO_READ)
        except:
            pass

        try:
            self.__dict__['maxFiles'] = submsg.FindU16(MSG_KEY_PARAMS_MAX_FILES)
        except:
            pass

        try:
            self.__dict__['chunkSize'] = submsg.FindU32(MSG_KEY_PARAMS_CHUNK_SIZE)
        except:
            pass

        try:
            self.__dict__['flags'] = submsg.FindU16(MSG_KEY_PARAMS_FLAGS)
        except:
            pass

        try:
            self.__dict__['dateType'] = submsg.FindU8(MSG_KEY_PARAMS_DATE_TYPE)
        except:
            pass

        try:
            self.__dict__['age'] = submsg.FindTime(MSG_KEY_PARAMS_AGE)
        except:
            pass

        try:
            self.__dict__['afterTime'] = submsg.FindTime(MSG_KEY_PARAMS_AFTER_TIME)
        except:
            pass

        try:
            self.__dict__['beforeTime'] = submsg.FindTime(MSG_KEY_PARAMS_BEFORE_TIME)
        except:
            pass

        self.__dict__['mask'] = submsg.FindString(MSG_KEY_PARAMS_MASK)
        self.__dict__['path'] = submsg.FindString(MSG_KEY_PARAMS_PATH)
        try:
            self.__dict__['minSize'] = submsg.FindU64(MSG_KEY_PARAMS_MINIMUM_SIZE)
        except:
            pass

        try:
            self.__dict__['maxSize'] = submsg.FindU64(MSG_KEY_PARAMS_MAXIMUM_SIZE)
        except:
            pass

        try:
            self.__dict__['provider'] = submsg.FindU32(MSG_KEY_PARAMS_FILE_PROVIDER)
        except:
            pass