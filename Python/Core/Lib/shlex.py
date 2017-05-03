# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: shlex.py
"""A lexical analyzer class for simple shell-like syntaxes."""
import os.path
import sys
from collections import deque
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

__all__ = [
 'shlex', 'split']

class shlex:
    """A lexical analyzer class for simple shell-like syntaxes."""

    def __init__(self, instream=None, infile=None, posix=False):
        if isinstance(instream, basestring):
            instream = StringIO(instream)
        if instream is not None:
            self.instream = instream
            self.infile = infile
        else:
            self.instream = sys.stdin
            self.infile = None
        self.posix = posix
        if posix:
            self.eof = None
        else:
            self.eof = ''
        self.commenters = '#'
        self.wordchars = 'abcdfeghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
        if self.posix:
            self.wordchars += '\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd8\xd9\xda\xdb\xdc\xdd\xde'
        self.whitespace = ' \t\r\n'
        self.whitespace_split = False
        self.quotes = '\'"'
        self.escape = '\\'
        self.escapedquotes = '"'
        self.state = ' '
        self.pushback = deque()
        self.lineno = 1
        self.debug = 0
        self.token = ''
        self.filestack = deque()
        self.source = None
        if self.debug:
            print 'shlex: reading from %s, line %d' % (
             self.instream, self.lineno)
        return

    def push_token(self, tok):
        """Push a token onto the stack popped by the get_token method"""
        if self.debug >= 1:
            print 'shlex: pushing token ' + repr(tok)
        self.pushback.appendleft(tok)

    def push_source(self, newstream, newfile=None):
        """Push an input source onto the lexer's input source stack."""
        if isinstance(newstream, basestring):
            newstream = StringIO(newstream)
        self.filestack.appendleft((self.infile, self.instream, self.lineno))
        self.infile = newfile
        self.instream = newstream
        self.lineno = 1
        if self.debug:
            if newfile is not None:
                print 'shlex: pushing to file %s' % (self.infile,)
            else:
                print 'shlex: pushing to stream %s' % (self.instream,)
        return

    def pop_source(self):
        """Pop the input source stack."""
        self.instream.close()
        self.infile, self.instream, self.lineno = self.filestack.popleft()
        if self.debug:
            print 'shlex: popping to %s, line %d' % (
             self.instream, self.lineno)
        self.state = ' '

    def get_token(self):
        """Get a token from the input stream (or from stack if it's nonempty)"""
        if self.pushback:
            tok = self.pushback.popleft()
            if self.debug >= 1:
                print 'shlex: popping token ' + repr(tok)
            return tok
        else:
            raw = self.read_token()
            if self.source is not None:
                while raw == self.source:
                    spec = self.sourcehook(self.read_token())
                    if spec:
                        newfile, newstream = spec
                        self.push_source(newstream, newfile)
                    raw = self.get_token()

            while raw == self.eof:
                if not self.filestack:
                    return self.eof
                self.pop_source()
                raw = self.get_token()

            if self.debug >= 1:
                if raw != self.eof:
                    print 'shlex: token=' + repr(raw)
                else:
                    print 'shlex: token=EOF'
            return raw

    def read_token(self):
        quoted = False
        escapedstate = ' '
        while True:
            nextchar = self.instream.read(1)
            if nextchar == '\n':
                self.lineno = self.lineno + 1
            if self.debug >= 3:
                print 'shlex: in state', repr(self.state),
                print 'I see character:', repr(nextchar)
            if self.state is None:
                self.token = ''
                break
            elif self.state == ' ':
                if not nextchar:
                    self.state = None
                    break
                elif nextchar in self.whitespace:
                    if self.debug >= 2:
                        print 'shlex: I see whitespace in whitespace state'
                    if self.token or self.posix and quoted:
                        break
                    else:
                        continue
                elif nextchar in self.commenters:
                    self.instream.readline()
                    self.lineno = self.lineno + 1
                elif self.posix and nextchar in self.escape:
                    escapedstate = 'a'
                    self.state = nextchar
                elif nextchar in self.wordchars:
                    self.token = nextchar
                    self.state = 'a'
                elif nextchar in self.quotes:
                    if not self.posix:
                        self.token = nextchar
                    self.state = nextchar
                elif self.whitespace_split:
                    self.token = nextchar
                    self.state = 'a'
                else:
                    self.token = nextchar
                    if self.token or self.posix and quoted:
                        break
                    else:
                        continue
            elif self.state in self.quotes:
                quoted = True
                if not nextchar:
                    if self.debug >= 2:
                        print 'shlex: I see EOF in quotes state'
                    raise ValueError, 'No closing quotation'
                if nextchar == self.state:
                    if not self.posix:
                        self.token = self.token + nextchar
                        self.state = ' '
                        break
                    else:
                        self.state = 'a'
                elif self.posix and nextchar in self.escape and self.state in self.escapedquotes:
                    escapedstate = self.state
                    self.state = nextchar
                else:
                    self.token = self.token + nextchar
            elif self.state in self.escape:
                if not nextchar:
                    if self.debug >= 2:
                        print 'shlex: I see EOF in escape state'
                    raise ValueError, 'No escaped character'
                if escapedstate in self.quotes and nextchar != self.state and nextchar != escapedstate:
                    self.token = self.token + self.state
                self.token = self.token + nextchar
                self.state = escapedstate
            elif self.state == 'a':
                if not nextchar:
                    self.state = None
                    break
                elif nextchar in self.whitespace:
                    if self.debug >= 2:
                        print 'shlex: I see whitespace in word state'
                    self.state = ' '
                    if self.token or self.posix and quoted:
                        break
                    else:
                        continue
                elif nextchar in self.commenters:
                    self.instream.readline()
                    self.lineno = self.lineno + 1
                    if self.posix:
                        self.state = ' '
                        if self.token or self.posix and quoted:
                            break
                        else:
                            continue
                elif self.posix and nextchar in self.quotes:
                    self.state = nextchar
                elif self.posix and nextchar in self.escape:
                    escapedstate = 'a'
                    self.state = nextchar
                elif nextchar in self.wordchars or nextchar in self.quotes or self.whitespace_split:
                    self.token = self.token + nextchar
                else:
                    self.pushback.appendleft(nextchar)
                    if self.debug >= 2:
                        print 'shlex: I see punctuation in word state'
                    self.state = ' '
                    if self.token:
                        break
                    else:
                        continue

        result = self.token
        self.token = ''
        if self.posix and not quoted and result == '':
            result = None
        if self.debug > 1:
            if result:
                print 'shlex: raw token=' + repr(result)
            else:
                print 'shlex: raw token=EOF'
        return result

    def sourcehook(self, newfile):
        """Hook called on a filename to be sourced."""
        if newfile[0] == '"':
            newfile = newfile[1:-1]
        if isinstance(self.infile, basestring) and not os.path.isabs(newfile):
            newfile = os.path.join(os.path.dirname(self.infile), newfile)
        return (newfile, open(newfile, 'r'))

    def error_leader(self, infile=None, lineno=None):
        """Emit a C-compiler-like, Emacs-friendly error-message leader."""
        if infile is None:
            infile = self.infile
        if lineno is None:
            lineno = self.lineno
        return '"%s", line %d: ' % (infile, lineno)

    def __iter__(self):
        return self

    def next(self):
        token = self.get_token()
        if token == self.eof:
            raise StopIteration
        return token


def split(s, comments=False, posix=True):
    lex = shlex(s, posix=posix)
    lex.whitespace_split = True
    if not comments:
        lex.commenters = ''
    return list(lex)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        lexer = shlex()
    else:
        file = sys.argv[1]
        lexer = shlex(open(file), file)
    while 1:
        tt = lexer.get_token()
        if tt:
            print 'Token: ' + repr(tt)
        else:
            break