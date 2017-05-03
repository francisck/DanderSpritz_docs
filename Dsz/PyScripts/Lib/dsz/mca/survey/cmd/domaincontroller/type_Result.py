# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
RESULT_FLAG_TYPE_WORKSTATION = 1
RESULT_FLAG_TYPE_SERVER = 2
RESULT_FLAG_TYPE_SQLSERVER = 4
RESULT_FLAG_TYPE_DOMAIN_CTRL = 8
RESULT_FLAG_TYPE_DOMAIN_BAKCTRL = 16
RESULT_FLAG_TYPE_TIME_SOURCE = 32
RESULT_FLAG_TYPE_AFP = 64
RESULT_FLAG_TYPE_NOVELL = 128
RESULT_FLAG_TYPE_DOMAIN_MEMBER = 256
RESULT_FLAG_TYPE_PRINTQ_SERVER = 512
RESULT_FLAG_TYPE_DIALIN_SERVER = 1024
RESULT_FLAG_TYPE_SERVER_UNIX = 2048
RESULT_FLAG_TYPE_NT = 4096
RESULT_FLAG_TYPE_WFW = 8192
RESULT_FLAG_TYPE_SERVER_MFPN = 16384
RESULT_FLAG_TYPE_SERVER_NT = 32768
RESULT_FLAG_TYPE_POTENTIAL_BROWSER = 65536
RESULT_FLAG_TYPE_BACKUP_BROWSER = 131072
RESULT_FLAG_TYPE_MASTER_BROWSER = 262144
RESULT_FLAG_TYPE_DOMAIN_MASTER = 524288
RESULT_FLAG_TYPE_SERVER_OSF = 1048576
RESULT_FLAG_TYPE_SERVER_VMS = 2097152
RESULT_FLAG_TYPE_WINDOWS = 4194304
RESULT_FLAG_TYPE_ALTERNATE_XPORT = 536870912
RESULT_FLAG_TYPE_LOCAL_LIST_ONLY = 1073741824
RESULT_FLAG_TYPE_DOMAIN_ENUM = 2147483648L
RESULT_ADDRTYPE_INET = 1
RESULT_ADDRTYPE_NETBIOS = 2
RESULT_FLAG_DC_PDC = 1
RESULT_FLAG_DC_GC = 4
RESULT_FLAG_DC_DS = 16
RESULT_FLAG_DC_KDC = 32
RESULT_FLAG_DC_TIMESERV = 64
RESULT_FLAG_DC_WRITABLE = 256

