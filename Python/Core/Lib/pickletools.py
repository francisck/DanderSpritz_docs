# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: pickletools.py
""""Executable documentation" for the pickle module.

Extensive comments about the pickle protocols and pickle-machine opcodes
can be found here.  Some functions meant for external use:

genops(pickle)
   Generate all the opcodes in a pickle, as (opcode, arg, position) triples.

dis(pickle, out=None, memo=None, indentlevel=4)
   Print a symbolic disassembly of a pickle.
"""
__all__ = [
 'dis', 'genops', 'optimize']
UP_TO_NEWLINE = -1
TAKEN_FROM_ARGUMENT1 = -2
TAKEN_FROM_ARGUMENT4 = -3

class ArgumentDescriptor(object):
    __slots__ = ('name', 'n', 'reader', 'doc')

    def __init__(self, name, n, reader, doc):
        self.name = name
        self.n = n
        self.reader = reader
        self.doc = doc


from struct import unpack as _unpack

def read_uint1(f):
    r"""
    >>> import StringIO
    >>> read_uint1(StringIO.StringIO('\xff'))
    255
    """
    data = f.read(1)
    if data:
        return ord(data)
    raise ValueError('not enough data in stream to read uint1')


uint1 = ArgumentDescriptor(name='uint1', n=1, reader=read_uint1, doc='One-byte unsigned integer.')

def read_uint2(f):
    r"""
    >>> import StringIO
    >>> read_uint2(StringIO.StringIO('\xff\x00'))
    255
    >>> read_uint2(StringIO.StringIO('\xff\xff'))
    65535
    """
    data = f.read(2)
    if len(data) == 2:
        return _unpack('<H', data)[0]
    raise ValueError('not enough data in stream to read uint2')


uint2 = ArgumentDescriptor(name='uint2', n=2, reader=read_uint2, doc='Two-byte unsigned integer, little-endian.')

def read_int4(f):
    r"""
    >>> import StringIO
    >>> read_int4(StringIO.StringIO('\xff\x00\x00\x00'))
    255
    >>> read_int4(StringIO.StringIO('\x00\x00\x00\x80')) == -(2**31)
    True
    """
    data = f.read(4)
    if len(data) == 4:
        return _unpack('<i', data)[0]
    raise ValueError('not enough data in stream to read int4')


int4 = ArgumentDescriptor(name='int4', n=4, reader=read_int4, doc="Four-byte signed integer, little-endian, 2's complement.")

def read_stringnl(f, decode=True, stripquotes=True):
    r"""
    >>> import StringIO
    >>> read_stringnl(StringIO.StringIO("'abcd'\nefg\n"))
    'abcd'
    
    >>> read_stringnl(StringIO.StringIO("\n"))
    Traceback (most recent call last):
    ...
    ValueError: no string quotes around ''
    
    >>> read_stringnl(StringIO.StringIO("\n"), stripquotes=False)
    ''
    
    >>> read_stringnl(StringIO.StringIO("''\n"))
    ''
    
    >>> read_stringnl(StringIO.StringIO('"abcd"'))
    Traceback (most recent call last):
    ...
    ValueError: no newline found when trying to read stringnl
    
    Embedded escapes are undone in the result.
    >>> read_stringnl(StringIO.StringIO(r"'a\n\\b\x00c\td'" + "\n'e'"))
    'a\n\\b\x00c\td'
    """
    data = f.readline()
    if not data.endswith('\n'):
        raise ValueError('no newline found when trying to read stringnl')
    data = data[:-1]
    if stripquotes:
        for q in '\'"':
            if data.startswith(q):
                if not data.endswith(q):
                    raise ValueError('strinq quote %r not found at both ends of %r' % (
                     q, data))
                data = data[1:-1]
                break
        else:
            raise ValueError('no string quotes around %r' % data)

    if decode:
        data = data.decode('string_escape')
    return data


stringnl = ArgumentDescriptor(name='stringnl', n=UP_TO_NEWLINE, reader=read_stringnl, doc='A newline-terminated string.\n\n                   This is a repr-style string, with embedded escapes, and\n                   bracketing quotes.\n                   ')

def read_stringnl_noescape(f):
    return read_stringnl(f, decode=False, stripquotes=False)


stringnl_noescape = ArgumentDescriptor(name='stringnl_noescape', n=UP_TO_NEWLINE, reader=read_stringnl_noescape, doc='A newline-terminated string.\n\n                        This is a str-style string, without embedded escapes,\n                        or bracketing quotes.  It should consist solely of\n                        printable ASCII characters.\n                        ')

def read_stringnl_noescape_pair(f):
    r"""
    >>> import StringIO
    >>> read_stringnl_noescape_pair(StringIO.StringIO("Queue\nEmpty\njunk"))
    'Queue Empty'
    """
    return '%s %s' % (read_stringnl_noescape(f), read_stringnl_noescape(f))


stringnl_noescape_pair = ArgumentDescriptor(name='stringnl_noescape_pair', n=UP_TO_NEWLINE, reader=read_stringnl_noescape_pair, doc='A pair of newline-terminated strings.\n\n                             These are str-style strings, without embedded\n                             escapes, or bracketing quotes.  They should\n                             consist solely of printable ASCII characters.\n                             The pair is returned as a single string, with\n                             a single blank separating the two strings.\n                             ')

def read_string4(f):
    r"""
    >>> import StringIO
    >>> read_string4(StringIO.StringIO("\x00\x00\x00\x00abc"))
    ''
    >>> read_string4(StringIO.StringIO("\x03\x00\x00\x00abcdef"))
    'abc'
    >>> read_string4(StringIO.StringIO("\x00\x00\x00\x03abcdef"))
    Traceback (most recent call last):
    ...
    ValueError: expected 50331648 bytes in a string4, but only 6 remain
    """
    n = read_int4(f)
    if n < 0:
        raise ValueError('string4 byte count < 0: %d' % n)
    data = f.read(n)
    if len(data) == n:
        return data
    raise ValueError('expected %d bytes in a string4, but only %d remain' % (
     n, len(data)))


string4 = ArgumentDescriptor(name='string4', n=TAKEN_FROM_ARGUMENT4, reader=read_string4, doc='A counted string.\n\n              The first argument is a 4-byte little-endian signed int giving\n              the number of bytes in the string, and the second argument is\n              that many bytes.\n              ')

def read_string1(f):
    r"""
    >>> import StringIO
    >>> read_string1(StringIO.StringIO("\x00"))
    ''
    >>> read_string1(StringIO.StringIO("\x03abcdef"))
    'abc'
    """
    n = read_uint1(f)
    data = f.read(n)
    if len(data) == n:
        return data
    raise ValueError('expected %d bytes in a string1, but only %d remain' % (
     n, len(data)))


string1 = ArgumentDescriptor(name='string1', n=TAKEN_FROM_ARGUMENT1, reader=read_string1, doc='A counted string.\n\n              The first argument is a 1-byte unsigned int giving the number\n              of bytes in the string, and the second argument is that many\n              bytes.\n              ')

