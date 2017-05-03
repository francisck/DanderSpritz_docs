# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz

def GetValue(hive, key, name, target='', extraOptions=''):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    cmd = 'registryquery -hive %s -key "%s" -value "%s" %s' % (hive, key, name, extraOptions)
    if len(target) > 0:
        newCmd = '%s -target "%s"' % (cmd, target)
        cmd = newCmd
    if not dsz.cmd.Run(cmd, dsz.RUN_FLAG_RECORD):
        raise RuntimeError, 'Registry query failed'
    value = dsz.cmd.data.Get('key::value::value', dsz.TYPE_STRING)
    type = dsz.cmd.data.Get('key::value::type', dsz.TYPE_STRING)
    if type[0] == 'REG_MULTI_SZ':
        value = _parseMultistring(value[0])
    return value


def SetValue(hive, key, name, data, type, target=''):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    cmd = 'registryadd -hive %s -key "%s" -value "%s" -data "%s" -type %s' % (hive, key, name, data, type)
    if len(target) > 0:
        newCmd = '%s -target "%s"' % (cmd, target)
        cmd = newCmd
    if not dsz.cmd.Run(cmd):
        raise RuntimeError, 'Registry set failed'


def _hexToChar(hex):
    val = int(hex, 16)
    if val == 32:
        return ' '
    else:
        if val == 33:
            return '!'
        if val == 34:
            return '"'
        if val == 35:
            return '#'
        if val == 36:
            return '$'
        if val == 37:
            return '%'
        if val == 38:
            return '&'
        if val == 39:
            return "'"
        if val == 40:
            return '('
        if val == 41:
            return ')'
        if val == 42:
            return '*'
        if val == 43:
            return '+'
        if val == 44:
            return ','
        if val == 45:
            return '-'
        if val == 46:
            return '.'
        if val == 47:
            return '/'
        if val == 48:
            return '0'
        if val == 49:
            return '1'
        if val == 50:
            return '2'
        if val == 51:
            return '3'
        if val == 52:
            return '4'
        if val == 53:
            return '5'
        if val == 54:
            return '6'
        if val == 55:
            return '7'
        if val == 56:
            return '8'
        if val == 57:
            return '9'
        if val == 58:
            return ':'
        if val == 59:
            return ';'
        if val == 60:
            return '<'
        if val == 61:
            return '='
        if val == 62:
            return '>'
        if val == 63:
            return '?'
        if val == 64:
            return '\\@'
        if val == 65:
            return 'A'
        if val == 66:
            return 'B'
        if val == 67:
            return 'C'
        if val == 68:
            return 'D'
        if val == 69:
            return 'E'
        if val == 70:
            return 'F'
        if val == 71:
            return 'G'
        if val == 72:
            return 'H'
        if val == 73:
            return 'I'
        if val == 74:
            return 'J'
        if val == 75:
            return 'K'
        if val == 76:
            return 'L'
        if val == 77:
            return 'M'
        if val == 78:
            return 'N'
        if val == 79:
            return 'O'
        if val == 80:
            return 'P'
        if val == 81:
            return 'Q'
        if val == 82:
            return 'R'
        if val == 83:
            return 'S'
        if val == 84:
            return 'T'
        if val == 85:
            return 'U'
        if val == 86:
            return 'V'
        if val == 87:
            return 'W'
        if val == 88:
            return 'X'
        if val == 89:
            return 'Y'
        if val == 90:
            return 'Z'
        if val == 91:
            return '['
        if val == 92:
            return '\\'
        if val == 93:
            return ']'
        if val == 94:
            return '^'
        if val == 95:
            return '_'
        if val == 96:
            return '`'
        if val == 97:
            return 'a'
        if val == 98:
            return 'b'
        if val == 99:
            return 'c'
        if val == 100:
            return 'd'
        if val == 101:
            return 'e'
        if val == 102:
            return 'f'
        if val == 103:
            return 'g'
        if val == 104:
            return 'h'
        if val == 105:
            return 'i'
        if val == 106:
            return 'j'
        if val == 107:
            return 'k'
        if val == 108:
            return 'l'
        if val == 109:
            return 'm'
        if val == 110:
            return 'n'
        if val == 111:
            return 'o'
        if val == 112:
            return 'p'
        if val == 113:
            return 'q'
        if val == 114:
            return 'r'
        if val == 115:
            return 's'
        if val == 116:
            return 't'
        if val == 117:
            return 'u'
        if val == 118:
            return 'v'
        if val == 119:
            return 'w'
        if val == 120:
            return 'x'
        if val == 121:
            return 'y'
        if val == 122:
            return 'z'
        if val == 123:
            return '{'
        if val == 124:
            return '|'
        if val == 125:
            return '}'
        if val == 126:
            return '~'
        return '?'


def _parseMultistring(value):
    index = 0
    interest = 4
    nulls = 0
    empties = 0
    values = list()
    while len(value) > 0:
        first = value[0:4]
        value = value[4:]
        number = first[0:2]
        null = first[2:]
        suffix = ''
        if null == '00':
            if number == '00':
                if nulls == 0:
                    empties = empties + 1
            else:
                nulls = 0
                suffix = _hexToChar(number)
        else:
            raise RuntimeError, 'Invalid characters for conversion'
        if len(suffix) > 0:
            while empties > 0:
                empties = empties - 1
                index = index + 1
                values.append('')

            if len(values) >= index + 1:
                values[index] = values[index] + suffix
            else:
                values.append(suffix)

    return values