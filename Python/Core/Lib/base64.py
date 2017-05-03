# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: base64.py
"""RFC 3548: Base16, Base32, Base64 Data Encodings"""
import re
import struct
import binascii
__all__ = [
 'encode', 'decode', 'encodestring', 'decodestring',
 'b64encode', 'b64decode', 'b32encode', 'b32decode',
 'b16encode', 'b16decode',
 'standard_b64encode', 'standard_b64decode',
 'urlsafe_b64encode', 'urlsafe_b64decode']
_translation = [ chr(_x) for _x in range(256) ]
EMPTYSTRING = ''

def _translate(s, altchars):
    translation = _translation[:]
    for k, v in altchars.items():
        translation[ord(k)] = v

    return s.translate(''.join(translation))


def b64encode(s, altchars=None):
    """Encode a string using Base64.
    
    s is the string to encode.  Optional altchars must be a string of at least
    length 2 (additional characters are ignored) which specifies an
    alternative alphabet for the '+' and '/' characters.  This allows an
    application to e.g. generate url or filesystem safe Base64 strings.
    
    The encoded string is returned.
    """
    encoded = binascii.b2a_base64(s)[:-1]
    if altchars is not None:
        return _translate(encoded, {'+': altchars[0],'/': altchars[1]})
    else:
        return encoded


def b64decode(s, altchars=None):
    """Decode a Base64 encoded string.
    
    s is the string to decode.  Optional altchars must be a string of at least
    length 2 (additional characters are ignored) which specifies the
    alternative alphabet used instead of the '+' and '/' characters.
    
    The decoded string is returned.  A TypeError is raised if s were
    incorrectly padded or if there are non-alphabet characters present in the
    string.
    """
    if altchars is not None:
        s = _translate(s, {altchars[0]: '+',altchars[1]: '/'})
    try:
        return binascii.a2b_base64(s)
    except binascii.Error as msg:
        raise TypeError(msg)

    return


def standard_b64encode(s):
    """Encode a string using the standard Base64 alphabet.
    
    s is the string to encode.  The encoded string is returned.
    """
    return b64encode(s)


def standard_b64decode(s):
    """Decode a string encoded with the standard Base64 alphabet.
    
    s is the string to decode.  The decoded string is returned.  A TypeError
    is raised if the string is incorrectly padded or if there are non-alphabet
    characters present in the string.
    """
    return b64decode(s)


def urlsafe_b64encode(s):
    """Encode a string using a url-safe Base64 alphabet.
    
    s is the string to encode.  The encoded string is returned.  The alphabet
    uses '-' instead of '+' and '_' instead of '/'.
    """
    return b64encode(s, '-_')


def urlsafe_b64decode(s):
    """Decode a string encoded with the standard Base64 alphabet.
    
    s is the string to decode.  The decoded string is returned.  A TypeError
    is raised if the string is incorrectly padded or if there are non-alphabet
    characters present in the string.
    
    The alphabet uses '-' instead of '+' and '_' instead of '/'.
    """
    return b64decode(s, '-_')


_b32alphabet = {0: 'A',
   9: 'J',18: 'S',27: '3',1: 'B',
   10: 'K',19: 'T',28: '4',2: 'C',
   11: 'L',20: 'U',29: '5',3: 'D',
   12: 'M',21: 'V',30: '6',4: 'E',
   13: 'N',22: 'W',31: '7',5: 'F',
   14: 'O',23: 'X',6: 'G',
   15: 'P',24: 'Y',7: 'H',
   16: 'Q',25: 'Z',8: 'I',
   17: 'R',26: '2'}
_b32tab = _b32alphabet.items()
_b32tab.sort()
_b32tab = [ v for k, v in _b32tab ]
_b32rev = dict([ (v, long(k)) for k, v in _b32alphabet.items() ])

def b32encode(s):
    """Encode a string using Base32.
    
    s is the string to encode.  The encoded string is returned.
    """
    parts = []
    quanta, leftover = divmod(len(s), 5)
    if leftover:
        s += '\x00' * (5 - leftover)
        quanta += 1
    for i in range(quanta):
        c1, c2, c3 = struct.unpack('!HHB', s[i * 5:(i + 1) * 5])
        c2 += (c1 & 1) << 16
        c3 += (c2 & 3) << 8
        parts.extend([_b32tab[c1 >> 11],
         _b32tab[c1 >> 6 & 31],
         _b32tab[c1 >> 1 & 31],
         _b32tab[c2 >> 12],
         _b32tab[c2 >> 7 & 31],
         _b32tab[c2 >> 2 & 31],
         _b32tab[c3 >> 5],
         _b32tab[c3 & 31]])

    encoded = EMPTYSTRING.join(parts)
    if leftover == 1:
        return encoded[:-6] + '======'
    if leftover == 2:
        return encoded[:-4] + '===='
    if leftover == 3:
        return encoded[:-3] + '==='
    if leftover == 4:
        return encoded[:-1] + '='
    return encoded