class ResultStatus:

    def __init__(self):
        self.__dict__['dcEnumStatus'] = 0
        self.__dict__['extraInfoRtn'] = 0
        self.__dict__['typeServ'] = 0
        self.__dict__['dc'] = ''

    def __getattr__(self, name):
        if name == 'dcEnumStatus':
            return self.__dict__['dcEnumStatus']
        if name == 'extraInfoRtn':
            return self.__dict__['extraInfoRtn']
        if name == 'typeServ':
            return self.__dict__['typeServ']
        if name == 'dc':
            return self.__dict__['dc']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'dcEnumStatus':
            self.__dict__['dcEnumStatus'] = value
        elif name == 'extraInfoRtn':
            self.__dict__['extraInfoRtn'] = value
        elif name == 'typeServ':
            self.__dict__['typeServ'] = value
        elif name == 'dc':
            self.__dict__['dc'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_STATUS_DC_ENUM_STATUS, self.__dict__['dcEnumStatus'])
        submsg.AddU32(MSG_KEY_RESULT_STATUS_EXTRA_INFO_RTN, self.__dict__['extraInfoRtn'])
        submsg.AddU32(MSG_KEY_RESULT_STATUS_TYPE_SERV, self.__dict__['typeServ'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_STATUS_DC, self.__dict__['dc'])
        mmsg.AddMessage(MSG_KEY_RESULT_STATUS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_STATUS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['dcEnumStatus'] = submsg.FindU32(MSG_KEY_RESULT_STATUS_DC_ENUM_STATUS)
        self.__dict__['extraInfoRtn'] = submsg.FindU32(MSG_KEY_RESULT_STATUS_EXTRA_INFO_RTN)
        self.__dict__['typeServ'] = submsg.FindU32(MSG_KEY_RESULT_STATUS_TYPE_SERV)
        self.__dict__['dc'] = submsg.FindString(MSG_KEY_RESULT_STATUS_DC)


class ResultDomainController:

    def __init__(self):
        self.__dict__['addressType'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['dcName'] = ''
        self.__dict__['dcAddress'] = ''
        self.__dict__['domainGuid'] = ''
        self.__dict__['domainName'] = ''
        self.__dict__['dnsForestName'] = ''
        self.__dict__['dcSiteName'] = ''
        self.__dict__['clientSiteName'] = ''

    def __getattr__(self, name):
        if name == 'addressType':
            return self.__dict__['addressType']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'dcName':
            return self.__dict__['dcName']
        if name == 'dcAddress':
            return self.__dict__['dcAddress']
        if name == 'domainGuid':
            return self.__dict__['domainGuid']
        if name == 'domainName':
            return self.__dict__['domainName']
        if name == 'dnsForestName':
            return self.__dict__['dnsForestName']
        if name == 'dcSiteName':
            return self.__dict__['dcSiteName']
        if name == 'clientSiteName':
            return self.__dict__['clientSiteName']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'addressType':
            self.__dict__['addressType'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'dcName':
            self.__dict__['dcName'] = value
        elif name == 'dcAddress':
            self.__dict__['dcAddress'] = value
        elif name == 'domainGuid':
            self.__dict__['domainGuid'] = value
        elif name == 'domainName':
            self.__dict__['domainName'] = value
        elif name == 'dnsForestName':
            self.__dict__['dnsForestName'] = value
        elif name == 'dcSiteName':
            self.__dict__['dcSiteName'] = value
        elif name == 'clientSiteName':
            self.__dict__['clientSiteName'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_DC_INFO_ADDRESS_TYPE, self.__dict__['addressType'])
        submsg.AddU32(MSG_KEY_RESULT_DC_INFO_FLAGS, self.__dict__['flags'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DC_INFO_DC_NAME, self.__dict__['dcName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DC_INFO_DC_ADDRESS, self.__dict__['dcAddress'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DC_INFO_DOMAIN_GUID, self.__dict__['domainGuid'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DC_INFO_DOMAIN_NAME, self.__dict__['domainName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DC_INFO_DNS_FOREST_NAME, self.__dict__['dnsForestName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DC_INFO_DC_SITE_NAME, self.__dict__['dcSiteName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DC_INFO_CLIENT_SITE_NAME, self.__dict__['clientSiteName'])
        mmsg.AddMessage(MSG_KEY_RESULT_DC_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_DC_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['addressType'] = submsg.FindU32(MSG_KEY_RESULT_DC_INFO_ADDRESS_TYPE)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_RESULT_DC_INFO_FLAGS)
        self.__dict__['dcName'] = submsg.FindString(MSG_KEY_RESULT_DC_INFO_DC_NAME)
        self.__dict__['dcAddress'] = submsg.FindString(MSG_KEY_RESULT_DC_INFO_DC_ADDRESS)
        self.__dict__['domainGuid'] = submsg.FindString(MSG_KEY_RESULT_DC_INFO_DOMAIN_GUID)
        self.__dict__['domainName'] = submsg.FindString(MSG_KEY_RESULT_DC_INFO_DOMAIN_NAME)
        self.__dict__['dnsForestName'] = submsg.FindString(MSG_KEY_RESULT_DC_INFO_DNS_FOREST_NAME)
        self.__dict__['dcSiteName'] = submsg.FindString(MSG_KEY_RESULT_DC_INFO_DC_SITE_NAME)
        self.__dict__['clientSiteName'] = submsg.FindString(MSG_KEY_RESULT_DC_INFO_CLIENT_SITE_NAME)