def read_unicodestringnl(f):
    r"""
    >>> import StringIO
    >>> read_unicodestringnl(StringIO.StringIO("abc\uabcd\njunk"))
    u'abc\uabcd'
    """
    data = f.readline()
    if not data.endswith('\n'):
        raise ValueError('no newline found when trying to read unicodestringnl')
    data = data[:-1]
    return unicode(data, 'raw-unicode-escape')


unicodestringnl = ArgumentDescriptor(name='unicodestringnl', n=UP_TO_NEWLINE, reader=read_unicodestringnl, doc='A newline-terminated Unicode string.\n\n                      This is raw-unicode-escape encoded, so consists of\n                      printable ASCII characters, and may contain embedded\n                      escape sequences.\n                      ')

def read_unicodestring4(f):
    r"""
    >>> import StringIO
    >>> s = u'abcd\uabcd'
    >>> enc = s.encode('utf-8')
    >>> enc
    'abcd\xea\xaf\x8d'
    >>> n = chr(len(enc)) + chr(0) * 3  # little-endian 4-byte length
    >>> t = read_unicodestring4(StringIO.StringIO(n + enc + 'junk'))
    >>> s == t
    True
    
    >>> read_unicodestring4(StringIO.StringIO(n + enc[:-1]))
    Traceback (most recent call last):
    ...
    ValueError: expected 7 bytes in a unicodestring4, but only 6 remain
    """
    n = read_int4(f)
    if n < 0:
        raise ValueError('unicodestring4 byte count < 0: %d' % n)
    data = f.read(n)
    if len(data) == n:
        return unicode(data, 'utf-8')
    raise ValueError('expected %d bytes in a unicodestring4, but only %d remain' % (
     n, len(data)))


unicodestring4 = ArgumentDescriptor(name='unicodestring4', n=TAKEN_FROM_ARGUMENT4, reader=read_unicodestring4, doc='A counted Unicode string.\n\n                    The first argument is a 4-byte little-endian signed int\n                    giving the number of bytes in the string, and the second\n                    argument-- the UTF-8 encoding of the Unicode string --\n                    contains that many bytes.\n                    ')

def read_decimalnl_short(f):
    r"""
    >>> import StringIO
    >>> read_decimalnl_short(StringIO.StringIO("1234\n56"))
    1234
    
    >>> read_decimalnl_short(StringIO.StringIO("1234L\n56"))
    Traceback (most recent call last):
    ...
    ValueError: trailing 'L' not allowed in '1234L'
    """
    s = read_stringnl(f, decode=False, stripquotes=False)
    if s.endswith('L'):
        raise ValueError("trailing 'L' not allowed in %r" % s)
    if s == '00':
        return False
    if s == '01':
        return True
    try:
        return int(s)
    except OverflowError:
        return long(s)


def read_decimalnl_long(f):
    r"""
    >>> import StringIO
    
    >>> read_decimalnl_long(StringIO.StringIO("1234\n56"))
    Traceback (most recent call last):
    ...
    ValueError: trailing 'L' required in '1234'
    
    Someday the trailing 'L' will probably go away from this output.
    
    >>> read_decimalnl_long(StringIO.StringIO("1234L\n56"))
    1234L
    
    >>> read_decimalnl_long(StringIO.StringIO("123456789012345678901234L\n6"))
    123456789012345678901234L
    """
    s = read_stringnl(f, decode=False, stripquotes=False)
    if not s.endswith('L'):
        raise ValueError("trailing 'L' required in %r" % s)
    return long(s)


decimalnl_short = ArgumentDescriptor(name='decimalnl_short', n=UP_TO_NEWLINE, reader=read_decimalnl_short, doc="A newline-terminated decimal integer literal.\n\n                          This never has a trailing 'L', and the integer fit\n                          in a short Python int on the box where the pickle\n                          was written -- but there's no guarantee it will fit\n                          in a short Python int on the box where the pickle\n                          is read.\n                          ")
decimalnl_long = ArgumentDescriptor(name='decimalnl_long', n=UP_TO_NEWLINE, reader=read_decimalnl_long, doc="A newline-terminated decimal integer literal.\n\n                         This has a trailing 'L', and can represent integers\n                         of any size.\n                         ")

def read_floatnl(f):
    r"""
    >>> import StringIO
    >>> read_floatnl(StringIO.StringIO("-1.25\n6"))
    -1.25
    """
    s = read_stringnl(f, decode=False, stripquotes=False)
    return float(s)


floatnl = ArgumentDescriptor(name='floatnl', n=UP_TO_NEWLINE, reader=read_floatnl, doc="A newline-terminated decimal floating literal.\n\n              In general this requires 17 significant digits for roundtrip\n              identity, and pickling then unpickling infinities, NaNs, and\n              minus zero doesn't work across boxes, or on some boxes even\n              on itself (e.g., Windows can't read the strings it produces\n              for infinities or NaNs).\n              ")

def read_float8(f):
    r"""
    >>> import StringIO, struct
    >>> raw = struct.pack(">d", -1.25)
    >>> raw
    '\xbf\xf4\x00\x00\x00\x00\x00\x00'
    >>> read_float8(StringIO.StringIO(raw + "\n"))
    -1.25
    """
    data = f.read(8)
    if len(data) == 8:
        return _unpack('>d', data)[0]
    raise ValueError('not enough data in stream to read float8')


float8 = ArgumentDescriptor(name='float8', n=8, reader=read_float8, doc='An 8-byte binary representation of a float, big-endian.\n\n             The format is unique to Python, and shared with the struct\n             module (format string \'>d\') "in theory" (the struct and cPickle\n             implementations don\'t share the code -- they should).  It\'s\n             strongly related to the IEEE-754 double format, and, in normal\n             cases, is in fact identical to the big-endian 754 double format.\n             On other boxes the dynamic range is limited to that of a 754\n             double, and "add a half and chop" rounding is used to reduce\n             the precision to 53 bits.  However, even on a 754 box,\n             infinities, NaNs, and minus zero may not be handled correctly\n             (may not survive roundtrip pickling intact).\n             ')
from pickle import decode_long

def read_long1(f):
    r"""
    >>> import StringIO
    >>> read_long1(StringIO.StringIO("\x00"))
    0L
    >>> read_long1(StringIO.StringIO("\x02\xff\x00"))
    255L
    >>> read_long1(StringIO.StringIO("\x02\xff\x7f"))
    32767L
    >>> read_long1(StringIO.StringIO("\x02\x00\xff"))
    -256L
    >>> read_long1(StringIO.StringIO("\x02\x00\x80"))
    -32768L
    """
    n = read_uint1(f)
    data = f.read(n)
    if len(data) != n:
        raise ValueError('not enough data in stream to read long1')
    return decode_long(data)


long1 = ArgumentDescriptor(name='long1', n=TAKEN_FROM_ARGUMENT1, reader=read_long1, doc="A binary long, little-endian, using 1-byte size.\n\n    This first reads one byte as an unsigned size, then reads that\n    many bytes and interprets them as a little-endian 2's-complement long.\n    If the size is 0, that's taken as a shortcut for the long 0L.\n    ")

