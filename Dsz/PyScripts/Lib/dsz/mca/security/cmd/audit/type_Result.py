# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import array
RESULT_FLAG_AUDIT_ONSUCCESS = 1
RESULT_FLAG_AUDIT_ONFAILURE = 2

class ResultAuditStatus:

    def __init__(self):
        self.__dict__['auditingEnabled'] = False

    def __getattr__(self, name):
        if name == 'auditingEnabled':
            return self.__dict__['auditingEnabled']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'auditingEnabled':
            self.__dict__['auditingEnabled'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddBool(MSG_KEY_RESULT_STATUS_ENABLED, self.__dict__['auditingEnabled'])
        mmsg.AddMessage(MSG_KEY_RESULT_STATUS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_STATUS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['auditingEnabled'] = submsg.FindBool(MSG_KEY_RESULT_STATUS_ENABLED)


class ResultCategory:

    def __init__(self):
        self.__dict__['flags'] = 0
        self.__dict__['categoryGuid'] = array.array('B')
        i = 0
        while i < 16:
            self.__dict__['categoryGuid'].append(0)
            i = i + 1

        self.__dict__['subcategoryGuid'] = array.array('B')
        i = 0
        while i < 16:
            self.__dict__['subcategoryGuid'].append(0)
            i = i + 1

        self.__dict__['category'] = ''
        self.__dict__['subcategory'] = ''

    def __getattr__(self, name):
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'categoryGuid':
            return self.__dict__['categoryGuid']
        if name == 'subcategoryGuid':
            return self.__dict__['subcategoryGuid']
        if name == 'category':
            return self.__dict__['category']
        if name == 'subcategory':
            return self.__dict__['subcategory']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'categoryGuid':
            self.__dict__['categoryGuid'] = value
        elif name == 'subcategoryGuid':
            self.__dict__['subcategoryGuid'] = value
        elif name == 'category':
            self.__dict__['category'] = value
        elif name == 'subcategory':
            self.__dict__['subcategory'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU16(MSG_KEY_RESULT_CATEGORY_FLAGS, self.__dict__['flags'])
        submsg.AddData(MSG_KEY_RESULT_CATEGORY_GUID_CATEGORY, self.__dict__['categoryGuid'])
        submsg.AddData(MSG_KEY_RESULT_CATEGORY_GUID_SUBCATEGORY, self.__dict__['subcategoryGuid'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_CATEGORY_NAME_CATEGORY, self.__dict__['category'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_CATEGORY_NAME_SUBCATEGORY, self.__dict__['subcategory'])
        mmsg.AddMessage(MSG_KEY_RESULT_CATEGORY, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_CATEGORY, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['flags'] = submsg.FindU16(MSG_KEY_RESULT_CATEGORY_FLAGS)
        self.__dict__['categoryGuid'] = submsg.FindData(MSG_KEY_RESULT_CATEGORY_GUID_CATEGORY)
        self.__dict__['subcategoryGuid'] = submsg.FindData(MSG_KEY_RESULT_CATEGORY_GUID_SUBCATEGORY)
        self.__dict__['category'] = submsg.FindString(MSG_KEY_RESULT_CATEGORY_NAME_CATEGORY)
        self.__dict__['subcategory'] = submsg.FindString(MSG_KEY_RESULT_CATEGORY_NAME_SUBCATEGORY)


class ResultModify:

    def __init__(self):
        self.__dict__['type'] = 0

    def __getattr__(self, name):
        if name == 'type':
            return self.__dict__['type']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'type':
            self.__dict__['type'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_MODIFY_TYPE, self.__dict__['type'])
        mmsg.AddMessage(MSG_KEY_RESULT_MODIFY, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_MODIFY, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_RESULT_MODIFY_TYPE)