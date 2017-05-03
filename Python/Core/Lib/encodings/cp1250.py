# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: cp1250.py
""" Python Character Mapping Codec cp1250 generated from 'MAPPINGS/VENDORS/MICSFT/WINDOWS/CP1250.TXT' with gencodec.py.

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
    return codecs.CodecInfo(name='cp1250', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)


decoding_table = u'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f\u20ac\ufffe\u201a\ufffe\u201e\u2026\u2020\u2021\ufffe\u2030\u0160\u2039\u015a\u0164\u017d\u0179\ufffe\u2018\u2019\u201c\u201d\u2022\u2013\u2014\ufffe\u2122\u0161\u203a\u015b\u0165\u017e\u017a\xa0\u02c7\u02d8\u0141\xa4\u0104\xa6\xa7\xa8\xa9\u015e\xab\xac\xad\xae\u017b\xb0\xb1\u02db\u0142\xb4\xb5\xb6\xb7\xb8\u0105\u015f\xbb\u013d\u02dd\u013e\u017c\u0154\xc1\xc2\u0102\xc4\u0139\u0106\xc7\u010c\xc9\u0118\xcb\u011a\xcd\xce\u010e\u0110\u0143\u0147\xd3\xd4\u0150\xd6\xd7\u0158\u016e\xda\u0170\xdc\xdd\u0162\xdf\u0155\xe1\xe2\u0103\xe4\u013a\u0107\xe7\u010d\xe9\u0119\xeb\u011b\xed\xee\u010f\u0111\u0144\u0148\xf3\xf4\u0151\xf6\xf7\u0159\u016f\xfa\u0171\xfc\xfd\u0163\u02d9'
encoding_table = codecs.charmap_build(decoding_table)