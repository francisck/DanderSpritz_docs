# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: ptcp154.py
""" Python Character Mapping Codec generated from 'PTCP154.txt' with gencodec.py.

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
    return codecs.CodecInfo(name='ptcp154', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamreader=StreamReader, streamwriter=StreamWriter)


decoding_map = codecs.make_identity_dict(range(256))
decoding_map.update({128: 1174,
   129: 1170,
   130: 1262,
   131: 1171,
   132: 8222,
   133: 8230,
   134: 1206,
   135: 1198,
   136: 1202,
   137: 1199,
   138: 1184,
   139: 1250,
   140: 1186,
   141: 1178,
   142: 1210,
   143: 1208,
   144: 1175,
   145: 8216,
   146: 8217,
   147: 8220,
   148: 8221,
   149: 8226,
   150: 8211,
   151: 8212,
   152: 1203,
   153: 1207,
   154: 1185,
   155: 1251,
   156: 1187,
   157: 1179,
   158: 1211,
   159: 1209,
   161: 1038,
   162: 1118,
   163: 1032,
   164: 1256,
   165: 1176,
   166: 1200,
   168: 1025,
   170: 1240,
   173: 1263,
   175: 1180,
   177: 1201,
   178: 1030,
   179: 1110,
   180: 1177,
   181: 1257,
   184: 1105,
   185: 8470,
   186: 1241,
   188: 1112,
   189: 1194,
   190: 1195,
   191: 1181,
   192: 1040,
   193: 1041,
   194: 1042,
   195: 1043,
   196: 1044,
   197: 1045,
   198: 1046,
   199: 1047,
   200: 1048,
   201: 1049,
   202: 1050,
   203: 1051,
   204: 1052,
   205: 1053,
   206: 1054,
   207: 1055,
   208: 1056,
   209: 1057,
   210: 1058,
   211: 1059,
   212: 1060,
   213: 1061,
   214: 1062,
   215: 1063,
   216: 1064,
   217: 1065,
   218: 1066,
   219: 1067,
   220: 1068,
   221: 1069,
   222: 1070,
   223: 1071,
   224: 1072,
   225: 1073,
   226: 1074,
   227: 1075,
   228: 1076,
   229: 1077,
   230: 1078,
   231: 1079,
   232: 1080,
   233: 1081,
   234: 1082,
   235: 1083,
   236: 1084,
   237: 1085,
   238: 1086,
   239: 1087,
   240: 1088,
   241: 1089,
   242: 1090,
   243: 1091,
   244: 1092,
   245: 1093,
   246: 1094,
   247: 1095,
   248: 1096,
   249: 1097,
   250: 1098,
   251: 1099,
   252: 1100,
   253: 1101,
   254: 1102,
   255: 1103
   })
encoding_map = codecs.make_encoding_map(decoding_map)