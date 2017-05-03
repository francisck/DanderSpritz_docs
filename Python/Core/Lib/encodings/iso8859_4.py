# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: iso8859_4.py
""" Python Character Mapping Codec iso8859_4 generated from 'MAPPINGS/ISO8859/8859-4.TXT' with gencodec.py.

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
    return codecs.CodecInfo(name='iso8859-4', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)


decoding_table = u'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\u0104\u0138\u0156\xa4\u0128\u013b\xa7\xa8\u0160\u0112\u0122\u0166\xad\u017d\xaf\xb0\u0105\u02db\u0157\xb4\u0129\u013c\u02c7\xb8\u0161\u0113\u0123\u0167\u014a\u017e\u014b\u0100\xc1\xc2\xc3\xc4\xc5\xc6\u012e\u010c\xc9\u0118\xcb\u0116\xcd\xce\u012a\u0110\u0145\u014c\u0136\xd4\xd5\xd6\xd7\xd8\u0172\xda\xdb\xdc\u0168\u016a\xdf\u0101\xe1\xe2\xe3\xe4\xe5\xe6\u012f\u010d\xe9\u0119\xeb\u0117\xed\xee\u012b\u0111\u0146\u014d\u0137\xf4\xf5\xf6\xf7\xf8\u0173\xfa\xfb\xfc\u0169\u016b\u02d9'
encoding_table = codecs.charmap_build(decoding_table)