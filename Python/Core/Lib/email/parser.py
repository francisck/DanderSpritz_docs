# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: parser.py
"""A parser of RFC 2822 and MIME email messages."""
__all__ = [
 'Parser', 'HeaderParser']
import warnings
from cStringIO import StringIO
from email.feedparser import FeedParser
from email.message import Message

class Parser:

    def __init__(self, *args, **kws):
        """Parser of RFC 2822 and MIME email messages.
        
        Creates an in-memory object tree representing the email message, which
        can then be manipulated and turned over to a Generator to return the
        textual representation of the message.
        
        The string must be formatted as a block of RFC 2822 headers and header
        continuation lines, optionally preceeded by a `Unix-from' header.  The
        header block is terminated either by the end of the string or by a
        blank line.
        
        _class is the class to instantiate for new message objects when they
        must be created.  This class must have a constructor that can take
        zero arguments.  Default is Message.Message.
        """
        if len(args) >= 1:
            if '_class' in kws:
                raise TypeError("Multiple values for keyword arg '_class'")
            kws['_class'] = args[0]
        if len(args) == 2:
            if 'strict' in kws:
                raise TypeError("Multiple values for keyword arg 'strict'")
            kws['strict'] = args[1]
        if len(args) > 2:
            raise TypeError('Too many arguments')
        if '_class' in kws:
            self._class = kws['_class']
            del kws['_class']
        else:
            self._class = Message
        if 'strict' in kws:
            warnings.warn("'strict' argument is deprecated (and ignored)", DeprecationWarning, 2)
            del kws['strict']
        if kws:
            raise TypeError('Unexpected keyword arguments')

    def parse(self, fp, headersonly=False):
        """Create a message structure from the data in a file.
        
        Reads all the data from the file and returns the root of the message
        structure.  Optional headersonly is a flag specifying whether to stop
        parsing after reading the headers or not.  The default is False,
        meaning it parses the entire contents of the file.
        """
        feedparser = FeedParser(self._class)
        if headersonly:
            feedparser._set_headersonly()
        while True:
            data = fp.read(8192)
            if not data:
                break
            feedparser.feed(data)

        return feedparser.close()

    def parsestr(self, text, headersonly=False):
        """Create a message structure from a string.
        
        Returns the root of the message structure.  Optional headersonly is a
        flag specifying whether to stop parsing after reading the headers or
        not.  The default is False, meaning it parses the entire contents of
        the file.
        """
        return self.parse(StringIO(text), headersonly=headersonly)


class HeaderParser(Parser):

    def parse(self, fp, headersonly=True):
        return Parser.parse(self, fp, True)

    def parsestr(self, text, headersonly=True):
        return Parser.parsestr(self, text, True)