def read_long4(f):
    r"""
    >>> import StringIO
    >>> read_long4(StringIO.StringIO("\x02\x00\x00\x00\xff\x00"))
    255L
    >>> read_long4(StringIO.StringIO("\x02\x00\x00\x00\xff\x7f"))
    32767L
    >>> read_long4(StringIO.StringIO("\x02\x00\x00\x00\x00\xff"))
    -256L
    >>> read_long4(StringIO.StringIO("\x02\x00\x00\x00\x00\x80"))
    -32768L
    >>> read_long1(StringIO.StringIO("\x00\x00\x00\x00"))
    0L
    """
    n = read_int4(f)
    if n < 0:
        raise ValueError('long4 byte count < 0: %d' % n)
    data = f.read(n)
    if len(data) != n:
        raise ValueError('not enough data in stream to read long4')
    return decode_long(data)


long4 = ArgumentDescriptor(name='long4', n=TAKEN_FROM_ARGUMENT4, reader=read_long4, doc="A binary representation of a long, little-endian.\n\n    This first reads four bytes as a signed size (but requires the\n    size to be >= 0), then reads that many bytes and interprets them\n    as a little-endian 2's-complement long.  If the size is 0, that's taken\n    as a shortcut for the long 0L, although LONG1 should really be used\n    then instead (and in any case where # of bytes < 256).\n    ")

class StackObject(object):
    __slots__ = ('name', 'obtype', 'doc')

    def __init__(self, name, obtype, doc):
        self.name = name
        if isinstance(obtype, tuple):
            for contained in obtype:
                pass

        self.obtype = obtype
        self.doc = doc

    def __repr__(self):
        return self.name


pyint = StackObject(name='int', obtype=int, doc='A short (as opposed to long) Python integer object.')
pylong = StackObject(name='long', obtype=long, doc='A long (as opposed to short) Python integer object.')
pyinteger_or_bool = StackObject(name='int_or_bool', obtype=(
 int, long, bool), doc='A Python integer object (short or long), or a Python bool.')
pybool = StackObject(name='bool', obtype=(
 bool,), doc='A Python bool object.')
pyfloat = StackObject(name='float', obtype=float, doc='A Python float object.')
pystring = StackObject(name='str', obtype=str, doc='A Python string object.')
pyunicode = StackObject(name='unicode', obtype=unicode, doc='A Python Unicode string object.')
pynone = StackObject(name='None', obtype=type(None), doc='The Python None object.')
pytuple = StackObject(name='tuple', obtype=tuple, doc='A Python tuple object.')
pylist = StackObject(name='list', obtype=list, doc='A Python list object.')
pydict = StackObject(name='dict', obtype=dict, doc='A Python dict object.')
anyobject = StackObject(name='any', obtype=object, doc='Any kind of object whatsoever.')
markobject = StackObject(name='mark', obtype=StackObject, doc="'The mark' is a unique object.\n\n                 Opcodes that operate on a variable number of objects\n                 generally don't embed the count of objects in the opcode,\n                 or pull it off the stack.  Instead the MARK opcode is used\n                 to push a special marker object on the stack, and then\n                 some other opcodes grab all the objects from the top of\n                 the stack down to (but not including) the topmost marker\n                 object.\n                 ")
stackslice = StackObject(name='stackslice', obtype=StackObject, doc='An object representing a contiguous slice of the stack.\n\n                 This is used in conjuction with markobject, to represent all\n                 of the stack following the topmost markobject.  For example,\n                 the POP_MARK opcode changes the stack from\n\n                     [..., markobject, stackslice]\n                 to\n                     [...]\n\n                 No matter how many object are on the stack after the topmost\n                 markobject, POP_MARK gets rid of all of them (including the\n                 topmost markobject too).\n                 ')

class OpcodeInfo(object):
    __slots__ = ('name', 'code', 'arg', 'stack_before', 'stack_after', 'proto', 'doc')

    def __init__(self, name, code, arg, stack_before, stack_after, proto, doc):
        self.name = name
        self.code = code
        self.arg = arg
        for x in stack_before:
            pass

        self.stack_before = stack_before
        for x in stack_after:
            pass

        self.stack_after = stack_after
        self.proto = proto
        self.doc = doc


