# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: generator.py
"""Classes to generate plain text from a message object tree."""
__all__ = [
 'Generator', 'DecodedGenerator']
import re
import sys
import time
import random
import warnings
from cStringIO import StringIO
from email.header import Header
UNDERSCORE = '_'
NL = '\n'
fcre = re.compile('^From ', re.MULTILINE)

def _is8bitstring(s):
    if isinstance(s, str):
        try:
            unicode(s, 'us-ascii')
        except UnicodeError:
            return True

    return False


class Generator():
    """Generates output from a Message object tree.
    
    This basic generator writes the message to the given file object as plain
    text.
    """

    def __init__(self, outfp, mangle_from_=True, maxheaderlen=78):
        """Create the generator for message flattening.
        
        outfp is the output file-like object for writing the message to.  It
        must have a write() method.
        
        Optional mangle_from_ is a flag that, when True (the default), escapes
        From_ lines in the body of the message by putting a `>' in front of
        them.
        
        Optional maxheaderlen specifies the longest length for a non-continued
        header.  When a header line is longer (in characters, with tabs
        expanded to 8 spaces) than maxheaderlen, the header will split as
        defined in the Header class.  Set maxheaderlen to zero to disable
        header wrapping.  The default is 78, as recommended (but not required)
        by RFC 2822.
        """
        self._fp = outfp
        self._mangle_from_ = mangle_from_
        self._maxheaderlen = maxheaderlen

    def write(self, s):
        self._fp.write(s)

    def flatten(self, msg, unixfrom=False):
        """Print the message object tree rooted at msg to the output file
        specified when the Generator instance was created.
        
        unixfrom is a flag that forces the printing of a Unix From_ delimiter
        before the first object in the message tree.  If the original message
        has no From_ delimiter, a `standard' one is crafted.  By default, this
        is False to inhibit the printing of any From_ delimiter.
        
        Note that for subobjects, no From_ line is printed.
        """
        if unixfrom:
            ufrom = msg.get_unixfrom()
            if not ufrom:
                ufrom = 'From nobody ' + time.ctime(time.time())
            print >> self._fp, ufrom
        self._write(msg)

    def clone(self, fp):
        """Clone this generator with the exact same options."""
        return self.__class__(fp, self._mangle_from_, self._maxheaderlen)

    def _write(self, msg):
        oldfp = self._fp
        try:
            self._fp = sfp = StringIO()
            self._dispatch(msg)
        finally:
            self._fp = oldfp

        meth = getattr(msg, '_write_headers', None)
        if meth is None:
            self._write_headers(msg)
        else:
            meth(self)
        self._fp.write(sfp.getvalue())
        return

    def _dispatch(self, msg):
        main = msg.get_content_maintype()
        sub = msg.get_content_subtype()
        specific = UNDERSCORE.join((main, sub)).replace('-', '_')
        meth = getattr(self, '_handle_' + specific, None)
        if meth is None:
            generic = main.replace('-', '_')
            meth = getattr(self, '_handle_' + generic, None)
            if meth is None:
                meth = self._writeBody
        meth(msg)
        return

    def _write_headers(self, msg):
        for h, v in msg.items():
            print >> self._fp, '%s:' % h,
            if self._maxheaderlen == 0:
                print >> self._fp, v
            elif isinstance(v, Header):
                print >> self._fp, v.encode()
            elif _is8bitstring(v):
                print >> self._fp, v
            else:
                print >> self._fp, Header(v, maxlinelen=self._maxheaderlen, header_name=h).encode()

        print >> self._fp

    def _handle_text(self, msg):
        payload = msg.get_payload()
        if payload is None:
            return
        else:
            if not isinstance(payload, basestring):
                raise TypeError('string payload expected: %s' % type(payload))
            if self._mangle_from_:
                payload = fcre.sub('>From ', payload)
            self._fp.write(payload)
            return

    _writeBody = _handle_text

    def _handle_multipart(self, msg):
        msgtexts = []
        subparts = msg.get_payload()
        if subparts is None:
            subparts = []
        elif isinstance(subparts, basestring):
            self._fp.write(subparts)
            return
        if not isinstance(subparts, list):
            subparts = [subparts]
        for part in subparts:
            s = StringIO()
            g = self.clone(s)
            g.flatten(part, unixfrom=False)
            msgtexts.append(s.getvalue())

        boundary = msg.get_boundary()
        if not boundary:
            alltext = NL.join(msgtexts)
            boundary = _make_boundary(alltext)
            msg.set_boundary(boundary)
        if msg.preamble is not None:
            print >> self._fp, msg.preamble
        print >> self._fp, '--' + boundary
        if msgtexts:
            self._fp.write(msgtexts.pop(0))
        for body_part in msgtexts:
            print >> self._fp, '\n--' + boundary
            self._fp.write(body_part)

        self._fp.write('\n--' + boundary + '--')
        if msg.epilogue is not None:
            print >> self._fp
            self._fp.write(msg.epilogue)
        return

    def _handle_multipart_signed(self, msg):
        old_maxheaderlen = self._maxheaderlen
        try:
            self._maxheaderlen = 0
            self._handle_multipart(msg)
        finally:
            self._maxheaderlen = old_maxheaderlen

    def _handle_message_delivery_status(self, msg):
        blocks = []
        for part in msg.get_payload():
            s = StringIO()
            g = self.clone(s)
            g.flatten(part, unixfrom=False)
            text = s.getvalue()
            lines = text.split('\n')
            if lines and lines[-1] == '':
                blocks.append(NL.join(lines[:-1]))
            else:
                blocks.append(text)

        self._fp.write(NL.join(blocks))

    def _handle_message(self, msg):
        s = StringIO()
        g = self.clone(s)
        payload = msg.get_payload()
        if isinstance(payload, list):
            g.flatten(msg.get_payload(0), unixfrom=False)
            payload = s.getvalue()
        self._fp.write(payload)


