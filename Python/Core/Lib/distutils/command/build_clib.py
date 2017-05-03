# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: build_clib.py
"""distutils.command.build_clib

Implements the Distutils 'build_clib' command, to build a C/C++ library
that is included in the module distribution and needed by an extension
module."""
__revision__ = '$Id$'
import os
from distutils.core import Command
from distutils.errors import DistutilsSetupError
from distutils.ccompiler import customize_compiler
from distutils import log

def show_compilers():
    from distutils.ccompiler import show_compilers
    show_compilers()


class build_clib(Command):
    description = 'build C/C++ libraries used by Python extensions'
    user_options = [
     ('build-clib=', 'b', 'directory to build C/C++ libraries to'),
     ('build-temp=', 't', 'directory to put temporary build by-products'),
     ('debug', 'g', 'compile with debugging information'),
     ('force', 'f', 'forcibly build everything (ignore file timestamps)'),
     ('compiler=', 'c', 'specify the compiler type')]
    boolean_options = [
     'debug', 'force']
    help_options = [
     (
      'help-compiler', None,
      'list available compilers', show_compilers)]

    def initialize_options(self):
        self.build_clib = None
        self.build_temp = None
        self.libraries = None
        self.include_dirs = None
        self.define = None
        self.undef = None
        self.debug = None
        self.force = 0
        self.compiler = None
        return

    def finalize_options(self):
        self.set_undefined_options('build', ('build_temp', 'build_clib'), ('build_temp',
                                                                           'build_temp'), ('compiler',
                                                                                           'compiler'), ('debug',
                                                                                                         'debug'), ('force',
                                                                                                                    'force'))
        self.libraries = self.distribution.libraries
        if self.libraries:
            self.check_library_list(self.libraries)
        if self.include_dirs is None:
            self.include_dirs = self.distribution.include_dirs or []
        if isinstance(self.include_dirs, str):
            self.include_dirs = self.include_dirs.split(os.pathsep)
        return

    def run(self):
        if not self.libraries:
            return
        else:
            from distutils.ccompiler import new_compiler
            self.compiler = new_compiler(compiler=self.compiler, dry_run=self.dry_run, force=self.force)
            customize_compiler(self.compiler)
            if self.include_dirs is not None:
                self.compiler.set_include_dirs(self.include_dirs)
            if self.define is not None:
                for name, value in self.define:
                    self.compiler.define_macro(name, value)

            if self.undef is not None:
                for macro in self.undef:
                    self.compiler.undefine_macro(macro)

            self.build_libraries(self.libraries)
            return

    def check_library_list(self, libraries):
        """Ensure that the list of libraries is valid.
        
        `library` is presumably provided as a command option 'libraries'.
        This method checks that it is a list of 2-tuples, where the tuples
        are (library_name, build_info_dict).
        
        Raise DistutilsSetupError if the structure is invalid anywhere;
        just returns otherwise.
        """
        if not isinstance(libraries, list):
            raise DistutilsSetupError, "'libraries' option must be a list of tuples"
        for lib in libraries:
            if not isinstance(lib, tuple) and len(lib) != 2:
                raise DistutilsSetupError, "each element of 'libraries' must a 2-tuple"
            name, build_info = lib
            if not isinstance(name, str):
                raise DistutilsSetupError, "first element of each tuple in 'libraries' " + 'must be a string (the library name)'
            if '/' in name or os.sep != '/' and os.sep in name:
                raise DistutilsSetupError, ("bad library name '%s': " + 'may not contain directory separators') % lib[0]
            if not isinstance(build_info, dict):
                raise DistutilsSetupError, "second element of each tuple in 'libraries' " + 'must be a dictionary (build info)'

    def get_library_names(self):
        if not self.libraries:
            return None
        else:
            lib_names = []
            for lib_name, build_info in self.libraries:
                lib_names.append(lib_name)

            return lib_names

    def get_source_files(self):
        self.check_library_list(self.libraries)
        filenames = []
        for lib_name, build_info in self.libraries:
            sources = build_info.get('sources')
            if sources is None or not isinstance(sources, (list, tuple)):
                raise DistutilsSetupError, "in 'libraries' option (library '%s'), 'sources' must be present and must be a list of source filenames" % lib_name
            filenames.extend(sources)

        return filenames

    def build_libraries(self, libraries):
        for lib_name, build_info in libraries:
            sources = build_info.get('sources')
            if sources is None or not isinstance(sources, (list, tuple)):
                raise DistutilsSetupError, ("in 'libraries' option (library '%s'), " + "'sources' must be present and must be " + 'a list of source filenames') % lib_name
            sources = list(sources)
            log.info("building '%s' library", lib_name)
            macros = build_info.get('macros')
            include_dirs = build_info.get('include_dirs')
            objects = self.compiler.compile(sources, output_dir=self.build_temp, macros=macros, include_dirs=include_dirs, debug=self.debug)
            self.compiler.create_static_lib(objects, lib_name, output_dir=self.build_clib, debug=self.debug)

        return