I = OpcodeInfo
opcodes = [
 I(name='INT', code='I', arg=decimalnl_short, stack_before=[], stack_after=[
  pyinteger_or_bool], proto=0, doc='Push an integer or bool.\n\n      The argument is a newline-terminated decimal literal string.\n\n      The intent may have been that this always fit in a short Python int,\n      but INT can be generated in pickles written on a 64-bit box that\n      require a Python long on a 32-bit box.  The difference between this\n      and LONG then is that INT skips a trailing \'L\', and produces a short\n      int whenever possible.\n\n      Another difference is due to that, when bool was introduced as a\n      distinct type in 2.3, builtin names True and False were also added to\n      2.2.2, mapping to ints 1 and 0.  For compatibility in both directions,\n      True gets pickled as INT + "I01\\n", and False as INT + "I00\\n".\n      Leading zeroes are never produced for a genuine integer.  The 2.3\n      (and later) unpicklers special-case these and return bool instead;\n      earlier unpicklers ignore the leading "0" and return the int.\n      '),
 I(name='BININT', code='J', arg=int4, stack_before=[], stack_after=[
  pyint], proto=1, doc='Push a four-byte signed integer.\n\n      This handles the full range of Python (short) integers on a 32-bit\n      box, directly as binary bytes (1 for the opcode and 4 for the integer).\n      If the integer is non-negative and fits in 1 or 2 bytes, pickling via\n      BININT1 or BININT2 saves space.\n      '),
 I(name='BININT1', code='K', arg=uint1, stack_before=[], stack_after=[
  pyint], proto=1, doc='Push a one-byte unsigned integer.\n\n      This is a space optimization for pickling very small non-negative ints,\n      in range(256).\n      '),
 I(name='BININT2', code='M', arg=uint2, stack_before=[], stack_after=[
  pyint], proto=1, doc='Push a two-byte unsigned integer.\n\n      This is a space optimization for pickling small positive ints, in\n      range(256, 2**16).  Integers in range(256) can also be pickled via\n      BININT2, but BININT1 instead saves a byte.\n      '),
 I(name='LONG', code='L', arg=decimalnl_long, stack_before=[], stack_after=[
  pylong], proto=0, doc="Push a long integer.\n\n      The same as INT, except that the literal ends with 'L', and always\n      unpickles to a Python long.  There doesn't seem a real purpose to the\n      trailing 'L'.\n\n      Note that LONG takes time quadratic in the number of digits when\n      unpickling (this is simply due to the nature of decimal->binary\n      conversion).  Proto 2 added linear-time (in C; still quadratic-time\n      in Python) LONG1 and LONG4 opcodes.\n      "),
 I(name='LONG1', code='\x8a', arg=long1, stack_before=[], stack_after=[
  pylong], proto=2, doc='Long integer using one-byte length.\n\n      A more efficient encoding of a Python long; the long1 encoding\n      says it all.'),
 I(name='LONG4', code='\x8b', arg=long4, stack_before=[], stack_after=[
  pylong], proto=2, doc='Long integer using found-byte length.\n\n      A more efficient encoding of a Python long; the long4 encoding\n      says it all.'),
 I(name='STRING', code='S', arg=stringnl, stack_before=[], stack_after=[
  pystring], proto=0, doc='Push a Python string object.\n\n      The argument is a repr-style string, with bracketing quote characters,\n      and perhaps embedded escapes.  The argument extends until the next\n      newline character.\n      '),
 I(name='BINSTRING', code='T', arg=string4, stack_before=[], stack_after=[
  pystring], proto=1, doc='Push a Python string object.\n\n      There are two arguments:  the first is a 4-byte little-endian signed int\n      giving the number of bytes in the string, and the second is that many\n      bytes, which are taken literally as the string content.\n      '),
 I(name='SHORT_BINSTRING', code='U', arg=string1, stack_before=[], stack_after=[
  pystring], proto=1, doc='Push a Python string object.\n\n      There are two arguments:  the first is a 1-byte unsigned int giving\n      the number of bytes in the string, and the second is that many bytes,\n      which are taken literally as the string content.\n      '),
 I(name='NONE', code='N', arg=None, stack_before=[], stack_after=[
  pynone], proto=0, doc='Push None on the stack.'),
 I(name='NEWTRUE', code='\x88', arg=None, stack_before=[], stack_after=[
  pybool], proto=2, doc='True.\n\n      Push True onto the stack.'),
 I(name='NEWFALSE', code='\x89', arg=None, stack_before=[], stack_after=[
  pybool], proto=2, doc='True.\n\n      Push False onto the stack.'),
 I(name='UNICODE', code='V', arg=unicodestringnl, stack_before=[], stack_after=[
  pyunicode], proto=0, doc='Push a Python Unicode string object.\n\n      The argument is a raw-unicode-escape encoding of a Unicode string,\n      and so may contain embedded escape sequences.  The argument extends\n      until the next newline character.\n      '),
 I(name='BINUNICODE', code='X', arg=unicodestring4, stack_before=[], stack_after=[
  pyunicode], proto=1, doc='Push a Python Unicode string object.\n\n      There are two arguments:  the first is a 4-byte little-endian signed int\n      giving the number of bytes in the string.  The second is that many\n      bytes, and is the UTF-8 encoding of the Unicode string.\n      '),
 I(name='FLOAT', code='F', arg=floatnl, stack_before=[], stack_after=[
  pyfloat], proto=0, doc="Newline-terminated decimal float literal.\n\n      The argument is repr(a_float), and in general requires 17 significant\n      digits for roundtrip conversion to be an identity (this is so for\n      IEEE-754 double precision values, which is what Python float maps to\n      on most boxes).\n\n      In general, FLOAT cannot be used to transport infinities, NaNs, or\n      minus zero across boxes (or even on a single box, if the platform C\n      library can't read the strings it produces for such things -- Windows\n      is like that), but may do less damage than BINFLOAT on boxes with\n      greater precision or dynamic range than IEEE-754 double.\n      "),
 I(name='BINFLOAT', code='G', arg=float8, stack_before=[], stack_after=[
  pyfloat], proto=1, doc='Float stored in binary form, with 8 bytes of data.\n\n      This generally requires less than half the space of FLOAT encoding.\n      In general, BINFLOAT cannot be used to transport infinities, NaNs, or\n      minus zero, raises an exception if the exponent exceeds the range of\n      an IEEE-754 double, and retains no more than 53 bits of precision (if\n      there are more than that, "add a half and chop" rounding is used to\n      cut it back to 53 significant bits).\n      '),
 I(name='EMPTY_LIST', code=']', arg=None, stack_before=[], stack_after=[
  pylist], proto=1, doc='Push an empty list.'),
 I(name='APPEND', code='a', arg=None, stack_before=[
  pylist, anyobject], stack_after=[
  pylist], proto=0, doc='Append an object to a list.\n\n      Stack before:  ... pylist anyobject\n      Stack after:   ... pylist+[anyobject]\n\n      although pylist is really extended in-place.\n      '),
 I(name='APPENDS', code='e', arg=None, stack_before=[
  pylist, markobject, stackslice], stack_after=[
  pylist], proto=1, doc='Extend a list by a slice of stack objects.\n\n      Stack before:  ... pylist markobject stackslice\n      Stack after:   ... pylist+stackslice\n\n      although pylist is really extended in-place.\n      '),
 I(name='LIST', code='l', arg=None, stack_before=[
  markobject, stackslice], stack_after=[
  pylist], proto=0, doc="Build a list out of the topmost stack slice, after markobject.\n\n      All the stack entries following the topmost markobject are placed into\n      a single Python list, which single list object replaces all of the\n      stack from the topmost markobject onward.  For example,\n\n      Stack before: ... markobject 1 2 3 'abc'\n      Stack after:  ... [1, 2, 3, 'abc']\n      "),
 I(name='EMPTY_TUPLE', code=')', arg=None, stack_before=[], stack_after=[
  pytuple], proto=1, doc='Push an empty tuple.'),
 I(name='TUPLE', code='t', arg=None, stack_before=[
  markobject, stackslice], stack_after=[
  pytuple], proto=0, doc="Build a tuple out of the topmost stack slice, after markobject.\n\n      All the stack entries following the topmost markobject are placed into\n      a single Python tuple, which single tuple object replaces all of the\n      stack from the topmost markobject onward.  For example,\n\n      Stack before: ... markobject 1 2 3 'abc'\n      Stack after:  ... (1, 2, 3, 'abc')\n      "),
 I(name='TUPLE1', code='\x85', arg=None, stack_before=[
  anyobject], stack_after=[
  pytuple], proto=2, doc='Build a one-tuple out of the topmost item on the stack.\n\n      This code pops one value off the stack and pushes a tuple of\n      length 1 whose one item is that value back onto it.  In other\n      words:\n\n          stack[-1] = tuple(stack[-1:])\n      '),
 I(name='TUPLE2', code='\x86', arg=None, stack_before=[
  anyobject, anyobject], stack_after=[
  pytuple], proto=2, doc='Build a two-tuple out of the top two items on the stack.\n\n      This code pops two values off the stack and pushes a tuple of\n      length 2 whose items are those values back onto it.  In other\n      words:\n\n          stack[-2:] = [tuple(stack[-2:])]\n      '),
 I(name='TUPLE3', code='\x87', arg=None, stack_before=[
  anyobject, anyobject, anyobject], stack_after=[
  pytuple], proto=2, doc='Build a three-tuple out of the top three items on the stack.\n\n      This code pops three values off the stack and pushes a tuple of\n      length 3 whose items are those values back onto it.  In other\n      words:\n\n          stack[-3:] = [tuple(stack[-3:])]\n      '),
 I(name='EMPTY_DICT', code='}', arg=None, stack_before=[], stack_after=[
  pydict], proto=1, doc='Push an empty dict.'),
 I(name='DICT', code='d', arg=None, stack_before=[
  markobject, stackslice], stack_after=[
  pydict], proto=0, doc="Build a dict out of the topmost stack slice, after markobject.\n\n      All the stack entries following the topmost markobject are placed into\n      a single Python dict, which single dict object replaces all of the\n      stack from the topmost markobject onward.  The stack slice alternates\n      key, value, key, value, ....  For example,\n\n      Stack before: ... markobject 1 2 3 'abc'\n      Stack after:  ... {1: 2, 3: 'abc'}\n      "),
 I(name='SETITEM', code='s', arg=None, stack_before=[
  pydict, anyobject, anyobject], stack_after=[
  pydict], proto=0, doc='Add a key+value pair to an existing dict.\n\n      Stack before:  ... pydict key value\n      Stack after:   ... pydict\n\n      where pydict has been modified via pydict[key] = value.\n      '),
 I(name='SETITEMS', code='u', arg=None, stack_before=[
  pydict, markobject, stackslice], stack_after=[
  pydict], proto=1, doc='Add an arbitrary number of key+value pairs to an existing dict.\n\n      The slice of the stack following the topmost markobject is taken as\n      an alternating sequence of keys and values, added to the dict\n      immediately under the topmost markobject.  Everything at and after the\n      topmost markobject is popped, leaving the mutated dict at the top\n      of the stack.\n\n      Stack before:  ... pydict markobject key_1 value_1 ... key_n value_n\n      Stack after:   ... pydict\n\n      where pydict has been modified via pydict[key_i] = value_i for i in\n      1, 2, ..., n, and in that order.\n      '),
 I(name='POP', code='0', arg=None, stack_before=[
  anyobject], stack_after=[], proto=0, doc='Discard the top stack item, shrinking the stack by one item.'),
 I(name='DUP', code='2', arg=None, stack_before=[
  anyobject], stack_after=[
  anyobject, anyobject], proto=0, doc='Push the top stack item onto the stack again, duplicating it.'),
 I(name='MARK', code='(', arg=None, stack_before=[], stack_after=[
  markobject], proto=0, doc='Push markobject onto the stack.\n\n      markobject is a unique object, used by other opcodes to identify a\n      region of the stack containing a variable number of objects for them\n      to work on.  See markobject.doc for more detail.\n      '),
 I(name='POP_MARK', code='1', arg=None, stack_before=[
  markobject, stackslice], stack_after=[], proto=1, doc='Pop all the stack objects at and above the topmost markobject.\n\n      When an opcode using a variable number of stack objects is done,\n      POP_MARK is used to remove those objects, and to remove the markobject\n      that delimited their starting position on the stack.\n      '),
 I(name='GET', code='g', arg=decimalnl_short, stack_before=[], stack_after=[
  anyobject], proto=0, doc='Read an object from the memo and push it on the stack.\n\n      The index of the memo object to push is given by the newline-terminated\n      decimal string following.  BINGET and LONG_BINGET are space-optimized\n      versions.\n      '),
 I(name='BINGET', code='h', arg=uint1, stack_before=[], stack_after=[
  anyobject], proto=1, doc='Read an object from the memo and push it on the stack.\n\n      The index of the memo object to push is given by the 1-byte unsigned\n      integer following.\n      '),
 I(name='LONG_BINGET', code='j', arg=int4, stack_before=[], stack_after=[
  anyobject], proto=1, doc='Read an object from the memo and push it on the stack.\n\n      The index of the memo object to push is given by the 4-byte signed\n      little-endian integer following.\n      '),
 I(name='PUT', code='p', arg=decimalnl_short, stack_before=[], stack_after=[], proto=0, doc='Store the stack top into the memo.  The stack is not popped.\n\n      The index of the memo location to write into is given by the newline-\n      terminated decimal string following.  BINPUT and LONG_BINPUT are\n      space-optimized versions.\n      '),
 I(name='BINPUT', code='q', arg=uint1, stack_before=[], stack_after=[], proto=1, doc='Store the stack top into the memo.  The stack is not popped.\n\n      The index of the memo location to write into is given by the 1-byte\n      unsigned integer following.\n      '),
 I(name='LONG_BINPUT', code='r', arg=int4, stack_before=[], stack_after=[], proto=1, doc='Store the stack top into the memo.  The stack is not popped.\n\n      The index of the memo location to write into is given by the 4-byte\n      signed little-endian integer following.\n      '),
 I(name='EXT1', code='\x82', arg=uint1, stack_before=[], stack_after=[
  anyobject], proto=2, doc='Extension code.\n\n      This code and the similar EXT2 and EXT4 allow using a registry\n      of popular objects that are pickled by name, typically classes.\n      It is envisioned that through a global negotiation and\n      registration process, third parties can set up a mapping between\n      ints and object names.\n\n      In order to guarantee pickle interchangeability, the extension\n      code registry ought to be global, although a range of codes may\n      be reserved for private use.\n\n      EXT1 has a 1-byte integer argument.  This is used to index into the\n      extension registry, and the object at that index is pushed on the stack.\n      '),
 I(name='EXT2', code='\x83', arg=uint2, stack_before=[], stack_after=[
  anyobject], proto=2, doc='Extension code.\n\n      See EXT1.  EXT2 has a two-byte integer argument.\n      '),
 I(name='EXT4', code='\x84', arg=int4, stack_before=[], stack_after=[
  anyobject], proto=2, doc='Extension code.\n\n      See EXT1.  EXT4 has a four-byte integer argument.\n      '),
 I(name='GLOBAL', code='c', arg=stringnl_noescape_pair, stack_before=[], stack_after=[
  anyobject], proto=0, doc='Push a global object (module.attr) on the stack.\n\n      Two newline-terminated strings follow the GLOBAL opcode.  The first is\n      taken as a module name, and the second as a class name.  The class\n      object module.class is pushed on the stack.  More accurately, the\n      object returned by self.find_class(module, class) is pushed on the\n      stack, so unpickling subclasses can override this form of lookup.\n      '),
 I(name='REDUCE', code='R', arg=None, stack_before=[
  anyobject, anyobject], stack_after=[
  anyobject], proto=0, doc="Push an object built from a callable and an argument tuple.\n\n      The opcode is named to remind of the __reduce__() method.\n\n      Stack before: ... callable pytuple\n      Stack after:  ... callable(*pytuple)\n\n      The callable and the argument tuple are the first two items returned\n      by a __reduce__ method.  Applying the callable to the argtuple is\n      supposed to reproduce the original object, or at least get it started.\n      If the __reduce__ method returns a 3-tuple, the last component is an\n      argument to be passed to the object's __setstate__, and then the REDUCE\n      opcode is followed by code to create setstate's argument, and then a\n      BUILD opcode to apply  __setstate__ to that argument.\n\n      If type(callable) is not ClassType, REDUCE complains unless the\n      callable has been registered with the copy_reg module's\n      safe_constructors dict, or the callable has a magic\n      '__safe_for_unpickling__' attribute with a true value.  I'm not sure\n      why it does this, but I've sure seen this complaint often enough when\n      I didn't want to <wink>.\n      "),
 I(name='BUILD', code='b', arg=None, stack_before=[
  anyobject, anyobject], stack_after=[
  anyobject], proto=0, doc='Finish building an object, via __setstate__ or dict update.\n\n      Stack before: ... anyobject argument\n      Stack after:  ... anyobject\n\n      where anyobject may have been mutated, as follows:\n\n      If the object has a __setstate__ method,\n\n          anyobject.__setstate__(argument)\n\n      is called.\n\n      Else the argument must be a dict, the object must have a __dict__, and\n      the object is updated via\n\n          anyobject.__dict__.update(argument)\n\n      This may raise RuntimeError in restricted execution mode (which\n      disallows access to __dict__ directly); in that case, the object\n      is updated instead via\n\n          for k, v in argument.items():\n              anyobject[k] = v\n      '),
 I(name='INST', code='i', arg=stringnl_noescape_pair, stack_before=[
  markobject, stackslice], stack_after=[
  anyobject], proto=0, doc="Build a class instance.\n\n      This is the protocol 0 version of protocol 1's OBJ opcode.\n      INST is followed by two newline-terminated strings, giving a\n      module and class name, just as for the GLOBAL opcode (and see\n      GLOBAL for more details about that).  self.find_class(module, name)\n      is used to get a class object.\n\n      In addition, all the objects on the stack following the topmost\n      markobject are gathered into a tuple and popped (along with the\n      topmost markobject), just as for the TUPLE opcode.\n\n      Now it gets complicated.  If all of these are true:\n\n        + The argtuple is empty (markobject was at the top of the stack\n          at the start).\n\n        + It's an old-style class object (the type of the class object is\n          ClassType).\n\n        + The class object does not have a __getinitargs__ attribute.\n\n      then we want to create an old-style class instance without invoking\n      its __init__() method (pickle has waffled on this over the years; not\n      calling __init__() is current wisdom).  In this case, an instance of\n      an old-style dummy class is created, and then we try to rebind its\n      __class__ attribute to the desired class object.  If this succeeds,\n      the new instance object is pushed on the stack, and we're done.  In\n      restricted execution mode it can fail (assignment to __class__ is\n      disallowed), and I'm not really sure what happens then -- it looks\n      like the code ends up calling the class object's __init__ anyway,\n      via falling into the next case.\n\n      Else (the argtuple is not empty, it's not an old-style class object,\n      or the class object does have a __getinitargs__ attribute), the code\n      first insists that the class object have a __safe_for_unpickling__\n      attribute.  Unlike as for the __safe_for_unpickling__ check in REDUCE,\n      it doesn't matter whether this attribute has a true or false value, it\n      only matters whether it exists (XXX this is a bug; cPickle\n      requires the attribute to be true).  If __safe_for_unpickling__\n      doesn't exist, UnpicklingError is raised.\n\n      Else (the class object does have a __safe_for_unpickling__ attr),\n      the class object obtained from INST's arguments is applied to the\n      argtuple obtained from the stack, and the resulting instance object\n      is pushed on the stack.\n\n      NOTE:  checks for __safe_for_unpickling__ went away in Python 2.3.\n      "),
 I(name='OBJ', code='o', arg=None, stack_before=[
  markobject, anyobject, stackslice], stack_after=[
  anyobject], proto=1, doc="Build a class instance.\n\n      This is the protocol 1 version of protocol 0's INST opcode, and is\n      very much like it.  The major difference is that the class object\n      is taken off the stack, allowing it to be retrieved from the memo\n      repeatedly if several instances of the same class are created.  This\n      can be much more efficient (in both time and space) than repeatedly\n      embedding the module and class names in INST opcodes.\n\n      Unlike INST, OBJ takes no arguments from the opcode stream.  Instead\n      the class object is taken off the stack, immediately above the\n      topmost markobject:\n\n      Stack before: ... markobject classobject stackslice\n      Stack after:  ... new_instance_object\n\n      As for INST, the remainder of the stack above the markobject is\n      gathered into an argument tuple, and then the logic seems identical,\n      except that no __safe_for_unpickling__ check is done (XXX this is\n      a bug; cPickle does test __safe_for_unpickling__).  See INST for\n      the gory details.\n\n      NOTE:  In Python 2.3, INST and OBJ are identical except for how they\n      get the class object.  That was always the intent; the implementations\n      had diverged for accidental reasons.\n      "),
 I(name='NEWOBJ', code='\x81', arg=None, stack_before=[
  anyobject, anyobject], stack_after=[
  anyobject], proto=2, doc='Build an object instance.\n\n      The stack before should be thought of as containing a class\n      object followed by an argument tuple (the tuple being the stack\n      top).  Call these cls and args.  They are popped off the stack,\n      and the value returned by cls.__new__(cls, *args) is pushed back\n      onto the stack.\n      '),
 I(name='PROTO', code='\x80', arg=uint1, stack_before=[], stack_after=[], proto=2, doc='Protocol version indicator.\n\n      For protocol 2 and above, a pickle must start with this opcode.\n      The argument is the protocol version, an int in range(2, 256).\n      '),
 I(name='STOP', code='.', arg=None, stack_before=[
  anyobject], stack_after=[], proto=0, doc="Stop the unpickling machine.\n\n      Every pickle ends with this opcode.  The object at the top of the stack\n      is popped, and that's the result of unpickling.  The stack should be\n      empty then.\n      "),
 I(name='PERSID', code='P', arg=stringnl_noescape, stack_before=[], stack_after=[
  anyobject], proto=0, doc='Push an object identified by a persistent ID.\n\n      The pickle module doesn\'t define what a persistent ID means.  PERSID\'s\n      argument is a newline-terminated str-style (no embedded escapes, no\n      bracketing quote characters) string, which *is* "the persistent ID".\n      The unpickler passes this string to self.persistent_load().  Whatever\n      object that returns is pushed on the stack.  There is no implementation\n      of persistent_load() in Python\'s unpickler:  it must be supplied by an\n      unpickler subclass.\n      '),
 I(name='BINPERSID', code='Q', arg=None, stack_before=[
  anyobject], stack_after=[
  anyobject], proto=1, doc='Push an object identified by a persistent ID.\n\n      Like PERSID, except the persistent ID is popped off the stack (instead\n      of being a string embedded in the opcode bytestream).  The persistent\n      ID is passed to self.persistent_load(), and whatever object that\n      returns is pushed on the stack.  See PERSID for more detail.\n      ')]