_FMT = '[Non-text (%(type)s) part of message omitted, filename %(filename)s]'

class DecodedGenerator(Generator):
    """Generates a text representation of a message.
    
    Like the Generator base class, except that non-text parts are substituted
    with a format string representing the part.
    """

    def __init__(self, outfp, mangle_from_=True, maxheaderlen=78, fmt=None):
        """Like Generator.__init__() except that an additional optional
        argument is allowed.
        
        Walks through all subparts of a message.  If the subpart is of main
        type `text', then it prints the decoded payload of the subpart.
        
        Otherwise, fmt is a format string that is used instead of the message
        payload.  fmt is expanded with the following keywords (in
        %(keyword)s format):
        
        type       : Full MIME type of the non-text part
        maintype   : Main MIME type of the non-text part
        subtype    : Sub-MIME type of the non-text part
        filename   : Filename of the non-text part
        description: Description associated with the non-text part
        encoding   : Content transfer encoding of the non-text part
        
        The default value for fmt is None, meaning
        
        [Non-text (%(type)s) part of message omitted, filename %(filename)s]
        """
        Generator.__init__(self, outfp, mangle_from_, maxheaderlen)
        if fmt is None:
            self._fmt = _FMT
        else:
            self._fmt = fmt
        return

    def _dispatch(self, msg):
        for part in msg.walk():
            maintype = part.get_content_maintype()
            if maintype == 'text':
                print >> self, part.get_payload(decode=True)
            elif maintype == 'multipart':
                pass
            else:
                print >> self, self._fmt % {'type': part.get_content_type(),
                   'maintype': part.get_content_maintype(),
                   'subtype': part.get_content_subtype(),
                   'filename': part.get_filename('[no filename]'),
                   'description': part.get('Content-Description', '[no description]'),
                   'encoding': part.get('Content-Transfer-Encoding', '[no encoding]')
                   }


_width = len(repr(sys.maxint - 1))
_fmt = '%%0%dd' % _width

def _make_boundary(text=None):
    token = random.randrange(sys.maxint)
    boundary = '===============' + _fmt % token + '=='
    if text is None:
        return boundary
    else:
        b = boundary
        counter = 0
        while True:
            cre = re.compile('^--' + re.escape(b) + '(--)?$', re.MULTILINE)
            if not cre.search(text):
                break
            b = boundary + '.' + str(counter)
            counter += 1

        return b