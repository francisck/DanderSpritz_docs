# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.process.windows

def _getProcessInfo(id, dataName):
    idStr = ''
    if id != 0:
        idStr = '-id %s' % id
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if not dsz.cmd.Run('processinfo %s' % idStr, dsz.RUN_FLAG_RECORD):
        raise RuntimeError, 'Command failed'
    info = dsz.cmd.data.Get(dataName, dsz.TYPE_STRING)
    return info[0]


def CheckForIds(ids):
    pList = dsz.process.GetList()
    numFound = 0
    for process in pList:
        for id in ids:
            if id == process[0]:
                numFound = numFound + 1
                break

        if numFound >= len(ids):
            break

    return numFound >= len(ids)


def FindByName(name):
    pList = dsz.process.GetList()
    isWindows = dsz.version.checks.IsWindows()
    found = list()
    for process in pList:
        if isWindows:
            if name.lower() == process[1].lower():
                found.append(process[0])
        elif name == process[1]:
            found.append(process[0])

    return found


def GetGroup(id=0):
    return _getProcessInfo(id, 'ProcessInfo::BasicInfo::PrimaryGroup::Name')


def GetList():
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if not dsz.cmd.Run('processes -list', dsz.RUN_FLAG_RECORD):
        raise RuntimeError, 'Command failed'
    ids = dsz.cmd.data.Get('InitialProcessListItem::ProcessItem::Id', dsz.TYPE_INT)
    names = dsz.cmd.data.Get('InitialProcessListItem::ProcessItem::Name', dsz.TYPE_STRING)
    rtn = list()
    i = 0
    while i < len(ids):
        rtn.append((ids[i], names[i]))
        i = i + 1

    return rtn


def GetOwner(id=0):
    return _getProcessInfo(id, 'ProcessInfo::BasicInfo::Owner::Name')


def GetUser(id=0):
    return _getProcessInfo(id, 'ProcessInfo::BasicInfo::User::Name')