del I
name2i = {}
code2i = {}
for i, d in enumerate(opcodes):
    if d.name in name2i:
        raise ValueError('repeated name %r at indices %d and %d' % (
         d.name, name2i[d.name], i))
    if d.code in code2i:
        raise ValueError('repeated code %r at indices %d and %d' % (
         d.code, code2i[d.code], i))
    name2i[d.name] = i
    code2i[d.code] = i

del name2i
del code2i
del i
del d
code2op = {}
for d in opcodes:
    code2op[d.code] = d

del d

def assure_pickle_consistency(verbose=False):
    import pickle
    import re
    copy = code2op.copy()
    for name in pickle.__all__:
        if not re.match('[A-Z][A-Z0-9_]+$', name):
            if verbose:
                print "skipping %r: it doesn't look like an opcode name" % name
            continue
        picklecode = getattr(pickle, name)
        if not isinstance(picklecode, str) or len(picklecode) != 1:
            if verbose:
                print "skipping %r: value %r doesn't look like a pickle code" % (
                 name, picklecode)
            continue
        if picklecode in copy:
            if verbose:
                print 'checking name %r w/ code %r for consistency' % (
                 name, picklecode)
            d = copy[picklecode]
            if d.name != name:
                raise ValueError("for pickle code %r, pickle.py uses name %r but we're using name %r" % (
                 picklecode,
                 name,
                 d.name))
            del copy[picklecode]
        else:
            raise ValueError("pickle.py appears to have a pickle opcode with name %r and code %r, but we don't" % (
             name, picklecode))

    if copy:
        msg = [
         "we appear to have pickle opcodes that pickle.py doesn't have:"]
        for code, d in copy.items():
            msg.append('    name %r with code %r' % (d.name, code))

        raise ValueError('\n'.join(msg))


