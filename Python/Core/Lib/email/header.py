# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: header.py
"""Header encoding and decoding functionality."""
__all__ = [
 'Header',
 'decode_header',
 'make_header']
import re
import binascii
import email.quoprimime
import email.base64mime
from email.errors import HeaderParseError
from email.charset import Charset
NL = '\n'
SPACE = ' '
USPACE = u' '
SPACE8 = ' ' * 8
UEMPTYSTRING = u''
MAXLINELEN = 76
USASCII = Charset('us-ascii')
UTF8 = Charset('utf-8')
ecre = re.compile('\n  =\\?                   # literal =?\n  (?P<charset>[^?]*?)   # non-greedy up to the next ? is the charset\n  \\?                    # literal ?\n  (?P<encoding>[qb])    # either a "q" or a "b", case insensitive\n  \\?                    # literal ?\n  (?P<encoded>.*?)      # non-greedy up to the next ?= is the encoded string\n  \\?=                   # literal ?=\n  (?=[ \\t]|$)           # whitespace or the end of the string\n  ', re.VERBOSE | re.IGNORECASE | re.MULTILINE)
fcre = re.compile('[\\041-\\176]+:$')
_embeded_header = re.compile('\\n[^ \\t]+:')
_max_append = email.quoprimime._max_append

def decode_header(header):
    """Decode a message header value without converting charset.
    
    Returns a list of (decoded_string, charset) pairs containing each of the
    decoded parts of the header.  Charset is None for non-encoded parts of the
    header, otherwise a lower-case string containing the name of the character
    set specified in the encoded string.
    
    An email.errors.HeaderParseError may be raised when certain decoding error
    occurs (e.g. a base64 decoding exception).
    """
    header = str(header)
    if not ecre.search(header):
        return [(header, None)]
    else:
        decoded = []
        dec = ''
        for line in header.splitlines():
            if not ecre.search(line):
                decoded.append((line, None))
                continue
            parts = ecre.split(line)
            while parts:
                unenc = parts.pop(0).strip()
                if unenc:
                    if decoded and decoded[-1][1] is None:
                        decoded[-1] = (
                         decoded[-1][0] + SPACE + unenc, None)
                    else:
                        decoded.append((unenc, None))
                if parts:
                    charset, encoding = [ s.lower() for s in parts[0:2] ]
                    encoded = parts[2]
                    dec = None
                    if encoding == 'q':
                        dec = email.quoprimime.header_decode(encoded)
                    elif encoding == 'b':
                        paderr = len(encoded) % 4
                        if paderr:
                            encoded += '==='[:4 - paderr]
                        try:
                            dec = email.base64mime.decode(encoded)
                        except binascii.Error:
                            raise HeaderParseError

                    if dec is None:
                        dec = encoded
                    if decoded and decoded[-1][1] == charset:
                        decoded[-1] = (
                         decoded[-1][0] + dec, decoded[-1][1])
                    else:
                        decoded.append((dec, charset))
                del parts[0:3]

        return decoded


def make_header(decoded_seq, maxlinelen=None, header_name=None, continuation_ws=' '):
    """Create a Header from a sequence of pairs as returned by decode_header()
    
    decode_header() takes a header value string and returns a sequence of
    pairs of the format (decoded_string, charset) where charset is the string
    name of the character set.
    
    This function takes one of those sequence of pairs and returns a Header
    instance.  Optional maxlinelen, header_name, and continuation_ws are as in
    the Header constructor.
    """
    h = Header(maxlinelen=maxlinelen, header_name=header_name, continuation_ws=continuation_ws)
    for s, charset in decoded_seq:
        if charset is not None and not isinstance(charset, Charset):
            charset = Charset(charset)
        h.append(s, charset)

    return h


