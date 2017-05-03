# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
"""A package for parsing, handling, and generating email messages."""
__version__ = '4.0.3'
__all__ = [
 'base64MIME',
 'Charset',
 'Encoders',
 'Errors',
 'Generator',
 'Header',
 'Iterators',
 'Message',
 'MIMEAudio',
 'MIMEBase',
 'MIMEImage',
 'MIMEMessage',
 'MIMEMultipart',
 'MIMENonMultipart',
 'MIMEText',
 'Parser',
 'quopriMIME',
 'Utils',
 'message_from_string',
 'message_from_file',
 'base64mime',
 'charset',
 'encoders',
 'errors',
 'generator',
 'header',
 'iterators',
 'message',
 'mime',
 'parser',
 'quoprimime',
 'utils']

def message_from_string(s, *args, **kws):
    """Parse a string into a Message object model.
    
    Optional _class and strict are passed to the Parser constructor.
    """
    from email.parser import Parser
    return Parser(*args, **kws).parsestr(s)


def message_from_file(fp, *args, **kws):
    """Read a file and parse its contents into a Message object model.
    
    Optional _class and strict are passed to the Parser constructor.
    """
    from email.parser import Parser
    return Parser(*args, **kws).parse(fp)


import sys

class LazyImporter(object):

    def __init__(self, module_name):
        self.__name__ = 'email.' + module_name

    def __getattr__(self, name):
        __import__(self.__name__)
        mod = sys.modules[self.__name__]
        self.__dict__.update(mod.__dict__)
        return getattr(mod, name)


_LOWERNAMES = [
 'Charset',
 'Encoders',
 'Errors',
 'FeedParser',
 'Generator',
 'Header',
 'Iterators',
 'Message',
 'Parser',
 'Utils',
 'base64MIME',
 'quopriMIME']
_MIMENAMES = [
 'Audio',
 'Base',
 'Image',
 'Message',
 'Multipart',
 'NonMultipart',
 'Text']
for _name in _LOWERNAMES:
    importer = LazyImporter(_name.lower())
    sys.modules['email.' + _name] = importer
    setattr(sys.modules['email'], _name, importer)

import email.mime
for _name in _MIMENAMES:
    importer = LazyImporter('mime.' + _name.lower())
    sys.modules['email.MIME' + _name] = importer
    setattr(sys.modules['email'], 'MIME' + _name, importer)
    setattr(sys.modules['email.mime'], _name, importer)