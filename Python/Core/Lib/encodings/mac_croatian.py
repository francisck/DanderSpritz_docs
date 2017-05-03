# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: mac_croatian.py
""" Python Character Mapping Codec mac_croatian generated from 'MAPPINGS/VENDORS/APPLE/CROATIAN.TXT' with gencodec.py.

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
    return codecs.CodecInfo(name='mac-croatian', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)


decoding_table = u'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f\xc4\xc5\xc7\xc9\xd1\xd6\xdc\xe1\xe0\xe2\xe4\xe3\xe5\xe7\xe9\xe8\xea\xeb\xed\xec\xee\xef\xf1\xf3\xf2\xf4\xf6\xf5\xfa\xf9\xfb\xfc\u2020\xb0\xa2\xa3\xa7\u2022\xb6\xdf\xae\u0160\u2122\xb4\xa8\u2260\u017d\xd8\u221e\xb1\u2264\u2265\u2206\xb5\u2202\u2211\u220f\u0161\u222b\xaa\xba\u03a9\u017e\xf8\xbf\xa1\xac\u221a\u0192\u2248\u0106\xab\u010c\u2026\xa0\xc0\xc3\xd5\u0152\u0153\u0110\u2014\u201c\u201d\u2018\u2019\xf7\u25ca\uf8ff\xa9\u2044\u20ac\u2039\u203a\xc6\xbb\u2013\xb7\u201a\u201e\u2030\xc2\u0107\xc1\u010d\xc8\xcd\xce\xcf\xcc\xd3\xd4\u0111\xd2\xda\xdb\xd9\u0131\u02c6\u02dc\xaf\u03c0\xcb\u02da\xb8\xca\xe6\u02c7'
encoding_table = codecs.charmap_build(decoding_table)