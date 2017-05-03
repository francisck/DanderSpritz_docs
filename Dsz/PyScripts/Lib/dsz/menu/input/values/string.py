# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: string.py
from dsz.menu.input.values.value import Value

class StringValue(Value):

    def CheckLength(value, valueObject):
        if valueObject.minLen != None:
            if len(value) < valueObject.minLen:
                return False
        if valueObject.maxLen != None:
            if len(value) > valueObject.maxLen:
                return False
        return True

    CheckLength = staticmethod(CheckLength)

    def __init__(self, name, value=None, comment='', minLen=None, maxLen=None):
        if value != None and not isinstance(value, str):
            raise RuntimeError("Initial value not of type 'str'")
        self.minLen = minLen
        self.maxLen = maxLen
        Value.__init__(self, name, 'StringValue', value, comment, StringValue.CheckLength, self)
        return