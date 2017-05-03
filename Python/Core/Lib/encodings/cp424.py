# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: cp424.py
""" Python Character Mapping Codec cp424 generated from 'MAPPINGS/VENDORS/MISC/CP424.TXT' with gencodec.py.

"""
import codecs

class Codec(codecs.Codec):

    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_table)

    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_table)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, encoding_table)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):

    def decode(self, input, final=False):
        return codecs.charmap_decode(input, self.errors, decoding_table)[0]


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


def getregentry():
    return codecs.CodecInfo(name='cp424', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)


decoding_table = u'\x00\x01\x02\x03\x9c\t\x86\x7f\x97\x8d\x8e\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x9d\x85\x08\x87\x18\x19\x92\x8f\x1c\x1d\x1e\x1f\x80\x81\x82\x83\x84\n\x17\x1b\x88\x89\x8a\x8b\x8c\x05\x06\x07\x90\x91\x16\x93\x94\x95\x96\x04\x98\x99\x9a\x9b\x14\x15\x9e\x1a \u05d0\u05d1\u05d2\u05d3\u05d4\u05d5\u05d6\u05d7\u05d8\xa2.<(+|&\u05d9\u05da\u05db\u05dc\u05dd\u05de\u05df\u05e0\u05e1!$*);\xac-/\u05e2\u05e3\u05e4\u05e5\u05e6\u05e7\u05e8\u05e9\xa6,%_>?\ufffe\u05ea\ufffe\ufffe\xa0\ufffe\ufffe\ufffe\u2017`:#@\'="\ufffeabcdefghi\xab\xbb\ufffe\ufffe\ufffe\xb1\xb0jklmnopqr\ufffe\ufffe\ufffe\xb8\ufffe\xa4\xb5~stuvwxyz\ufffe\ufffe\ufffe\ufffe\ufffe\xae^\xa3\xa5\xb7\xa9\xa7\xb6\xbc\xbd\xbe[]\xaf\xa8\xb4\xd7{ABCDEFGHI\xad\ufffe\ufffe\ufffe\ufffe\ufffe}JKLMNOPQR\xb9\ufffe\ufffe\ufffe\ufffe\ufffe\\\xf7STUVWXYZ\xb2\ufffe\ufffe\ufffe\ufffe\ufffe0123456789\xb3\ufffe\ufffe\ufffe\ufffe\x9f'
encoding_table = codecs.charmap_build(decoding_table)