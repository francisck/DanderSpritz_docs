# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: tokenize.py
"""Tokenization help for Python programs.

generate_tokens(readline) is a generator that breaks a stream of
text into Python tokens.  It accepts a readline-like method which is called
repeatedly to get the next line of input (or "" for EOF).  It generates
5-tuples with these members:

    the token type (see token.py)
    the token (a string)
    the starting (row, column) indices of the token (a 2-tuple of ints)
    the ending (row, column) indices of the token (a 2-tuple of ints)
    the original line (string)

It is designed to match the working of the Python tokenizer exactly, except
that it produces COMMENT tokens for comments and gives type OP for all
operators

Older entry points
    tokenize_loop(readline, tokeneater)
    tokenize(readline, tokeneater=printtoken)
are the same, except instead of generating tokens, tokeneater is a callback
function to which the 5 fields described above are passed as 5 arguments,
each time a new token is found."""
__author__ = 'Ka-Ping Yee <ping@lfw.org>'
__credits__ = 'GvR, ESR, Tim Peters, Thomas Wouters, Fred Drake, Skip Montanaro'
import string
import re
from codecs import BOM_UTF8, lookup
from lib2to3.pgen2.token import *
from . import token
__all__ = [ x for x in dir(token) if x[0] != '_' ] + ['tokenize',
 'generate_tokens', 'untokenize']
del token
try:
    bytes
except NameError:
    bytes = str

def group(*choices):
    return '(' + '|'.join(choices) + ')'


def any(*choices):
    return group(*choices) + '*'


def maybe(*choices):
    return group(*choices) + '?'


Whitespace = '[ \\f\\t]*'
Comment = '#[^\\r\\n]*'
Ignore = Whitespace + any('\\\\\\r?\\n' + Whitespace) + maybe(Comment)
Name = '[a-zA-Z_]\\w*'
Binnumber = '0[bB][01]*'
Hexnumber = '0[xX][\\da-fA-F]*[lL]?'
Octnumber = '0[oO]?[0-7]*[lL]?'
Decnumber = '[1-9]\\d*[lL]?'
Intnumber = group(Binnumber, Hexnumber, Octnumber, Decnumber)
Exponent = '[eE][-+]?\\d+'
Pointfloat = group('\\d+\\.\\d*', '\\.\\d+') + maybe(Exponent)
Expfloat = '\\d+' + Exponent
Floatnumber = group(Pointfloat, Expfloat)
Imagnumber = group('\\d+[jJ]', Floatnumber + '[jJ]')
Number = group(Imagnumber, Floatnumber, Intnumber)
Single = "[^'\\\\]*(?:\\\\.[^'\\\\]*)*'"
Double = '[^"\\\\]*(?:\\\\.[^"\\\\]*)*"'
Single3 = "[^'\\\\]*(?:(?:\\\\.|'(?!''))[^'\\\\]*)*'''"
Double3 = '[^"\\\\]*(?:(?:\\\\.|"(?!""))[^"\\\\]*)*"""'
Triple = group("[ubUB]?[rR]?'''", '[ubUB]?[rR]?"""')
String = group("[uU]?[rR]?'[^\\n'\\\\]*(?:\\\\.[^\\n'\\\\]*)*'", '[uU]?[rR]?"[^\\n"\\\\]*(?:\\\\.[^\\n"\\\\]*)*"')
Operator = group('\\*\\*=?', '>>=?', '<<=?', '<>', '!=', '//=?', '->', '[+\\-*/%&|^=<>]=?', '~')
Bracket = '[][(){}]'
Special = group('\\r?\\n', '[:;.,`@]')
Funny = group(Operator, Bracket, Special)
PlainToken = group(Number, Funny, String, Name)
Token = Ignore + PlainToken
ContStr = group("[uUbB]?[rR]?'[^\\n'\\\\]*(?:\\\\.[^\\n'\\\\]*)*" + group("'", '\\\\\\r?\\n'), '[uUbB]?[rR]?"[^\\n"\\\\]*(?:\\\\.[^\\n"\\\\]*)*' + group('"', '\\\\\\r?\\n'))
PseudoExtras = group('\\\\\\r?\\n', Comment, Triple)
PseudoToken = Whitespace + group(PseudoExtras, Number, Funny, ContStr, Name)
tokenprog, pseudoprog, single3prog, double3prog = map(re.compile, (Token, PseudoToken, Single3, Double3))
endprogs = {"'": re.compile(Single),'"': re.compile(Double),"'''": single3prog,
   '"""': double3prog,"r'''": single3prog,
   'r"""': double3prog,"u'''": single3prog,
   'u"""': double3prog,"b'''": single3prog,
   'b"""': double3prog,"ur'''": single3prog,
   'ur"""': double3prog,"br'''": single3prog,
   'br"""': double3prog,"R'''": single3prog,
   'R"""': double3prog,"U'''": single3prog,
   'U"""': double3prog,"B'''": single3prog,
   'B"""': double3prog,"uR'''": single3prog,
   'uR"""': double3prog,"Ur'''": single3prog,
   'Ur"""': double3prog,"UR'''": single3prog,
   'UR"""': double3prog,"bR'''": single3prog,
   'bR"""': double3prog,"Br'''": single3prog,
   'Br"""': double3prog,"BR'''": single3prog,
   'BR"""': double3prog,'r': None,
   'R': None,'u': None,
   'U': None,'b': None,
   'B': None}
