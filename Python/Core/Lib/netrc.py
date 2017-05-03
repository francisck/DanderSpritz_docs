# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: netrc.py
"""An object-oriented interface to .netrc files."""
import os
import shlex
__all__ = [
 'netrc', 'NetrcParseError']

class NetrcParseError(Exception):
    """Exception raised on syntax errors in the .netrc file."""

    def __init__(self, msg, filename=None, lineno=None):
        self.filename = filename
        self.lineno = lineno
        self.msg = msg
        Exception.__init__(self, msg)

    def __str__(self):
        return '%s (%s, line %s)' % (self.msg, self.filename, self.lineno)


class netrc:

    def __init__(self, file=None):
        if file is None:
            try:
                file = os.path.join(os.environ['HOME'], '.netrc')
            except KeyError:
                raise IOError('Could not find .netrc: $HOME is not set')

        self.hosts = {}
        self.macros = {}
        with open(file) as fp:
            self._parse(file, fp)
        return

    def _parse(self, file, fp):
        lexer = shlex.shlex(fp)
        lexer.wordchars += '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        lexer.commenters = lexer.commenters.replace('#', '')
        while 1:
            toplevel = tt = lexer.get_token()
            if not tt:
                break
            elif tt[0] == '#':
                pos = len(tt) + 1
                lexer.instream.seek(-pos, 1)
                lexer.instream.readline()
                continue
            elif tt == 'machine':
                entryname = lexer.get_token()
            elif tt == 'default':
                entryname = 'default'
            elif tt == 'macdef':
                entryname = lexer.get_token()
                self.macros[entryname] = []
                lexer.whitespace = ' \t'
                while 1:
                    line = lexer.instream.readline()
                    if not line or line == '\n':
                        lexer.whitespace = ' \t\r\n'
                        break
                    self.macros[entryname].append(line)

                continue
            else:
                raise NetrcParseError('bad toplevel token %r' % tt, file, lexer.lineno)
            login = ''
            account = password = None
            self.hosts[entryname] = {}
            while 1:
                tt = lexer.get_token()
                if tt.startswith('#') or tt in {'', 'machine', 'default', 'macdef'}:
                    if password:
                        self.hosts[entryname] = (
                         login, account, password)
                        lexer.push_token(tt)
                        break
                    else:
                        raise NetrcParseError('malformed %s entry %s terminated by %s' % (
                         toplevel, entryname, repr(tt)), file, lexer.lineno)
                elif tt == 'login' or tt == 'user':
                    login = lexer.get_token()
                elif tt == 'account':
                    account = lexer.get_token()
                elif tt == 'password':
                    password = lexer.get_token()
                else:
                    raise NetrcParseError('bad follower token %r' % tt, file, lexer.lineno)

        return

    def authenticators(self, host):
        """Return a (user, account, password) tuple for given host."""
        if host in self.hosts:
            return self.hosts[host]
        else:
            if 'default' in self.hosts:
                return self.hosts['default']
            return None
            return None

    def __repr__(self):
        """Dump the class data in the format of a .netrc file."""
        rep = ''
        for host in self.hosts.keys():
            attrs = self.hosts[host]
            rep = rep + 'machine ' + host + '\n\tlogin ' + repr(attrs[0]) + '\n'
            if attrs[1]:
                rep = rep + 'account ' + repr(attrs[1])
            rep = rep + '\tpassword ' + repr(attrs[2]) + '\n'

        for macro in self.macros.keys():
            rep = rep + 'macdef ' + macro + '\n'
            for line in self.macros[macro]:
                rep = rep + line

            rep = rep + '\n'

        return rep


if __name__ == '__main__':
    print netrc()