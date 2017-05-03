# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: hp_roman8.py
""" Python Character Mapping Codec generated from 'hp_roman8.txt' with gencodec.py.

    Based on data from ftp://dkuug.dk/i18n/charmaps/HP-ROMAN8 (Keld Simonsen)

    Original source: LaserJet IIP Printer User's Manual HP part no
    33471-90901, Hewlet-Packard, June 1989.

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
    return codecs.CodecInfo(name='hp-roman8', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamwriter=StreamWriter, streamreader=StreamReader)


decoding_map = codecs.make_identity_dict(range(256))
decoding_map.update({161: 192,
   162: 194,
   163: 200,
   164: 202,
   165: 203,
   166: 206,
   167: 207,
   168: 180,
   169: 715,
   170: 710,
   171: 168,
   172: 732,
   173: 217,
   174: 219,
   175: 8356,
   176: 175,
   177: 221,
   178: 253,
   179: 176,
   180: 199,
   181: 231,
   182: 209,
   183: 241,
   184: 161,
   185: 191,
   186: 164,
   187: 163,
   188: 165,
   189: 167,
   190: 402,
   191: 162,
   192: 226,
   193: 234,
   194: 244,
   195: 251,
   196: 225,
   197: 233,
   198: 243,
   199: 250,
   200: 224,
   201: 232,
   202: 242,
   203: 249,
   204: 228,
   205: 235,
   206: 246,
   207: 252,
   208: 197,
   209: 238,
   210: 216,
   211: 198,
   212: 229,
   213: 237,
   214: 248,
   215: 230,
   216: 196,
   217: 236,
   218: 214,
   219: 220,
   220: 201,
   221: 239,
   222: 223,
   223: 212,
   224: 193,
   225: 195,
   226: 227,
   227: 208,
   228: 240,
   229: 205,
   230: 204,
   231: 211,
   232: 210,
   233: 213,
   234: 245,
   235: 352,
   236: 353,
   237: 218,
   238: 376,
   239: 255,
   240: 222,
   241: 254,
   242: 183,
   243: 181,
   244: 182,
   245: 190,
   246: 8212,
   247: 188,
   248: 189,
   249: 170,
   250: 186,
   251: 171,
   252: 9632,
   253: 187,
   254: 177,
   255: None
   })
encoding_map = codecs.make_encoding_map(decoding_map)