# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: iso8859_16.py
""" Python Character Mapping Codec iso8859_16 generated from 'MAPPINGS/ISO8859/8859-16.TXT' with gencodec.py.

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
    return codecs.CodecInfo(name='iso8859-16', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)


decoding_table = u'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\u0104\u0105\u0141\u20ac\u201e\u0160\xa7\u0161\xa9\u0218\xab\u0179\xad\u017a\u017b\xb0\xb1\u010c\u0142\u017d\u201d\xb6\xb7\u017e\u010d\u0219\xbb\u0152\u0153\u0178\u017c\xc0\xc1\xc2\u0102\xc4\u0106\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\u0110\u0143\xd2\xd3\xd4\u0150\xd6\u015a\u0170\xd9\xda\xdb\xdc\u0118\u021a\xdf\xe0\xe1\xe2\u0103\xe4\u0107\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\u0111\u0144\xf2\xf3\xf4\u0151\xf6\u015b\u0171\xf9\xfa\xfb\xfc\u0119\u021b\xff'
encoding_table = codecs.charmap_build(decoding_table)