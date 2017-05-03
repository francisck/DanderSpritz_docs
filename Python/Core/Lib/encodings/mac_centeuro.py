# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: mac_centeuro.py
""" Python Character Mapping Codec mac_centeuro generated from 'MAPPINGS/VENDORS/APPLE/CENTEURO.TXT' with gencodec.py.

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
    return codecs.CodecInfo(name='mac-centeuro', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)


decoding_table = u'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f\xc4\u0100\u0101\xc9\u0104\xd6\xdc\xe1\u0105\u010c\xe4\u010d\u0106\u0107\xe9\u0179\u017a\u010e\xed\u010f\u0112\u0113\u0116\xf3\u0117\xf4\xf6\xf5\xfa\u011a\u011b\xfc\u2020\xb0\u0118\xa3\xa7\u2022\xb6\xdf\xae\xa9\u2122\u0119\xa8\u2260\u0123\u012e\u012f\u012a\u2264\u2265\u012b\u0136\u2202\u2211\u0142\u013b\u013c\u013d\u013e\u0139\u013a\u0145\u0146\u0143\xac\u221a\u0144\u0147\u2206\xab\xbb\u2026\xa0\u0148\u0150\xd5\u0151\u014c\u2013\u2014\u201c\u201d\u2018\u2019\xf7\u25ca\u014d\u0154\u0155\u0158\u2039\u203a\u0159\u0156\u0157\u0160\u201a\u201e\u0161\u015a\u015b\xc1\u0164\u0165\xcd\u017d\u017e\u016a\xd3\xd4\u016b\u016e\xda\u016f\u0170\u0171\u0172\u0173\xdd\xfd\u0137\u017b\u0141\u017c\u0122\u02c7'
encoding_table = codecs.charmap_build(decoding_table)