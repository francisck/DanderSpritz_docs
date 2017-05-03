# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: time.py
from dsz.menu.input.values.value import Value
import re
from datetime import datetime

class DateTimeValue(Value):

    def CheckDateTime(value, valueObject):
        try:
            valueObject.dateTimeValue = DateTimeValue.StringToDateTime(value)
            if valueObject.dateTimeValue == None:
                return False
            if valueObject.minDateTime != None or valueObject.maxDateTime != None:
                if valueObject.minDateTime != None and valueObject.dateTimeValue < valueObject.minDateTime.dateTimeValue:
                    return False
                if valueObject.maxDateTime != None and valueObject.dateTimeValue > valueObject.maxDateTime.dateTimeValue:
                    return False
            return True
        except:
            return False

        return

    CheckDateTime = staticmethod(CheckDateTime)

    def StringToDateTime(value):
        if isinstance(value, datetime):
            return value
        else:
            try:
                m = re.match('(\\d{4})-(\\d{1,2})-(\\d{1,2})(?: (\\d{1,2})\\:(\\d{1,2})\\:(\\d{1,2}))?$', value)
                if m == None:
                    return
                year = int(m.group(1) if m.group(1) != None else 0)
                month = int(m.group(2) if m.group(2) != None else 0)
                day = int(m.group(3) if m.group(3) != None else 0)
                hour = int(m.group(4) if m.group(4) != None else 0)
                minute = int(m.group(5) if m.group(5) != None else 0)
                second = int(m.group(6) if m.group(6) != None else 0)
                micro = 0
                return datetime(year, month, day, hour, minute, second, micro)
            except:
                raise
                return

            return

    StringToDateTime = staticmethod(StringToDateTime)

    def __init__(self, name, value=None, comment='', minDateTime=None, maxDateTime=None):
        if value != None and not isinstance(value, str):
            raise RuntimeError("Initial value not of type 'str'")
        if minDateTime != None:
            self.minDateTime = DateTimeValue('minDateTime', minDateTime, minDateTime=None, maxDateTime=None)
        else:
            self.minDateTime = None
        if maxDateTime != None:
            self.maxDateTime = DateTimeValue('maxDateTime', maxDateTime, minDateTime=None, maxDateTime=None)
        else:
            self.maxDateTime = None
        self.year = 0
        self.month = 0
        self.day = 0
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.dateTimeValue = None
        Value.__init__(self, name, 'DateTimeValue', value, comment, DateTimeValue.CheckDateTime, self)
        return

    def GetRange(self):
        rangeStr = ''
        if self.minDateTime != None:
            rangeStr += 'minDateTime=%d' % self.minDateTime
        if self.maxDateTime != None:
            if len(rangeStr) > 0:
                rangeStr += ' '
            rangeStr += 'maxDateTime=%d' % self.maxDateTime
        return rangeStr

    def SetTimeInSeconds(self, s):
        self.dateTimeValue = datetime.fromtimestamp(s)
        self.value = '%s' % self.dateTimeValue
        DateTimeValue.CheckDateTime(self.dateTimeValue, self)

    def GetTimeInSeconds(self):
        diff = self.dateTimeValue - datetime.fromtimestamp(0)
        totalSeconds = diff.days * 3600 * 24 + diff.seconds
        return totalSeconds