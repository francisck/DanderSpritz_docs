# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: utf_16.py
""" Python 'utf-16' Codec


Written by Marc-Andre Lemburg (mal@lemburg.com).

(c) Copyright CNRI, All Rights Reserved. NO WARRANTY.

"""
import codecs
import sys
encode = codecs.utf_16_encode

def decode(input, errors='strict'):
    return codecs.utf_16_decode(input, errors, True)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def __init__(self, errors='strict'):
        codecs.IncrementalEncoder.__init__(self, errors)
        self.encoder = None
        return

    def encode(self, input, final=False):
        if self.encoder is None:
            result = codecs.utf_16_encode(input, self.errors)[0]
            if sys.byteorder == 'little':
                self.encoder = codecs.utf_16_le_encode
            else:
                self.encoder = codecs.utf_16_be_encode
            return result
        else:
            return self.encoder(input, self.errors)[0]

    def reset(self):
        codecs.IncrementalEncoder.reset(self)
        self.encoder = None
        return

    def getstate(self):
        if self.encoder is None:
            return 2
        else:
            return 0

    def setstate(self, state):
        if state:
            self.encoder = None
        elif sys.byteorder == 'little':
            self.encoder = codecs.utf_16_le_encode
        else:
            self.encoder = codecs.utf_16_be_encode
        return


class IncrementalDecoder(codecs.BufferedIncrementalDecoder):

    def __init__(self, errors='strict'):
        codecs.BufferedIncrementalDecoder.__init__(self, errors)
        self.decoder = None
        return

    def _buffer_decode(self, input, errors, final):
        if self.decoder is None:
            output, consumed, byteorder = codecs.utf_16_ex_decode(input, errors, 0, final)
            if byteorder == -1:
                self.decoder = codecs.utf_16_le_decode
            elif byteorder == 1:
                self.decoder = codecs.utf_16_be_decode
            elif consumed >= 2:
                raise UnicodeError('UTF-16 stream does not start with BOM')
            return (output, consumed)
        else:
            return self.decoder(input, self.errors, final)

    def reset(self):
        codecs.BufferedIncrementalDecoder.reset(self)
        self.decoder = None
        return


class StreamWriter(codecs.StreamWriter):

    def __init__(self, stream, errors='strict'):
        codecs.StreamWriter.__init__(self, stream, errors)
        self.encoder = None
        return

    def reset(self):
        codecs.StreamWriter.reset(self)
        self.encoder = None
        return

    def encode(self, input, errors='strict'):
        if self.encoder is None:
            result = codecs.utf_16_encode(input, errors)
            if sys.byteorder == 'little':
                self.encoder = codecs.utf_16_le_encode
            else:
                self.encoder = codecs.utf_16_be_encode
            return result
        else:
            return self.encoder(input, errors)
            return


class StreamReader(codecs.StreamReader):

    def reset(self):
        codecs.StreamReader.reset(self)
        try:
            del self.decode
        except AttributeError:
            pass

    def decode(self, input, errors='strict'):
        object, consumed, byteorder = codecs.utf_16_ex_decode(input, errors, 0, False)
        if byteorder == -1:
            self.decode = codecs.utf_16_le_decode
        elif byteorder == 1:
            self.decode = codecs.utf_16_be_decode
        elif consumed >= 2:
            raise UnicodeError, 'UTF-16 stream does not start with BOM'
        return (object, consumed)


def getregentry():
    return codecs.CodecInfo(name='utf-16', encode=encode, decode=decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)