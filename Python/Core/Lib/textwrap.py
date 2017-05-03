# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: textwrap.py
"""Text wrapping and filling.
"""
__revision__ = '$Id$'
import string
import re
__all__ = [
 'TextWrapper', 'wrap', 'fill', 'dedent']
_whitespace = '\t\n\x0b\x0c\r '

class TextWrapper():
    """
    Object for wrapping/filling text.  The public interface consists of
    the wrap() and fill() methods; the other methods are just there for
    subclasses to override in order to tweak the default behaviour.
    If you want to completely replace the main wrapping algorithm,
    you'll probably have to override _wrap_chunks().
    
    Several instance attributes control various aspects of wrapping:
      width (default: 70)
        the maximum width of wrapped lines (unless break_long_words
        is false)
      initial_indent (default: "")
        string that will be prepended to the first line of wrapped
        output.  Counts towards the line's width.
      subsequent_indent (default: "")
        string that will be prepended to all lines save the first
        of wrapped output; also counts towards each line's width.
      expand_tabs (default: true)
        Expand tabs in input text to spaces before further processing.
        Each tab will become 1 .. 8 spaces, depending on its position in
        its line.  If false, each tab is treated as a single character.
      replace_whitespace (default: true)
        Replace all whitespace characters in the input text by spaces
        after tab expansion.  Note that if expand_tabs is false and
        replace_whitespace is true, every tab will be converted to a
        single space!
      fix_sentence_endings (default: false)
        Ensure that sentence-ending punctuation is always followed
        by two spaces.  Off by default because the algorithm is
        (unavoidably) imperfect.
      break_long_words (default: true)
        Break words longer than 'width'.  If false, those words will not
        be broken, and some lines might be longer than 'width'.
      break_on_hyphens (default: true)
        Allow breaking hyphenated words. If true, wrapping will occur
        preferably on whitespaces and right after hyphens part of
        compound words.
      drop_whitespace (default: true)
        Drop leading and trailing whitespace from lines.
    """
    whitespace_trans = string.maketrans(_whitespace, ' ' * len(_whitespace))
    unicode_whitespace_trans = {}
    uspace = ord(u' ')
    for x in map(ord, _whitespace):
        unicode_whitespace_trans[x] = uspace

    wordsep_re = re.compile('(\\s+|[^\\s\\w]*\\w+[^0-9\\W]-(?=\\w+[^0-9\\W])|(?<=[\\w\\!\\"\\\'\\&\\.\\,\\?])-{2,}(?=\\w))')
    wordsep_simple_re = re.compile('(\\s+)')
    sentence_end_re = re.compile('[%s][\\.\\!\\?][\\"\\\']?\\Z' % string.lowercase)

    def __init__(self, width=70, initial_indent='', subsequent_indent='', expand_tabs=True, replace_whitespace=True, fix_sentence_endings=False, break_long_words=True, drop_whitespace=True, break_on_hyphens=True):
        self.width = width
        self.initial_indent = initial_indent
        self.subsequent_indent = subsequent_indent
        self.expand_tabs = expand_tabs
        self.replace_whitespace = replace_whitespace
        self.fix_sentence_endings = fix_sentence_endings
        self.break_long_words = break_long_words
        self.drop_whitespace = drop_whitespace
        self.break_on_hyphens = break_on_hyphens
        self.wordsep_re_uni = re.compile(self.wordsep_re.pattern, re.U)
        self.wordsep_simple_re_uni = re.compile(self.wordsep_simple_re.pattern, re.U)

    def _munge_whitespace(self, text):
        """_munge_whitespace(text : string) -> string
        
                Munge whitespace in text: expand tabs and convert all other
                whitespace characters to spaces.  Eg. " foo     bar
        
        baz"
                becomes " foo    bar  baz".
                """
        if self.expand_tabs:
            text = text.expandtabs()
        if self.replace_whitespace:
            if isinstance(text, str):
                text = text.translate(self.whitespace_trans)
            elif isinstance(text, unicode):
                text = text.translate(self.unicode_whitespace_trans)
        return text

    def _split(self, text):
        """_split(text : string) -> [string]
        
        Split the text to wrap into indivisible chunks.  Chunks are
        not quite the same as words; see _wrap_chunks() for full
        details.  As an example, the text
          Look, goof-ball -- use the -b option!
        breaks into the following chunks:
          'Look,', ' ', 'goof-', 'ball', ' ', '--', ' ',
          'use', ' ', 'the', ' ', '-b', ' ', 'option!'
        if break_on_hyphens is True, or in:
          'Look,', ' ', 'goof-ball', ' ', '--', ' ',
          'use', ' ', 'the', ' ', '-b', ' ', option!'
        otherwise.
        """
        if isinstance(text, unicode):
            if self.break_on_hyphens:
                pat = self.wordsep_re_uni
            else:
                pat = self.wordsep_simple_re_uni
        elif self.break_on_hyphens:
            pat = self.wordsep_re
        else:
            pat = self.wordsep_simple_re
        chunks = pat.split(text)
        chunks = filter(None, chunks)
        return chunks

    def _fix_sentence_endings(self, chunks):
        """_fix_sentence_endings(chunks : [string])
        
                Correct for sentence endings buried in 'chunks'.  Eg. when the
                original text contains "... foo.
        Bar ...", munge_whitespace()
                and split() will convert that to [..., "foo.", " ", "Bar", ...]
                which has one too few spaces; this method simply changes the one
                space to two.
                """
        i = 0
        patsearch = self.sentence_end_re.search
        while i < len(chunks) - 1:
            if chunks[i + 1] == ' ' and patsearch(chunks[i]):
                chunks[i + 1] = '  '
                i += 2
            else:
                i += 1

    def _handle_long_word(self, reversed_chunks, cur_line, cur_len, width):
        """_handle_long_word(chunks : [string],
                             cur_line : [string],
                             cur_len : int, width : int)
        
        Handle a chunk of text (most likely a word, not whitespace) that
        is too long to fit in any line.
        """
        if width < 1:
            space_left = 1
        else:
            space_left = width - cur_len
        if self.break_long_words:
            cur_line.append(reversed_chunks[-1][:space_left])
            reversed_chunks[-1] = reversed_chunks[-1][space_left:]
        elif not cur_line:
            cur_line.append(reversed_chunks.pop())

    def _wrap_chunks(self, chunks):
        """_wrap_chunks(chunks : [string]) -> [string]
        
        Wrap a sequence of text chunks and return a list of lines of
        length 'self.width' or less.  (If 'break_long_words' is false,
        some lines may be longer than this.)  Chunks correspond roughly
        to words and the whitespace between them: each chunk is
        indivisible (modulo 'break_long_words'), but a line break can
        come between any two chunks.  Chunks should not have internal
        whitespace; ie. a chunk is either all whitespace or a "word".
        Whitespace chunks will be removed from the beginning and end of
        lines, but apart from that whitespace is preserved.
        """
        lines = []
        if self.width <= 0:
            raise ValueError('invalid width %r (must be > 0)' % self.width)
        chunks.reverse()
        while chunks:
            cur_line = []
            cur_len = 0
            if lines:
                indent = self.subsequent_indent
            else:
                indent = self.initial_indent
            width = self.width - len(indent)
            if self.drop_whitespace and chunks[-1].strip() == '' and lines:
                del chunks[-1]
            while chunks:
                l = len(chunks[-1])
                if cur_len + l <= width:
                    cur_line.append(chunks.pop())
                    cur_len += l
                else:
                    break

            if chunks and len(chunks[-1]) > width:
                self._handle_long_word(chunks, cur_line, cur_len, width)
            if self.drop_whitespace and cur_line and cur_line[-1].strip() == '':
                del cur_line[-1]
            if cur_line:
                lines.append(indent + ''.join(cur_line))

        return lines

    def wrap(self, text):
        """wrap(text : string) -> [string]
        
        Reformat the single paragraph in 'text' so it fits in lines of
        no more than 'self.width' columns, and return a list of wrapped
        lines.  Tabs in 'text' are expanded with string.expandtabs(),
        and all other whitespace characters (including newline) are
        converted to space.
        """
        text = self._munge_whitespace(text)
        chunks = self._split(text)
        if self.fix_sentence_endings:
            self._fix_sentence_endings(chunks)
        return self._wrap_chunks(chunks)

    def fill(self, text):
        """fill(text : string) -> string
        
        Reformat the single paragraph in 'text' to fit in lines of no
        more than 'self.width' columns, and return a new string
        containing the entire wrapped paragraph.
        """
        return '\n'.join(self.wrap(text))


