# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: sndhdr.py
"""Routines to help recognizing sound files.

Function whathdr() recognizes various types of sound file headers.
It understands almost all headers that SOX can decode.

The return tuple contains the following items, in this order:
- file type (as SOX understands it)
- sampling rate (0 if unknown or hard to decode)
- number of channels (0 if unknown or hard to decode)
- number of frames in the file (-1 if unknown or hard to decode)
- number of bits/sample, or 'U' for U-LAW, or 'A' for A-LAW

If the file doesn't have a recognizable type, it returns None.
If the file can't be opened, IOError is raised.

To compute the total time, divide the number of frames by the
sampling rate (a frame contains a sample for each channel).

Function what() calls whathdr().  (It used to also use some
heuristics for raw data, but this doesn't work very well.)

Finally, the function test() is a simple main program that calls
what() for all files mentioned on the argument list.  For directory
arguments it calls what() for all files in that directory.  Default
argument is "." (testing all files in the current directory).  The
option -r tells it to recurse down directories found inside
explicitly given directories.
"""
__all__ = [
 'what', 'whathdr']

def what(filename):
    """Guess the type of a sound file"""
    res = whathdr(filename)
    return res


def whathdr(filename):
    """Recognize sound headers"""
    f = open(filename, 'rb')
    h = f.read(512)
    for tf in tests:
        res = tf(h, f)
        if res:
            return res

    return None


tests = []

def test_aifc(h, f):
    import aifc
    if h[:4] != 'FORM':
        return
    else:
        if h[8:12] == 'AIFC':
            fmt = 'aifc'
        elif h[8:12] == 'AIFF':
            fmt = 'aiff'
        else:
            return
        f.seek(0)
        try:
            a = aifc.openfp(f, 'r')
        except (EOFError, aifc.Error):
            return

        return (
         fmt, a.getframerate(), a.getnchannels(),
         a.getnframes(), 8 * a.getsampwidth())


tests.append(test_aifc)

def test_au(h, f):
    if h[:4] == '.snd':
        f = get_long_be
    elif h[:4] in ('\x00ds.', 'dns.'):
        f = get_long_le
    else:
        return None
    type = 'au'
    hdr_size = f(h[4:8])
    data_size = f(h[8:12])
    encoding = f(h[12:16])
    rate = f(h[16:20])
    nchannels = f(h[20:24])
    sample_size = 1
    if encoding == 1:
        sample_bits = 'U'
    elif encoding == 2:
        sample_bits = 8
    elif encoding == 3:
        sample_bits = 16
        sample_size = 2
    else:
        sample_bits = '?'
    frame_size = sample_size * nchannels
    return (
     type, rate, nchannels, data_size // frame_size, sample_bits)


tests.append(test_au)

def test_hcom(h, f):
    if h[65:69] != 'FSSD' or h[128:132] != 'HCOM':
        return None
    else:
        divisor = get_long_be(h[144:148])
        return (
         'hcom', 22050 // divisor, 1, -1, 8)


tests.append(test_hcom)

def test_voc(h, f):
    if h[:20] != 'Creative Voice File\x1a':
        return None
    else:
        sbseek = get_short_le(h[20:22])
        rate = 0
        if 0 <= sbseek < 500 and h[sbseek] == '\x01':
            ratecode = ord(h[sbseek + 4])
            rate = int(1000000.0 / (256 - ratecode))
        return ('voc', rate, 1, -1, 8)


tests.append(test_voc)

def test_wav(h, f):
    if h[:4] != 'RIFF' or h[8:12] != 'WAVE' or h[12:16] != 'fmt ':
        return None
    else:
        style = get_short_le(h[20:22])
        nchannels = get_short_le(h[22:24])
        rate = get_long_le(h[24:28])
        sample_bits = get_short_le(h[34:36])
        return (
         'wav', rate, nchannels, -1, sample_bits)


tests.append(test_wav)

def test_8svx(h, f):
    if h[:4] != 'FORM' or h[8:12] != '8SVX':
        return None
    else:
        return ('8svx', 0, 1, 0, 8)


tests.append(test_8svx)

def test_sndt(h, f):
    if h[:5] == 'SOUND':
        nsamples = get_long_le(h[8:12])
        rate = get_short_le(h[20:22])
        return (
         'sndt', rate, 1, nsamples, 8)


tests.append(test_sndt)

def test_sndr(h, f):
    if h[:2] == '\x00\x00':
        rate = get_short_le(h[2:4])
        if 4000 <= rate <= 25000:
            return ('sndr', rate, 1, -1, 8)


tests.append(test_sndr)

def get_long_be(s):
    return ord(s[0]) << 24 | ord(s[1]) << 16 | ord(s[2]) << 8 | ord(s[3])


def get_long_le(s):
    return ord(s[3]) << 24 | ord(s[2]) << 16 | ord(s[1]) << 8 | ord(s[0])


def get_short_be(s):
    return ord(s[0]) << 8 | ord(s[1])


def get_short_le(s):
    return ord(s[1]) << 8 | ord(s[0])


def test():
    import sys
    recursive = 0
    if sys.argv[1:] and sys.argv[1] == '-r':
        del sys.argv[1:2]
        recursive = 1
    try:
        if sys.argv[1:]:
            testall(sys.argv[1:], recursive, 1)
        else:
            testall(['.'], recursive, 1)
    except KeyboardInterrupt:
        sys.stderr.write('\n[Interrupted]\n')
        sys.exit(1)


def testall(list, recursive, toplevel):
    import sys
    import os
    for filename in list:
        if os.path.isdir(filename):
            print filename + '/:',
            if recursive or toplevel:
                print 'recursing down:'
                import glob
                names = glob.glob(os.path.join(filename, '*'))
                testall(names, recursive, 0)
            else:
                print '*** directory (use -r) ***'
        else:
            print filename + ':',
            sys.stdout.flush()
            try:
                print what(filename)
            except IOError:
                print '*** not found ***'


if __name__ == '__main__':
    test()