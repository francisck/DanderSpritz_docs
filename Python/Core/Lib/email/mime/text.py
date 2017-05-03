# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: text.py
"""Class representing text/* type MIME documents."""
__all__ = [
 'MIMEText']
from email.encoders import encode_7or8bit
from email.mime.nonmultipart import MIMENonMultipart

class MIMEText(MIMENonMultipart):
    """Class for generating text/* type MIME documents."""

    def __init__(self, _text, _subtype='plain', _charset='us-ascii'):
        """Create a text/* type MIME document.
        
        _text is the string for this message object.
        
        _subtype is the MIME sub content type, defaulting to "plain".
        
        _charset is the character set parameter added to the Content-Type
        header.  This defaults to "us-ascii".  Note that as a side-effect, the
        Content-Transfer-Encoding header will also be set.
        """
        MIMENonMultipart.__init__(self, 'text', _subtype, **{'charset': _charset})
        self.set_payload(_text, _charset)