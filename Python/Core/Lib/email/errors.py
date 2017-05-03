# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
"""email package exception classes."""

class MessageError(Exception):
    """Base class for errors in the email package."""
    pass


class MessageParseError(MessageError):
    """Base class for message parsing errors."""
    pass


class HeaderParseError(MessageParseError):
    """Error while parsing headers."""
    pass


class BoundaryError(MessageParseError):
    """Couldn't find terminating boundary."""
    pass


class MultipartConversionError(MessageError, TypeError):
    """Conversion to a multipart is prohibited."""
    pass


class CharsetError(MessageError):
    """An illegal charset was given."""
    pass


class MessageDefect:
    """Base class for a message defect."""

    def __init__(self, line=None):
        self.line = line


class NoBoundaryInMultipartDefect(MessageDefect):
    """A message claimed to be a multipart but had no boundary parameter."""
    pass


class StartBoundaryNotFoundDefect(MessageDefect):
    """The claimed start boundary was never found."""
    pass


class FirstHeaderLineIsContinuationDefect(MessageDefect):
    """A message had a continuation line as its first header line."""
    pass


class MisplacedEnvelopeHeaderDefect(MessageDefect):
    """A 'Unix-from' header was found in the middle of a header block."""
    pass


class MalformedHeaderDefect(MessageDefect):
    """Found a header that was missing a colon, or was otherwise malformed."""
    pass


class MultipartInvariantViolationDefect(MessageDefect):
    """A message claimed to be a multipart but no subparts were found."""
    pass