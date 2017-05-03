# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: emxccompiler.py
"""distutils.emxccompiler

Provides the EMXCCompiler class, a subclass of UnixCCompiler that
handles the EMX port of the GNU C compiler to OS/2.
"""
__revision__ = '$Id$'
import os
import sys
import copy
from distutils.ccompiler import gen_preprocess_options, gen_lib_options
from distutils.unixccompiler import UnixCCompiler
from distutils.file_util import write_file
from distutils.errors import DistutilsExecError, CompileError, UnknownFileError
from distutils import log

class EMXCCompiler(UnixCCompiler):
    compiler_type = 'emx'
    obj_extension = '.obj'
    static_lib_extension = '.lib'
    shared_lib_extension = '.dll'
    static_lib_format = '%s%s'
    shared_lib_format = '%s%s'
    res_extension = '.res'
    exe_extension = '.exe'

    def __init__(self, verbose=0, dry_run=0, force=0):
        UnixCCompiler.__init__(self, verbose, dry_run, force)
        status, details = check_config_h()
        self.debug_print("Python's GCC status: %s (details: %s)" % (
         status, details))
        if status is not CONFIG_H_OK:
            self.warn("Python's pyconfig.h doesn't seem to support your compiler.  " + 'Reason: %s.' % details + 'Compiling may fail because of undefined preprocessor macros.')
        self.gcc_version, self.ld_version = get_versions()
        self.debug_print(self.compiler_type + ': gcc %s, ld %s\n' % (
         self.gcc_version,
         self.ld_version))
        self.set_executables(compiler='gcc -Zomf -Zmt -O3 -fomit-frame-pointer -mprobe -Wall', compiler_so='gcc -Zomf -Zmt -O3 -fomit-frame-pointer -mprobe -Wall', linker_exe='gcc -Zomf -Zmt -Zcrtdll', linker_so='gcc -Zomf -Zmt -Zcrtdll -Zdll')
        self.dll_libraries = [
         'gcc']

    def _compile(self, obj, src, ext, cc_args, extra_postargs, pp_opts):
        if ext == '.rc':
            try:
                self.spawn(['rc', '-r', src])
            except DistutilsExecError as msg:
                raise CompileError, msg

        else:
            try:
                self.spawn(self.compiler_so + cc_args + [src, '-o', obj] + extra_postargs)
            except DistutilsExecError as msg:
                raise CompileError, msg

    def link(self, target_desc, objects, output_filename, output_dir=None, libraries=None, library_dirs=None, runtime_library_dirs=None, export_symbols=None, debug=0, extra_preargs=None, extra_postargs=None, build_temp=None, target_lang=None):
        extra_preargs = copy.copy(extra_preargs or [])
        libraries = copy.copy(libraries or [])
        objects = copy.copy(objects or [])
        libraries.extend(self.dll_libraries)
        if export_symbols is not None and target_desc != self.EXECUTABLE:
            temp_dir = os.path.dirname(objects[0])
            dll_name, dll_extension = os.path.splitext(os.path.basename(output_filename))
            def_file = os.path.join(temp_dir, dll_name + '.def')
            contents = [
             'LIBRARY %s INITINSTANCE TERMINSTANCE' % os.path.splitext(os.path.basename(output_filename))[0],
             'DATA MULTIPLE NONSHARED',
             'EXPORTS']
            for sym in export_symbols:
                contents.append('  "%s"' % sym)

            self.execute(write_file, (def_file, contents), 'writing %s' % def_file)
            objects.append(def_file)
        if not debug:
            extra_preargs.append('-s')
        UnixCCompiler.link(self, target_desc, objects, output_filename, output_dir, libraries, library_dirs, runtime_library_dirs, None, debug, extra_preargs, extra_postargs, build_temp, target_lang)
        return

    def object_filenames(self, source_filenames, strip_dir=0, output_dir=''):
        if output_dir is None:
            output_dir = ''
        obj_names = []
        for src_name in source_filenames:
            base, ext = os.path.splitext(os.path.normcase(src_name))
            if ext not in self.src_extensions + ['.rc']:
                raise UnknownFileError, "unknown file type '%s' (from '%s')" % (
                 ext, src_name)
            if strip_dir:
                base = os.path.basename(base)
            if ext == '.rc':
                obj_names.append(os.path.join(output_dir, base + self.res_extension))
            else:
                obj_names.append(os.path.join(output_dir, base + self.obj_extension))

        return obj_names

    def find_library_file(self, dirs, lib, debug=0):
        shortlib = '%s.lib' % lib
        longlib = 'lib%s.lib' % lib
        try:
            emx_dirs = os.environ['LIBRARY_PATH'].split(';')
        except KeyError:
            emx_dirs = []

        for dir in dirs + emx_dirs:
            shortlibp = os.path.join(dir, shortlib)
            longlibp = os.path.join(dir, longlib)
            if os.path.exists(shortlibp):
                return shortlibp
            if os.path.exists(longlibp):
                return longlibp

        return None


CONFIG_H_OK = 'ok'
CONFIG_H_NOTOK = 'not ok'
CONFIG_H_UNCERTAIN = 'uncertain'

def check_config_h():
    """Check if the current Python installation (specifically, pyconfig.h)
    appears amenable to building extensions with GCC.  Returns a tuple
    (status, details), where 'status' is one of the following constants:
      CONFIG_H_OK
        all is well, go ahead and compile
      CONFIG_H_NOTOK
        doesn't look good
      CONFIG_H_UNCERTAIN
        not sure -- unable to read pyconfig.h
    'details' is a human-readable string explaining the situation.
    
    Note there are two ways to conclude "OK": either 'sys.version' contains
    the string "GCC" (implying that this Python was built with GCC), or the
    installed "pyconfig.h" contains the string "__GNUC__".
    """
    from distutils import sysconfig
    import string
    if string.find(sys.version, 'GCC') >= 0:
        return (CONFIG_H_OK, "sys.version mentions 'GCC'")
    else:
        fn = sysconfig.get_config_h_filename()
        try:
            f = open(fn)
            try:
                s = f.read()
            finally:
                f.close()

        except IOError as exc:
            return (
             CONFIG_H_UNCERTAIN,
             "couldn't read '%s': %s" % (fn, exc.strerror))

        if string.find(s, '__GNUC__') >= 0:
            return (CONFIG_H_OK, "'%s' mentions '__GNUC__'" % fn)
        return (
         CONFIG_H_NOTOK, "'%s' does not mention '__GNUC__'" % fn)


def get_versions():
    """ Try to find out the versions of gcc and ld.
        If not possible it returns None for it.
    """
    from distutils.version import StrictVersion
    from distutils.spawn import find_executable
    import re
    gcc_exe = find_executable('gcc')
    if gcc_exe:
        out = os.popen(gcc_exe + ' -dumpversion', 'r')
        try:
            out_string = out.read()
        finally:
            out.close()

        result = re.search('(\\d+\\.\\d+\\.\\d+)', out_string)
        if result:
            gcc_version = StrictVersion(result.group(1))
        else:
            gcc_version = None
    else:
        gcc_version = None
    ld_version = None
    return (
     gcc_version, ld_version)