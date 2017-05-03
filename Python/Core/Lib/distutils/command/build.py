# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: build.py
"""distutils.command.build

Implements the Distutils 'build' command."""
__revision__ = '$Id$'
import sys
import os
from distutils.util import get_platform
from distutils.core import Command
from distutils.errors import DistutilsOptionError

def show_compilers():
    from distutils.ccompiler import show_compilers
    show_compilers()


class build(Command):
    description = 'build everything needed to install'
    user_options = [
     ('build-base=', 'b', 'base directory for build library'),
     ('build-purelib=', None, 'build directory for platform-neutral distributions'),
     ('build-platlib=', None, 'build directory for platform-specific distributions'),
     (
      'build-lib=', None,
      'build directory for all distribution (defaults to either ' + 'build-purelib or build-platlib'),
     ('build-scripts=', None, 'build directory for scripts'),
     ('build-temp=', 't', 'temporary build directory'),
     (
      'plat-name=', 'p',
      'platform name to build for, if supported (default: %s)' % get_platform()),
     ('compiler=', 'c', 'specify the compiler type'),
     ('debug', 'g', 'compile extensions and libraries with debugging information'),
     ('force', 'f', 'forcibly build everything (ignore file timestamps)'),
     ('executable=', 'e', 'specify final destination interpreter path (build.py)')]
    boolean_options = [
     'debug', 'force']
    help_options = [
     (
      'help-compiler', None,
      'list available compilers', show_compilers)]

    def initialize_options(self):
        self.build_base = 'build'
        self.build_purelib = None
        self.build_platlib = None
        self.build_lib = None
        self.build_temp = None
        self.build_scripts = None
        self.compiler = None
        self.plat_name = None
        self.debug = None
        self.force = 0
        self.executable = None
        return

    def finalize_options(self):
        if self.plat_name is None:
            self.plat_name = get_platform()
        elif os.name != 'nt':
            raise DistutilsOptionError("--plat-name only supported on Windows (try using './configure --help' on your platform)")
        plat_specifier = '.%s-%s' % (self.plat_name, sys.version[0:3])
        if hasattr(sys, 'gettotalrefcount'):
            plat_specifier += '-pydebug'
        if self.build_purelib is None:
            self.build_purelib = os.path.join(self.build_base, 'lib')
        if self.build_platlib is None:
            self.build_platlib = os.path.join(self.build_base, 'lib' + plat_specifier)
        if self.build_lib is None:
            if self.distribution.ext_modules:
                self.build_lib = self.build_platlib
            else:
                self.build_lib = self.build_purelib
        if self.build_temp is None:
            self.build_temp = os.path.join(self.build_base, 'temp' + plat_specifier)
        if self.build_scripts is None:
            self.build_scripts = os.path.join(self.build_base, 'scripts-' + sys.version[0:3])
        if self.executable is None:
            self.executable = os.path.normpath(sys.executable)
        return

    def run(self):
        for cmd_name in self.get_sub_commands():
            self.run_command(cmd_name)

    def has_pure_modules(self):
        return self.distribution.has_pure_modules()

    def has_c_libraries(self):
        return self.distribution.has_c_libraries()

    def has_ext_modules(self):
        return self.distribution.has_ext_modules()

    def has_scripts(self):
        return self.distribution.has_scripts()

    sub_commands = [
     (
      'build_py', has_pure_modules),
     (
      'build_clib', has_c_libraries),
     (
      'build_ext', has_ext_modules),
     (
      'build_scripts', has_scripts)]