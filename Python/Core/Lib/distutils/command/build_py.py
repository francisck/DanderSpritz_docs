# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: build_py.py
"""distutils.command.build_py

Implements the Distutils 'build_py' command."""
__revision__ = '$Id$'
import os
import sys
from glob import glob
from distutils.core import Command
from distutils.errors import DistutilsOptionError, DistutilsFileError
from distutils.util import convert_path
from distutils import log

class build_py(Command):
    description = '"build" pure Python modules (copy to build directory)'
    user_options = [
     ('build-lib=', 'd', 'directory to "build" (copy) to'),
     ('compile', 'c', 'compile .py to .pyc'),
     ('no-compile', None, "don't compile .py files [default]"),
     ('optimize=', 'O', 'also compile with optimization: -O1 for "python -O", -O2 for "python -OO", and -O0 to disable [default: -O0]'),
     ('force', 'f', 'forcibly build everything (ignore file timestamps)')]
    boolean_options = [
     'compile', 'force']
    negative_opt = {'no-compile': 'compile'}

    def initialize_options(self):
        self.build_lib = None
        self.py_modules = None
        self.package = None
        self.package_data = None
        self.package_dir = None
        self.compile = 0
        self.optimize = 0
        self.force = None
        return

    def finalize_options(self):
        self.set_undefined_options('build', ('build_lib', 'build_lib'), ('force', 'force'))
        self.packages = self.distribution.packages
        self.py_modules = self.distribution.py_modules
        self.package_data = self.distribution.package_data
        self.package_dir = {}
        if self.distribution.package_dir:
            for name, path in self.distribution.package_dir.items():
                self.package_dir[name] = convert_path(path)

        self.data_files = self.get_data_files()
        if not isinstance(self.optimize, int):
            try:
                self.optimize = int(self.optimize)
            except (ValueError, AssertionError):
                raise DistutilsOptionError('optimize must be 0, 1, or 2')

    def run(self):
        if self.py_modules:
            self.build_modules()
        if self.packages:
            self.build_packages()
            self.build_package_data()
        self.byte_compile(self.get_outputs(include_bytecode=0))

    def get_data_files(self):
        """Generate list of '(package,src_dir,build_dir,filenames)' tuples"""
        data = []
        if not self.packages:
            return data
        for package in self.packages:
            src_dir = self.get_package_dir(package)
            build_dir = os.path.join(*([self.build_lib] + package.split('.')))
            plen = 0
            if src_dir:
                plen = len(src_dir) + 1
            filenames = [ file[plen:] for file in self.find_data_files(package, src_dir) ]
            data.append((package, src_dir, build_dir, filenames))

        return data

    def find_data_files(self, package, src_dir):
        """Return filenames for package's data files in 'src_dir'"""
        globs = self.package_data.get('', []) + self.package_data.get(package, [])
        files = []
        for pattern in globs:
            filelist = glob(os.path.join(src_dir, convert_path(pattern)))
            files.extend([ fn for fn in filelist if fn not in files ])

        return files

    def build_package_data(self):
        """Copy data files into build directory"""
        for package, src_dir, build_dir, filenames in self.data_files:
            for filename in filenames:
                target = os.path.join(build_dir, filename)
                self.mkpath(os.path.dirname(target))
                self.copy_file(os.path.join(src_dir, filename), target, preserve_mode=False)

    def get_package_dir(self, package):
        """Return the directory, relative to the top of the source
        distribution, where package 'package' should be found
        (at least according to the 'package_dir' option, if any)."""
        path = package.split('.')
        if not self.package_dir:
            if path:
                return os.path.join(*path)
            else:
                return ''

        else:
            tail = []
            while path:
                try:
                    pdir = self.package_dir['.'.join(path)]
                except KeyError:
                    tail.insert(0, path[-1])
                    del path[-1]
                else:
                    tail.insert(0, pdir)
                    return os.path.join(*tail)

            else:
                pdir = self.package_dir.get('')
                if pdir is not None:
                    tail.insert(0, pdir)
                if tail:
                    return os.path.join(*tail)
                return ''

        return

    def check_package(self, package, package_dir):
        if package_dir != '':
            if not os.path.exists(package_dir):
                raise DistutilsFileError("package directory '%s' does not exist" % package_dir)
            if not os.path.isdir(package_dir):
                raise DistutilsFileError("supposed package directory '%s' exists, but is not a directory" % package_dir)
        if package:
            init_py = os.path.join(package_dir, '__init__.py')
            if os.path.isfile(init_py):
                return init_py
            log.warn("package init file '%s' not found " + '(or not a regular file)', init_py)
        return None

    def check_module(self, module, module_file):
        if not os.path.isfile(module_file):
            log.warn('file %s (for module %s) not found', module_file, module)
            return False
        else:
            return True

    def find_package_modules(self, package, package_dir):
        self.check_package(package, package_dir)
        module_files = glob(os.path.join(package_dir, '*.py'))
        modules = []
        setup_script = os.path.abspath(self.distribution.script_name)
        for f in module_files:
            abs_f = os.path.abspath(f)
            if abs_f != setup_script:
                module = os.path.splitext(os.path.basename(f))[0]
                modules.append((package, module, f))
            else:
                self.debug_print('excluding %s' % setup_script)

        return modules

    def find_modules(self):
        """Finds individually-specified Python modules, ie. those listed by
        module name in 'self.py_modules'.  Returns a list of tuples (package,
        module_base, filename): 'package' is a tuple of the path through
        package-space to the module; 'module_base' is the bare (no
        packages, no dots) module name, and 'filename' is the path to the
        ".py" file (relative to the distribution root) that implements the
        module.
        """
        packages = {}
        modules = []
        for module in self.py_modules:
            path = module.split('.')
            package = '.'.join(path[0:-1])
            module_base = path[-1]
            try:
                package_dir, checked = packages[package]
            except KeyError:
                package_dir = self.get_package_dir(package)
                checked = 0

            if not checked:
                init_py = self.check_package(package, package_dir)
                packages[package] = (package_dir, 1)
                if init_py:
                    modules.append((package, '__init__', init_py))
            module_file = os.path.join(package_dir, module_base + '.py')
            if not self.check_module(module, module_file):
                continue
            modules.append((package, module_base, module_file))

        return modules

    def find_all_modules(self):
        """Compute the list of all modules that will be built, whether
        they are specified one-module-at-a-time ('self.py_modules') or
        by whole packages ('self.packages').  Return a list of tuples
        (package, module, module_file), just like 'find_modules()' and
        'find_package_modules()' do."""
        modules = []
        if self.py_modules:
            modules.extend(self.find_modules())
        if self.packages:
            for package in self.packages:
                package_dir = self.get_package_dir(package)
                m = self.find_package_modules(package, package_dir)
                modules.extend(m)

        return modules

    def get_source_files(self):
        return [ module[-1] for module in self.find_all_modules() ]

    def get_module_outfile(self, build_dir, package, module):
        outfile_path = [
         build_dir] + list(package) + [module + '.py']
        return os.path.join(*outfile_path)

    def get_outputs(self, include_bytecode=1):
        modules = self.find_all_modules()
        outputs = []
        for package, module, module_file in modules:
            package = package.split('.')
            filename = self.get_module_outfile(self.build_lib, package, module)
            outputs.append(filename)
            if include_bytecode:
                if self.compile:
                    outputs.append(filename + 'c')
                if self.optimize > 0:
                    outputs.append(filename + 'o')

        outputs += [ os.path.join(build_dir, filename) for package, src_dir, build_dir, filenames in self.data_files for filename in filenames
                   ]
        return outputs

    def build_module(self, module, module_file, package):
        if isinstance(package, str):
            package = package.split('.')
        elif not isinstance(package, (list, tuple)):
            raise TypeError("'package' must be a string (dot-separated), list, or tuple")
        outfile = self.get_module_outfile(self.build_lib, package, module)
        dir = os.path.dirname(outfile)
        self.mkpath(dir)
        return self.copy_file(module_file, outfile, preserve_mode=0)

    def build_modules(self):
        modules = self.find_modules()
        for package, module, module_file in modules:
            self.build_module(module, module_file, package)

    def build_packages(self):
        for package in self.packages:
            package_dir = self.get_package_dir(package)
            modules = self.find_package_modules(package, package_dir)
            for package_, module, module_file in modules:
                self.build_module(module, module_file, package)

    def byte_compile(self, files):
        if sys.dont_write_bytecode:
            self.warn('byte-compiling is disabled, skipping.')
            return
        from distutils.util import byte_compile
        prefix = self.build_lib
        if prefix[-1] != os.sep:
            prefix = prefix + os.sep
        if self.compile:
            byte_compile(files, optimize=0, force=self.force, prefix=prefix, dry_run=self.dry_run)
        if self.optimize > 0:
            byte_compile(files, optimize=self.optimize, force=self.force, prefix=prefix, dry_run=self.dry_run)