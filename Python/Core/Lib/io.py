# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: io.py
"""The io module provides the Python interfaces to stream handling. The
builtin open function is defined in this module.

At the top of the I/O hierarchy is the abstract base class IOBase. It
defines the basic interface to a stream. Note, however, that there is no
separation between reading and writing to streams; implementations are
allowed to throw an IOError if they do not support a given operation.

Extending IOBase is RawIOBase which deals simply with the reading and
writing of raw bytes to a stream. FileIO subclasses RawIOBase to provide
an interface to OS files.

BufferedIOBase deals with buffering on a raw byte stream (RawIOBase). Its
subclasses, BufferedWriter, BufferedReader, and BufferedRWPair buffer
streams that are readable, writable, and both respectively.
BufferedRandom provides a buffered interface to random access
streams. BytesIO is a simple stream of in-memory bytes.

Another IOBase subclass, TextIOBase, deals with the encoding and decoding
of streams into text. TextIOWrapper, which extends it, is a buffered text
interface to a buffered raw stream (`BufferedIOBase`). Finally, StringIO
is a in-memory stream for text.

Argument names are not part of the specification, and only the arguments
of open() are intended to be used as keyword arguments.

data:

DEFAULT_BUFFER_SIZE

   An int containing the default buffer size used by the module's buffered
   I/O classes. open() uses the file's blksize (as obtained by os.stat) if
   possible.
"""
__author__ = "Guido van Rossum <guido@python.org>, Mike Verdone <mike.verdone@gmail.com>, Mark Russell <mark.russell@zen.co.uk>, Antoine Pitrou <solipsis@pitrou.net>, Amaury Forgeot d'Arc <amauryfa@gmail.com>, Benjamin Peterson <benjamin@python.org>"
__all__ = [
 'BlockingIOError', 'open', 'IOBase', 'RawIOBase', 'FileIO',
 'BytesIO', 'StringIO', 'BufferedIOBase',
 'BufferedReader', 'BufferedWriter', 'BufferedRWPair',
 'BufferedRandom', 'TextIOBase', 'TextIOWrapper',
 'UnsupportedOperation', 'SEEK_SET', 'SEEK_CUR', 'SEEK_END']
import _io
import abc
from _io import DEFAULT_BUFFER_SIZE, BlockingIOError, UnsupportedOperation, open, FileIO, BytesIO, StringIO, BufferedReader, BufferedWriter, BufferedRWPair, BufferedRandom, IncrementalNewlineDecoder, TextIOWrapper
OpenWrapper = _io.open
SEEK_SET = 0
SEEK_CUR = 1
SEEK_END = 2

class IOBase(_io._IOBase):
    __metaclass__ = abc.ABCMeta


class RawIOBase(_io._RawIOBase, IOBase):
    pass


class BufferedIOBase(_io._BufferedIOBase, IOBase):
    pass


class TextIOBase(_io._TextIOBase, IOBase):
    pass


RawIOBase.register(FileIO)
for klass in (BytesIO, BufferedReader, BufferedWriter, BufferedRandom,
 BufferedRWPair):
    BufferedIOBase.register(klass)

for klass in (StringIO, TextIOWrapper):
    TextIOBase.register(klass)

del klass