triple_quoted = {}
for t in ("'''", '"""', "r'''", 'r"""', "R'''", 'R"""', "u'''", 'u"""', "U'''", 'U"""',
          "b'''", 'b"""', "B'''", 'B"""', "ur'''", 'ur"""', "Ur'''", 'Ur"""', "uR'''",
          'uR"""', "UR'''", 'UR"""', "br'''", 'br"""', "Br'''", 'Br"""', "bR'''",
          'bR"""', "BR'''", 'BR"""'):
    triple_quoted[t] = t

single_quoted = {}
for t in ("'", '"', "r'", 'r"', "R'", 'R"', "u'", 'u"', "U'", 'U"', "b'", 'b"', "B'",
          'B"', "ur'", 'ur"', "Ur'", 'Ur"', "uR'", 'uR"', "UR'", 'UR"', "br'", 'br"',
          "Br'", 'Br"', "bR'", 'bR"', "BR'", 'BR"'):
    single_quoted[t] = t

tabsize = 8

class TokenError(Exception):
    pass


class StopTokenizing(Exception):
    pass


def printtoken(type, token, start, end, line):
    srow, scol = start
    erow, ecol = end
    print '%d,%d-%d,%d:\t%s\t%s' % (
     srow, scol, erow, ecol, tok_name[type], repr(token))


def tokenize(readline, tokeneater=printtoken):
    """
    The tokenize() function accepts two parameters: one representing the
    input stream, and one providing an output mechanism for tokenize().
    
    The first parameter, readline, must be a callable object which provides
    the same interface as the readline() method of built-in file objects.
    Each call to the function should return one line of input as a string.
    
    The second parameter, tokeneater, must also be a callable object. It is
    called once for each token, with five arguments, corresponding to the
    tuples generated by generate_tokens().
    """
    try:
        tokenize_loop(readline, tokeneater)
    except StopTokenizing:
        pass


def tokenize_loop(readline, tokeneater):
    for token_info in generate_tokens(readline):
        tokeneater(*token_info)


class Untokenizer:

    def __init__(self):
        self.tokens = []
        self.prev_row = 1
        self.prev_col = 0

    def add_whitespace(self, start):
        row, col = start
        col_offset = col - self.prev_col
        if col_offset:
            self.tokens.append(' ' * col_offset)

    def untokenize(self, iterable):
        for t in iterable:
            if len(t) == 2:
                self.compat(t, iterable)
                break
            tok_type, token, start, end, line = t
            self.add_whitespace(start)
            self.tokens.append(token)
            self.prev_row, self.prev_col = end
            if tok_type in (NEWLINE, NL):
                self.prev_row += 1
                self.prev_col = 0

        return ''.join(self.tokens)

    def compat(self, token, iterable):
        startline = False
        indents = []
        toks_append = self.tokens.append
        toknum, tokval = token
        if toknum in (NAME, NUMBER):
            tokval += ' '
        if toknum in (NEWLINE, NL):
            startline = True
        for tok in iterable:
            toknum, tokval = tok[:2]
            if toknum in (NAME, NUMBER):
                tokval += ' '
            if toknum == INDENT:
                indents.append(tokval)
                continue
            elif toknum == DEDENT:
                indents.pop()
                continue
            elif toknum in (NEWLINE, NL):
                startline = True
            elif startline and indents:
                toks_append(indents[-1])
                startline = False
            toks_append(tokval)


