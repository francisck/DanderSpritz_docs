# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: settings.py.override
import dsz

def CheckConfigLocal():
    if dsz.ui.Prompt('Do you want to configure with FC?', True):
        return False
    else:
        return True


def Finalize(payloadFile):
    return dsz.cmd.Run('python Payload/_Prep.py -args "-action disable -file %s"' % payloadFile)