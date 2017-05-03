# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: tkMessageBox.py
from tkCommonDialog import Dialog
ERROR = 'error'
INFO = 'info'
QUESTION = 'question'
WARNING = 'warning'
ABORTRETRYIGNORE = 'abortretryignore'
OK = 'ok'
OKCANCEL = 'okcancel'
RETRYCANCEL = 'retrycancel'
YESNO = 'yesno'
YESNOCANCEL = 'yesnocancel'
ABORT = 'abort'
RETRY = 'retry'
IGNORE = 'ignore'
OK = 'ok'
CANCEL = 'cancel'
YES = 'yes'
NO = 'no'

class Message(Dialog):
    """A message box"""
    command = 'tk_messageBox'


def _show(title=None, message=None, _icon=None, _type=None, **options):
    if _icon and 'icon' not in options:
        options['icon'] = _icon
    if _type and 'type' not in options:
        options['type'] = _type
    if title:
        options['title'] = title
    if message:
        options['message'] = message
    res = Message(**options).show()
    if isinstance(res, bool):
        if res:
            return YES
        return NO
    return str(res)


def showinfo(title=None, message=None, **options):
    """Show an info message"""
    return _show(title, message, INFO, OK, **options)


def showwarning(title=None, message=None, **options):
    """Show a warning message"""
    return _show(title, message, WARNING, OK, **options)


def showerror(title=None, message=None, **options):
    """Show an error message"""
    return _show(title, message, ERROR, OK, **options)


def askquestion(title=None, message=None, **options):
    """Ask a question"""
    return _show(title, message, QUESTION, YESNO, **options)


def askokcancel(title=None, message=None, **options):
    """Ask if operation should proceed; return true if the answer is ok"""
    s = _show(title, message, QUESTION, OKCANCEL, **options)
    return s == OK


def askyesno(title=None, message=None, **options):
    """Ask a question; return true if the answer is yes"""
    s = _show(title, message, QUESTION, YESNO, **options)
    return s == YES


def askyesnocancel(title=None, message=None, **options):
    """Ask a question; return true if the answer is yes, None if cancelled."""
    s = _show(title, message, QUESTION, YESNOCANCEL, **options)
    s = str(s)
    if s == CANCEL:
        return None
    else:
        return s == YES


def askretrycancel(title=None, message=None, **options):
    """Ask if operation should be retried; return true if the answer is yes"""
    s = _show(title, message, WARNING, RETRYCANCEL, **options)
    return s == RETRY


if __name__ == '__main__':
    print 'info', showinfo('Spam', 'Egg Information')
    print 'warning', showwarning('Spam', 'Egg Warning')
    print 'error', showerror('Spam', 'Egg Alert')
    print 'question', askquestion('Spam', 'Question?')
    print 'proceed', askokcancel('Spam', 'Proceed?')
    print 'yes/no', askyesno('Spam', 'Got it?')
    print 'yes/no/cancel', askyesnocancel('Spam', 'Want it?')
    print 'try again', askretrycancel('Spam', 'Try again?')