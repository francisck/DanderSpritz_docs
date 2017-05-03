# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: utf_32_le.py
"""
Python 'utf-32-le' Codec
"""
import codecs
encode = codecs.utf_32_le_encode

def decode(input, errors='strict'):
    return codecs.utf_32_le_decode(input, errors, True)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final=False):
        return codecs.utf_32_le_encode(input, self.errors)[0]


class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    _buffer_decode = codecs.utf_32_le_decode


class StreamWriter(codecs.StreamWriter):
    encode = codecs.utf_32_le_encode


class StreamReader(codecs.StreamReader):
    decode = codecs.utf_32_le_decode


def getregentry():
    return codecs.CodecInfo(name='utf-32-le', encode=encode, decode=decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)