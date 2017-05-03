# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import array
import array
RESULT_NT_KEY_SIZE = 16
RESULT_NT_FLAG_EXCEPTION = 1
RESULT_NT_FLAG_EXPIRED = 2
RESULT_NT_FLAG_NT_PRESENT = 4
RESULT_NT_FLAG_LM_PRESENT = 8

class ResultNtPassword:

    def __init__(self):
        self.__dict__['rid'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['ntOwfPassword'] = array.array('B')
        i = 0
        while i < RESULT_NT_KEY_SIZE:
            self.__dict__['ntOwfPassword'].append(0)
            i = i + 1

        self.__dict__['lmOwfPassword'] = array.array('B')
        i = 0
        while i < RESULT_NT_KEY_SIZE:
            self.__dict__['lmOwfPassword'].append(0)
            i = i + 1

        self.__dict__['user'] = ''

    def __getattr__(self, name):
        if name == 'rid':
            return self.__dict__['rid']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'ntOwfPassword':
            return self.__dict__['ntOwfPassword']
        if name == 'lmOwfPassword':
            return self.__dict__['lmOwfPassword']
        if name == 'user':
            return self.__dict__['user']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'rid':
            self.__dict__['rid'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'ntOwfPassword':
            self.__dict__['ntOwfPassword'] = value
        elif name == 'lmOwfPassword':
            self.__dict__['lmOwfPassword'] = value
        elif name == 'user':
            self.__dict__['user'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_NT_RID, self.__dict__['rid'])
        submsg.AddU16(MSG_KEY_RESULT_NT_FLAGS, self.__dict__['flags'])
        submsg.AddData(MSG_KEY_RESULT_NT_NT_OWF_PASSWORD, self.__dict__['ntOwfPassword'])
        submsg.AddData(MSG_KEY_RESULT_NT_LM_OWF_PASSWORD, self.__dict__['lmOwfPassword'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_NT_USER, self.__dict__['user'])
        mmsg.AddMessage(MSG_KEY_RESULT_NT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_NT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['rid'] = submsg.FindU32(MSG_KEY_RESULT_NT_RID)
        self.__dict__['flags'] = submsg.FindU16(MSG_KEY_RESULT_NT_FLAGS)
        self.__dict__['ntOwfPassword'] = submsg.FindData(MSG_KEY_RESULT_NT_NT_OWF_PASSWORD)
        self.__dict__['lmOwfPassword'] = submsg.FindData(MSG_KEY_RESULT_NT_LM_OWF_PASSWORD)
        self.__dict__['user'] = submsg.FindString(MSG_KEY_RESULT_NT_USER)


class ResultNtCachedPassword:

    def __init__(self):
        self.__dict__['data'] = array.array('B')
        self.__dict__['secret'] = ''

    def __getattr__(self, name):
        if name == 'data':
            return self.__dict__['data']
        if name == 'secret':
            return self.__dict__['secret']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'data':
            self.__dict__['data'] = value
        elif name == 'secret':
            self.__dict__['secret'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddData(MSG_KEY_RESULT_NT_CACHED_DATA, self.__dict__['data'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_NT_CACHED_SECRET, self.__dict__['secret'])
        mmsg.AddMessage(MSG_KEY_RESULT_NT_CACHED, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_NT_CACHED, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['data'] = submsg.FindData(MSG_KEY_RESULT_NT_CACHED_DATA)
        self.__dict__['secret'] = submsg.FindString(MSG_KEY_RESULT_NT_CACHED_SECRET)


class ResultUnixPassword:

    def __init__(self):
        self.__dict__['user'] = ''
        self.__dict__['hash'] = ''
        self.__dict__['expired'] = False

    def __getattr__(self, name):
        if name == 'user':
            return self.__dict__['user']
        if name == 'hash':
            return self.__dict__['hash']
        if name == 'expired':
            return self.__dict__['expired']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'user':
            self.__dict__['user'] = value
        elif name == 'hash':
            self.__dict__['hash'] = value
        elif name == 'expired':
            self.__dict__['expired'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_UNIX_USER, self.__dict__['user'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_UNIX_HASH, self.__dict__['hash'])
        submsg.AddBool(MSG_KEY_RESULT_UNIX_EXPIRED, self.__dict__['expired'])
        mmsg.AddMessage(MSG_KEY_RESULT_UNIX, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_UNIX, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['user'] = submsg.FindString(MSG_KEY_RESULT_UNIX_USER)
        self.__dict__['hash'] = submsg.FindString(MSG_KEY_RESULT_UNIX_HASH)
        self.__dict__['expired'] = submsg.FindBool(MSG_KEY_RESULT_UNIX_EXPIRED)


class ResultNtDigestPassword:

    def __init__(self):
        self.__dict__['user'] = ''
        self.__dict__['domain'] = ''
        self.__dict__['password'] = ''

    def __getattr__(self, name):
        if name == 'user':
            return self.__dict__['user']
        if name == 'domain':
            return self.__dict__['domain']
        if name == 'password':
            return self.__dict__['password']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'user':
            self.__dict__['user'] = value
        elif name == 'domain':
            self.__dict__['domain'] = value
        elif name == 'password':
            self.__dict__['password'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_DIGEST_USER, self.__dict__['user'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DIGEST_DOMAIN, self.__dict__['domain'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DIGEST_PASSWORD, self.__dict__['password'])
        mmsg.AddMessage(MSG_KEY_RESULT_DIGEST, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_DIGEST, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['user'] = submsg.FindString(MSG_KEY_RESULT_DIGEST_USER)
        self.__dict__['domain'] = submsg.FindString(MSG_KEY_RESULT_DIGEST_DOMAIN)
        self.__dict__['password'] = submsg.FindString(MSG_KEY_RESULT_DIGEST_PASSWORD)