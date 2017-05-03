# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: ascii.py
"""Constants and membership tests for ASCII characters"""
NUL = 0
SOH = 1
STX = 2
ETX = 3
EOT = 4
ENQ = 5
ACK = 6
BEL = 7
BS = 8
TAB = 9
HT = 9
LF = 10
NL = 10
VT = 11
FF = 12
CR = 13
SO = 14
SI = 15
DLE = 16
DC1 = 17
DC2 = 18
DC3 = 19
DC4 = 20
NAK = 21
SYN = 22
ETB = 23
CAN = 24
EM = 25
SUB = 26
ESC = 27
FS = 28
GS = 29
RS = 30
US = 31
SP = 32
DEL = 127
controlnames = [
 'NUL', 'SOH', 'STX', 'ETX', 'EOT', 'ENQ', 'ACK', 'BEL',
 'BS', 'HT', 'LF', 'VT', 'FF', 'CR', 'SO', 'SI',
 'DLE', 'DC1', 'DC2', 'DC3', 'DC4', 'NAK', 'SYN', 'ETB',
 'CAN', 'EM', 'SUB', 'ESC', 'FS', 'GS', 'RS', 'US',
 'SP']

def _ctoi(c):
    if type(c) == type(''):
        return ord(c)
    else:
        return c


def isalnum(c):
    return isalpha(c) or isdigit(c)


def isalpha(c):
    return isupper(c) or islower(c)


def isascii(c):
    return _ctoi(c) <= 127


def isblank(c):
    return _ctoi(c) in (8, 32)


def iscntrl(c):
    return _ctoi(c) <= 31


def isdigit(c):
    return _ctoi(c) >= 48 and _ctoi(c) <= 57


def isgraph(c):
    return _ctoi(c) >= 33 and _ctoi(c) <= 126


def islower(c):
    return _ctoi(c) >= 97 and _ctoi(c) <= 122


def isprint(c):
    return _ctoi(c) >= 32 and _ctoi(c) <= 126


def ispunct(c):
    return _ctoi(c) != 32 and not isalnum(c)


def isspace(c):
    return _ctoi(c) in (9, 10, 11, 12, 13, 32)


def isupper(c):
    return _ctoi(c) >= 65 and _ctoi(c) <= 90


def isxdigit(c):
    return isdigit(c) or _ctoi(c) >= 65 and _ctoi(c) <= 70 or _ctoi(c) >= 97 and _ctoi(c) <= 102


def isctrl(c):
    return _ctoi(c) < 32


def ismeta(c):
    return _ctoi(c) > 127


def ascii(c):
    if type(c) == type(''):
        return chr(_ctoi(c) & 127)
    else:
        return _ctoi(c) & 127


def ctrl(c):
    if type(c) == type(''):
        return chr(_ctoi(c) & 31)
    else:
        return _ctoi(c) & 31


def alt(c):
    if type(c) == type(''):
        return chr(_ctoi(c) | 128)
    else:
        return _ctoi(c) | 128


def unctrl(c):
    bits = _ctoi(c)
    if bits == 127:
        rep = '^?'
    elif isprint(bits & 127):
        rep = chr(bits & 127)
    else:
        rep = '^' + chr((bits & 127 | 32) + 32)
    if bits & 128:
        return '!' + rep
    return rep