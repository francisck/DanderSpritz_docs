# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: XmlCommandBase.py


class XmlCommandBase:

    def __init__(self):
        self.m_setParams = {}
        self.m_name = ''
        self.m_dataName = ''
        self.m_help = []
        self.m_optional = False

    def AddSetParameter(self, paramName, value):
        self.m_setParams[paramName] = value

    def AppendParameters(self, params):
        for setKey in self.m_setParams.keys():
            params[setKey] = self.m_setParams[setKey]

    def GetDataName(self):
        return self.m_dataName

    def GetHelp(self, index):
        if index < len(self.m_help):
            return self.m_help[index]
        else:
            return ''

    def GetHelpSize(self):
        return len(self.m_help)

    def GetName(self):
        return self.m_name

    def IsOptional(self):
        return self.m_optional

    def SetDataName(self, newName):
        self.m_dataName = newName

    def SetHelp(self, values):
        self.m_help = list(values)

    def SetName(self, newName):
        self.m_name = newName

    def SetOptional(self, opt):
        self.m_optional = opt