assure_pickle_consistency()
del assure_pickle_consistency

def genops(pickle):
    """Generate all the opcodes in a pickle.
    
    'pickle' is a file-like object, or string, containing the pickle.
    
    Each opcode in the pickle is generated, from the current pickle position,
    stopping after a STOP opcode is delivered.  A triple is generated for
    each opcode:
    
        opcode, arg, pos
    
    opcode is an OpcodeInfo record, describing the current opcode.
    
    If the opcode has an argument embedded in the pickle, arg is its decoded
    value, as a Python object.  If the opcode doesn't have an argument, arg
    is None.
    
    If the pickle has a tell() method, pos was the value of pickle.tell()
    before reading the current opcode.  If the pickle is a string object,
    it's wrapped in a StringIO object, and the latter's tell() result is
    used.  Else (the pickle doesn't have a tell(), and it's not obvious how
    to query its current position) pos is None.
    """
    import cStringIO as StringIO
    if isinstance(pickle, str):
        pickle = StringIO.StringIO(pickle)
    if hasattr(pickle, 'tell'):
        getpos = pickle.tell
    else:
        getpos = lambda : None
    while True:
        pos = getpos()
        code = pickle.read(1)
        opcode = code2op.get(code)
        if opcode is None:
            if code == '':
                raise ValueError('pickle exhausted before seeing STOP')
            else:
                raise ValueError('at position %s, opcode %r unknown' % (
                 pos is None and '<unknown>' or pos,
                 code))
        if opcode.arg is None:
            arg = None
        else:
            arg = opcode.arg.reader(pickle)
        yield (
         opcode, arg, pos)
        if code == '.':
            break

    return


