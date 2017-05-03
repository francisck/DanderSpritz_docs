# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: util.py
"""distutils.util

Miscellaneous utility functions -- anything that doesn't fit into
one of the other *util.py modules.
"""
__revision__ = '$Id$'
import sys
import os
import string
import re
from distutils.errors import DistutilsPlatformError
from distutils.dep_util import newer
from distutils.spawn import spawn
from distutils import log
from distutils.errors import DistutilsByteCompileError

def get_platform():
    """Return a string that identifies the current platform.  This is used
    mainly to distinguish platform-specific build directories and
    platform-specific built distributions.  Typically includes the OS name
    and version and the architecture (as supplied by 'os.uname()'),
    although the exact information included depends on the OS; eg. for IRIX
    the architecture isn't particularly important (IRIX only runs on SGI
    hardware), but for Linux the kernel version isn't particularly
    important.
    
    Examples of returned values:
       linux-i586
       linux-alpha (?)
       solaris-2.6-sun4u
       irix-5.3
       irix64-6.2
    
    Windows will return one of:
       win-amd64 (64bit Windows on AMD64 (aka x86_64, Intel64, EM64T, etc)
       win-ia64 (64bit Windows on Itanium)
       win32 (all others - specifically, sys.platform is returned)
    
    For other non-POSIX platforms, currently just returns 'sys.platform'.
    """
    if os.name == 'nt':
        prefix = ' bit ('
        i = string.find(sys.version, prefix)
        if i == -1:
            return sys.platform
        j = string.find(sys.version, ')', i)
        look = sys.version[i + len(prefix):j].lower()
        if look == 'amd64':
            return 'win-amd64'
        if look == 'itanium':
            return 'win-ia64'
        return sys.platform
    else:
        if os.name != 'posix' or not hasattr(os, 'uname'):
            return sys.platform
        osname, host, release, version, machine = os.uname()
        osname = string.lower(osname)
        osname = string.replace(osname, '/', '')
        machine = string.replace(machine, ' ', '_')
        machine = string.replace(machine, '/', '-')
        if osname[:5] == 'linux':
            return '%s-%s' % (osname, machine)
        if osname[:5] == 'sunos':
            if release[0] >= '5':
                osname = 'solaris'
                release = '%d.%s' % (int(release[0]) - 3, release[2:])
        else:
            if osname[:4] == 'irix':
                return '%s-%s' % (osname, release)
            if osname[:3] == 'aix':
                return '%s-%s.%s' % (osname, version, release)
        if osname[:6] == 'cygwin':
            osname = 'cygwin'
            rel_re = re.compile('[\\d.]+')
            m = rel_re.match(release)
            if m:
                release = m.group()
        elif osname[:6] == 'darwin':
            from distutils.sysconfig import get_config_vars
            cfgvars = get_config_vars()
            macver = cfgvars.get('MACOSX_DEPLOYMENT_TARGET')
            macrelease = macver
            try:
                f = open('/System/Library/CoreServices/SystemVersion.plist')
            except IOError:
                pass
            else:
                try:
                    m = re.search('<key>ProductUserVisibleVersion</key>\\s*' + '<string>(.*?)</string>', f.read())
                    if m is not None:
                        macrelease = '.'.join(m.group(1).split('.')[:2])
                finally:
                    f.close()

            if not macver:
                macver = macrelease
            if macver:
                from distutils.sysconfig import get_config_vars
                release = macver
                osname = 'macosx'
                if macrelease + '.' >= '10.4.' and '-arch' in get_config_vars().get('CFLAGS', '').strip():
                    machine = 'fat'
                    cflags = get_config_vars().get('CFLAGS')
                    archs = re.findall('-arch\\s+(\\S+)', cflags)
                    archs = tuple(sorted(set(archs)))
                    if len(archs) == 1:
                        machine = archs[0]
                    elif archs == ('i386', 'ppc'):
                        machine = 'fat'
                    elif archs == ('i386', 'x86_64'):
                        machine = 'intel'
                    elif archs == ('i386', 'ppc', 'x86_64'):
                        machine = 'fat3'
                    elif archs == ('ppc64', 'x86_64'):
                        machine = 'fat64'
                    elif archs == ('i386', 'ppc', 'ppc64', 'x86_64'):
                        machine = 'universal'
                    else:
                        raise ValueError("Don't know machine value for archs=%r" % (archs,))
                elif machine == 'i386':
                    if sys.maxint >= 4294967296L:
                        machine = 'x86_64'
                elif machine in ('PowerPC', 'Power_Macintosh'):
                    machine = 'ppc'
                    if sys.maxint >= 4294967296L:
                        machine = 'ppc64'
        return '%s-%s-%s' % (osname, release, machine)


