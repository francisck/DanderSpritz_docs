# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: extension.py
"""distutils.extension

Provides the Extension class, used to describe C/C++ extension
modules in setup scripts."""
__revision__ = '$Id$'
import os
import string
import sys
from types import *
try:
    import warnings
except ImportError:
    warnings = None

class Extension:
    """Just a collection of attributes that describes an extension
    module and everything needed to build it (hopefully in a portable
    way, but there are hooks that let you be as unportable as you need).
    
    Instance attributes:
      name : string
        the full name of the extension, including any packages -- ie.
        *not* a filename or pathname, but Python dotted name
      sources : [string]
        list of source filenames, relative to the distribution root
        (where the setup script lives), in Unix form (slash-separated)
        for portability.  Source files may be C, C++, SWIG (.i),
        platform-specific resource files, or whatever else is recognized
        by the "build_ext" command as source for a Python extension.
      include_dirs : [string]
        list of directories to search for C/C++ header files (in Unix
        form for portability)
      define_macros : [(name : string, value : string|None)]
        list of macros to define; each macro is defined using a 2-tuple,
        where 'value' is either the string to define it to or None to
        define it without a particular value (equivalent of "#define
        FOO" in source or -DFOO on Unix C compiler command line)
      undef_macros : [string]
        list of macros to undefine explicitly
      library_dirs : [string]
        list of directories to search for C/C++ libraries at link time
      libraries : [string]
        list of library names (not filenames or paths) to link against
      runtime_library_dirs : [string]
        list of directories to search for C/C++ libraries at run time
        (for shared extensions, this is when the extension is loaded)
      extra_objects : [string]
        list of extra files to link with (eg. object files not implied
        by 'sources', static library that must be explicitly specified,
        binary resource files, etc.)
      extra_compile_args : [string]
        any extra platform- and compiler-specific information to use
        when compiling the source files in 'sources'.  For platforms and
        compilers where "command line" makes sense, this is typically a
        list of command-line arguments, but for other platforms it could
        be anything.
      extra_link_args : [string]
        any extra platform- and compiler-specific information to use
        when linking object files together to create the extension (or
        to create a new static Python interpreter).  Similar
        interpretation as for 'extra_compile_args'.
      export_symbols : [string]
        list of symbols to be exported from a shared extension.  Not
        used on all platforms, and not generally necessary for Python
        extensions, which typically export exactly one symbol: "init" +
        extension_name.
      swig_opts : [string]
        any extra options to pass to SWIG if a source file has the .i
        extension.
      depends : [string]
        list of files that the extension depends on
      language : string
        extension language (i.e. "c", "c++", "objc"). Will be detected
        from the source extensions if not provided.
    """

    def __init__(self, name, sources, include_dirs=None, define_macros=None, undef_macros=None, library_dirs=None, libraries=None, runtime_library_dirs=None, extra_objects=None, extra_compile_args=None, extra_link_args=None, export_symbols=None, swig_opts=None, depends=None, language=None, **kw):
        self.name = name
        self.sources = sources
        self.include_dirs = include_dirs or []
        self.define_macros = define_macros or []
        self.undef_macros = undef_macros or []
        self.library_dirs = library_dirs or []
        self.libraries = libraries or []
        self.runtime_library_dirs = runtime_library_dirs or []
        self.extra_objects = extra_objects or []
        self.extra_compile_args = extra_compile_args or []
        self.extra_link_args = extra_link_args or []
        self.export_symbols = export_symbols or []
        self.swig_opts = swig_opts or []
        self.depends = depends or []
        self.language = language
        if len(kw):
            L = kw.keys()
            L.sort()
            L = map(repr, L)
            msg = 'Unknown Extension options: ' + string.join(L, ', ')
            if warnings is not None:
                warnings.warn(msg)
            else:
                sys.stderr.write(msg + '\n')
        return


def read_setup_file(filename):
    from distutils.sysconfig import parse_makefile, expand_makefile_vars, _variable_rx
    from distutils.text_file import TextFile
    from distutils.util import split_quoted
    vars = parse_makefile(filename)
    file = TextFile(filename, strip_comments=1, skip_blanks=1, join_lines=1, lstrip_ws=1, rstrip_ws=1)
    try:
        extensions = []
        while 1:
            line = file.readline()
            if line is None:
                break
            if _variable_rx.match(line):
                continue
                if line[0] == line[-1] == '*':
                    file.warn("'%s' lines not handled yet" % line)
                    continue
            line = expand_makefile_vars(line, vars)
            words = split_quoted(line)
            module = words[0]
            ext = Extension(module, [])
            append_next_word = None
            for word in words[1:]:
                if append_next_word is not None:
                    append_next_word.append(word)
                    append_next_word = None
                    continue
                suffix = os.path.splitext(word)[1]
                switch = word[0:2]
                value = word[2:]
                if suffix in ('.c', '.cc', '.cpp', '.cxx', '.c++', '.m', '.mm'):
                    ext.sources.append(word)
                elif switch == '-I':
                    ext.include_dirs.append(value)
                elif switch == '-D':
                    equals = string.find(value, '=')
                    if equals == -1:
                        ext.define_macros.append((value, None))
                    else:
                        ext.define_macros.append((value[0:equals],
                         value[equals + 2:]))
                elif switch == '-U':
                    ext.undef_macros.append(value)
                elif switch == '-C':
                    ext.extra_compile_args.append(word)
                elif switch == '-l':
                    ext.libraries.append(value)
                elif switch == '-L':
                    ext.library_dirs.append(value)
                elif switch == '-R':
                    ext.runtime_library_dirs.append(value)
                elif word == '-rpath':
                    append_next_word = ext.runtime_library_dirs
                elif word == '-Xlinker':
                    append_next_word = ext.extra_link_args
                elif word == '-Xcompiler':
                    append_next_word = ext.extra_compile_args
                elif switch == '-u':
                    ext.extra_link_args.append(word)
                    if not value:
                        append_next_word = ext.extra_link_args
                elif word == '-Xcompiler':
                    append_next_word = ext.extra_compile_args
                elif switch == '-u':
                    ext.extra_link_args.append(word)
                    if not value:
                        append_next_word = ext.extra_link_args
                elif suffix in ('.a', '.so', '.sl', '.o', '.dylib'):
                    ext.extra_objects.append(word)
                else:
                    file.warn("unrecognized argument '%s'" % word)

            extensions.append(ext)

    finally:
        file.close()

    return extensions