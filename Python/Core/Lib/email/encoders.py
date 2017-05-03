# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: encoders.py
"""Encodings and related functions."""
__all__ = [
 'encode_7or8bit',
 'encode_base64',
 'encode_noop',
 'encode_quopri']
import base64
from quopri import encodestring as _encodestring

def _qencode(s):
    enc = _encodestring(s, quotetabs=True)
    return enc.replace(' ', '=20')


def _bencode(s):
    if not s:
        return s
    hasnewline = s[-1] == '\n'
    value = base64.encodestring(s)
    if not hasnewline and value[-1] == '\n':
        return value[:-1]
    return value


def encode_base64(msg):
    """Encode the message's payload in Base64.
    
    Also, add an appropriate Content-Transfer-Encoding header.
    """
    orig = msg.get_payload()
    encdata = _bencode(orig)
    msg.set_payload(encdata)
    msg['Content-Transfer-Encoding'] = 'base64'


def encode_quopri(msg):
    """Encode the message's payload in quoted-printable.
    
    Also, add an appropriate Content-Transfer-Encoding header.
    """
    orig = msg.get_payload()
    encdata = _qencode(orig)
    msg.set_payload(encdata)
    msg['Content-Transfer-Encoding'] = 'quoted-printable'


def encode_7or8bit(msg):
    """Set the Content-Transfer-Encoding header to 7bit or 8bit."""
    orig = msg.get_payload()
    if orig is None:
        msg['Content-Transfer-Encoding'] = '7bit'
        return
    else:
        try:
            orig.encode('ascii')
        except UnicodeError:
            msg['Content-Transfer-Encoding'] = '8bit'
        else:
            msg['Content-Transfer-Encoding'] = '7bit'

        return


def encode_noop(msg):
    """Do nothing."""
    pass