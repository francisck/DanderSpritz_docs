# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: version.py
"""Provides classes to represent module version numbers (one class for
each style of version numbering).  There are currently two such classes
implemented: StrictVersion and LooseVersion.

Every version number class implements the following interface:
  * the 'parse' method takes a string and parses it to some internal
    representation; if the string is an invalid version number,
    'parse' raises a ValueError exception
  * the class constructor takes an optional string argument which,
    if supplied, is passed to 'parse'
  * __str__ reconstructs the string that was passed to 'parse' (or
    an equivalent string -- ie. one that will generate an equivalent
    version number instance)
  * __repr__ generates Python code to recreate the version number instance
  * __cmp__ compares the current instance with either another instance
    of the same class or a string (which will be parsed to an instance
    of the same class, thus must follow the same rules)
"""
import string
import re
from types import StringType

class Version:
    """Abstract base class for version numbering classes.  Just provides
    constructor (__init__) and reproducer (__repr__), because those
    seem to be the same for all version numbering classes.
    """

    def __init__(self, vstring=None):
        if vstring:
            self.parse(vstring)

    def __repr__(self):
        return "%s ('%s')" % (self.__class__.__name__, str(self))


class StrictVersion(Version):
    """Version numbering for anal retentives and software idealists.
    Implements the standard interface for version number classes as
    described above.  A version number consists of two or three
    dot-separated numeric components, with an optional "pre-release" tag
    on the end.  The pre-release tag consists of the letter 'a' or 'b'
    followed by a number.  If the numeric components of two version
    numbers are equal, then one with a pre-release tag will always
    be deemed earlier (lesser) than one without.
    
    The following are valid version numbers (shown in the order that
    would be obtained by sorting according to the supplied cmp function):
    
        0.4       0.4.0  (these two are equivalent)
        0.4.1
        0.5a1
        0.5b3
        0.5
        0.9.6
        1.0
        1.0.4a3
        1.0.4b1
        1.0.4
    
    The following are examples of invalid version numbers:
    
        1
        2.7.2.2
        1.3.a4
        1.3pl1
        1.3c4
    
    The rationale for this version numbering system will be explained
    in the distutils documentation.
    """
    version_re = re.compile('^(\\d+) \\. (\\d+) (\\. (\\d+))? ([ab](\\d+))?$', re.VERBOSE)

    def parse(self, vstring):
        match = self.version_re.match(vstring)
        if not match:
            raise ValueError, "invalid version number '%s'" % vstring
        major, minor, patch, prerelease, prerelease_num = match.group(1, 2, 4, 5, 6)
        if patch:
            self.version = tuple(map(string.atoi, [major, minor, patch]))
        else:
            self.version = tuple(map(string.atoi, [major, minor]) + [0])
        if prerelease:
            self.prerelease = (
             prerelease[0], string.atoi(prerelease_num))
        else:
            self.prerelease = None
        return

    def __str__(self):
        if self.version[2] == 0:
            vstring = string.join(map(str, self.version[0:2]), '.')
        else:
            vstring = string.join(map(str, self.version), '.')
        if self.prerelease:
            vstring = vstring + self.prerelease[0] + str(self.prerelease[1])
        return vstring

    def __cmp__(self, other):
        if isinstance(other, StringType):
            other = StrictVersion(other)
        compare = cmp(self.version, other.version)
        if compare == 0:
            if not self.prerelease and not other.prerelease:
                return 0
            if self.prerelease and not other.prerelease:
                return -1
            if not self.prerelease and other.prerelease:
                return 1
            if self.prerelease and other.prerelease:
                return cmp(self.prerelease, other.prerelease)
        else:
            return compare


class LooseVersion(Version):
    """Version numbering for anarchists and software realists.
    Implements the standard interface for version number classes as
    described above.  A version number consists of a series of numbers,
    separated by either periods or strings of letters.  When comparing
    version numbers, the numeric components will be compared
    numerically, and the alphabetic components lexically.  The following
    are all valid version numbers, in no particular order:
    
        1.5.1
        1.5.2b2
        161
        3.10a
        8.02
        3.4j
        1996.07.12
        3.2.pl0
        3.1.1.6
        2g6
        11g
        0.960923
        2.2beta29
        1.13++
        5.5.kw
        2.0b1pl0
    
    In fact, there is no such thing as an invalid version number under
    this scheme; the rules for comparison are simple and predictable,
    but may not always give the results you want (for some definition
    of "want").
    """
    component_re = re.compile('(\\d+ | [a-z]+ | \\.)', re.VERBOSE)

    def __init__(self, vstring=None):
        if vstring:
            self.parse(vstring)

    def parse(self, vstring):
        self.vstring = vstring
        components = filter(lambda x: x and x != '.', self.component_re.split(vstring))
        for i in range(len(components)):
            try:
                components[i] = int(components[i])
            except ValueError:
                pass

        self.version = components

    def __str__(self):
        return self.vstring

    def __repr__(self):
        return "LooseVersion ('%s')" % str(self)

    def __cmp__(self, other):
        if isinstance(other, StringType):
            other = LooseVersion(other)
        return cmp(self.version, other.version)