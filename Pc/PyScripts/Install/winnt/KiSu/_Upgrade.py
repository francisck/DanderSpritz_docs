# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _Upgrade.py
import dsz
import dsz.lp
dsz.lp.AddResDirToPath('DeMi')
import demi
import demi.windows.module
import glob
import os
import re
import shutil
import sys

def main():
    dsz.control.echo.Off()
    localFile = sys.argv[1]
    procName = sys.argv[2]
    upgradedFromNewer = demi.windows.module.Upgrade('Pc', localFile, 'wshtcpip', demi.registry.PC.Id, ask=False)
    if not upgradedFromNewer:
        dsz.ui.Echo('    NOT FOUND, Must retry with older name...', dsz.GOOD)
    return upgradedFromNewer or demi.windows.module.Upgrade('Pc', localFile, 'PC', demi.registry.PC.Id, ask=False)


if __name__ == '__main__':
    if main() != True:
        sys.exit(-1)