def wrap(text, width=70, **kwargs):
    """Wrap a single paragraph of text, returning a list of wrapped lines.
    
    Reformat the single paragraph in 'text' so it fits in lines of no
    more than 'width' columns, and return a list of wrapped lines.  By
    default, tabs in 'text' are expanded with string.expandtabs(), and
    all other whitespace characters (including newline) are converted to
    space.  See TextWrapper class for available keyword args to customize
    wrapping behaviour.
    """
    w = TextWrapper(width=width, **kwargs)
    return w.wrap(text)


def fill(text, width=70, **kwargs):
    """Fill a single paragraph of text, returning a new string.
    
    Reformat the single paragraph in 'text' to fit in lines of no more
    than 'width' columns, and return a new string containing the entire
    wrapped paragraph.  As with wrap(), tabs are expanded and other
    whitespace characters converted to space.  See TextWrapper class for
    available keyword args to customize wrapping behaviour.
    """
    w = TextWrapper(width=width, **kwargs)
    return w.fill(text)


_whitespace_only_re = re.compile('^[ \t]+$', re.MULTILINE)
_leading_whitespace_re = re.compile('(^[ \t]*)(?:[^ \t\n])', re.MULTILINE)

def dedent(text):
    """Remove any common leading whitespace from every line in `text`.
    
    This can be used to make triple-quoted strings line up with the left
    edge of the display, while still presenting them in the source code
    in indented form.
    
    Note that tabs and spaces are both treated as whitespace, but they
    are not equal: the lines "  hello" and "    hello" are
    considered to have no common leading whitespace.  (This behaviour is
    new in Python 2.5; older versions of this module incorrectly
    expanded tabs before searching for common leading whitespace.)
    """
    margin = None
    text = _whitespace_only_re.sub('', text)
    indents = _leading_whitespace_re.findall(text)
    for indent in indents:
        if margin is None:
            margin = indent
        elif indent.startswith(margin):
            pass
        elif margin.startswith(indent):
            margin = indent
        else:
            margin = ''
            break

    if 0 and margin:
        for line in text.split('\n'):
            pass

    if margin:
        text = re.sub('(?m)^' + margin, '', text)
    return text


if __name__ == '__main__':
    print dedent('Hello there.\n  This is indented.')