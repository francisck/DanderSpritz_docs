# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import re
from datetime import datetime

def OutputBool(value, description, storageName, recordData=False, strFieldLen=35):
    fmt = '%%%ds : %%s' % strFieldLen
    dsz.ui.Echo(fmt % (description, value))
    if recordData:
        dsz.script.data.Add(storageName, '%s' % value, dsz.TYPE_BOOL)
    return '%s' % value


def OutputDuration(value, valueType, description, storageName, recordData=False, strFieldLen=35):
    fmt = '%%%ds : %%s' % strFieldLen
    days = 0
    hours = 0
    minutes = 0
    seconds = 0
    milliseconds = 0
    if valueType.lower() == 'ms':
        milliseconds = value % 1000
        seconds = value / 1000 % 60
        minutes = value / 1000 / 60 % 60
        hours = value / 1000 / 60 / 60 % 24
        days = value / 1000 / 60 / 60 / 24
    elif valueType.lower() == 's':
        seconds = value % 60
        minutes = value / 60 % 60
        hours = value / 60 / 60 % 24
        days = value / 60 / 60 / 24
    elif valueType.lower() == 'm':
        minutes = value % 60
        hours = value / 60 % 24
        days = value / 60 / 24
    elif valueType.lower() == 'h':
        hours = value % 24
        days = value / 24
    elif valueType.lower() == 'd':
        days = value
    else:
        raise RuntimeError("Invalid type ('%s') for duration" % valueType)
    if days > 0:
        timeStr = '%dd%dh%dm%ds' % (days, hours, minutes, seconds)
        if milliseconds > 0:
            timeStr += '%dms' % milliseconds
    elif hours > 0:
        timeStr = '%dh%dm%ds' % (hours, minutes, seconds)
        if milliseconds > 0:
            timeStr += '%dms' % milliseconds
    elif minutes > 0:
        timeStr = '%dm%ds' % (minutes, seconds)
        if milliseconds > 0:
            timeStr += '%dms' % milliseconds
    elif seconds > 0:
        timeStr = '%ds' % seconds
        if milliseconds > 0:
            timeStr += '%dms' % milliseconds
    elif milliseconds > 0:
        timeStr = '%dms' % milliseconds
    else:
        timeStr = '0%s' % valueType.lower()
    dsz.ui.Echo(fmt % (description, timeStr))
    if recordData:
        dsz.script.data.Add(storageName, '%s' % timeStr, dsz.TYPE_STRING)
    return '%s' % timeStr


def OutputFrzAddr(addr, description, storageName, recordData=False, strFieldLen=35):
    if not isinstance(addr, str):
        addr = 'z%d.%d.%d.%d' % (addr >> 24 & 255, addr >> 16 & 255, addr >> 8 & 255, addr & 255)
    fmt = '%%%ds : %%s' % strFieldLen
    dsz.ui.Echo(fmt % (description, addr))
    if recordData:
        dsz.script.data.Add(storageName, '%s' % addr, dsz.TYPE_STRING)
    return '%s' % addr


def OutputInt(value, description, storageName, recordData=False, strFieldLen=35, valueFmt='%d'):
    fmt = '%%%ds : %s' % (strFieldLen, valueFmt)
    dsz.ui.Echo(fmt % (description, value))
    if recordData:
        dsz.script.data.Add(storageName, valueFmt % value, dsz.TYPE_INT)
    return valueFmt % value


def OutputSbzUuid(value, description, storageName, recordData=False, strFieldLen=35):
    fmt = '%%%ds : %%s' % strFieldLen
    sections = re.split('-', value)
    if sections != None and len(sections) == 5:
        uuid = '%s-%s-%s-%s%s' % (sections[0], sections[1], sections[2], sections[3], sections[4])
    else:
        uuid = value
    dsz.ui.Echo(fmt % (description, uuid))
    if recordData:
        dsz.script.data.Add(storageName, '%s' % uuid, dsz.TYPE_STRING)
    return '%s' % uuid


def OutputString(value, description, storageName, recordData=False, strFieldLen=35):
    fmt = '%%%ds : %%s' % strFieldLen
    dsz.ui.Echo(fmt % (description, value))
    if recordData:
        dsz.script.data.Add(storageName, '%s' % value, dsz.TYPE_STRING)
    return '%s' % value


def OutputTimestamp(ts, description, storageName, recordData=False, strFieldLen=35, milliseconds=None):
    if milliseconds != None:
        fmt = '%%%ds : %%s (%%s ms)' % strFieldLen
    else:
        fmt = '%%%ds : %%s' % strFieldLen
    try:
        t = datetime.fromtimestamp(ts)
    except:
        t = None

    if milliseconds != None:
        dsz.ui.Echo(fmt % (description, t, milliseconds))
    else:
        dsz.ui.Echo(fmt % (description, t))
    if recordData:
        dsz.script.data.Add(storageName, '%s' % t, dsz.TYPE_STRING)
        if milliseconds != None:
            dsz.script.data.Add('%sMs' % storageName, '%s' % milliseconds, dsz.TYPE_STRING)
    if milliseconds != None:
        return '%s%sMs' % (t, milliseconds)
    else:
        return '%s' % t
        return