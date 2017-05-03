# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: tabnanny.py
"""The Tab Nanny despises ambiguous indentation.  She knows no mercy.

tabnanny -- Detection of ambiguous indentation

For the time being this module is intended to be called as a script.
However it is possible to import it into an IDE and use the function
check() described below.

Warning: The API provided by this module is likely to change in future
releases; such changes may not be backward compatible.
"""
__version__ = '6'
import os
import sys
import getopt
import tokenize
if not hasattr(tokenize, 'NL'):
    raise ValueError("tokenize.NL doesn't exist -- tokenize module too old")
__all__ = ['check', 'NannyNag', 'process_tokens']
verbose = 0
filename_only = 0

def errprint(*args):
    sep = ''
    for arg in args:
        sys.stderr.write(sep + str(arg))
        sep = ' '

    sys.stderr.write('\n')


def main():
    global verbose
    global filename_only
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'qv')
    except getopt.error as msg:
        errprint(msg)
        return

    for o, a in opts:
        if o == '-q':
            filename_only = filename_only + 1
        if o == '-v':
            verbose = verbose + 1

    if not args:
        errprint('Usage:', sys.argv[0], '[-v] file_or_directory ...')
        return
    for arg in args:
        check(arg)


class NannyNag(Exception):
    """
    Raised by tokeneater() if detecting an ambiguous indent.
    Captured and handled in check().
    """

    def __init__(self, lineno, msg, line):
        self.lineno, self.msg, self.line = lineno, msg, line

    def get_lineno(self):
        return self.lineno

    def get_msg(self):
        return self.msg

    def get_line(self):
        return self.line


def check(file):
    """check(file_or_dir)
    
    If file_or_dir is a directory and not a symbolic link, then recursively
    descend the directory tree named by file_or_dir, checking all .py files
    along the way. If file_or_dir is an ordinary Python source file, it is
    checked for whitespace related problems. The diagnostic messages are
    written to standard output using the print statement.
    """
    if os.path.isdir(file) and not os.path.islink(file):
        if verbose:
            print '%r: listing directory' % (file,)
        names = os.listdir(file)
        for name in names:
            fullname = os.path.join(file, name)
            if os.path.isdir(fullname) and not os.path.islink(fullname) or os.path.normcase(name[-3:]) == '.py':
                check(fullname)

        return
    try:
        f = open(file)
    except IOError as msg:
        errprint('%r: I/O Error: %s' % (file, msg))
        return

    if verbose > 1:
        print 'checking %r ...' % file
    try:
        process_tokens(tokenize.generate_tokens(f.readline))
    except tokenize.TokenError as msg:
        errprint('%r: Token Error: %s' % (file, msg))
        return
    except IndentationError as msg:
        errprint('%r: Indentation Error: %s' % (file, msg))
        return
    except NannyNag as nag:
        badline = nag.get_lineno()
        line = nag.get_line()
        if verbose:
            print '%r: *** Line %d: trouble in tab city! ***' % (file, badline)
            print 'offending line: %r' % (line,)
            print nag.get_msg()
        else:
            if ' ' in file:
                file = '"' + file + '"'
            if filename_only:
                print file
            else:
                print file, badline, repr(line)
        return

    if verbose:
        print '%r: Clean bill of health.' % (file,)


class Whitespace:
    S, T = ' \t'

    def __init__(self, ws):
        self.raw = ws
        S, T = Whitespace.S, Whitespace.T
        count = []
        b = n = nt = 0
        for ch in self.raw:
            if ch == S:
                n = n + 1
                b = b + 1
            elif ch == T:
                n = n + 1
                nt = nt + 1
                if b >= len(count):
                    count = count + [0] * (b - len(count) + 1)
                count[b] = count[b] + 1
                b = 0
            else:
                break

        self.n = n
        self.nt = nt
        self.norm = (tuple(count), b)
        self.is_simple = len(count) <= 1

    def longest_run_of_spaces(self):
        count, trailing = self.norm
        return max(len(count) - 1, trailing)

    def indent_level(self, tabsize):
        count, trailing = self.norm
        il = 0
        for i in range(tabsize, len(count)):
            il = il + i / tabsize * count[i]

        return trailing + tabsize * (il + self.nt)

    def equal(self, other):
        return self.norm == other.norm

    def not_equal_witness(self, other):
        n = max(self.longest_run_of_spaces(), other.longest_run_of_spaces()) + 1
        a = []
        for ts in range(1, n + 1):
            if self.indent_level(ts) != other.indent_level(ts):
                a.append((ts,
                 self.indent_level(ts),
                 other.indent_level(ts)))

        return a

    def less(self, other):
        if self.n >= other.n:
            return False
        if self.is_simple and other.is_simple:
            return self.nt <= other.nt
        n = max(self.longest_run_of_spaces(), other.longest_run_of_spaces()) + 1
        for ts in range(2, n + 1):
            if self.indent_level(ts) >= other.indent_level(ts):
                return False

        return True

    def not_less_witness(self, other):
        n = max(self.longest_run_of_spaces(), other.longest_run_of_spaces()) + 1
        a = []
        for ts in range(1, n + 1):
            if self.indent_level(ts) >= other.indent_level(ts):
                a.append((ts,
                 self.indent_level(ts),
                 other.indent_level(ts)))

        return a


def format_witnesses(w):
    firsts = map(lambda tup: str(tup[0]), w)
    prefix = 'at tab size'
    if len(w) > 1:
        prefix = prefix + 's'
    return prefix + ' ' + ', '.join(firsts)


def process_tokens(tokens):
    INDENT = tokenize.INDENT
    DEDENT = tokenize.DEDENT
    NEWLINE = tokenize.NEWLINE
    JUNK = (tokenize.COMMENT, tokenize.NL)
    indents = [Whitespace('')]
    check_equal = 0
    for type, token, start, end, line in tokens:
        if type == NEWLINE:
            check_equal = 1
        elif type == INDENT:
            check_equal = 0
            thisguy = Whitespace(token)
            if not indents[-1].less(thisguy):
                witness = indents[-1].not_less_witness(thisguy)
                msg = 'indent not greater e.g. ' + format_witnesses(witness)
                raise NannyNag(start[0], msg, line)
            indents.append(thisguy)
        elif type == DEDENT:
            check_equal = 1
            del indents[-1]
        elif check_equal and type not in JUNK:
            check_equal = 0
            thisguy = Whitespace(line)
            if not indents[-1].equal(thisguy):
                witness = indents[-1].not_equal_witness(thisguy)
                msg = 'indent not equal e.g. ' + format_witnesses(witness)
                raise NannyNag(start[0], msg, line)


if __name__ == '__main__':
    main()