def b32decode(s, casefold=False, map01=None):
    """Decode a Base32 encoded string.
    
    s is the string to decode.  Optional casefold is a flag specifying whether
    a lowercase alphabet is acceptable as input.  For security purposes, the
    default is False.
    
    RFC 3548 allows for optional mapping of the digit 0 (zero) to the letter O
    (oh), and for optional mapping of the digit 1 (one) to either the letter I
    (eye) or letter L (el).  The optional argument map01 when not None,
    specifies which letter the digit 1 should be mapped to (when map01 is not
    None, the digit 0 is always mapped to the letter O).  For security
    purposes the default is None, so that 0 and 1 are not allowed in the
    input.
    
    The decoded string is returned.  A TypeError is raised if s were
    incorrectly padded or if there are non-alphabet characters present in the
    string.
    """
    quanta, leftover = divmod(len(s), 8)
    if leftover:
        raise TypeError('Incorrect padding')
    if map01:
        s = _translate(s, {'0': 'O','1': map01})
    if casefold:
        s = s.upper()
    padchars = 0
    mo = re.search('(?P<pad>[=]*)$', s)
    if mo:
        padchars = len(mo.group('pad'))
        if padchars > 0:
            s = s[:-padchars]
    parts = []
    acc = 0
    shift = 35
    for c in s:
        val = _b32rev.get(c)
        if val is None:
            raise TypeError('Non-base32 digit found')
        acc += _b32rev[c] << shift
        shift -= 5
        if shift < 0:
            parts.append(binascii.unhexlify('%010x' % acc))
            acc = 0
            shift = 35

    last = binascii.unhexlify('%010x' % acc)
    if padchars == 0:
        last = ''
    elif padchars == 1:
        last = last[:-1]
    elif padchars == 3:
        last = last[:-2]
    elif padchars == 4:
        last = last[:-3]
    elif padchars == 6:
        last = last[:-4]
    else:
        raise TypeError('Incorrect padding')
    parts.append(last)
    return EMPTYSTRING.join(parts)


def b16encode(s):
    """Encode a string using Base16.
    
    s is the string to encode.  The encoded string is returned.
    """
    return binascii.hexlify(s).upper()


def b16decode(s, casefold=False):
    """Decode a Base16 encoded string.
    
    s is the string to decode.  Optional casefold is a flag specifying whether
    a lowercase alphabet is acceptable as input.  For security purposes, the
    default is False.
    
    The decoded string is returned.  A TypeError is raised if s were
    incorrectly padded or if there are non-alphabet characters present in the
    string.
    """
    if casefold:
        s = s.upper()
    if re.search('[^0-9A-F]', s):
        raise TypeError('Non-base16 digit found')
    return binascii.unhexlify(s)


MAXLINESIZE = 76
MAXBINSIZE = MAXLINESIZE // 4 * 3

def encode(input, output):
    """Encode a file."""
    while True:
        s = input.read(MAXBINSIZE)
        if not s:
            break
        while len(s) < MAXBINSIZE:
            ns = input.read(MAXBINSIZE - len(s))
            if not ns:
                break
            s += ns

        line = binascii.b2a_base64(s)
        output.write(line)


def decode(input, output):
    """Decode a file."""
    while True:
        line = input.readline()
        if not line:
            break
        s = binascii.a2b_base64(line)
        output.write(s)


def encodestring(s):
    """Encode a string into multiple lines of base-64 data."""
    pieces = []
    for i in range(0, len(s), MAXBINSIZE):
        chunk = s[i:i + MAXBINSIZE]
        pieces.append(binascii.b2a_base64(chunk))

    return ''.join(pieces)


def decodestring(s):
    """Decode a string."""
    return binascii.a2b_base64(s)


def test():
    """Small test program"""
    import sys
    import getopt
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'deut')
    except getopt.error as msg:
        sys.stdout = sys.stderr
        print msg
        print "usage: %s [-d|-e|-u|-t] [file|-]\n        -d, -u: decode\n        -e: encode (default)\n        -t: encode and decode string 'Aladdin:open sesame'" % sys.argv[0]
        sys.exit(2)

    func = encode
    for o, a in opts:
        if o == '-e':
            func = encode
        if o == '-d':
            func = decode
        if o == '-u':
            func = decode
        if o == '-t':
            test1()
            return

    if args and args[0] != '-':
        with open(args[0], 'rb') as f:
            func(f, sys.stdout)
    else:
        func(sys.stdin, sys.stdout)


def test1():
    s0 = 'Aladdin:open sesame'
    s1 = encodestring(s0)
    s2 = decodestring(s1)
    print s0, repr(s1), s2


if __name__ == '__main__':
    test()