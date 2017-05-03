# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: DataHandlerInput.py


class DataHandlerInput:

    def __init__(self):
        self.m_data = ()
        self.m_status = 0
        self.m_messageType = 0
        self.m_dest = 0
        self.m_priority = 0
        self.m_producerInterface = 0
        self.m_producerProvider = 0
        self.m_taskIds = ()
        self.m_uuid = None
        self.m_collectTime = None
        return

    def GetCollectTime(self):
        return self.m_collectTime

    def SetCollectTime(self, collectTime):
        self.m_collectTime = collectTime

    def GetData(self):
        return self.m_data

    def SetData(self, data):
        self.m_data = data

    def GetDest(self):
        return self.m_dest

    def SetDest(self, dest):
        self.m_dest = dest

    def GetMessageType(self):
        return self.m_messageType

    def SetMessageType(self, messageType):
        self.m_messageType = messageType

    def GetPriority(self):
        return self.m_priority

    def SetPriority(self, priority):
        self.m_priority = priority

    def GetProducerInterface(self):
        return self.m_producerInterface

    def SetProducerInterface(self, iface):
        self.m_producerInterface = iface

    def GetProducerProvider(self):
        return self.m_producerProvider

    def SetProducerProvider(self, provider):
        self.m_producerProvider = provider

    def GetStatus(self):
        return self.m_status

    def SetStatus(self, status):
        self.m_status = status

    def GetTaskIds(self):
        return self.m_taskIds

    def SetTaskIds(self, ids):
        self.m_taskIds = ids

    def GetUuid(self):
        return self.m_uuid

    def SetUuid(self, uuid):
        self.m_uuid = uuid