cookie_re = re.compile('coding[:=]\\s*([-\\w.]+)')

def _get_normal_name(orig_enc):
    """Imitates get_normal_name in tokenizer.c."""
    enc = orig_enc[:12].lower().replace('_', '-')
    if enc == 'utf-8' or enc.startswith('utf-8-'):
        return 'utf-8'
    if enc in ('latin-1', 'iso-8859-1', 'iso-latin-1') or enc.startswith(('latin-1-',
                                                                          'iso-8859-1-',
                                                                          'iso-latin-1-')):
        return 'iso-8859-1'
    return orig_enc


def detect_encoding(readline):
    """
    The detect_encoding() function is used to detect the encoding that should
    be used to decode a Python source file. It requires one argment, readline,
    in the same way as the tokenize() generator.
    
    It will call readline a maximum of twice, and return the encoding used
    (as a string) and a list of any lines (left as bytes) it has read
    in.
    
    It detects the encoding from the presence of a utf-8 bom or an encoding
    cookie as specified in pep-0263. If both a bom and a cookie are present, but
    disagree, a SyntaxError will be raised. If the encoding cookie is an invalid
    charset, raise a SyntaxError.  Note that if a utf-8 bom is found,
    'utf-8-sig' is returned.
    
    If no encoding is specified, then the default of 'utf-8' will be returned.
    """
    bom_found = False
    encoding = None
    default = 'utf-8'

    def read_or_stop():
        try:
            return readline()
        except StopIteration:
            return bytes()

    def find_cookie(line):
        try:
            line_string = line.decode('ascii')
        except UnicodeDecodeError:
            return None

        matches = cookie_re.findall(line_string)
        if not matches:
            return None
        else:
            encoding = _get_normal_name(matches[0])
            try:
                codec = lookup(encoding)
            except LookupError:
                raise SyntaxError('unknown encoding: ' + encoding)

            if bom_found:
                if codec.name != 'utf-8':
                    raise SyntaxError('encoding problem: utf-8')
                encoding += '-sig'
            return encoding

    first = read_or_stop()
    if first.startswith(BOM_UTF8):
        bom_found = True
        first = first[3:]
        default = 'utf-8-sig'
    if not first:
        return (default, [])
    else:
        encoding = find_cookie(first)
        if encoding:
            return (encoding, [first])
        second = read_or_stop()
        if not second:
            return (default, [first])
        encoding = find_cookie(second)
        if encoding:
            return (encoding, [first, second])
        return (
         default, [first, second])


def untokenize(iterable):
    """Transform tokens back into Python source code.
    
    Each element returned by the iterable must be a token sequence
    with at least two elements, a token number and token value.  If
    only two tokens are passed, the resulting output is poor.
    
    Round-trip invariant for full input:
        Untokenized source will match input source exactly
    
    Round-trip invariant for limited intput:
        # Output text will tokenize the back to the input
        t1 = [tok[:2] for tok in generate_tokens(f.readline)]
        newcode = untokenize(t1)
        readline = iter(newcode.splitlines(1)).next
        t2 = [tok[:2] for tokin generate_tokens(readline)]
        assert t1 == t2
    """
    ut = Untokenizer()
    return ut.untokenize(iterable)


