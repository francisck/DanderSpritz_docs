# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: stat.py
"""Constants/functions for interpreting results of os.stat() and os.lstat().

Suggested usage: from stat import *
"""
ST_MODE = 0
ST_INO = 1
ST_DEV = 2
ST_NLINK = 3
ST_UID = 4
ST_GID = 5
ST_SIZE = 6
ST_ATIME = 7
ST_MTIME = 8
ST_CTIME = 9

def S_IMODE(mode):
    return mode & 4095


def S_IFMT(mode):
    return mode & 61440


S_IFDIR = 16384
S_IFCHR = 8192
S_IFBLK = 24576
S_IFREG = 32768
S_IFIFO = 4096
S_IFLNK = 40960
S_IFSOCK = 49152

def S_ISDIR(mode):
    return S_IFMT(mode) == S_IFDIR


def S_ISCHR(mode):
    return S_IFMT(mode) == S_IFCHR


def S_ISBLK(mode):
    return S_IFMT(mode) == S_IFBLK


def S_ISREG(mode):
    return S_IFMT(mode) == S_IFREG


def S_ISFIFO(mode):
    return S_IFMT(mode) == S_IFIFO


def S_ISLNK(mode):
    return S_IFMT(mode) == S_IFLNK


def S_ISSOCK(mode):
    return S_IFMT(mode) == S_IFSOCK


S_ISUID = 2048
S_ISGID = 1024
S_ENFMT = S_ISGID
S_ISVTX = 512
S_IREAD = 256
S_IWRITE = 128
S_IEXEC = 64
S_IRWXU = 448
S_IRUSR = 256
S_IWUSR = 128
S_IXUSR = 64
S_IRWXG = 56
S_IRGRP = 32
S_IWGRP = 16
S_IXGRP = 8
S_IRWXO = 7
S_IROTH = 4
S_IWOTH = 2
S_IXOTH = 1
UF_NODUMP = 1
UF_IMMUTABLE = 2
UF_APPEND = 4
UF_OPAQUE = 8
UF_NOUNLINK = 16
SF_ARCHIVED = 65536
SF_IMMUTABLE = 131072
SF_APPEND = 262144
SF_NOUNLINK = 1048576
SF_SNAPSHOT = 2097152