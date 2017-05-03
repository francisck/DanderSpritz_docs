# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.MclTime
RESULT_PRIV_GUEST = 1
RESULT_PRIV_USER = 2
RESULT_PRIV_ADMIN = 4
RESULT_AUTH_FLAG_PRINT = 1
RESULT_AUTH_FLAG_COMM = 2
RESULT_AUTH_FLAG_SERVER = 4
RESULT_AUTH_FLAG_ACCOUNTS = 8
RESULT_USER_FLAG_SCRIPT = 1
RESULT_USER_FLAG_ACCOUNTDISABLE = 2
RESULT_USER_FLAG_HOMEDIR_REQUIRED = 4
RESULT_USER_FLAG_LOCKOUT = 8
RESULT_USER_FLAG_PASSWD_NOTREQD = 16
RESULT_USER_FLAG_PASSWD_CANT_CHANGE = 32
RESULT_USER_FLAG_ENCRYPTED_TEXT_PASSWORD_ALLOWED = 64
RESULT_USER_FLAG_TEMP_DUPLICATE_ACCOUNT = 128
RESULT_USER_FLAG_NORMAL_ACCOUNT = 256
RESULT_USER_FLAG_INTERDOMAIN_TRUST_ACCOUNT = 512
RESULT_USER_FLAG_WORKSTATION_TRUST_ACCOUNT = 1024
RESULT_USER_FLAG_SERVER_TRUST_ACCOUNT = 2048
RESULT_USER_FLAG_DONT_EXPIRE_PASSWD = 4096
RESULT_USER_FLAG_SMARTCARD_REQUIRED = 8192
RESULT_USER_FLAG_TRUSTED_FOR_DELEGATION = 16384
RESULT_USER_FLAG_NOT_DELEGATED = 32768
RESULT_USER_FLAG_USE_DES_KEY_ONLY = 65536
RESULT_USER_FLAG_DONT_REQUIRE_PREAUTH = 131072
RESULT_USER_FLAG_PASSWORD_EXPIRED = 262144
RESULT_USER_FLAG_TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION = 524288
RESULT_USER_FLAG_MNS_LOGON_ACCOUNT = 1048576
RESULT_USER_FLAG_NO_AUTH_DATA_REQUIRED = 2097152
RESULT_USER_FLAG_PARTIAL_SECRETS_ACCOUNT = 4194304
RESULT_USER_FLAG_USE_AES_KEYS = 8388608

class Result:

    def __init__(self):
        self.__dict__['passwordLastChanged'] = mcl.object.MclTime.MclTime()
        self.__dict__['privs'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['authFlags'] = 0
        self.__dict__['lastLogon'] = mcl.object.MclTime.MclTime()
        self.__dict__['acctExpires'] = mcl.object.MclTime.MclTime()
        self.__dict__['numLogons'] = 0
        self.__dict__['userId'] = 0
        self.__dict__['primaryGroupId'] = 0
        self.__dict__['name'] = ''
        self.__dict__['comment'] = ''
        self.__dict__['fullName'] = ''
        self.__dict__['homeDir'] = ''
        self.__dict__['userShell'] = ''

    def __getattr__(self, name):
        if name == 'passwordLastChanged':
            return self.__dict__['passwordLastChanged']
        if name == 'privs':
            return self.__dict__['privs']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'authFlags':
            return self.__dict__['authFlags']
        if name == 'lastLogon':
            return self.__dict__['lastLogon']
        if name == 'acctExpires':
            return self.__dict__['acctExpires']
        if name == 'numLogons':
            return self.__dict__['numLogons']
        if name == 'userId':
            return self.__dict__['userId']
        if name == 'primaryGroupId':
            return self.__dict__['primaryGroupId']
        if name == 'name':
            return self.__dict__['name']
        if name == 'comment':
            return self.__dict__['comment']
        if name == 'fullName':
            return self.__dict__['fullName']
        if name == 'homeDir':
            return self.__dict__['homeDir']
        if name == 'userShell':
            return self.__dict__['userShell']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'passwordLastChanged':
            self.__dict__['passwordLastChanged'] = value
        elif name == 'privs':
            self.__dict__['privs'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'authFlags':
            self.__dict__['authFlags'] = value
        elif name == 'lastLogon':
            self.__dict__['lastLogon'] = value
        elif name == 'acctExpires':
            self.__dict__['acctExpires'] = value
        elif name == 'numLogons':
            self.__dict__['numLogons'] = value
        elif name == 'userId':
            self.__dict__['userId'] = value
        elif name == 'primaryGroupId':
            self.__dict__['primaryGroupId'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        elif name == 'comment':
            self.__dict__['comment'] = value
        elif name == 'fullName':
            self.__dict__['fullName'] = value
        elif name == 'homeDir':
            self.__dict__['homeDir'] = value
        elif name == 'userShell':
            self.__dict__['userShell'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddTime(MSG_KEY_RESULT_PASSWORD_LAST_CHANGED, self.__dict__['passwordLastChanged'])
        submsg.AddU32(MSG_KEY_RESULT_PRIVILEGES, self.__dict__['privs'])
        submsg.AddU32(MSG_KEY_RESULT_FLAGS, self.__dict__['flags'])
        submsg.AddU32(MSG_KEY_RESULT_AUTH_FLAGS, self.__dict__['authFlags'])
        submsg.AddTime(MSG_KEY_RESULT_LAST_LOGON, self.__dict__['lastLogon'])
        submsg.AddTime(MSG_KEY_RESULT_ACCOUNT_EXPIRES, self.__dict__['acctExpires'])
        submsg.AddU32(MSG_KEY_RESULT_NUM_LOGONS, self.__dict__['numLogons'])
        submsg.AddU32(MSG_KEY_RESULT_USER_ID, self.__dict__['userId'])
        submsg.AddU32(MSG_KEY_RESULT_PRIMARY_GROUP_ID, self.__dict__['primaryGroupId'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_NAME, self.__dict__['name'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_COMMENT, self.__dict__['comment'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_FULL_NAME, self.__dict__['fullName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_HOME_DIR, self.__dict__['homeDir'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_USER_SHELL, self.__dict__['userShell'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['passwordLastChanged'] = submsg.FindTime(MSG_KEY_RESULT_PASSWORD_LAST_CHANGED)
        self.__dict__['privs'] = submsg.FindU32(MSG_KEY_RESULT_PRIVILEGES)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_RESULT_FLAGS)
        self.__dict__['authFlags'] = submsg.FindU32(MSG_KEY_RESULT_AUTH_FLAGS)
        self.__dict__['lastLogon'] = submsg.FindTime(MSG_KEY_RESULT_LAST_LOGON)
        self.__dict__['acctExpires'] = submsg.FindTime(MSG_KEY_RESULT_ACCOUNT_EXPIRES)
        self.__dict__['numLogons'] = submsg.FindU32(MSG_KEY_RESULT_NUM_LOGONS)
        self.__dict__['userId'] = submsg.FindU32(MSG_KEY_RESULT_USER_ID)
        self.__dict__['primaryGroupId'] = submsg.FindU32(MSG_KEY_RESULT_PRIMARY_GROUP_ID)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_NAME)
        self.__dict__['comment'] = submsg.FindString(MSG_KEY_RESULT_COMMENT)
        self.__dict__['fullName'] = submsg.FindString(MSG_KEY_RESULT_FULL_NAME)
        self.__dict__['homeDir'] = submsg.FindString(MSG_KEY_RESULT_HOME_DIR)
        self.__dict__['userShell'] = submsg.FindString(MSG_KEY_RESULT_USER_SHELL)