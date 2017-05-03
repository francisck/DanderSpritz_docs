# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _Upgrade.py
import dsz
import dsz.lp
import dsz.menu
import dsz.user
import datetime
import socket
import sys
import xml.dom.minidom
OldName = 'oldname'
Driver = 'driver'
Method = 'method'

def main():
    dsz.control.echo.Off()
    cmdParams = dsz.lp.cmdline.ParseCommandLine(sys.argv, '_DmGz.txt')
    if len(cmdParams) == 0:
        return False
    if Method in cmdParams:
        method = '-method %s' % cmdParams[Method][0]
    else:
        method = ''
    if Driver in cmdParams:
        driver = '-driver %s' % cmdParams[Driver][0]
    else:
        driver = ''
    if OldName in cmdParams:
        oldname = '-driver %s' % cmdParams[OldName][0]
    else:
        oldname = ''
    if not dsz.cmd.Run('python Install/_Uninstall.py -args "%s %s"' % (oldname, method)):
        return False
    if not dsz.cmd.Run('python Install/_Install.py -args "%s %s"' % (driver, method)):
        return False
    return True


if __name__ == '__main__':
    if main() != True:
        sys.exit(-1)