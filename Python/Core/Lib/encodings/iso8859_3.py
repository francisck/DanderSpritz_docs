# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: iso8859_3.py
""" Python Character Mapping Codec iso8859_3 generated from 'MAPPINGS/ISO8859/8859-3.TXT' with gencodec.py.

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
    return codecs.CodecInfo(name='iso8859-3', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)


decoding_table = u'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\u0126\u02d8\xa3\xa4\ufffe\u0124\xa7\xa8\u0130\u015e\u011e\u0134\xad\ufffe\u017b\xb0\u0127\xb2\xb3\xb4\xb5\u0125\xb7\xb8\u0131\u015f\u011f\u0135\xbd\ufffe\u017c\xc0\xc1\xc2\ufffe\xc4\u010a\u0108\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\ufffe\xd1\xd2\xd3\xd4\u0120\xd6\xd7\u011c\xd9\xda\xdb\xdc\u016c\u015c\xdf\xe0\xe1\xe2\ufffe\xe4\u010b\u0109\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\ufffe\xf1\xf2\xf3\xf4\u0121\xf6\xf7\u011d\xf9\xfa\xfb\xfc\u016d\u015d\u02d9'
encoding_table = codecs.charmap_build(decoding_table)