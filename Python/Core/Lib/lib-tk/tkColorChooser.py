# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: tkColorChooser.py
from tkCommonDialog import Dialog

class Chooser(Dialog):
    """Ask for a color"""
    command = 'tk_chooseColor'

    def _fixoptions(self):
        try:
            color = self.options['initialcolor']
            if isinstance(color, tuple):
                self.options['initialcolor'] = '#%02x%02x%02x' % color
        except KeyError:
            pass

    def _fixresult(self, widget, result):
        if not result or not str(result):
            return (None, None)
        else:
            r, g, b = widget.winfo_rgb(result)
            return (
             (
              r / 256, g / 256, b / 256), str(result))


def askcolor(color=None, **options):
    """Ask for a color"""
    if color:
        options = options.copy()
        options['initialcolor'] = color
    return Chooser(**options).show()


if __name__ == '__main__':
    print 'color', askcolor()