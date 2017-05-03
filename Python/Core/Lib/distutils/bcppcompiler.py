# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: bcppcompiler.py
"""distutils.bcppcompiler

Contains BorlandCCompiler, an implementation of the abstract CCompiler class
for the Borland C++ compiler.
"""
__revision__ = '$Id$'
import os
from distutils.errors import DistutilsExecError, CompileError, LibError, LinkError, UnknownFileError
from distutils.ccompiler import CCompiler, gen_preprocess_options
from distutils.file_util import write_file
from distutils.dep_util import newer
from distutils import log

class BCPPCompiler(CCompiler):
    """Concrete class that implements an interface to the Borland C/C++
    compiler, as defined by the CCompiler abstract class.
    """
    compiler_type = 'bcpp'
    executables = {}
    _c_extensions = [
     '.c']
    _cpp_extensions = ['.cc', '.cpp', '.cxx']
    src_extensions = _c_extensions + _cpp_extensions
    obj_extension = '.obj'
    static_lib_extension = '.lib'
    shared_lib_extension = '.dll'
    static_lib_format = shared_lib_format = '%s%s'
    exe_extension = '.exe'

    def __init__(self, verbose=0, dry_run=0, force=0):
        CCompiler.__init__(self, verbose, dry_run, force)
        self.cc = 'bcc32.exe'
        self.linker = 'ilink32.exe'
        self.lib = 'tlib.exe'
        self.preprocess_options = None
        self.compile_options = ['/tWM', '/O2', '/q', '/g0']
        self.compile_options_debug = ['/tWM', '/Od', '/q', '/g0']
        self.ldflags_shared = [
         '/Tpd', '/Gn', '/q', '/x']
        self.ldflags_shared_debug = ['/Tpd', '/Gn', '/q', '/x']
        self.ldflags_static = []
        self.ldflags_exe = ['/Gn', '/q', '/x']
        self.ldflags_exe_debug = ['/Gn', '/q', '/x', '/r']
        return

    def compile(self, sources, output_dir=None, macros=None, include_dirs=None, debug=0, extra_preargs=None, extra_postargs=None, depends=None):
        macros, objects, extra_postargs, pp_opts, build = self._setup_compile(output_dir, macros, include_dirs, sources, depends, extra_postargs)
        compile_opts = extra_preargs or []
        compile_opts.append('-c')
        if debug:
            compile_opts.extend(self.compile_options_debug)
        else:
            compile_opts.extend(self.compile_options)
        for obj in objects:
            try:
                src, ext = build[obj]
            except KeyError:
                continue

            src = os.path.normpath(src)
            obj = os.path.normpath(obj)
            self.mkpath(os.path.dirname(obj))
            if ext == '.res':
                continue
            if ext == '.rc':
                try:
                    self.spawn(['brcc32', '-fo', obj, src])
                except DistutilsExecError as msg:
                    raise CompileError, msg

                continue
            if ext in self._c_extensions:
                input_opt = ''
            elif ext in self._cpp_extensions:
                input_opt = '-P'
            else:
                input_opt = ''
            output_opt = '-o' + obj
            try:
                self.spawn([
                 self.cc] + compile_opts + pp_opts + [input_opt, output_opt] + extra_postargs + [src])
            except DistutilsExecError as msg:
                raise CompileError, msg

        return objects

    def create_static_lib(self, objects, output_libname, output_dir=None, debug=0, target_lang=None):
        objects, output_dir = self._fix_object_args(objects, output_dir)
        output_filename = self.library_filename(output_libname, output_dir=output_dir)
        if self._need_link(objects, output_filename):
            lib_args = [
             output_filename, '/u'] + objects
            if debug:
                pass
            try:
                self.spawn([self.lib] + lib_args)
            except DistutilsExecError as msg:
                raise LibError, msg

        else:
            log.debug('skipping %s (up-to-date)', output_filename)

    def link(self, target_desc, objects, output_filename, output_dir=None, libraries=None, library_dirs=None, runtime_library_dirs=None, export_symbols=None, debug=0, extra_preargs=None, extra_postargs=None, build_temp=None, target_lang=None):
        objects, output_dir = self._fix_object_args(objects, output_dir)
        libraries, library_dirs, runtime_library_dirs = self._fix_lib_args(libraries, library_dirs, runtime_library_dirs)
        if runtime_library_dirs:
            log.warn("I don't know what to do with 'runtime_library_dirs': %s", str(runtime_library_dirs))
        if output_dir is not None:
            output_filename = os.path.join(output_dir, output_filename)
        if self._need_link(objects, output_filename):
            if target_desc == CCompiler.EXECUTABLE:
                startup_obj = 'c0w32'
                if debug:
                    ld_args = self.ldflags_exe_debug[:]
                else:
                    ld_args = self.ldflags_exe[:]
            else:
                startup_obj = 'c0d32'
                if debug:
                    ld_args = self.ldflags_shared_debug[:]
                else:
                    ld_args = self.ldflags_shared[:]
            if export_symbols is None:
                def_file = ''
            else:
                head, tail = os.path.split(output_filename)
                modname, ext = os.path.splitext(tail)
                temp_dir = os.path.dirname(objects[0])
                def_file = os.path.join(temp_dir, '%s.def' % modname)
                contents = ['EXPORTS']
                for sym in export_symbols or []:
                    contents.append('  %s=_%s' % (sym, sym))

                self.execute(write_file, (def_file, contents), 'writing %s' % def_file)
            objects2 = map(os.path.normpath, objects)
            objects = [
             startup_obj]
            resources = []
            for file in objects2:
                base, ext = os.path.splitext(os.path.normcase(file))
                if ext == '.res':
                    resources.append(file)
                else:
                    objects.append(file)

            for l in library_dirs:
                ld_args.append('/L%s' % os.path.normpath(l))

            ld_args.append('/L.')
            ld_args.extend(objects)
            ld_args.extend([',', output_filename])
            ld_args.append(',,')
            for lib in libraries:
                libfile = self.find_library_file(library_dirs, lib, debug)
                if libfile is None:
                    ld_args.append(lib)
                else:
                    ld_args.append(libfile)

            ld_args.append('import32')
            ld_args.append('cw32mt')
            ld_args.extend([',', def_file])
            ld_args.append(',')
            ld_args.extend(resources)
            if extra_preargs:
                ld_args[:0] = extra_preargs
            if extra_postargs:
                ld_args.extend(extra_postargs)
            self.mkpath(os.path.dirname(output_filename))
            try:
                self.spawn([self.linker] + ld_args)
            except DistutilsExecError as msg:
                raise LinkError, msg

        else:
            log.debug('skipping %s (up-to-date)', output_filename)
        return

    def find_library_file(self, dirs, lib, debug=0):
        if debug:
            dlib = lib + '_d'
            try_names = (dlib + '_bcpp', lib + '_bcpp', dlib, lib)
        else:
            try_names = (
             lib + '_bcpp', lib)
        for dir in dirs:
            for name in try_names:
                libfile = os.path.join(dir, self.library_filename(name))
                if os.path.exists(libfile):
                    return libfile

        else:
            return None

        return None

    def object_filenames(self, source_filenames, strip_dir=0, output_dir=''):
        if output_dir is None:
            output_dir = ''
        obj_names = []
        for src_name in source_filenames:
            base, ext = os.path.splitext(os.path.normcase(src_name))
            if ext not in self.src_extensions + ['.rc', '.res']:
                raise UnknownFileError, "unknown file type '%s' (from '%s')" % (
                 ext, src_name)
            if strip_dir:
                base = os.path.basename(base)
            if ext == '.res':
                obj_names.append(os.path.join(output_dir, base + ext))
            elif ext == '.rc':
                obj_names.append(os.path.join(output_dir, base + '.res'))
            else:
                obj_names.append(os.path.join(output_dir, base + self.obj_extension))

        return obj_names

    def preprocess(self, source, output_file=None, macros=None, include_dirs=None, extra_preargs=None, extra_postargs=None):
        _, macros, include_dirs = self._fix_compile_args(None, macros, include_dirs)
        pp_opts = gen_preprocess_options(macros, include_dirs)
        pp_args = ['cpp32.exe'] + pp_opts
        if output_file is not None:
            pp_args.append('-o' + output_file)
        if extra_preargs:
            pp_args[:0] = extra_preargs
        if extra_postargs:
            pp_args.extend(extra_postargs)
        pp_args.append(source)
        if self.force or output_file is None or newer(source, output_file):
            if output_file:
                self.mkpath(os.path.dirname(output_file))
            try:
                self.spawn(pp_args)
            except DistutilsExecError as msg:
                print msg
                raise CompileError, msg

        return