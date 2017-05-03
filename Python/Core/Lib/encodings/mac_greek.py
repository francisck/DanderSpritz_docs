# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: mac_greek.py
""" Python Character Mapping Codec mac_greek generated from 'MAPPINGS/VENDORS/APPLE/GREEK.TXT' with gencodec.py.

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
    return codecs.CodecInfo(name='mac-greek', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)


decoding_table = u'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f\xc4\xb9\xb2\xc9\xb3\xd6\xdc\u0385\xe0\xe2\xe4\u0384\xa8\xe7\xe9\xe8\xea\xeb\xa3\u2122\xee\xef\u2022\xbd\u2030\xf4\xf6\xa6\u20ac\xf9\xfb\xfc\u2020\u0393\u0394\u0398\u039b\u039e\u03a0\xdf\xae\xa9\u03a3\u03aa\xa7\u2260\xb0\xb7\u0391\xb1\u2264\u2265\xa5\u0392\u0395\u0396\u0397\u0399\u039a\u039c\u03a6\u03ab\u03a8\u03a9\u03ac\u039d\xac\u039f\u03a1\u2248\u03a4\xab\xbb\u2026\xa0\u03a5\u03a7\u0386\u0388\u0153\u2013\u2015\u201c\u201d\u2018\u2019\xf7\u0389\u038a\u038c\u038e\u03ad\u03ae\u03af\u03cc\u038f\u03cd\u03b1\u03b2\u03c8\u03b4\u03b5\u03c6\u03b3\u03b7\u03b9\u03be\u03ba\u03bb\u03bc\u03bd\u03bf\u03c0\u03ce\u03c1\u03c3\u03c4\u03b8\u03c9\u03c2\u03c7\u03c5\u03b6\u03ca\u03cb\u0390\u03b0\xad'
encoding_table = codecs.charmap_build(decoding_table)