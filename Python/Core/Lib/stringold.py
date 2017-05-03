# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: stringold.py
"""Common string manipulations.

Public module variables:

whitespace -- a string containing all characters considered whitespace
lowercase -- a string containing all characters considered lowercase letters
uppercase -- a string containing all characters considered uppercase letters
letters -- a string containing all characters considered letters
digits -- a string containing all characters considered decimal digits
hexdigits -- a string containing all characters considered hexadecimal digits
octdigits -- a string containing all characters considered octal digits

"""
from warnings import warnpy3k
warnpy3k('the stringold module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
whitespace = ' \t\n\r\x0b\x0c'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = lowercase + uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
_idmap = ''
for i in range(256):
    _idmap = _idmap + chr(i)

del i
index_error = ValueError
atoi_error = ValueError
atof_error = ValueError
atol_error = ValueError

def lower(s):
    """lower(s) -> string
    
    Return a copy of the string s converted to lowercase.
    
    """
    return s.lower()


def upper(s):
    """upper(s) -> string
    
    Return a copy of the string s converted to uppercase.
    
    """
    return s.upper()


def swapcase(s):
    """swapcase(s) -> string
    
    Return a copy of the string s with upper case characters
    converted to lowercase and vice versa.
    
    """
    return s.swapcase()


def strip(s):
    """strip(s) -> string
    
    Return a copy of the string s with leading and trailing
    whitespace removed.
    
    """
    return s.strip()


def lstrip(s):
    """lstrip(s) -> string
    
    Return a copy of the string s with leading whitespace removed.
    
    """
    return s.lstrip()


def rstrip(s):
    """rstrip(s) -> string
    
    Return a copy of the string s with trailing whitespace
    removed.
    
    """
    return s.rstrip()


def split(s, sep=None, maxsplit=0):
    """split(str [,sep [,maxsplit]]) -> list of strings
    
    Return a list of the words in the string s, using sep as the
    delimiter string.  If maxsplit is nonzero, splits into at most
    maxsplit words If sep is not specified, any whitespace string
    is a separator.  Maxsplit defaults to 0.
    
    (split and splitfields are synonymous)
    
    """
    return s.split(sep, maxsplit)


splitfields = split

def join(words, sep=' '):
    """join(list [,sep]) -> string
    
    Return a string composed of the words in list, with
    intervening occurrences of sep.  The default separator is a
    single space.
    
    (joinfields and join are synonymous)
    
    """
    return sep.join(words)


joinfields = join
_apply = apply

def index(s, *args):
    """index(s, sub [,start [,end]]) -> int
    
    Like find but raises ValueError when the substring is not found.
    
    """
    return _apply(s.index, args)


def rindex(s, *args):
    """rindex(s, sub [,start [,end]]) -> int
    
    Like rfind but raises ValueError when the substring is not found.
    
    """
    return _apply(s.rindex, args)


def count(s, *args):
    """count(s, sub[, start[,end]]) -> int
    
    Return the number of occurrences of substring sub in string
    s[start:end].  Optional arguments start and end are
    interpreted as in slice notation.
    
    """
    return _apply(s.count, args)


def find(s, *args):
    """find(s, sub [,start [,end]]) -> in
    
    Return the lowest index in s where substring sub is found,
    such that sub is contained within s[start,end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Return -1 on failure.
    
    """
    return _apply(s.find, args)


def rfind(s, *args):
    """rfind(s, sub [,start [,end]]) -> int
    
    Return the highest index in s where substring sub is found,
    such that sub is contained within s[start,end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Return -1 on failure.
    
    """
    return _apply(s.rfind, args)


_float = float
_int = int
_long = long
_StringType = type('')

def atof(s):
    """atof(s) -> float
    
    Return the floating point number represented by the string s.
    
    """
    if type(s) == _StringType:
        return _float(s)
    raise TypeError('argument 1: expected string, %s found' % type(s).__name__)


def atoi(*args):
    """atoi(s [,base]) -> int
    
    Return the integer represented by the string s in the given
    base, which defaults to 10.  The string s must consist of one
    or more digits, possibly preceded by a sign.  If base is 0, it
    is chosen from the leading characters of s, 0 for octal, 0x or
    0X for hexadecimal.  If base is 16, a preceding 0x or 0X is
    accepted.
    
    """
    try:
        s = args[0]
    except IndexError:
        raise TypeError('function requires at least 1 argument: %d given' % len(args))

    if type(s) == _StringType:
        return _apply(_int, args)
    raise TypeError('argument 1: expected string, %s found' % type(s).__name__)


def atol(*args):
    """atol(s [,base]) -> long
    
    Return the long integer represented by the string s in the
    given base, which defaults to 10.  The string s must consist
    of one or more digits, possibly preceded by a sign.  If base
    is 0, it is chosen from the leading characters of s, 0 for
    octal, 0x or 0X for hexadecimal.  If base is 16, a preceding
    0x or 0X is accepted.  A trailing L or l is not accepted,
    unless base is 0.
    
    """
    try:
        s = args[0]
    except IndexError:
        raise TypeError('function requires at least 1 argument: %d given' % len(args))

    if type(s) == _StringType:
        return _apply(_long, args)
    raise TypeError('argument 1: expected string, %s found' % type(s).__name__)


def ljust(s, width):
    """ljust(s, width) -> string
    
    Return a left-justified version of s, in a field of the
    specified width, padded with spaces as needed.  The string is
    never truncated.
    
    """
    n = width - len(s)
    if n <= 0:
        return s
    return s + ' ' * n


def rjust(s, width):
    """rjust(s, width) -> string
    
    Return a right-justified version of s, in a field of the
    specified width, padded with spaces as needed.  The string is
    never truncated.
    
    """
    n = width - len(s)
    if n <= 0:
        return s
    return ' ' * n + s


def center(s, width):
    """center(s, width) -> string
    
    Return a center version of s, in a field of the specified
    width. padded with spaces as needed.  The string is never
    truncated.
    
    """
    n = width - len(s)
    if n <= 0:
        return s
    half = n / 2
    if n % 2 and width % 2:
        half = half + 1
    return ' ' * half + s + ' ' * (n - half)


def zfill(x, width):
    """zfill(x, width) -> string
    
    Pad a numeric string x with zeros on the left, to fill a field
    of the specified width.  The string x is never truncated.
    
    """
    if type(x) == type(''):
        s = x
    else:
        s = repr(x)
    n = len(s)
    if n >= width:
        return s
    sign = ''
    if s[0] in ('-', '+'):
        sign, s = s[0], s[1:]
    return sign + '0' * (width - n) + s


def expandtabs(s, tabsize=8):
    """expandtabs(s [,tabsize]) -> string
    
    Return a copy of the string s with all tab characters replaced
    by the appropriate number of spaces, depending on the current
    column, and the tabsize (default 8).
    
    """
    res = line = ''
    for c in s:
        if c == '\t':
            c = ' ' * (tabsize - len(line) % tabsize)
        line = line + c
        if c == '\n':
            res = res + line
            line = ''

    return res + line


def translate(s, table, deletions=''):
    """translate(s,table [,deletechars]) -> string
    
    Return a copy of the string s, where all characters occurring
    in the optional argument deletechars are removed, and the
    remaining characters have been mapped through the given
    translation table, which must be a string of length 256.
    
    """
    return s.translate(table, deletions)


def capitalize(s):
    """capitalize(s) -> string
    
    Return a copy of the string s with only its first character
    capitalized.
    
    """
    return s.capitalize()


def capwords(s, sep=None):
    """capwords(s, [sep]) -> string
    
    Split the argument into words using split, capitalize each
    word using capitalize, and join the capitalized words using
    join. Note that this replaces runs of whitespace characters by
    a single space.
    
    """
    return join(map(capitalize, s.split(sep)), sep or ' ')


_idmapL = None

def maketrans(fromstr, tostr):
    """maketrans(frm, to) -> string
    
    Return a translation table (a string of 256 bytes long)
    suitable for use in string.translate.  The strings frm and to
    must be of the same length.
    
    """
    global _idmapL
    if len(fromstr) != len(tostr):
        raise ValueError, 'maketrans arguments must have same length'
    if not _idmapL:
        _idmapL = list(_idmap)
    L = _idmapL[:]
    fromstr = map(ord, fromstr)
    for i in range(len(fromstr)):
        L[fromstr[i]] = tostr[i]

    return join(L, '')


def replace(s, old, new, maxsplit=0):
    """replace (str, old, new[, maxsplit]) -> string
    
    Return a copy of string str with all occurrences of substring
    old replaced by new. If the optional argument maxsplit is
    given, only the first maxsplit occurrences are replaced.
    
    """
    return s.replace(old, new, maxsplit)


try:
    ''.upper
except AttributeError:
    from stringold import *

try:
    from strop import maketrans, lowercase, uppercase, whitespace
    letters = lowercase + uppercase
except ImportError:
    pass