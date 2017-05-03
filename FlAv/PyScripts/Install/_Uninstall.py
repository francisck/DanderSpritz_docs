# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _Uninstall.py
import dsz
import dsz.lp
import dsz.menu
import dsz.user
import datetime
import socket
import sys
import xml.dom.minidom
Driver = 'driver'
Method = 'method'

def main():
    dsz.control.echo.Off()
    cmdParams = dsz.lp.cmdline.ParseCommandLine(sys.argv, '_FlAv.txt')
    if len(cmdParams) == 0:
        return False
    if Method in cmdParams:
        method = '-method %s' % cmdParams[Method][0]
    else:
        method = ''
    if not dsz.cmd.Run('python _FlAv.py -args "-action uninstall -quiet %s"' % method):
        return False
    return True


if __name__ == '__main__':
    if main() != True:
        sys.exit(-1)