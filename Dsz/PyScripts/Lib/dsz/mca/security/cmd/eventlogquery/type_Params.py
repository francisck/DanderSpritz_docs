# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
PARAMS_FLAG_USE_CLASSIC_LOG = 1

class QueryParams:

    def __init__(self):
        self.__dict__['startNum'] = 0
        self.__dict__['endNum'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['target'] = ''

    def __getattr__(self, name):
        if name == 'startNum':
            return self.__dict__['startNum']
        if name == 'endNum':
            return self.__dict__['endNum']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'target':
            return self.__dict__['target']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'startNum':
            self.__dict__['startNum'] = value
        elif name == 'endNum':
            self.__dict__['endNum'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'target':
            self.__dict__['target'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_PARAMS_QUERY_INFO_START_NUMBER, self.__dict__['startNum'])
        submsg.AddU64(MSG_KEY_PARAMS_QUERY_INFO_END_NUMBER, self.__dict__['endNum'])
        submsg.AddU32(MSG_KEY_PARAMS_QUERY_INFO_FLAGS, self.__dict__['flags'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_QUERY_INFO_TARGET, self.__dict__['target'])
        mmsg.AddMessage(MSG_KEY_PARAMS_QUERY_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_QUERY_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['startNum'] = submsg.FindU64(MSG_KEY_PARAMS_QUERY_INFO_START_NUMBER)
        self.__dict__['endNum'] = submsg.FindU64(MSG_KEY_PARAMS_QUERY_INFO_END_NUMBER)
        try:
            self.__dict__['flags'] = submsg.FindU32(MSG_KEY_PARAMS_QUERY_INFO_FLAGS)
        except:
            pass

        try:
            self.__dict__['target'] = submsg.FindString(MSG_KEY_PARAMS_QUERY_INFO_TARGET)
        except:
            pass


class FilterParams:

    def __init__(self):
        self.__dict__['eventId'] = 0
        self.__dict__['startRecord'] = 0
        self.__dict__['numToParse'] = 0
        self.__dict__['maxReturned'] = 1000
        self.__dict__['flags'] = 0
        self.__dict__['target'] = ''
        self.__dict__['log'] = ''
        self.__dict__['sidFilter'] = ''
        self.__dict__['stringFilter'] = ''
        self.__dict__['xpath'] = ''

    def __getattr__(self, name):
        if name == 'eventId':
            return self.__dict__['eventId']
        if name == 'startRecord':
            return self.__dict__['startRecord']
        if name == 'numToParse':
            return self.__dict__['numToParse']
        if name == 'maxReturned':
            return self.__dict__['maxReturned']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'target':
            return self.__dict__['target']
        if name == 'log':
            return self.__dict__['log']
        if name == 'sidFilter':
            return self.__dict__['sidFilter']
        if name == 'stringFilter':
            return self.__dict__['stringFilter']
        if name == 'xpath':
            return self.__dict__['xpath']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'eventId':
            self.__dict__['eventId'] = value
        elif name == 'startRecord':
            self.__dict__['startRecord'] = value
        elif name == 'numToParse':
            self.__dict__['numToParse'] = value
        elif name == 'maxReturned':
            self.__dict__['maxReturned'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'target':
            self.__dict__['target'] = value
        elif name == 'log':
            self.__dict__['log'] = value
        elif name == 'sidFilter':
            self.__dict__['sidFilter'] = value
        elif name == 'stringFilter':
            self.__dict__['stringFilter'] = value
        elif name == 'xpath':
            self.__dict__['xpath'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_FILTER_EVENT_ID, self.__dict__['eventId'])
        submsg.AddU64(MSG_KEY_PARAMS_FILTER_START_RECORD, self.__dict__['startRecord'])
        submsg.AddU32(MSG_KEY_PARAMS_FILTER_NUM_TO_PARSE, self.__dict__['numToParse'])
        submsg.AddU32(MSG_KEY_PARAMS_FILTER_MAX_RETURNED, self.__dict__['maxReturned'])
        submsg.AddU32(MSG_KEY_PARAMS_FILTER_FLAGS, self.__dict__['flags'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_FILTER_TARGET, self.__dict__['target'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_FILTER_LOG, self.__dict__['log'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_FILTER_SID_FILTER, self.__dict__['sidFilter'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_FILTER_STRING_FILTER, self.__dict__['stringFilter'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_FILTER_XPATH, self.__dict__['xpath'])
        mmsg.AddMessage(MSG_KEY_PARAMS_FILTER, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_FILTER, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['eventId'] = submsg.FindU32(MSG_KEY_PARAMS_FILTER_EVENT_ID)
        except:
            pass

        self.__dict__['startRecord'] = submsg.FindU64(MSG_KEY_PARAMS_FILTER_START_RECORD)
        try:
            self.__dict__['numToParse'] = submsg.FindU32(MSG_KEY_PARAMS_FILTER_NUM_TO_PARSE)
        except:
            pass

        try:
            self.__dict__['maxReturned'] = submsg.FindU32(MSG_KEY_PARAMS_FILTER_MAX_RETURNED)
        except:
            pass

        try:
            self.__dict__['flags'] = submsg.FindU32(MSG_KEY_PARAMS_FILTER_FLAGS)
        except:
            pass

        try:
            self.__dict__['target'] = submsg.FindString(MSG_KEY_PARAMS_FILTER_TARGET)
        except:
            pass

        self.__dict__['log'] = submsg.FindString(MSG_KEY_PARAMS_FILTER_LOG)
        try:
            self.__dict__['sidFilter'] = submsg.FindString(MSG_KEY_PARAMS_FILTER_SID_FILTER)
        except:
            pass

        try:
            self.__dict__['stringFilter'] = submsg.FindString(MSG_KEY_PARAMS_FILTER_STRING_FILTER)
        except:
            pass

        try:
            self.__dict__['xpath'] = submsg.FindString(MSG_KEY_PARAMS_FILTER_XPATH)
        except:
            pass