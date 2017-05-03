# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: cp875.py
""" Python Character Mapping Codec cp875 generated from 'MAPPINGS/VENDORS/MICSFT/EBCDIC/CP875.TXT' with gencodec.py.

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
    return codecs.CodecInfo(name='cp875', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)


decoding_table = u'\x00\x01\x02\x03\x9c\t\x86\x7f\x97\x8d\x8e\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x9d\x85\x08\x87\x18\x19\x92\x8f\x1c\x1d\x1e\x1f\x80\x81\x82\x83\x84\n\x17\x1b\x88\x89\x8a\x8b\x8c\x05\x06\x07\x90\x91\x16\x93\x94\x95\x96\x04\x98\x99\x9a\x9b\x14\x15\x9e\x1a \u0391\u0392\u0393\u0394\u0395\u0396\u0397\u0398\u0399[.<(+!&\u039a\u039b\u039c\u039d\u039e\u039f\u03a0\u03a1\u03a3]$*);^-/\u03a4\u03a5\u03a6\u03a7\u03a8\u03a9\u03aa\u03ab|,%_>?\xa8\u0386\u0388\u0389\xa0\u038a\u038c\u038e\u038f`:#@\'="\u0385abcdefghi\u03b1\u03b2\u03b3\u03b4\u03b5\u03b6\xb0jklmnopqr\u03b7\u03b8\u03b9\u03ba\u03bb\u03bc\xb4~stuvwxyz\u03bd\u03be\u03bf\u03c0\u03c1\u03c3\xa3\u03ac\u03ad\u03ae\u03ca\u03af\u03cc\u03cd\u03cb\u03ce\u03c2\u03c4\u03c5\u03c6\u03c7\u03c8{ABCDEFGHI\xad\u03c9\u0390\u03b0\u2018\u2015}JKLMNOPQR\xb1\xbd\x1a\u0387\u2019\xa6\\\x1aSTUVWXYZ\xb2\xa7\x1a\x1a\xab\xac0123456789\xb3\xa9\x1a\x1a\xbb\x9f'
encoding_table = codecs.charmap_build(decoding_table)