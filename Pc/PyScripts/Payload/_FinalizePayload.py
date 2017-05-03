# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _FinalizePayload.py
import dsz
import pc.payload.settings
import sys

def main():
    if len(sys.argv) != 2:
        dsz.ui.Echo('Usage: %s <payloadFile>' % sys.argv[0], dsz.ERROR)
        return False
    return pc.payload.settings.Finalize(sys.argv[1])


if __name__ == '__main__':
    if main() != True:
        sys.exit(-1)