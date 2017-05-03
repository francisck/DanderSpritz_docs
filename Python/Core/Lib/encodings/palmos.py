# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: palmos.py
""" Python Character Mapping Codec for PalmOS 3.5.

Written by Sjoerd Mullender (sjoerd@acm.org); based on iso8859_15.py.

"""
import codecs

class Codec(codecs.Codec):

    def encode(self, input, errors='strict'):
        return codecs.charmap_encode(input, errors, encoding_map)

    def decode(self, input, errors='strict'):
        return codecs.charmap_decode(input, errors, decoding_map)


class IncrementalEncoder(codecs.IncrementalEncoder):

    def encode(self, input, final=False):
        return codecs.charmap_encode(input, self.errors, encoding_map)[0]


class IncrementalDecoder(codecs.IncrementalDecoder):

    def decode(self, input, final=False):
        return codecs.charmap_decode(input, self.errors, decoding_map)[0]


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


def getregentry():
    return codecs.CodecInfo(name='palmos', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)


decoding_map = codecs.make_identity_dict(range(256))
decoding_map.update({128: 8364,
   130: 8218,
   131: 402,
   132: 8222,
   133: 8230,
   134: 8224,
   135: 8225,
   136: 710,
   137: 8240,
   138: 352,
   139: 8249,
   140: 338,
   141: 9830,
   142: 9827,
   143: 9829,
   144: 9824,
   145: 8216,
   146: 8217,
   147: 8220,
   148: 8221,
   149: 8226,
   150: 8211,
   151: 8212,
   152: 732,
   153: 8482,
   154: 353,
   156: 339,
   159: 376
   })
encoding_map = codecs.make_encoding_map(decoding_map)