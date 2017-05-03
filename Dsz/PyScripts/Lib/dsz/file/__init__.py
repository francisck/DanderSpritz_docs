# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz

def Exists(file, path=''):
    if len(path) == 0:
        cmd = 'dir "%s"' % file
    else:
        cmd = 'dir -path "%s/" -mask "%s"' % (path, file)
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if not dsz.cmd.Run(cmd, dsz.RUN_FLAG_RECORD):
        raise RuntimeError, 'Dir command failed'
    try:
        return dsz.cmd.data.Size('DirItem::FileItem') > 0
    except:
        return False


def GetNames(file, path=''):
    if len(path) == 0:
        cmd = 'dir "%s"' % file
    else:
        cmd = 'dir -path "%s/" -mask "%s"' % (path, file)
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if not dsz.cmd.Run(cmd, dsz.RUN_FLAG_RECORD):
        raise RuntimeError, 'Dir command failed'
    try:
        return dsz.cmd.data.Get('DirItem::FileItem::name', dsz.TYPE_STRING)
    except:
        return list()