class Header():

    def __init__(self, s=None, charset=None, maxlinelen=None, header_name=None, continuation_ws=' ', errors='strict'):
        """Create a MIME-compliant header that can contain many character sets.
        
        Optional s is the initial header value.  If None, the initial header
        value is not set.  You can later append to the header with .append()
        method calls.  s may be a byte string or a Unicode string, but see the
        .append() documentation for semantics.
        
        Optional charset serves two purposes: it has the same meaning as the
        charset argument to the .append() method.  It also sets the default
        character set for all subsequent .append() calls that omit the charset
        argument.  If charset is not provided in the constructor, the us-ascii
        charset is used both as s's initial charset and as the default for
        subsequent .append() calls.
        
        The maximum line length can be specified explicit via maxlinelen.  For
        splitting the first line to a shorter value (to account for the field
        header which isn't included in s, e.g. `Subject') pass in the name of
        the field in header_name.  The default maxlinelen is 76.
        
        continuation_ws must be RFC 2822 compliant folding whitespace (usually
        either a space or a hard tab) which will be prepended to continuation
        lines.
        
        errors is passed through to the .append() call.
        """
        if charset is None:
            charset = USASCII
        if not isinstance(charset, Charset):
            charset = Charset(charset)
        self._charset = charset
        self._continuation_ws = continuation_ws
        cws_expanded_len = len(continuation_ws.replace('\t', SPACE8))
        self._chunks = []
        if s is not None:
            self.append(s, charset, errors)
        if maxlinelen is None:
            maxlinelen = MAXLINELEN
        if header_name is None:
            self._firstlinelen = maxlinelen
        else:
            self._firstlinelen = maxlinelen - len(header_name) - 2
        self._maxlinelen = maxlinelen - cws_expanded_len
        return

    def __str__(self):
        """A synonym for self.encode()."""
        return self.encode()

    def __unicode__(self):
        """Helper for the built-in unicode function."""
        uchunks = []
        lastcs = None
        for s, charset in self._chunks:
            nextcs = charset
            if uchunks:
                if lastcs not in (None, 'us-ascii'):
                    if nextcs in (None, 'us-ascii'):
                        uchunks.append(USPACE)
                        nextcs = None
                elif nextcs not in (None, 'us-ascii'):
                    uchunks.append(USPACE)
            lastcs = nextcs
            uchunks.append(unicode(s, str(charset)))

        return UEMPTYSTRING.join(uchunks)

    def __eq__(self, other):
        return other == self.encode()

    def __ne__(self, other):
        return not self == other

    def append(self, s, charset=None, errors='strict'):
        """Append a string to the MIME header.
        
        Optional charset, if given, should be a Charset instance or the name
        of a character set (which will be converted to a Charset instance).  A
        value of None (the default) means that the charset given in the
        constructor is used.
        
        s may be a byte string or a Unicode string.  If it is a byte string
        (i.e. isinstance(s, str) is true), then charset is the encoding of
        that byte string, and a UnicodeError will be raised if the string
        cannot be decoded with that charset.  If s is a Unicode string, then
        charset is a hint specifying the character set of the characters in
        the string.  In this case, when producing an RFC 2822 compliant header
        using RFC 2047 rules, the Unicode string will be encoded using the
        following charsets in order: us-ascii, the charset hint, utf-8.  The
        first character set not to provoke a UnicodeError is used.
        
        Optional `errors' is passed as the third argument to any unicode() or
        ustr.encode() call.
        """
        if charset is None:
            charset = self._charset
        elif not isinstance(charset, Charset):
            charset = Charset(charset)
        if charset != '8bit':
            if isinstance(s, str):
                incodec = charset.input_codec or 'us-ascii'
                ustr = unicode(s, incodec, errors)
                outcodec = charset.output_codec or 'us-ascii'
                ustr.encode(outcodec, errors)
            elif isinstance(s, unicode):
                for charset in (USASCII, charset, UTF8):
                    try:
                        outcodec = charset.output_codec or 'us-ascii'
                        s = s.encode(outcodec, errors)
                        break
                    except UnicodeError:
                        pass

        self._chunks.append((s, charset))
        return

    def _split(self, s, charset, maxlinelen, splitchars):
        splittable = charset.to_splittable(s)
        encoded = charset.from_splittable(splittable, True)
        elen = charset.encoded_header_len(encoded)
        if elen <= maxlinelen:
            return [(encoded, charset)]
        if charset == '8bit':
            return [(s, charset)]
        if charset == 'us-ascii':
            return self._split_ascii(s, charset, maxlinelen, splitchars)
        if elen == len(s):
            splitpnt = maxlinelen
            first = charset.from_splittable(splittable[:splitpnt], False)
            last = charset.from_splittable(splittable[splitpnt:], False)
        else:
            first, last = _binsplit(splittable, charset, maxlinelen)
        fsplittable = charset.to_splittable(first)
        fencoded = charset.from_splittable(fsplittable, True)
        chunk = [(fencoded, charset)]
        return chunk + self._split(last, charset, self._maxlinelen, splitchars)

    def _split_ascii(self, s, charset, firstlen, splitchars):
        chunks = _split_ascii(s, firstlen, self._maxlinelen, self._continuation_ws, splitchars)
        return zip(chunks, [charset] * len(chunks))

    def _encode_chunks(self, newchunks, maxlinelen):
        chunks = []
        for header, charset in newchunks:
            if not header:
                continue
            if charset is None or charset.header_encoding is None:
                s = header
            else:
                s = charset.header_encode(header)
            if chunks and chunks[-1].endswith(' '):
                extra = ''
            else:
                extra = ' '
            _max_append(chunks, s, maxlinelen, extra)

        joiner = NL + self._continuation_ws
        return joiner.join(chunks)

    def encode(self, splitchars=';, '):
        """Encode a message header into an RFC-compliant format.
        
        There are many issues involved in converting a given string for use in
        an email header.  Only certain character sets are readable in most
        email clients, and as header strings can only contain a subset of
        7-bit ASCII, care must be taken to properly convert and encode (with
        Base64 or quoted-printable) header strings.  In addition, there is a
        75-character length limit on any given encoded header field, so
        line-wrapping must be performed, even with double-byte character sets.
        
        This method will do its best to convert the string to the correct
        character set used in email, and encode and line wrap it safely with
        the appropriate scheme for that character set.
        
        If the given charset is not known or an error occurs during
        conversion, this function will return the header untouched.
        
        Optional splitchars is a string containing characters to split long
        ASCII lines on, in rough support of RFC 2822's `highest level
        syntactic breaks'.  This doesn't affect RFC 2047 encoded lines.
        """
        newchunks = []
        maxlinelen = self._firstlinelen
        lastlen = 0
        for s, charset in self._chunks:
            targetlen = maxlinelen - lastlen - 1
            if targetlen < charset.encoded_header_len(''):
                targetlen = maxlinelen
            newchunks += self._split(s, charset, targetlen, splitchars)
            lastchunk, lastcharset = newchunks[-1]
            lastlen = lastcharset.encoded_header_len(lastchunk)

        value = self._encode_chunks(newchunks, maxlinelen)
        if _embeded_header.search(value):
            raise HeaderParseError('header value appears to contain an embedded header: {!r}'.format(value))
        return value


