# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz

def GetWellKnownSid(wellknown, addr=dsz.script.Env['target_address']):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    envName = '_WELLKNOWN_SID_%s' % wellknown
    if dsz.env.Check(envName, 0, addr):
        return dsz.env.Get(envName, 0, addr)
    if not dsz.cmd.Run('dst=%s sidlookup -wellknown "%s"' % (addr, wellknown), dsz.RUN_FLAG_RECORD):
        return wellknown
    try:
        name = dsz.cmd.data.Get('Sid::Name', dsz.TYPE_STRING)
        try:
            dsz.env.Set(envName, name[0], 0, addr)
        except:
            pass

        return name[0]
    except:
        return wellknown


def GetUserSid(sid, local=False, addr=dsz.script.Env['target_address']):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    envName = '_USER_SID_%s' % sid
    if dsz.env.Check(envName, 0, addr):
        return dsz.env.Get(envName, 0, addr)
    if not dsz.cmd.Run('dst=%s sidlookup -user -name "%s"' % (addr, sid), dsz.RUN_FLAG_RECORD):
        return sid
    try:
        name = dsz.cmd.data.Get('Sid::Name', dsz.TYPE_STRING)
        try:
            dsz.env.Set(envName, name[0], 0, addr)
        except:
            pass

        return name[0]
    except:
        return sid