def convert_path(pathname):
    """Return 'pathname' as a name that will work on the native filesystem,
    i.e. split it on '/' and put it back together again using the current
    directory separator.  Needed because filenames in the setup script are
    always supplied in Unix style, and have to be converted to the local
    convention before we can actually use them in the filesystem.  Raises
    ValueError on non-Unix-ish systems if 'pathname' either starts or
    ends with a slash.
    """
    if os.sep == '/':
        return pathname
    if not pathname:
        return pathname
    if pathname[0] == '/':
        raise ValueError, "path '%s' cannot be absolute" % pathname
    if pathname[-1] == '/':
        raise ValueError, "path '%s' cannot end with '/'" % pathname
    paths = string.split(pathname, '/')
    while '.' in paths:
        paths.remove('.')

    if not paths:
        return os.curdir
    return os.path.join(*paths)


def change_root(new_root, pathname):
    """Return 'pathname' with 'new_root' prepended.  If 'pathname' is
    relative, this is equivalent to "os.path.join(new_root,pathname)".
    Otherwise, it requires making 'pathname' relative and then joining the
    two, which is tricky on DOS/Windows and Mac OS.
    """
    if os.name == 'posix':
        if not os.path.isabs(pathname):
            return os.path.join(new_root, pathname)
        else:
            return os.path.join(new_root, pathname[1:])

    else:
        if os.name == 'nt':
            drive, path = os.path.splitdrive(pathname)
            if path[0] == '\\':
                path = path[1:]
            return os.path.join(new_root, path)
        if os.name == 'os2':
            drive, path = os.path.splitdrive(pathname)
            if path[0] == os.sep:
                path = path[1:]
            return os.path.join(new_root, path)
        raise DistutilsPlatformError, "nothing known about platform '%s'" % os.name


_environ_checked = 0

def check_environ():
    """Ensure that 'os.environ' has all the environment variables we
    guarantee that users can use in config files, command-line options,
    etc.  Currently this includes:
      HOME - user's home directory (Unix only)
      PLAT - description of the current platform, including hardware
             and OS (see 'get_platform()')
    """
    global _environ_checked
    if _environ_checked:
        return
    if os.name == 'posix' and 'HOME' not in os.environ:
        import pwd
        os.environ['HOME'] = pwd.getpwuid(os.getuid())[5]
    if 'PLAT' not in os.environ:
        os.environ['PLAT'] = get_platform()
    _environ_checked = 1


def subst_vars(s, local_vars):
    """Perform shell/Perl-style variable substitution on 'string'.  Every
    occurrence of '$' followed by a name is considered a variable, and
    variable is substituted by the value found in the 'local_vars'
    dictionary, or in 'os.environ' if it's not in 'local_vars'.
    'os.environ' is first checked/augmented to guarantee that it contains
    certain values: see 'check_environ()'.  Raise ValueError for any
    variables not found in either 'local_vars' or 'os.environ'.
    """
    check_environ()

    def _subst(match, local_vars=local_vars):
        var_name = match.group(1)
        if var_name in local_vars:
            return str(local_vars[var_name])
        else:
            return os.environ[var_name]

    try:
        return re.sub('\\$([a-zA-Z_][a-zA-Z_0-9]*)', _subst, s)
    except KeyError as var:
        raise ValueError, "invalid variable '$%s'" % var


def grok_environment_error(exc, prefix='error: '):
    """Generate a useful error message from an EnvironmentError (IOError or
    OSError) exception object.  Handles Python 1.5.1 and 1.5.2 styles, and
    does what it can to deal with exception objects that don't have a
    filename (which happens when the error is due to a two-file operation,
    such as 'rename()' or 'link()'.  Returns the error message as a string
    prefixed with 'prefix'.
    """
    if hasattr(exc, 'filename') and hasattr(exc, 'strerror'):
        if exc.filename:
            error = prefix + '%s: %s' % (exc.filename, exc.strerror)
        else:
            error = prefix + '%s' % exc.strerror
    else:
        error = prefix + str(exc[-1])
    return error


_wordchars_re = _squote_re = _dquote_re = None

def _init_regex():
    global _dquote_re
    global _squote_re
    global _wordchars_re
    _wordchars_re = re.compile('[^\\\\\\\'\\"%s ]*' % string.whitespace)
    _squote_re = re.compile("'(?:[^'\\\\]|\\\\.)*'")
    _dquote_re = re.compile('"(?:[^"\\\\]|\\\\.)*"')


def split_quoted(s):
    """Split a string up according to Unix shell-like rules for quotes and
    backslashes.  In short: words are delimited by spaces, as long as those
    spaces are not escaped by a backslash, or inside a quoted string.
    Single and double quotes are equivalent, and the quote characters can
    be backslash-escaped.  The backslash is stripped from any two-character
    escape sequence, leaving only the escaped character.  The quote
    characters are stripped from any quoted string.  Returns a list of
    words.
    """
    if _wordchars_re is None:
        _init_regex()
    s = string.strip(s)
    words = []
    pos = 0
    while s:
        m = _wordchars_re.match(s, pos)
        end = m.end()
        if end == len(s):
            words.append(s[:end])
            break
        if s[end] in string.whitespace:
            words.append(s[:end])
            s = string.lstrip(s[end:])
            pos = 0
        elif s[end] == '\\':
            s = s[:end] + s[end + 1:]
            pos = end + 1
        else:
            if s[end] == "'":
                m = _squote_re.match(s, end)
            elif s[end] == '"':
                m = _dquote_re.match(s, end)
            else:
                raise RuntimeError, "this can't happen (bad char '%c')" % s[end]
            if m is None:
                raise ValueError, 'bad string (mismatched %s quotes?)' % s[end]
            beg, end = m.span()
            s = s[:beg] + s[beg + 1:end - 1] + s[end:]
            pos = m.end() - 2
        if pos >= len(s):
            words.append(s)
            break

    return words


