# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: cp1006.py
""" Python Character Mapping Codec cp1006 generated from 'MAPPINGS/VENDORS/MISC/CP1006.TXT' with gencodec.py.

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
    return codecs.CodecInfo(name='cp1006', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)


decoding_table = u'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\u06f0\u06f1\u06f2\u06f3\u06f4\u06f5\u06f6\u06f7\u06f8\u06f9\u060c\u061b\xad\u061f\ufe81\ufe8d\ufe8e\ufe8e\ufe8f\ufe91\ufb56\ufb58\ufe93\ufe95\ufe97\ufb66\ufb68\ufe99\ufe9b\ufe9d\ufe9f\ufb7a\ufb7c\ufea1\ufea3\ufea5\ufea7\ufea9\ufb84\ufeab\ufead\ufb8c\ufeaf\ufb8a\ufeb1\ufeb3\ufeb5\ufeb7\ufeb9\ufebb\ufebd\ufebf\ufec1\ufec5\ufec9\ufeca\ufecb\ufecc\ufecd\ufece\ufecf\ufed0\ufed1\ufed3\ufed5\ufed7\ufed9\ufedb\ufb92\ufb94\ufedd\ufedf\ufee0\ufee1\ufee3\ufb9e\ufee5\ufee7\ufe85\ufeed\ufba6\ufba8\ufba9\ufbaa\ufe80\ufe89\ufe8a\ufe8b\ufef1\ufef2\ufef3\ufbb0\ufbae\ufe7c\ufe7d'
encoding_table = codecs.charmap_build(decoding_table)