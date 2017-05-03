# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: frzaddress.py
from dsz.menu.input.values.value import Value
import re

class FrzAddressValue(Value):

    def CheckAddress(value, valueObject):
        try:
            m = re.match('z(\\d+)\\.(\\d+)\\.(\\d+)\\.(\\d+)$', value)
            if m == None:
                return False
            val1 = int(m.group(1))
            val2 = int(m.group(2))
            val3 = int(m.group(3))
            val4 = int(m.group(4))
            if val1 < 0 or val1 > 255 or val2 < 0 or val2 > 255 or val3 < 0 or val3 > 255 or val4 < 0 or val4 > 255:
                return False
            if not valueObject.allowInvalid and val1 == 0 and val2 == 0 and val3 == 0 and val4 == 0:
                return False
            valueObject.intValue = val1 << 24 | val2 << 16 | val3 << 8 | val4
        except:
            return False

        return True

    CheckAddress = staticmethod(CheckAddress)

    def __init__(self, name, value=None, comment='', allowInvalid=False):
        if value != None and not isinstance(value, str):
            raise RuntimeError("Initial value not of type 'str'")
        self.allowInvalid = allowInvalid
        self.intValue = None
        Value.__init__(self, name, 'FrzAddressValue', value, comment, FrzAddressValue.CheckAddress, self)
        return