def execute(func, args, msg=None, verbose=0, dry_run=0):
    """Perform some action that affects the outside world (eg.  by
    writing to the filesystem).  Such actions are special because they
    are disabled by the 'dry_run' flag.  This method takes care of all
    that bureaucracy for you; all you have to do is supply the
    function to call and an argument tuple for it (to embody the
    "external action" being performed), and an optional message to
    print.
    """
    if msg is None:
        msg = '%s%r' % (func.__name__, args)
        if msg[-2:] == ',)':
            msg = msg[0:-2] + ')'
    log.info(msg)
    if not dry_run:
        func(*args)
    return


def strtobool(val):
    """Convert a string representation of truth to true (1) or false (0).
    
    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    'val' is anything else.
    """
    val = string.lower(val)
    if val in ('y', 'yes', 't', 'true', 'on', '1'):
        return 1
    if val in ('n', 'no', 'f', 'false', 'off', '0'):
        return 0
    raise ValueError, 'invalid truth value %r' % (val,)


def byte_compile(py_files, optimize=0, force=0, prefix=None, base_dir=None, verbose=1, dry_run=0, direct=None):
    """Byte-compile a collection of Python source files to either .pyc
    or .pyo files in the same directory.  'py_files' is a list of files
    to compile; any files that don't end in ".py" are silently skipped.
    'optimize' must be one of the following:
      0 - don't optimize (generate .pyc)
      1 - normal optimization (like "python -O")
      2 - extra optimization (like "python -OO")
    If 'force' is true, all files are recompiled regardless of
    timestamps.
    
    The source filename encoded in each bytecode file defaults to the
    filenames listed in 'py_files'; you can modify these with 'prefix' and
    'basedir'.  'prefix' is a string that will be stripped off of each
    source filename, and 'base_dir' is a directory name that will be
    prepended (after 'prefix' is stripped).  You can supply either or both
    (or neither) of 'prefix' and 'base_dir', as you wish.
    
    If 'dry_run' is true, doesn't actually do anything that would
    affect the filesystem.
    
    Byte-compilation is either done directly in this interpreter process
    with the standard py_compile module, or indirectly by writing a
    temporary script and executing it.  Normally, you should let
    'byte_compile()' figure out to use direct compilation or not (see
    the source for details).  The 'direct' flag is used by the script
    generated in indirect mode; unless you know what you're doing, leave
    it set to None.
    """
    if sys.dont_write_bytecode:
        raise DistutilsByteCompileError('byte-compiling is disabled.')
    if direct is None:
        direct = __debug__ and optimize == 0
    if not direct:
        try:
            from tempfile import mkstemp
            script_fd, script_name = mkstemp('.py')
        except ImportError:
            from tempfile import mktemp
            script_fd, script_name = None, mktemp('.py')

        log.info("writing byte-compilation script '%s'", script_name)
        if not dry_run:
            if script_fd is not None:
                script = os.fdopen(script_fd, 'w')
            else:
                script = open(script_name, 'w')
            script.write('from distutils.util import byte_compile\nfiles = [\n')
            script.write(string.join(map(repr, py_files), ',\n') + ']\n')
            script.write('\nbyte_compile(files, optimize=%r, force=%r,\n             prefix=%r, base_dir=%r,\n             verbose=%r, dry_run=0,\n             direct=1)\n' % (optimize, force, prefix, base_dir, verbose))
            script.close()
        cmd = [sys.executable, script_name]
        if optimize == 1:
            cmd.insert(1, '-O')
        elif optimize == 2:
            cmd.insert(1, '-OO')
        spawn(cmd, dry_run=dry_run)
        execute(os.remove, (script_name,), 'removing %s' % script_name, dry_run=dry_run)
    else:
        from py_compile import compile
        for file in py_files:
            if file[-3:] != '.py':
                continue
            cfile = file + (__debug__ and 'c' or 'o')
            dfile = file
            if prefix:
                if file[:len(prefix)] != prefix:
                    raise ValueError, "invalid prefix: filename %r doesn't start with %r" % (
                     file, prefix)
                dfile = dfile[len(prefix):]
            if base_dir:
                dfile = os.path.join(base_dir, dfile)
            cfile_base = os.path.basename(cfile)
            if direct:
                if force or newer(file, cfile):
                    log.info('byte-compiling %s to %s', file, cfile_base)
                    if not dry_run:
                        compile(file, cfile, dfile)
                else:
                    log.debug('skipping byte-compilation of %s to %s', file, cfile_base)

    return


def rfc822_escape(header):
    """Return a version of the string escaped for inclusion in an
    RFC-822 header, by ensuring there are 8 spaces space after each newline.
    """
    lines = string.split(header, '\n')
    header = string.join(lines, '\n' + '        ')
    return header