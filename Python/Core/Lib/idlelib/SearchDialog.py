# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: SearchDialog.py
from Tkinter import *
from idlelib import SearchEngine
from idlelib.SearchDialogBase import SearchDialogBase

def _setup(text):
    root = text._root()
    engine = SearchEngine.get(root)
    if not hasattr(engine, '_searchdialog'):
        engine._searchdialog = SearchDialog(root, engine)
    return engine._searchdialog


def find(text):
    pat = text.get('sel.first', 'sel.last')
    return _setup(text).open(text, pat)


def find_again(text):
    return _setup(text).find_again(text)


def find_selection(text):
    return _setup(text).find_selection(text)


class SearchDialog(SearchDialogBase):

    def create_widgets(self):
        f = SearchDialogBase.create_widgets(self)
        self.make_button('Find', self.default_command, 1)

    def default_command(self, event=None):
        if not self.engine.getprog():
            return
        if self.find_again(self.text):
            self.close()

    def find_again(self, text):
        if not self.engine.getpat():
            self.open(text)
            return False
        else:
            if not self.engine.getprog():
                return False
            res = self.engine.search_text(text)
            if res:
                line, m = res
                i, j = m.span()
                first = '%d.%d' % (line, i)
                last = '%d.%d' % (line, j)
                try:
                    selfirst = text.index('sel.first')
                    sellast = text.index('sel.last')
                    if selfirst == first and sellast == last:
                        text.bell()
                        return False
                except TclError:
                    pass

                text.tag_remove('sel', '1.0', 'end')
                text.tag_add('sel', first, last)
                text.mark_set('insert', self.engine.isback() and first or last)
                text.see('insert')
                return True
            text.bell()
            return False

    def find_selection(self, text):
        pat = text.get('sel.first', 'sel.last')
        if pat:
            self.engine.setcookedpat(pat)
        return self.find_again(text)