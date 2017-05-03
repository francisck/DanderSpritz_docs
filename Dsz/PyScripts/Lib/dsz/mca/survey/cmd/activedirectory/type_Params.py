# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
PARAMS_QUERY_TYPE_MODE = 1
PARAMS_QUERY_TYPE_COMPUTERS = 2
PARAMS_QUERY_TYPE_GROUPS = 3
PARAMS_QUERY_TYPE_USERS = 4
PARAMS_QUERY_TYPE_USERINFO = 5

class Params:

    def __init__(self):
        self.__dict__['queryType'] = 0
        self.__dict__['pagesize'] = 100
        self.__dict__['queryInfo'] = ''
        self.__dict__['adsPath'] = 'LDAP:'

    def __getattr__(self, name):
        if name == 'queryType':
            return self.__dict__['queryType']
        if name == 'pagesize':
            return self.__dict__['pagesize']
        if name == 'queryInfo':
            return self.__dict__['queryInfo']
        if name == 'adsPath':
            return self.__dict__['adsPath']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'queryType':
            self.__dict__['queryType'] = value
        elif name == 'pagesize':
            self.__dict__['pagesize'] = value
        elif name == 'queryInfo':
            self.__dict__['queryInfo'] = value
        elif name == 'adsPath':
            self.__dict__['adsPath'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_QUERY_TYPE, self.__dict__['queryType'])
        submsg.AddU32(MSG_KEY_PARAMS_PAGE_SIZE, self.__dict__['pagesize'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_QUERY_INFO, self.__dict__['queryInfo'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_ADS_PATH, self.__dict__['adsPath'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['queryType'] = submsg.FindU8(MSG_KEY_PARAMS_QUERY_TYPE)
        try:
            self.__dict__['pagesize'] = submsg.FindU32(MSG_KEY_PARAMS_PAGE_SIZE)
        except:
            pass

        try:
            self.__dict__['queryInfo'] = submsg.FindString(MSG_KEY_PARAMS_QUERY_INFO)
        except:
            pass

        try:
            self.__dict__['adsPath'] = submsg.FindString(MSG_KEY_PARAMS_ADS_PATH)
        except:
            pass