def _split_ascii(s, firstlen, restlen, continuation_ws, splitchars):
    lines = []
    maxlen = firstlen
    for line in s.splitlines():
        line = line.lstrip()
        if len(line) < maxlen:
            lines.append(line)
            maxlen = restlen
            continue
        for ch in splitchars:
            if ch in line:
                break
        else:
            lines.append(line)
            maxlen = restlen
            continue

        cre = re.compile('%s\\s*' % ch)
        if ch in ';,':
            eol = ch
        else:
            eol = ''
        joiner = eol + ' '
        joinlen = len(joiner)
        wslen = len(continuation_ws.replace('\t', SPACE8))
        this = []
        linelen = 0
        for part in cre.split(line):
            curlen = linelen + max(0, len(this) - 1) * joinlen
            partlen = len(part)
            onfirstline = not lines
            if ch == ' ' and onfirstline and len(this) == 1 and fcre.match(this[0]):
                this.append(part)
                linelen += partlen
            elif curlen + partlen > maxlen:
                if this:
                    lines.append(joiner.join(this) + eol)
                if partlen > maxlen and ch != ' ':
                    subl = _split_ascii(part, maxlen, restlen, continuation_ws, ' ')
                    lines.extend(subl[:-1])
                    this = [subl[-1]]
                else:
                    this = [
                     part]
                linelen = wslen + len(this[-1])
                maxlen = restlen
            else:
                this.append(part)
                linelen += partlen

        if this:
            lines.append(joiner.join(this))

    return lines


def _binsplit(splittable, charset, maxlinelen):
    i = 0
    j = len(splittable)
    while i < j:
        m = i + j + 1 >> 1
        chunk = charset.from_splittable(splittable[:m], True)
        chunklen = charset.encoded_header_len(chunk)
        if chunklen <= maxlinelen:
            i = m
        else:
            j = m - 1

    first = charset.from_splittable(splittable[:i], False)
    last = charset.from_splittable(splittable[i:], False)
    return (
     first, last)