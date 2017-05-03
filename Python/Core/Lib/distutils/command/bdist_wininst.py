# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: bdist_wininst.py
"""distutils.command.bdist_wininst

Implements the Distutils 'bdist_wininst' command: create a windows installer
exe-program."""
__revision__ = '$Id$'
import sys
import os
import string
from sysconfig import get_python_version
from distutils.core import Command
from distutils.dir_util import remove_tree
from distutils.errors import DistutilsOptionError, DistutilsPlatformError
from distutils import log
from distutils.util import get_platform

class bdist_wininst(Command):
    description = 'create an executable installer for MS Windows'
    user_options = [
     ('bdist-dir=', None, 'temporary directory for creating the distribution'),
     (
      'plat-name=', 'p',
      'platform name to embed in generated filenames (default: %s)' % get_platform()),
     (
      'keep-temp', 'k',
      'keep the pseudo-installation tree around after ' + 'creating the distribution archive'),
     (
      'target-version=', None,
      'require a specific python version' + ' on the target system'),
     ('no-target-compile', 'c', 'do not compile .py to .pyc on the target system'),
     ('no-target-optimize', 'o', 'do not compile .py to .pyo (optimized)on the target system'),
     ('dist-dir=', 'd', 'directory to put final built distributions in'),
     ('bitmap=', 'b', 'bitmap to use for the installer instead of python-powered logo'),
     ('title=', 't', 'title to display on the installer background instead of default'),
     ('skip-build', None, 'skip rebuilding everything (for testing/debugging)'),
     ('install-script=', None, 'basename of installation script to be run afterinstallation or before deinstallation'),
     ('pre-install-script=', None, 'Fully qualified filename of a script to be run before any files are installed.  This script need not be in the distribution'),
     ('user-access-control=', None, "specify Vista's UAC handling - 'none'/default=no handling, 'auto'=use UAC if target Python installed for all users, 'force'=always use UAC")]
    boolean_options = [
     'keep-temp', 'no-target-compile', 'no-target-optimize',
     'skip-build']

    def initialize_options(self):
        self.bdist_dir = None
        self.plat_name = None
        self.keep_temp = 0
        self.no_target_compile = 0
        self.no_target_optimize = 0
        self.target_version = None
        self.dist_dir = None
        self.bitmap = None
        self.title = None
        self.skip_build = 0
        self.install_script = None
        self.pre_install_script = None
        self.user_access_control = None
        return

    def finalize_options(self):
        if self.bdist_dir is None:
            if self.skip_build and self.plat_name:
                bdist = self.distribution.get_command_obj('bdist')
                bdist.plat_name = self.plat_name
            bdist_base = self.get_finalized_command('bdist').bdist_base
            self.bdist_dir = os.path.join(bdist_base, 'wininst')
        if not self.target_version:
            self.target_version = ''
        if not self.skip_build and self.distribution.has_ext_modules():
            short_version = get_python_version()
            if self.target_version and self.target_version != short_version:
                raise DistutilsOptionError, "target version can only be %s, or the '--skip-build' option must be specified" % (
                 short_version,)
            self.target_version = short_version
        self.set_undefined_options('bdist', ('dist_dir', 'dist_dir'), ('plat_name',
                                                                       'plat_name'))
        if self.install_script:
            for script in self.distribution.scripts:
                if self.install_script == os.path.basename(script):
                    break
            else:
                raise DistutilsOptionError, "install_script '%s' not found in scripts" % self.install_script

        return

    def run(self):
        if sys.platform != 'win32' and (self.distribution.has_ext_modules() or self.distribution.has_c_libraries()):
            raise DistutilsPlatformError('distribution contains extensions and/or C libraries; must be compiled on a Windows 32 platform')
        if not self.skip_build:
            self.run_command('build')
        install = self.reinitialize_command('install', reinit_subcommands=1)
        install.root = self.bdist_dir
        install.skip_build = self.skip_build
        install.warn_dir = 0
        install.plat_name = self.plat_name
        install_lib = self.reinitialize_command('install_lib')
        install_lib.compile = 0
        install_lib.optimize = 0
        if self.distribution.has_ext_modules():
            target_version = self.target_version
            if not target_version:
                target_version = sys.version[0:3]
            plat_specifier = '.%s-%s' % (self.plat_name, target_version)
            build = self.get_finalized_command('build')
            build.build_lib = os.path.join(build.build_base, 'lib' + plat_specifier)
        for key in ('purelib', 'platlib', 'headers', 'scripts', 'data'):
            value = string.upper(key)
            if key == 'headers':
                value = value + '/Include/$dist_name'
            setattr(install, 'install_' + key, value)

        log.info('installing to %s', self.bdist_dir)
        install.ensure_finalized()
        sys.path.insert(0, os.path.join(self.bdist_dir, 'PURELIB'))
        install.run()
        del sys.path[0]
        from tempfile import mktemp
        archive_basename = mktemp()
        fullname = self.distribution.get_fullname()
        arcname = self.make_archive(archive_basename, 'zip', root_dir=self.bdist_dir)
        self.create_exe(arcname, fullname, self.bitmap)
        if self.distribution.has_ext_modules():
            pyversion = get_python_version()
        else:
            pyversion = 'any'
        self.distribution.dist_files.append(('bdist_wininst', pyversion,
         self.get_installer_filename(fullname)))
        log.debug("removing temporary file '%s'", arcname)
        os.remove(arcname)
        if not self.keep_temp:
            remove_tree(self.bdist_dir, dry_run=self.dry_run)

    def get_inidata(self):
        lines = []
        metadata = self.distribution.metadata
        lines.append('[metadata]')
        info = (metadata.long_description or '') + '\n'

        def escape(s):
            return string.replace(s, '\n', '\\n')

        for name in ['author', 'author_email', 'description', 'maintainer',
         'maintainer_email', 'name', 'url', 'version']:
            data = getattr(metadata, name, '')
            if data:
                info = info + '\n    %s: %s' % (
                 string.capitalize(name), escape(data))
                lines.append('%s=%s' % (name, escape(data)))

        lines.append('\n[Setup]')
        if self.install_script:
            lines.append('install_script=%s' % self.install_script)
        lines.append('info=%s' % escape(info))
        lines.append('target_compile=%d' % (not self.no_target_compile))
        lines.append('target_optimize=%d' % (not self.no_target_optimize))
        if self.target_version:
            lines.append('target_version=%s' % self.target_version)
        if self.user_access_control:
            lines.append('user_access_control=%s' % self.user_access_control)
        title = self.title or self.distribution.get_fullname()
        lines.append('title=%s' % escape(title))
        import time
        import distutils
        build_info = 'Built %s with distutils-%s' % (
         time.ctime(time.time()), distutils.__version__)
        lines.append('build_info=%s' % build_info)
        return string.join(lines, '\n')

    def create_exe(self, arcname, fullname, bitmap=None):
        import struct
        self.mkpath(self.dist_dir)
        cfgdata = self.get_inidata()
        installer_name = self.get_installer_filename(fullname)
        self.announce('creating %s' % installer_name)
        if bitmap:
            bitmapdata = open(bitmap, 'rb').read()
            bitmaplen = len(bitmapdata)
        else:
            bitmaplen = 0
        file = open(installer_name, 'wb')
        file.write(self.get_exe_bytes())
        if bitmap:
            file.write(bitmapdata)
        try:
            unicode
        except NameError:
            pass
        else:
            if isinstance(cfgdata, unicode):
                cfgdata = cfgdata.encode('mbcs')

        cfgdata = cfgdata + '\x00'
        if self.pre_install_script:
            script_data = open(self.pre_install_script, 'r').read()
            cfgdata = cfgdata + script_data + '\n\x00'
        else:
            cfgdata = cfgdata + '\x00'
        file.write(cfgdata)
        header = struct.pack('<iii', 305419899, len(cfgdata), bitmaplen)
        file.write(header)
        file.write(open(arcname, 'rb').read())

    def get_installer_filename(self, fullname):
        if self.target_version:
            installer_name = os.path.join(self.dist_dir, '%s.%s-py%s.exe' % (
             fullname, self.plat_name, self.target_version))
        else:
            installer_name = os.path.join(self.dist_dir, '%s.%s.exe' % (fullname, self.plat_name))
        return installer_name

    def get_exe_bytes(self):
        from distutils.msvccompiler import get_build_version
        cur_version = get_python_version()
        if self.target_version and self.target_version != cur_version:
            if self.target_version > cur_version:
                bv = get_build_version()
            elif self.target_version < '2.4':
                bv = 6.0
            else:
                bv = 7.1
        else:
            bv = get_build_version()
        directory = os.path.dirname(__file__)
        if self.plat_name != 'win32' and self.plat_name[:3] == 'win':
            sfix = self.plat_name[3:]
        else:
            sfix = ''
        filename = os.path.join(directory, 'wininst-%.1f%s.exe' % (bv, sfix))
        f = open(filename, 'rb')
        try:
            return f.read()
        finally:
            f.close()