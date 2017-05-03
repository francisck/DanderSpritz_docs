# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: duration.py
from dsz.menu.input.values.value import Value
import re

class DurationValue(Value):

    def CheckDuration(value, valueObject):
        try:
            duration = DurationValue.ConvertStringToDuration(value)
            if duration == None:
                return False
            if valueObject.minDuration != None or valueObject.maxDuration != None:
                if valueObject.minDuration != None:
                    if duration['totalSeconds'] < valueObject.minDuration.totalSeconds:
                        return False
                    if duration['totalSeconds'] == valueObject.minDuration.totalSeconds:
                        if duration['milliseconds'] < valueObject.minDuration.milliseconds:
                            return False
                if valueObject.maxDuration != None:
                    if duration['totalSeconds'] > valueObject.maxDuration.totalSeconds:
                        return False
                    if duration['totalSeconds'] == valueObject.maxDuration.totalSeconds:
                        if duration['milliseconds'] > valueObject.maxDuration.milliseconds:
                            return False
            valueObject.days = duration['days']
            valueObject.hours = duration['hours']
            valueObject.minutes = duration['minutes']
            valueObject.seconds = duration['seconds']
            valueObject.milliseconds = duration['milliseconds']
            valueObject.totalSeconds = duration['totalSeconds']
            return True
        except:
            return False

        return

    CheckDuration = staticmethod(CheckDuration)

    def ConvertStringToDuration(value):
        try:
            if len(value) == 0:
                return
            m = re.match('(\\d+d)?(\\d+h)?(\\d+m(?!s))?(\\d+s)?(\\d+ms)?$', value)
            if m == None:
                return
            duration = {}
            duration['days'] = 0
            duration['hours'] = 0
            duration['minutes'] = 0
            duration['seconds'] = 0
            duration['milliseconds'] = 0
            duration['totalSeconds'] = 0
            i = 1
            while i <= 5:
                val = m.group(i)
                if val == None:
                    pass
                elif val.endswith('ms'):
                    duration['milliseconds'] = int(val.rstrip('ms'))
                elif val.endswith('d'):
                    duration['days'] = int(val.rstrip('d'))
                elif val.endswith('h'):
                    duration['hours'] = int(val.rstrip('h'))
                elif val.endswith('m'):
                    duration['minutes'] = int(val.rstrip('m'))
                elif val.endswith('s'):
                    duration['seconds'] = int(val.rstrip('s'))
                else:
                    return
                i = i + 1

            if duration['hours'] > 23:
                return
            if duration['minutes'] > 59:
                return
            if duration['seconds'] > 59:
                return
            if duration['milliseconds'] > 999:
                return
            duration['totalSeconds'] = duration['days'] * 24 * 60 * 60 + duration['hours'] * 60 * 60 + duration['minutes'] * 60 + duration['seconds']
            return duration
        except:
            return

        return

    ConvertStringToDuration = staticmethod(ConvertStringToDuration)

    def __init__(self, name, value=None, comment='', minDuration=None, maxDuration=None):
        if value != None and not isinstance(value, str):
            raise RuntimeError("Initial value not of type 'str'")
        if minDuration != None:
            self.minDuration = DurationValue('minDuration', minDuration)
        else:
            self.minDuration = None
        if maxDuration != None:
            self.maxDuration = DurationValue('maxDuration', maxDuration)
        else:
            self.maxDuration = None
        self.days = 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0
        self.totalSeconds = 0
        Value.__init__(self, name, 'DurationValue', value, comment, DurationValue.CheckDuration, self)
        return

    def GetRange(self):
        rangeStr = ''
        if self.minDuration != None:
            rangeStr += 'minDuration=%s' % self.minDuration.value
        if self.maxDuration != None:
            if len(rangeStr) > 0:
                rangeStr += ' '
            rangeStr += 'maxDuration=%s' % self.maxDuration.value
        return rangeStr

    def SetTotalSeconds(self, input):
        input = int(input)
        if int(input) < 0:
            raise RuntimeError('Time cannot be below zero')
        self.totalSeconds = input
        s = input % 60
        input = input / 60
        m = input % 60
        input = input / 60
        h = input % 24
        input = input / 24
        d = input
        self.seconds = s
        self.minutes = m
        self.hours = h
        self.days = d
        if self.days > 0:
            self.value = '%sd%sh%sm%ss' % (self.days, self.hours, self.minutes, self.seconds)
        elif self.hours > 0:
            self.value = '%sh%sm%ss' % (self.hours, self.minutes, self.seconds)
        elif self.minutes > 0:
            self.value = '%sm%ss' % (self.minutes, self.seconds)
        else:
            self.value = '%ss' % self.seconds