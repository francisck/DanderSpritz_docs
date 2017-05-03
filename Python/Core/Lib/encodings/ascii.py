# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: ascii.py
""" Python 'ascii' Codec


Written by Marc-Andre Lemburg (mal@lemburg.com).

(c) Copyright CNRI, All Rights Reserved. NO WARRANTY.

"""
import codecs

class Codec(codecs.Codec):
    encode = codecs.ascii_encode
    decode = codecs.ascii_decode


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final=False):
        return codecs.ascii_encode(input, self.errors)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):

    def decode(self, input, final=False):
        return codecs.ascii_decode(input, self.errors)[0]


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


class StreamConverter(StreamWriter, StreamReader):
    encode = codecs.ascii_decode
    decode = codecs.ascii_encode


def getregentry():
    return codecs.CodecInfo(name='ascii', encode=Codec.encode, decode=Codec.decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamwriter=StreamWriter, streamreader=StreamReader)