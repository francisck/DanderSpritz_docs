# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: AutoExpand.py
import string
import re

class AutoExpand:
    menudefs = [
     (
      'edit',
      [
       ('E_xpand Word', '<<expand-word>>')])]
    wordchars = string.ascii_letters + string.digits + '_'

    def __init__(self, editwin):
        self.text = editwin.text
        self.state = None
        return

    def expand_word_event(self, event):
        curinsert = self.text.index('insert')
        curline = self.text.get('insert linestart', 'insert lineend')
        if not self.state:
            words = self.getwords()
            index = 0
        else:
            words, index, insert, line = self.state
            if insert != curinsert or line != curline:
                words = self.getwords()
                index = 0
            if not words:
                self.text.bell()
                return 'break'
        word = self.getprevword()
        self.text.delete('insert - %d chars' % len(word), 'insert')
        newword = words[index]
        index = (index + 1) % len(words)
        if index == 0:
            self.text.bell()
        self.text.insert('insert', newword)
        curinsert = self.text.index('insert')
        curline = self.text.get('insert linestart', 'insert lineend')
        self.state = (words, index, curinsert, curline)
        return 'break'

    def getwords(self):
        word = self.getprevword()
        if not word:
            return []
        before = self.text.get('1.0', 'insert wordstart')
        wbefore = re.findall('\\b' + word + '\\w+\\b', before)
        del before
        after = self.text.get('insert wordend', 'end')
        wafter = re.findall('\\b' + word + '\\w+\\b', after)
        del after
        if not wbefore and not wafter:
            return []
        words = []
        dict = {}
        wbefore.reverse()
        for w in wbefore:
            if dict.get(w):
                continue
            words.append(w)
            dict[w] = w

        for w in wafter:
            if dict.get(w):
                continue
            words.append(w)
            dict[w] = w

        words.append(word)
        return words

    def getprevword(self):
        line = self.text.get('insert linestart', 'insert')
        i = len(line)
        while i > 0 and line[i - 1] in self.wordchars:
            i = i - 1

        return line[i:]