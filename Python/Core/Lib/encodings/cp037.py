# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: cp037.py
""" Python Character Mapping Codec cp037 generated from 'MAPPINGS/VENDORS/MICSFT/EBCDIC/CP037.TXT' with gencodec.py.

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
    return codecs.CodecInfo(name='cp037', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)


decoding_table = u'\x00\x01\x02\x03\x9c\t\x86\x7f\x97\x8d\x8e\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x9d\x85\x08\x87\x18\x19\x92\x8f\x1c\x1d\x1e\x1f\x80\x81\x82\x83\x84\n\x17\x1b\x88\x89\x8a\x8b\x8c\x05\x06\x07\x90\x91\x16\x93\x94\x95\x96\x04\x98\x99\x9a\x9b\x14\x15\x9e\x1a \xa0\xe2\xe4\xe0\xe1\xe3\xe5\xe7\xf1\xa2.<(+|&\xe9\xea\xeb\xe8\xed\xee\xef\xec\xdf!$*);\xac-/\xc2\xc4\xc0\xc1\xc3\xc5\xc7\xd1\xa6,%_>?\xf8\xc9\xca\xcb\xc8\xcd\xce\xcf\xcc`:#@\'="\xd8abcdefghi\xab\xbb\xf0\xfd\xfe\xb1\xb0jklmnopqr\xaa\xba\xe6\xb8\xc6\xa4\xb5~stuvwxyz\xa1\xbf\xd0\xdd\xde\xae^\xa3\xa5\xb7\xa9\xa7\xb6\xbc\xbd\xbe[]\xaf\xa8\xb4\xd7{ABCDEFGHI\xad\xf4\xf6\xf2\xf3\xf5}JKLMNOPQR\xb9\xfb\xfc\xf9\xfa\xff\\\xf7STUVWXYZ\xb2\xd4\xd6\xd2\xd3\xd50123456789\xb3\xdb\xdc\xd9\xda\x9f'
encoding_table = codecs.charmap_build(decoding_table)