# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: imghdr.py
"""Recognize image file formats based on their first few bytes."""
__all__ = [
 'what']

def what(file, h=None):
    if h is None:
        if isinstance(file, basestring):
            f = open(file, 'rb')
            h = f.read(32)
        else:
            location = file.tell()
            h = file.read(32)
            file.seek(location)
            f = None
    else:
        f = None
    try:
        for tf in tests:
            res = tf(h, f)
            if res:
                return res

    finally:
        if f:
            f.close()

    return


tests = []

def test_jpeg(h, f):
    """JPEG data in JFIF format"""
    if h[6:10] == 'JFIF':
        return 'jpeg'


tests.append(test_jpeg)

def test_exif(h, f):
    """JPEG data in Exif format"""
    if h[6:10] == 'Exif':
        return 'jpeg'


tests.append(test_exif)

def test_png(h, f):
    if h[:8] == '\x89PNG\r\n\x1a\n':
        return 'png'


tests.append(test_png)

def test_gif(h, f):
    """GIF ('87 and '89 variants)"""
    if h[:6] in ('GIF87a', 'GIF89a'):
        return 'gif'


tests.append(test_gif)

def test_tiff(h, f):
    """TIFF (can be in Motorola or Intel byte order)"""
    if h[:2] in ('MM', 'II'):
        return 'tiff'


tests.append(test_tiff)

def test_rgb(h, f):
    """SGI image library"""
    if h[:2] == '\x01\xda':
        return 'rgb'


tests.append(test_rgb)

def test_pbm(h, f):
    """PBM (portable bitmap)"""
    if len(h) >= 3 and h[0] == 'P' and h[1] in '14' and h[2] in ' \t\n\r':
        return 'pbm'


tests.append(test_pbm)

def test_pgm(h, f):
    """PGM (portable graymap)"""
    if len(h) >= 3 and h[0] == 'P' and h[1] in '25' and h[2] in ' \t\n\r':
        return 'pgm'


tests.append(test_pgm)

def test_ppm(h, f):
    """PPM (portable pixmap)"""
    if len(h) >= 3 and h[0] == 'P' and h[1] in '36' and h[2] in ' \t\n\r':
        return 'ppm'


tests.append(test_ppm)

def test_rast(h, f):
    """Sun raster file"""
    if h[:4] == 'Y\xa6j\x95':
        return 'rast'


tests.append(test_rast)

def test_xbm(h, f):
    """X bitmap (X10 or X11)"""
    s = '#define '
    if h[:len(s)] == s:
        return 'xbm'


tests.append(test_xbm)

def test_bmp(h, f):
    if h[:2] == 'BM':
        return 'bmp'


tests.append(test_bmp)

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