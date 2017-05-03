# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: feedparser.py
"""FeedParser - An email feed parser.

The feed parser implements an interface for incrementally parsing an email
message, line by line.  This has advantages for certain applications, such as
those reading email messages off a socket.

FeedParser.feed() is the primary interface for pushing new data into the
parser.  It returns when there's nothing more it can do with the available
data.  When you have no more data to push into the parser, call .close().
This completes the parsing and returns the root message object.

The other advantage of this parser is that it will never throw a parsing
exception.  Instead, when it finds something unexpected, it adds a 'defect' to
the current message.  Defects are just instances that live on the message
object's .defects attribute.
"""
__all__ = [
 'FeedParser']
import re
from email import errors
from email import message
NLCRE = re.compile('\r\n|\r|\n')
NLCRE_bol = re.compile('(\r\n|\r|\n)')
NLCRE_eol = re.compile('(\r\n|\r|\n)\\Z')
NLCRE_crack = re.compile('(\r\n|\r|\n)')
headerRE = re.compile('^(From |[\\041-\\071\\073-\\176]{1,}:|[\\t ])')
EMPTYSTRING = ''
NL = '\n'
NeedMoreData = object()

class BufferedSubFile(object):
    """A file-ish object that can have new data loaded into it.
    
    You can also push and pop line-matching predicates onto a stack.  When the
    current predicate matches the current line, a false EOF response
    (i.e. empty string) is returned instead.  This lets the parser adhere to a
    simple abstraction -- it parses until EOF closes the current message.
    """

    def __init__(self):
        self._partial = ''
        self._lines = []
        self._eofstack = []
        self._closed = False

    def push_eof_matcher(self, pred):
        self._eofstack.append(pred)

    def pop_eof_matcher(self):
        return self._eofstack.pop()

    def close(self):
        self._lines.append(self._partial)
        self._partial = ''
        self._closed = True

    def readline(self):
        if not self._lines:
            if self._closed:
                return ''
            return NeedMoreData
        line = self._lines.pop()
        for ateof in self._eofstack[::-1]:
            if ateof(line):
                self._lines.append(line)
                return ''

        return line

    def unreadline(self, line):
        self._lines.append(line)

    def push(self, data):
        """Push some new data into this object."""
        data, self._partial = self._partial + data, ''
        parts = NLCRE_crack.split(data)
        self._partial = parts.pop()
        if not self._partial and parts and parts[-1].endswith('\r'):
            self._partial = parts.pop(-2) + parts.pop()
        lines = []
        for i in range(len(parts) // 2):
            lines.append(parts[i * 2] + parts[i * 2 + 1])

        self.pushlines(lines)

    def pushlines(self, lines):
        self._lines[:0] = lines[::-1]

    def is_closed(self):
        return self._closed

    def __iter__(self):
        return self

    def next(self):
        line = self.readline()
        if line == '':
            raise StopIteration
        return line


class FeedParser:
    """A feed-style parser of email."""

    def __init__(self, _factory=message.Message):
        """_factory is called with no arguments to create a new message obj"""
        self._factory = _factory
        self._input = BufferedSubFile()
        self._msgstack = []
        self._parse = self._parsegen().next
        self._cur = None
        self._last = None
        self._headersonly = False
        return

    def _set_headersonly(self):
        self._headersonly = True

    def feed(self, data):
        """Push more data into the parser."""
        self._input.push(data)
        self._call_parse()

    def _call_parse(self):
        try:
            self._parse()
        except StopIteration:
            pass

    def close(self):
        """Parse all remaining data and return the root message object."""
        self._input.close()
        self._call_parse()
        root = self._pop_message()
        if root.get_content_maintype() == 'multipart' and not root.is_multipart():
            root.defects.append(errors.MultipartInvariantViolationDefect())
        return root

    def _new_message(self):
        msg = self._factory()
        if self._cur and self._cur.get_content_type() == 'multipart/digest':
            msg.set_default_type('message/rfc822')
        if self._msgstack:
            self._msgstack[-1].attach(msg)
        self._msgstack.append(msg)
        self._cur = msg
        self._last = msg

    def _pop_message(self):
        retval = self._msgstack.pop()
        if self._msgstack:
            self._cur = self._msgstack[-1]
        else:
            self._cur = None
        return retval

    def _parsegen(self):
        self._new_message()
        headers = []
        for line in self._input:
            if line is NeedMoreData:
                yield NeedMoreData
                continue
            if not headerRE.match(line):
                if not NLCRE.match(line):
                    self._input.unreadline(line)
                break
            headers.append(line)

        self._parse_headers(headers)
        if self._headersonly:
            lines = []
            while True:
                line = self._input.readline()
                if line is NeedMoreData:
                    yield NeedMoreData
                    continue
                if line == '':
                    break
                lines.append(line)

            self._cur.set_payload(EMPTYSTRING.join(lines))
            return
        else:
            if self._cur.get_content_type() == 'message/delivery-status':
                while True:
                    self._input.push_eof_matcher(NLCRE.match)
                    for retval in self._parsegen():
                        if retval is NeedMoreData:
                            yield NeedMoreData
                            continue
                        break

                    msg = self._pop_message()
                    self._input.pop_eof_matcher()
                    while True:
                        line = self._input.readline()
                        if line is NeedMoreData:
                            yield NeedMoreData
                            continue
                        break

                    while True:
                        line = self._input.readline()
                        if line is NeedMoreData:
                            yield NeedMoreData
                            continue
                        break

                    if line == '':
                        break
                    self._input.unreadline(line)

                return
            if self._cur.get_content_maintype() == 'message':
                for retval in self._parsegen():
                    if retval is NeedMoreData:
                        yield NeedMoreData
                        continue
                    break

                self._pop_message()
                return
            if self._cur.get_content_maintype() == 'multipart':
                boundary = self._cur.get_boundary()
                if boundary is None:
                    self._cur.defects.append(errors.NoBoundaryInMultipartDefect())
                    lines = []
                    for line in self._input:
                        if line is NeedMoreData:
                            yield NeedMoreData
                            continue
                        lines.append(line)

                    self._cur.set_payload(EMPTYSTRING.join(lines))
                    return
                separator = '--' + boundary
                boundaryre = re.compile('(?P<sep>' + re.escape(separator) + ')(?P<end>--)?(?P<ws>[ \\t]*)(?P<linesep>\\r\\n|\\r|\\n)?$')
                capturing_preamble = True
                preamble = []
                linesep = False
                while True:
                    line = self._input.readline()
                    if line is NeedMoreData:
                        yield NeedMoreData
                        continue
                    if line == '':
                        break
                    mo = boundaryre.match(line)
                    if mo:
                        if mo.group('end'):
                            linesep = mo.group('linesep')
                            break
                        if capturing_preamble:
                            if preamble:
                                lastline = preamble[-1]
                                eolmo = NLCRE_eol.search(lastline)
                                if eolmo:
                                    preamble[-1] = lastline[:-len(eolmo.group(0))]
                                self._cur.preamble = EMPTYSTRING.join(preamble)
                            capturing_preamble = False
                            self._input.unreadline(line)
                            continue
                        while True:
                            line = self._input.readline()
                            if line is NeedMoreData:
                                yield NeedMoreData
                                continue
                            mo = boundaryre.match(line)
                            if not mo:
                                self._input.unreadline(line)
                                break

                        self._input.push_eof_matcher(boundaryre.match)
                        for retval in self._parsegen():
                            if retval is NeedMoreData:
                                yield NeedMoreData
                                continue
                            break

                        if self._last.get_content_maintype() == 'multipart':
                            epilogue = self._last.epilogue
                            if epilogue == '':
                                self._last.epilogue = None
                            elif epilogue is not None:
                                mo = NLCRE_eol.search(epilogue)
                                if mo:
                                    end = len(mo.group(0))
                                    self._last.epilogue = epilogue[:-end]
                        else:
                            payload = self._last.get_payload()
                            if isinstance(payload, basestring):
                                mo = NLCRE_eol.search(payload)
                                if mo:
                                    payload = payload[:-len(mo.group(0))]
                                    self._last.set_payload(payload)
                        self._input.pop_eof_matcher()
                        self._pop_message()
                        self._last = self._cur
                    else:
                        preamble.append(line)

                if capturing_preamble:
                    self._cur.defects.append(errors.StartBoundaryNotFoundDefect())
                    self._cur.set_payload(EMPTYSTRING.join(preamble))
                    epilogue = []
                    for line in self._input:
                        if line is NeedMoreData:
                            yield NeedMoreData
                            continue

                    self._cur.epilogue = EMPTYSTRING.join(epilogue)
                    return
                if linesep:
                    epilogue = [
                     '']
                else:
                    epilogue = []
                for line in self._input:
                    if line is NeedMoreData:
                        yield NeedMoreData
                        continue
                    epilogue.append(line)

                if epilogue:
                    firstline = epilogue[0]
                    bolmo = NLCRE_bol.match(firstline)
                    if bolmo:
                        epilogue[0] = firstline[len(bolmo.group(0)):]
                self._cur.epilogue = EMPTYSTRING.join(epilogue)
                return
            lines = []
            for line in self._input:
                if line is NeedMoreData:
                    yield NeedMoreData
                    continue
                lines.append(line)

            self._cur.set_payload(EMPTYSTRING.join(lines))
            return

    def _parse_headers(self, lines):
        lastheader = ''
        lastvalue = []
        for lineno, line in enumerate(lines):
            if line[0] in ' \t':
                if not lastheader:
                    defect = errors.FirstHeaderLineIsContinuationDefect(line)
                    self._cur.defects.append(defect)
                    continue
                lastvalue.append(line)
                continue
            if lastheader:
                lhdr = EMPTYSTRING.join(lastvalue)[:-1].rstrip('\r\n')
                self._cur[lastheader] = lhdr
                lastheader, lastvalue = '', []
            if line.startswith('From '):
                if lineno == 0:
                    mo = NLCRE_eol.search(line)
                    if mo:
                        line = line[:-len(mo.group(0))]
                    self._cur.set_unixfrom(line)
                    continue
                else:
                    if lineno == len(lines) - 1:
                        self._input.unreadline(line)
                        return
                    defect = errors.MisplacedEnvelopeHeaderDefect(line)
                    self._cur.defects.append(defect)
                    continue
            i = line.find(':')
            if i < 0:
                defect = errors.MalformedHeaderDefect(line)
                self._cur.defects.append(defect)
                continue
            lastheader = line[:i]
            lastvalue = [line[i + 1:].lstrip()]

        if lastheader:
            self._cur[lastheader] = EMPTYSTRING.join(lastvalue).rstrip('\r\n')