def optimize(p):
    """Optimize a pickle string by removing unused PUT opcodes"""
    gets = set()
    puts = []
    prevpos = None
    for opcode, arg, pos in genops(p):
        if prevpos is not None:
            puts.append((prevarg, prevpos, pos))
            prevpos = None
        if 'PUT' in opcode.name:
            prevarg, prevpos = arg, pos
        elif 'GET' in opcode.name:
            gets.add(arg)

    s = []
    i = 0
    for arg, start, stop in puts:
        j = stop if arg in gets else start
        s.append(p[i:j])
        i = stop

    s.append(p[i:])
    return ''.join(s)


def dis(pickle, out=None, memo=None, indentlevel=4):
    """Produce a symbolic disassembly of a pickle.
    
    'pickle' is a file-like object, or string, containing a (at least one)
    pickle.  The pickle is disassembled from the current position, through
    the first STOP opcode encountered.
    
    Optional arg 'out' is a file-like object to which the disassembly is
    printed.  It defaults to sys.stdout.
    
    Optional arg 'memo' is a Python dict, used as the pickle's memo.  It
    may be mutated by dis(), if the pickle contains PUT or BINPUT opcodes.
    Passing the same memo object to another dis() call then allows disassembly
    to proceed across multiple pickles that were all created by the same
    pickler with the same memo.  Ordinarily you don't need to worry about this.
    
    Optional arg indentlevel is the number of blanks by which to indent
    a new MARK level.  It defaults to 4.
    
    In addition to printing the disassembly, some sanity checks are made:
    
    + All embedded opcode arguments "make sense".
    
    + Explicit and implicit pop operations have enough items on the stack.
    
    + When an opcode implicitly refers to a markobject, a markobject is
      actually on the stack.
    
    + A memo entry isn't referenced before it's defined.
    
    + The markobject isn't stored in the memo.
    
    + A memo entry isn't redefined.
    """
    stack = []
    if memo is None:
        memo = {}
    maxproto = -1
    markstack = []
    indentchunk = ' ' * indentlevel
    errormsg = None
    for opcode, arg, pos in genops(pickle):
        if pos is not None:
            print >> out, '%5d:' % pos,
        line = '%-4s %s%s' % (repr(opcode.code)[1:-1],
         indentchunk * len(markstack),
         opcode.name)
        maxproto = max(maxproto, opcode.proto)
        before = opcode.stack_before
        after = opcode.stack_after
        numtopop = len(before)
        markmsg = None
        if markobject in before or opcode.name == 'POP' and stack and stack[-1] is markobject:
            if markstack:
                markpos = markstack.pop()
                if markpos is None:
                    markmsg = '(MARK at unknown opcode offset)'
                else:
                    markmsg = '(MARK at %d)' % markpos
                while stack[-1] is not markobject:
                    stack.pop()

                stack.pop()
                try:
                    numtopop = before.index(markobject)
                except ValueError:
                    numtopop = 0

            else:
                errormsg = markmsg = 'no MARK exists on stack'
        if opcode.name in ('PUT', 'BINPUT', 'LONG_BINPUT'):
            if arg in memo:
                errormsg = 'memo key %r already defined' % arg
            elif not stack:
                errormsg = "stack is empty -- can't store into memo"
            elif stack[-1] is markobject:
                errormsg = "can't store markobject in the memo"
            else:
                memo[arg] = stack[-1]
        elif opcode.name in ('GET', 'BINGET', 'LONG_BINGET'):
            if arg in memo:
                after = [memo[arg]]
            else:
                errormsg = 'memo key %r has never been stored into' % arg
        if arg is not None or markmsg:
            line += ' ' * (10 - len(opcode.name))
            if arg is not None:
                line += ' ' + repr(arg)
            if markmsg:
                line += ' ' + markmsg
        print >> out, line
        if errormsg:
            raise ValueError(errormsg)
        if len(stack) < numtopop:
            raise ValueError('tries to pop %d items from stack with only %d items' % (
             numtopop, len(stack)))
        if numtopop:
            del stack[-numtopop:]
        if markobject in after:
            markstack.append(pos)
        stack.extend(after)

    print >> out, 'highest protocol among opcodes =', maxproto
    if stack:
        raise ValueError('stack not empty after STOP: %r' % stack)
    return


class _Example:

    def __init__(self, value):
        self.value = value


