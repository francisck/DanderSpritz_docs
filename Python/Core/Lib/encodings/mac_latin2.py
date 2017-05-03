# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: mac_latin2.py
""" Python Character Mapping Codec generated from 'LATIN2.TXT' with gencodec.py.

Written by Marc-Andre Lemburg (mal@lemburg.com).

(c) Copyright CNRI, All Rights Reserved. NO WARRANTY.
(c) Copyright 2000 Guido van Rossum.

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
    return codecs.CodecInfo(name='mac-latin2', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)


decoding_map = codecs.make_identity_dict(range(256))
decoding_map.update({128: 196,
   129: 256,
   130: 257,
   131: 201,
   132: 260,
   133: 214,
   134: 220,
   135: 225,
   136: 261,
   137: 268,
   138: 228,
   139: 269,
   140: 262,
   141: 263,
   142: 233,
   143: 377,
   144: 378,
   145: 270,
   146: 237,
   147: 271,
   148: 274,
   149: 275,
   150: 278,
   151: 243,
   152: 279,
   153: 244,
   154: 246,
   155: 245,
   156: 250,
   157: 282,
   158: 283,
   159: 252,
   160: 8224,
   161: 176,
   162: 280,
   164: 167,
   165: 8226,
   166: 182,
   167: 223,
   168: 174,
   170: 8482,
   171: 281,
   172: 168,
   173: 8800,
   174: 291,
   175: 302,
   176: 303,
   177: 298,
   178: 8804,
   179: 8805,
   180: 299,
   181: 310,
   182: 8706,
   183: 8721,
   184: 322,
   185: 315,
   186: 316,
   187: 317,
   188: 318,
   189: 313,
   190: 314,
   191: 325,
   192: 326,
   193: 323,
   194: 172,
   195: 8730,
   196: 324,
   197: 327,
   198: 8710,
   199: 171,
   200: 187,
   201: 8230,
   202: 160,
   203: 328,
   204: 336,
   205: 213,
   206: 337,
   207: 332,
   208: 8211,
   209: 8212,
   210: 8220,
   211: 8221,
   212: 8216,
   213: 8217,
   214: 247,
   215: 9674,
   216: 333,
   217: 340,
   218: 341,
   219: 344,
   220: 8249,
   221: 8250,
   222: 345,
   223: 342,
   224: 343,
   225: 352,
   226: 8218,
   227: 8222,
   228: 353,
   229: 346,
   230: 347,
   231: 193,
   232: 356,
   233: 357,
   234: 205,
   235: 381,
   236: 382,
   237: 362,
   238: 211,
   239: 212,
   240: 363,
   241: 366,
   242: 218,
   243: 367,
   244: 368,
   245: 369,
   246: 370,
   247: 371,
   248: 221,
   249: 253,
   250: 311,
   251: 379,
   252: 321,
   253: 380,
   254: 290,
   255: 711
   })
encoding_map = codecs.make_encoding_map(decoding_map)