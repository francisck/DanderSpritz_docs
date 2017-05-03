# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: idna.py
import stringprep
import re
import codecs
from unicodedata import ucd_3_2_0 as unicodedata
dots = re.compile(u'[.\u3002\uff0e\uff61]')
ace_prefix = 'xn--'
uace_prefix = unicode(ace_prefix, 'ascii')

def nameprep(label):
    newlabel = []
    for c in label:
        if stringprep.in_table_b1(c):
            continue
        newlabel.append(stringprep.map_table_b2(c))

    label = u''.join(newlabel)
    label = unicodedata.normalize('NFKC', label)
    for c in label:
        if stringprep.in_table_c12(c) or stringprep.in_table_c22(c) or stringprep.in_table_c3(c) or stringprep.in_table_c4(c) or stringprep.in_table_c5(c) or stringprep.in_table_c6(c) or stringprep.in_table_c7(c) or stringprep.in_table_c8(c) or stringprep.in_table_c9(c):
            raise UnicodeError('Invalid character %r' % c)

    RandAL = map(stringprep.in_table_d1, label)
    for c in RandAL:
        if c:
            if filter(stringprep.in_table_d2, label):
                raise UnicodeError('Violation of BIDI requirement 2')
            if not RandAL[0] or not RandAL[-1]:
                raise UnicodeError('Violation of BIDI requirement 3')

    return label


def ToASCII(label):
    try:
        label = label.encode('ascii')
    except UnicodeError:
        pass
    else:
        if 0 < len(label) < 64:
            return label
        raise UnicodeError('label empty or too long')

    label = nameprep(label)
    try:
        label = label.encode('ascii')
    except UnicodeError:
        pass
    else:
        if 0 < len(label) < 64:
            return label
        raise UnicodeError('label empty or too long')

    if label.startswith(uace_prefix):
        raise UnicodeError('Label starts with ACE prefix')
    label = label.encode('punycode')
    label = ace_prefix + label
    if 0 < len(label) < 64:
        return label
    raise UnicodeError('label empty or too long')


def ToUnicode(label):
    if isinstance(label, str):
        pure_ascii = True
    else:
        try:
            label = label.encode('ascii')
            pure_ascii = True
        except UnicodeError:
            pure_ascii = False

    if not pure_ascii:
        label = nameprep(label)
        try:
            label = label.encode('ascii')
        except UnicodeError:
            raise UnicodeError('Invalid character in IDN label')

    if not label.startswith(ace_prefix):
        return unicode(label, 'ascii')
    label1 = label[len(ace_prefix):]
    result = label1.decode('punycode')
    label2 = ToASCII(result)
    if label.lower() != label2:
        raise UnicodeError('IDNA does not round-trip', label, label2)
    return result


class Codec(codecs.Codec):

    def encode(self, input, errors='strict'):
        if errors != 'strict':
            raise UnicodeError('unsupported error handling ' + errors)
        if not input:
            return ('', 0)
        result = []
        labels = dots.split(input)
        if labels and len(labels[-1]) == 0:
            trailing_dot = '.'
            del labels[-1]
        else:
            trailing_dot = ''
        for label in labels:
            result.append(ToASCII(label))

        return (
         '.'.join(result) + trailing_dot, len(input))

    def decode(self, input, errors='strict'):
        if errors != 'strict':
            raise UnicodeError('Unsupported error handling ' + errors)
        if not input:
            return (u'', 0)
        if isinstance(input, unicode):
            labels = dots.split(input)
        else:
            input = str(input)
            unicode(input, 'ascii')
            labels = input.split('.')
        if labels and len(labels[-1]) == 0:
            trailing_dot = u'.'
            del labels[-1]
        else:
            trailing_dot = u''
        result = []
        for label in labels:
            result.append(ToUnicode(label))

        return (
         u'.'.join(result) + trailing_dot, len(input))


class IncrementalEncoder(codecs.BufferedIncrementalEncoder):

    def _buffer_encode(self, input, errors, final):
        if errors != 'strict':
            raise UnicodeError('unsupported error handling ' + errors)
        if not input:
            return ('', 0)
        labels = dots.split(input)
        trailing_dot = u''
        if labels:
            if not labels[-1]:
                trailing_dot = '.'
                del labels[-1]
            elif not final:
                del labels[-1]
                if labels:
                    trailing_dot = '.'
        result = []
        size = 0
        for label in labels:
            result.append(ToASCII(label))
            if size:
                size += 1
            size += len(label)

        result = '.'.join(result) + trailing_dot
        size += len(trailing_dot)
        return (
         result, size)


class IncrementalDecoder(codecs.BufferedIncrementalDecoder):

    def _buffer_decode(self, input, errors, final):
        if errors != 'strict':
            raise UnicodeError('Unsupported error handling ' + errors)
        if not input:
            return (u'', 0)
        if isinstance(input, unicode):
            labels = dots.split(input)
        else:
            input = str(input)
            unicode(input, 'ascii')
            labels = input.split('.')
        trailing_dot = u''
        if labels:
            if not labels[-1]:
                trailing_dot = u'.'
                del labels[-1]
            elif not final:
                del labels[-1]
                if labels:
                    trailing_dot = u'.'
        result = []
        size = 0
        for label in labels:
            result.append(ToUnicode(label))
            if size:
                size += 1
            size += len(label)

        result = u'.'.join(result) + trailing_dot
        size += len(trailing_dot)
        return (
         result, size)


class StreamWriter(Codec, codecs.StreamWriter):
    pass


class StreamReader(Codec, codecs.StreamReader):
    pass


def getregentry():
    return codecs.CodecInfo(name='idna', encode=Codec().encode, decode=Codec().decode, incrementalencoder=IncrementalEncoder, incrementaldecoder=IncrementalDecoder, streamwriter=StreamWriter, streamreader=StreamReader)