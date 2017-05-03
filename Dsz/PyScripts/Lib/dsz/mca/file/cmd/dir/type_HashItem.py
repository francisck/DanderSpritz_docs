# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_HashItem.py
from types import *
import array
HASH_ITEM_TYPE_UNKNOWN = 0
HASH_ITEM_TYPE_MD5 = 1
HASH_ITEM_TYPE_SHA1 = 2
HASH_ITEM_TYPE_SHA256 = 3
HASH_ITEM_TYPE_SHA512 = 4

class HashItem:

    def __init__(self):
        self.__dict__['type'] = HASH_ITEM_TYPE_UNKNOWN
        self.__dict__['hash'] = array.array('B')

    def __getattr__(self, name):
        if name == 'type':
            return self.__dict__['type']
        if name == 'hash':
            return self.__dict__['hash']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'type':
            self.__dict__['type'] = value
        elif name == 'hash':
            self.__dict__['hash'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_FILE_HASH_TYPE, self.__dict__['type'])
        submsg.AddData(MSG_KEY_FILE_HASH_HASH, self.__dict__['hash'])
        mmsg.AddMessage(MSG_KEY_FILE_HASH, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_FILE_HASH, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_FILE_HASH_TYPE)
        self.__dict__['hash'] = submsg.FindData(MSG_KEY_FILE_HASH_HASH)