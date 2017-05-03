# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
import mcl.object.MclTime
PARAM_FLAG_RECURSIVE = 1
PARAM_FLAG_DIRS_ONLY = 2
PARAM_FLAG_PERFORM_HASH_MD5 = 4
PARAM_FLAG_PERFORM_HASH_SHA1 = 8
PARAM_FLAG_PERFORM_HASH_SHA256 = 16
PARAM_FLAG_PERFORM_HASH_SHA512 = 32
PARAM_TIME_TYPE_NONE = 0
PARAM_TIME_TYPE_ACCESSED = 1
PARAM_TIME_TYPE_MODIFIED = 2
PARAM_TIME_TYPE_CREATED = 3

class Params:

    def __init__(self):
        self.__dict__['flags'] = 0
        self.__dict__['maxEntries'] = 0
        self.__dict__['dateType'] = PARAM_TIME_TYPE_NONE
        self.__dict__['age'] = mcl.object.MclTime.MclTime()
        self.__dict__['afterTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['beforeTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['chunkSize'] = 65536
        self.__dict__['depth'] = 0
        self.__dict__['mask'] = ''
        self.__dict__['path'] = ''

    def __getattr__(self, name):
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'maxEntries':
            return self.__dict__['maxEntries']
        if name == 'dateType':
            return self.__dict__['dateType']
        if name == 'age':
            return self.__dict__['age']
        if name == 'afterTime':
            return self.__dict__['afterTime']
        if name == 'beforeTime':
            return self.__dict__['beforeTime']
        if name == 'chunkSize':
            return self.__dict__['chunkSize']
        if name == 'depth':
            return self.__dict__['depth']
        if name == 'mask':
            return self.__dict__['mask']
        if name == 'path':
            return self.__dict__['path']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'maxEntries':
            self.__dict__['maxEntries'] = value
        elif name == 'dateType':
            self.__dict__['dateType'] = value
        elif name == 'age':
            self.__dict__['age'] = value
        elif name == 'afterTime':
            self.__dict__['afterTime'] = value
        elif name == 'beforeTime':
            self.__dict__['beforeTime'] = value
        elif name == 'chunkSize':
            self.__dict__['chunkSize'] = value
        elif name == 'depth':
            self.__dict__['depth'] = value
        elif name == 'mask':
            self.__dict__['mask'] = value
        elif name == 'path':
            self.__dict__['path'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_FLAGS, self.__dict__['flags'])
        submsg.AddU32(MSG_KEY_PARAMS_MAX_ENTRIES, self.__dict__['maxEntries'])
        submsg.AddU8(MSG_KEY_PARAMS_DATETYPE, self.__dict__['dateType'])
        submsg.AddTime(MSG_KEY_PARAMS_AGE, self.__dict__['age'])
        submsg.AddTime(MSG_KEY_PARAMS_AFTERTIME, self.__dict__['afterTime'])
        submsg.AddTime(MSG_KEY_PARAMS_BEFORETIME, self.__dict__['beforeTime'])
        submsg.AddU32(MSG_KEY_PARAMS_CHUNKSIZE, self.__dict__['chunkSize'])
        submsg.AddU32(MSG_KEY_PARAMS_DEPTH, self.__dict__['depth'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_MASK, self.__dict__['mask'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_PATH, self.__dict__['path'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_PARAMS_FLAGS)
        try:
            self.__dict__['maxEntries'] = submsg.FindU32(MSG_KEY_PARAMS_MAX_ENTRIES)
        except:
            pass

        try:
            self.__dict__['dateType'] = submsg.FindU8(MSG_KEY_PARAMS_DATETYPE)
        except:
            pass

        try:
            self.__dict__['age'] = submsg.FindTime(MSG_KEY_PARAMS_AGE)
        except:
            pass

        try:
            self.__dict__['afterTime'] = submsg.FindTime(MSG_KEY_PARAMS_AFTERTIME)
        except:
            pass

        try:
            self.__dict__['beforeTime'] = submsg.FindTime(MSG_KEY_PARAMS_BEFORETIME)
        except:
            pass

        try:
            self.__dict__['chunkSize'] = submsg.FindU32(MSG_KEY_PARAMS_CHUNKSIZE)
        except:
            pass

        try:
            self.__dict__['depth'] = submsg.FindU32(MSG_KEY_PARAMS_DEPTH)
        except:
            pass

        self.__dict__['mask'] = submsg.FindString(MSG_KEY_PARAMS_MASK)
        self.__dict__['path'] = submsg.FindString(MSG_KEY_PARAMS_PATH)