_dis_test = '\n>>> import pickle\n>>> x = [1, 2, (3, 4), {\'abc\': u"def"}]\n>>> pkl = pickle.dumps(x, 0)\n>>> dis(pkl)\n    0: (    MARK\n    1: l        LIST       (MARK at 0)\n    2: p    PUT        0\n    5: I    INT        1\n    8: a    APPEND\n    9: I    INT        2\n   12: a    APPEND\n   13: (    MARK\n   14: I        INT        3\n   17: I        INT        4\n   20: t        TUPLE      (MARK at 13)\n   21: p    PUT        1\n   24: a    APPEND\n   25: (    MARK\n   26: d        DICT       (MARK at 25)\n   27: p    PUT        2\n   30: S    STRING     \'abc\'\n   37: p    PUT        3\n   40: V    UNICODE    u\'def\'\n   45: p    PUT        4\n   48: s    SETITEM\n   49: a    APPEND\n   50: .    STOP\nhighest protocol among opcodes = 0\n\nTry again with a "binary" pickle.\n\n>>> pkl = pickle.dumps(x, 1)\n>>> dis(pkl)\n    0: ]    EMPTY_LIST\n    1: q    BINPUT     0\n    3: (    MARK\n    4: K        BININT1    1\n    6: K        BININT1    2\n    8: (        MARK\n    9: K            BININT1    3\n   11: K            BININT1    4\n   13: t            TUPLE      (MARK at 8)\n   14: q        BINPUT     1\n   16: }        EMPTY_DICT\n   17: q        BINPUT     2\n   19: U        SHORT_BINSTRING \'abc\'\n   24: q        BINPUT     3\n   26: X        BINUNICODE u\'def\'\n   34: q        BINPUT     4\n   36: s        SETITEM\n   37: e        APPENDS    (MARK at 3)\n   38: .    STOP\nhighest protocol among opcodes = 1\n\nExercise the INST/OBJ/BUILD family.\n\n>>> import pickletools\n>>> dis(pickle.dumps(pickletools.dis, 0))\n    0: c    GLOBAL     \'pickletools dis\'\n   17: p    PUT        0\n   20: .    STOP\nhighest protocol among opcodes = 0\n\n>>> from pickletools import _Example\n>>> x = [_Example(42)] * 2\n>>> dis(pickle.dumps(x, 0))\n    0: (    MARK\n    1: l        LIST       (MARK at 0)\n    2: p    PUT        0\n    5: (    MARK\n    6: i        INST       \'pickletools _Example\' (MARK at 5)\n   28: p    PUT        1\n   31: (    MARK\n   32: d        DICT       (MARK at 31)\n   33: p    PUT        2\n   36: S    STRING     \'value\'\n   45: p    PUT        3\n   48: I    INT        42\n   52: s    SETITEM\n   53: b    BUILD\n   54: a    APPEND\n   55: g    GET        1\n   58: a    APPEND\n   59: .    STOP\nhighest protocol among opcodes = 0\n\n>>> dis(pickle.dumps(x, 1))\n    0: ]    EMPTY_LIST\n    1: q    BINPUT     0\n    3: (    MARK\n    4: (        MARK\n    5: c            GLOBAL     \'pickletools _Example\'\n   27: q            BINPUT     1\n   29: o            OBJ        (MARK at 4)\n   30: q        BINPUT     2\n   32: }        EMPTY_DICT\n   33: q        BINPUT     3\n   35: U        SHORT_BINSTRING \'value\'\n   42: q        BINPUT     4\n   44: K        BININT1    42\n   46: s        SETITEM\n   47: b        BUILD\n   48: h        BINGET     2\n   50: e        APPENDS    (MARK at 3)\n   51: .    STOP\nhighest protocol among opcodes = 1\n\nTry "the canonical" recursive-object test.\n\n>>> L = []\n>>> T = L,\n>>> L.append(T)\n>>> L[0] is T\nTrue\n>>> T[0] is L\nTrue\n>>> L[0][0] is L\nTrue\n>>> T[0][0] is T\nTrue\n>>> dis(pickle.dumps(L, 0))\n    0: (    MARK\n    1: l        LIST       (MARK at 0)\n    2: p    PUT        0\n    5: (    MARK\n    6: g        GET        0\n    9: t        TUPLE      (MARK at 5)\n   10: p    PUT        1\n   13: a    APPEND\n   14: .    STOP\nhighest protocol among opcodes = 0\n\n>>> dis(pickle.dumps(L, 1))\n    0: ]    EMPTY_LIST\n    1: q    BINPUT     0\n    3: (    MARK\n    4: h        BINGET     0\n    6: t        TUPLE      (MARK at 3)\n    7: q    BINPUT     1\n    9: a    APPEND\n   10: .    STOP\nhighest protocol among opcodes = 1\n\nNote that, in the protocol 0 pickle of the recursive tuple, the disassembler\nhas to emulate the stack in order to realize that the POP opcode at 16 gets\nrid of the MARK at 0.\n\n>>> dis(pickle.dumps(T, 0))\n    0: (    MARK\n    1: (        MARK\n    2: l            LIST       (MARK at 1)\n    3: p        PUT        0\n    6: (        MARK\n    7: g            GET        0\n   10: t            TUPLE      (MARK at 6)\n   11: p        PUT        1\n   14: a        APPEND\n   15: 0        POP\n   16: 0        POP        (MARK at 0)\n   17: g    GET        1\n   20: .    STOP\nhighest protocol among opcodes = 0\n\n>>> dis(pickle.dumps(T, 1))\n    0: (    MARK\n    1: ]        EMPTY_LIST\n    2: q        BINPUT     0\n    4: (        MARK\n    5: h            BINGET     0\n    7: t            TUPLE      (MARK at 4)\n    8: q        BINPUT     1\n   10: a        APPEND\n   11: 1        POP_MARK   (MARK at 0)\n   12: h    BINGET     1\n   14: .    STOP\nhighest protocol among opcodes = 1\n\nTry protocol 2.\n\n>>> dis(pickle.dumps(L, 2))\n    0: \\x80 PROTO      2\n    2: ]    EMPTY_LIST\n    3: q    BINPUT     0\n    5: h    BINGET     0\n    7: \\x85 TUPLE1\n    8: q    BINPUT     1\n   10: a    APPEND\n   11: .    STOP\nhighest protocol among opcodes = 2\n\n>>> dis(pickle.dumps(T, 2))\n    0: \\x80 PROTO      2\n    2: ]    EMPTY_LIST\n    3: q    BINPUT     0\n    5: h    BINGET     0\n    7: \\x85 TUPLE1\n    8: q    BINPUT     1\n   10: a    APPEND\n   11: 0    POP\n   12: h    BINGET     1\n   14: .    STOP\nhighest protocol among opcodes = 2\n'
_memo_test = '\n>>> import pickle\n>>> from StringIO import StringIO\n>>> f = StringIO()\n>>> p = pickle.Pickler(f, 2)\n>>> x = [1, 2, 3]\n>>> p.dump(x)\n>>> p.dump(x)\n>>> f.seek(0)\n>>> memo = {}\n>>> dis(f, memo=memo)\n    0: \\x80 PROTO      2\n    2: ]    EMPTY_LIST\n    3: q    BINPUT     0\n    5: (    MARK\n    6: K        BININT1    1\n    8: K        BININT1    2\n   10: K        BININT1    3\n   12: e        APPENDS    (MARK at 5)\n   13: .    STOP\nhighest protocol among opcodes = 2\n>>> dis(f, memo=memo)\n   14: \\x80 PROTO      2\n   16: h    BINGET     0\n   18: .    STOP\nhighest protocol among opcodes = 2\n'
__test__ = {'disassembler_test': _dis_test,'disassembler_memo_test': _memo_test
   }

def _test():
    import doctest
    return doctest.testmod()


if __name__ == '__main__':
    _test()