def generate_tokens(readline):
    """
    The generate_tokens() generator requires one argment, readline, which
    must be a callable object which provides the same interface as the
    readline() method of built-in file objects. Each call to the function
    should return one line of input as a string.  Alternately, readline
    can be a callable function terminating with StopIteration:
        readline = open(myfile).next    # Example of alternate readline
    
    The generator produces 5-tuples with these members: the token type; the
    token string; a 2-tuple (srow, scol) of ints specifying the row and
    column where the token begins in the source; a 2-tuple (erow, ecol) of
    ints specifying the row and column where the token ends in the source;
    and the line on which the token was found. The line passed is the
    logical line; continuation lines are included.
    """
    lnum = parenlev = continued = 0
    namechars, numchars = string.ascii_letters + '_', '0123456789'
    contstr, needcont = ('', 0)
    contline = None
    indents = [0]
    while 1:
        try:
            line = readline()
        except StopIteration:
            line = ''

        lnum = lnum + 1
        pos, max = 0, len(line)
        if contstr:
            if not line:
                raise TokenError, ('EOF in multi-line string', strstart)
            endmatch = endprog.match(line)
            if endmatch:
                pos = end = endmatch.end(0)
                yield (STRING, contstr + line[:end],
                 strstart, (lnum, end), contline + line)
                contstr, needcont = ('', 0)
                contline = None
            elif needcont and line[-2:] != '\\\n' and line[-3:] != '\\\r\n':
                yield (
                 ERRORTOKEN, contstr + line,
                 strstart, (lnum, len(line)), contline)
                contstr = ''
                contline = None
                continue
            else:
                contstr = contstr + line
                contline = contline + line
                continue
        elif parenlev == 0 and not continued:
            if not line:
                break
            column = 0
            while pos < max:
                if line[pos] == ' ':
                    column = column + 1
                elif line[pos] == '\t':
                    column = (column // tabsize + 1) * tabsize
                elif line[pos] == '\x0c':
                    column = 0
                else:
                    break
                pos = pos + 1

            if pos == max:
                break
            if line[pos] in '#\r\n':
                if line[pos] == '#':
                    comment_token = line[pos:].rstrip('\r\n')
                    nl_pos = pos + len(comment_token)
                    yield (COMMENT, comment_token,
                     (
                      lnum, pos), (lnum, pos + len(comment_token)), line)
                    yield (NL, line[nl_pos:],
                     (
                      lnum, nl_pos), (lnum, len(line)), line)
                else:
                    yield (
                     (
                      NL, COMMENT)[line[pos] == '#'], line[pos:],
                     (
                      lnum, pos), (lnum, len(line)), line)
                continue
            if column > indents[-1]:
                indents.append(column)
                yield (INDENT, line[:pos], (lnum, 0), (lnum, pos), line)
            while column < indents[-1]:
                if column not in indents:
                    raise IndentationError('unindent does not match any outer indentation level', (
                     '<tokenize>', lnum, pos, line))
                indents = indents[:-1]
                yield (DEDENT, '', (lnum, pos), (lnum, pos), line)

        else:
            if not line:
                raise TokenError, ('EOF in multi-line statement', (lnum, 0))
            continued = 0
        while pos < max:
            pseudomatch = pseudoprog.match(line, pos)
            if pseudomatch:
                start, end = pseudomatch.span(1)
                spos, epos, pos = (lnum, start), (lnum, end), end
                token, initial = line[start:end], line[start]
                if initial in numchars or initial == '.' and token != '.':
                    yield (
                     NUMBER, token, spos, epos, line)
                elif initial in '\r\n':
                    newline = NEWLINE
                    if parenlev > 0:
                        newline = NL
                    yield (
                     newline, token, spos, epos, line)
                elif initial == '#':
                    yield (COMMENT, token, spos, epos, line)
                elif token in triple_quoted:
                    endprog = endprogs[token]
                    endmatch = endprog.match(line, pos)
                    if endmatch:
                        pos = endmatch.end(0)
                        token = line[start:pos]
                        yield (STRING, token, spos, (lnum, pos), line)
                    else:
                        strstart = (
                         lnum, start)
                        contstr = line[start:]
                        contline = line
                        break
                elif initial in single_quoted or token[:2] in single_quoted or token[:3] in single_quoted:
                    if token[-1] == '\n':
                        strstart = (
                         lnum, start)
                        endprog = endprogs[initial] or endprogs[token[1]] or endprogs[token[2]]
                        contstr, needcont = line[start:], 1
                        contline = line
                        break
                    else:
                        yield (
                         STRING, token, spos, epos, line)
                elif initial in namechars:
                    yield (
                     NAME, token, spos, epos, line)
                elif initial == '\\':
                    yield (NL, token, spos, (lnum, pos), line)
                    continued = 1
                else:
                    if initial in '([{':
                        parenlev = parenlev + 1
                    elif initial in ')]}':
                        parenlev = parenlev - 1
                    yield (
                     OP, token, spos, epos, line)
            else:
                yield (
                 ERRORTOKEN, line[pos],
                 (
                  lnum, pos), (lnum, pos + 1), line)
                pos = pos + 1

    for indent in indents[1:]:
        yield (
         DEDENT, '', (lnum, 0), (lnum, 0), '')

    yield (
     ENDMARKER, '', (lnum, 0), (lnum, 0), '')
    return


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        tokenize(open(sys.argv[1]).readline)
    else:
        tokenize(sys.stdin.readline)