# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: doctest.py
"""Module doctest -- a framework for running examples in docstrings.

In simplest use, end each module M to be tested with:

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()

Then running the module as a script will cause the examples in the
docstrings to get executed and verified:

python M.py

This won't display anything unless an example fails, in which case the
failing example(s) and the cause(s) of the failure(s) are printed to stdout
(why not stderr? because stderr is a lame hack <0.2 wink>), and the final
line of output is "Test failed.".

Run it with the -v switch instead:

python M.py -v

and a detailed report of all examples tried is printed to stdout, along
with assorted summaries at the end.

You can force verbose mode by passing "verbose=True" to testmod, or prohibit
it by passing "verbose=False".  In either of those cases, sys.argv is not
examined by testmod.

There are a variety of other ways to run doctests, including integration
with the unittest framework, and support for running non-Python text
files containing doctests.  There are also many ways to override parts
of doctest's default behaviors.  See the Library Reference Manual for
details.
"""
__docformat__ = 'reStructuredText en'
__all__ = [
 'register_optionflag',
 'DONT_ACCEPT_TRUE_FOR_1',
 'DONT_ACCEPT_BLANKLINE',
 'NORMALIZE_WHITESPACE',
 'ELLIPSIS',
 'SKIP',
 'IGNORE_EXCEPTION_DETAIL',
 'COMPARISON_FLAGS',
 'REPORT_UDIFF',
 'REPORT_CDIFF',
 'REPORT_NDIFF',
 'REPORT_ONLY_FIRST_FAILURE',
 'REPORTING_FLAGS',
 'Example',
 'DocTest',
 'DocTestParser',
 'DocTestFinder',
 'DocTestRunner',
 'OutputChecker',
 'DocTestFailure',
 'UnexpectedException',
 'DebugRunner',
 'testmod',
 'testfile',
 'run_docstring_examples',
 'Tester',
 'DocTestSuite',
 'DocFileSuite',
 'set_unittest_reportflags',
 'script_from_examples',
 'testsource',
 'debug_src',
 'debug']
import __future__
import sys
import traceback
import inspect
import linecache
import os
import re
import unittest
import difflib
import pdb
import tempfile
import warnings
from StringIO import StringIO
from collections import namedtuple
TestResults = namedtuple('TestResults', 'failed attempted')
OPTIONFLAGS_BY_NAME = {}

def register_optionflag(name):
    return OPTIONFLAGS_BY_NAME.setdefault(name, 1 << len(OPTIONFLAGS_BY_NAME))


DONT_ACCEPT_TRUE_FOR_1 = register_optionflag('DONT_ACCEPT_TRUE_FOR_1')
DONT_ACCEPT_BLANKLINE = register_optionflag('DONT_ACCEPT_BLANKLINE')
NORMALIZE_WHITESPACE = register_optionflag('NORMALIZE_WHITESPACE')
ELLIPSIS = register_optionflag('ELLIPSIS')
SKIP = register_optionflag('SKIP')
IGNORE_EXCEPTION_DETAIL = register_optionflag('IGNORE_EXCEPTION_DETAIL')
COMPARISON_FLAGS = DONT_ACCEPT_TRUE_FOR_1 | DONT_ACCEPT_BLANKLINE | NORMALIZE_WHITESPACE | ELLIPSIS | SKIP | IGNORE_EXCEPTION_DETAIL
REPORT_UDIFF = register_optionflag('REPORT_UDIFF')
REPORT_CDIFF = register_optionflag('REPORT_CDIFF')
REPORT_NDIFF = register_optionflag('REPORT_NDIFF')
REPORT_ONLY_FIRST_FAILURE = register_optionflag('REPORT_ONLY_FIRST_FAILURE')
REPORTING_FLAGS = REPORT_UDIFF | REPORT_CDIFF | REPORT_NDIFF | REPORT_ONLY_FIRST_FAILURE
BLANKLINE_MARKER = '<BLANKLINE>'
ELLIPSIS_MARKER = '...'

def _extract_future_flags(globs):
    """
    Return the compiler-flags associated with the future features that
    have been imported into the given namespace (globs).
    """
    flags = 0
    for fname in __future__.all_feature_names:
        feature = globs.get(fname, None)
        if feature is getattr(__future__, fname):
            flags |= feature.compiler_flag

    return flags


def _normalize_module(module, depth=2):
    """
    Return the module specified by `module`.  In particular:
      - If `module` is a module, then return module.
      - If `module` is a string, then import and return the
        module with that name.
      - If `module` is None, then return the calling module.
        The calling module is assumed to be the module of
        the stack frame at the given depth in the call stack.
    """
    if inspect.ismodule(module):
        return module
    else:
        if isinstance(module, (str, unicode)):
            return __import__(module, globals(), locals(), ['*'])
        if module is None:
            return sys.modules[sys._getframe(depth).f_globals['__name__']]
        raise TypeError('Expected a module, string, or None')
        return


def _load_testfile(filename, package, module_relative):
    if module_relative:
        package = _normalize_module(package, 3)
        filename = _module_relative_path(package, filename)
        if hasattr(package, '__loader__'):
            if hasattr(package.__loader__, 'get_data'):
                file_contents = package.__loader__.get_data(filename)
                return (
                 file_contents.replace(os.linesep, '\n'), filename)
    with open(filename) as f:
        return (f.read(), filename)


_encoding = getattr(sys.__stdout__, 'encoding', None) or 'utf-8'

def _indent(s, indent=4):
    """
    Add the given number of space characters to the beginning of
    every non-blank line in `s`, and return the result.
    If the string `s` is Unicode, it is encoded using the stdout
    encoding and the `backslashreplace` error handler.
    """
    if isinstance(s, unicode):
        s = s.encode(_encoding, 'backslashreplace')
    return re.sub('(?m)^(?!$)', indent * ' ', s)


def _exception_traceback(exc_info):
    """
    Return a string containing a traceback message for the given
    exc_info tuple (as returned by sys.exc_info()).
    """
    excout = StringIO()
    exc_type, exc_val, exc_tb = exc_info
    traceback.print_exception(exc_type, exc_val, exc_tb, file=excout)
    return excout.getvalue()


class _SpoofOut(StringIO):

    def getvalue(self):
        result = StringIO.getvalue(self)
        if result and not result.endswith('\n'):
            result += '\n'
        if hasattr(self, 'softspace'):
            del self.softspace
        return result

    def truncate(self, size=None):
        StringIO.truncate(self, size)
        if hasattr(self, 'softspace'):
            del self.softspace
        if not self.buf:
            self.buf = ''


def _ellipsis_match(want, got):
    """
    Essentially the only subtle case:
    >>> _ellipsis_match('aa...aa', 'aaa')
    False
    """
    if ELLIPSIS_MARKER not in want:
        return want == got
    ws = want.split(ELLIPSIS_MARKER)
    startpos, endpos = 0, len(got)
    w = ws[0]
    if w:
        if got.startswith(w):
            startpos = len(w)
            del ws[0]
        else:
            return False
    w = ws[-1]
    if w:
        if got.endswith(w):
            endpos -= len(w)
            del ws[-1]
        else:
            return False
    if startpos > endpos:
        return False
    for w in ws:
        startpos = got.find(w, startpos, endpos)
        if startpos < 0:
            return False
        startpos += len(w)

    return True


def _comment_line(line):
    """Return a commented form of the given line"""
    line = line.rstrip()
    if line:
        return '# ' + line
    else:
        return '#'


class _OutputRedirectingPdb(pdb.Pdb):
    """
    A specialized version of the python debugger that redirects stdout
    to a given stream when interacting with the user.  Stdout is *not*
    redirected when traced code is executed.
    """

    def __init__(self, out):
        self.__out = out
        self.__debugger_used = False
        pdb.Pdb.__init__(self, stdout=out)
        self.use_rawinput = 1

    def set_trace(self, frame=None):
        self.__debugger_used = True
        if frame is None:
            frame = sys._getframe().f_back
        pdb.Pdb.set_trace(self, frame)
        return

    def set_continue(self):
        if self.__debugger_used:
            pdb.Pdb.set_continue(self)

    def trace_dispatch(self, *args):
        save_stdout = sys.stdout
        sys.stdout = self.__out
        try:
            return pdb.Pdb.trace_dispatch(self, *args)
        finally:
            sys.stdout = save_stdout


def _module_relative_path(module, path):
    if not inspect.ismodule(module):
        raise TypeError, 'Expected a module: %r' % module
    if path.startswith('/'):
        raise ValueError, 'Module-relative files may not have absolute paths'
    if hasattr(module, '__file__'):
        basedir = os.path.split(module.__file__)[0]
    elif module.__name__ == '__main__':
        if len(sys.argv) > 0 and sys.argv[0] != '':
            basedir = os.path.split(sys.argv[0])[0]
        else:
            basedir = os.curdir
    else:
        raise ValueError("Can't resolve paths relative to the module " + module + ' (it has no __file__)')
    return os.path.join(basedir, *path.split('/'))


class Example():
    """
    A single doctest example, consisting of source code and expected
    output.  `Example` defines the following attributes:
    
      - source: A single Python statement, always ending with a newline.
        The constructor adds a newline if needed.
    
      - want: The expected output from running the source code (either
        from stdout, or a traceback in case of exception).  `want` ends
        with a newline unless it's empty, in which case it's an empty
        string.  The constructor adds a newline if needed.
    
      - exc_msg: The exception message generated by the example, if
        the example is expected to generate an exception; or `None` if
        it is not expected to generate an exception.  This exception
        message is compared against the return value of
        `traceback.format_exception_only()`.  `exc_msg` ends with a
        newline unless it's `None`.  The constructor adds a newline
        if needed.
    
      - lineno: The line number within the DocTest string containing
        this Example where the Example begins.  This line number is
        zero-based, with respect to the beginning of the DocTest.
    
      - indent: The example's indentation in the DocTest string.
        I.e., the number of space characters that preceed the
        example's first prompt.
    
      - options: A dictionary mapping from option flags to True or
        False, which is used to override default options for this
        example.  Any option flags not contained in this dictionary
        are left at their default value (as specified by the
        DocTestRunner's optionflags).  By default, no options are set.
    """

    def __init__(self, source, want, exc_msg=None, lineno=0, indent=0, options=None):
        if not source.endswith('\n'):
            source += '\n'
        if want and not want.endswith('\n'):
            want += '\n'
        if exc_msg is not None and not exc_msg.endswith('\n'):
            exc_msg += '\n'
        self.source = source
        self.want = want
        self.lineno = lineno
        self.indent = indent
        if options is None:
            options = {}
        self.options = options
        self.exc_msg = exc_msg
        return


class DocTest():
    """
    A collection of doctest examples that should be run in a single
    namespace.  Each `DocTest` defines the following attributes:
    
      - examples: the list of examples.
    
      - globs: The namespace (aka globals) that the examples should
        be run in.
    
      - name: A name identifying the DocTest (typically, the name of
        the object whose docstring this DocTest was extracted from).
    
      - filename: The name of the file that this DocTest was extracted
        from, or `None` if the filename is unknown.
    
      - lineno: The line number within filename where this DocTest
        begins, or `None` if the line number is unavailable.  This
        line number is zero-based, with respect to the beginning of
        the file.
    
      - docstring: The string that the examples were extracted from,
        or `None` if the string is unavailable.
    """

    def __init__(self, examples, globs, name, filename, lineno, docstring):
        """
        Create a new DocTest containing the given examples.  The
        DocTest's globals are initialized with a copy of `globs`.
        """
        self.examples = examples
        self.docstring = docstring
        self.globs = globs.copy()
        self.name = name
        self.filename = filename
        self.lineno = lineno

    def __repr__(self):
        if len(self.examples) == 0:
            examples = 'no examples'
        elif len(self.examples) == 1:
            examples = '1 example'
        else:
            examples = '%d examples' % len(self.examples)
        return '<DocTest %s from %s:%s (%s)>' % (
         self.name, self.filename, self.lineno, examples)

    def __cmp__(self, other):
        if not isinstance(other, DocTest):
            return -1
        return cmp((self.name, self.filename, self.lineno, id(self)), (
         other.name, other.filename, other.lineno, id(other)))


class DocTestParser():
    """
    A class used to parse strings containing doctest examples.
    """
    _EXAMPLE_RE = re.compile('\n        # Source consists of a PS1 line followed by zero or more PS2 lines.\n        (?P<source>\n            (?:^(?P<indent> [ ]*) >>>    .*)    # PS1 line\n            (?:\\n           [ ]*  \\.\\.\\. .*)*)  # PS2 lines\n        \\n?\n        # Want consists of any non-blank lines that do not start with PS1.\n        (?P<want> (?:(?![ ]*$)    # Not a blank line\n                     (?![ ]*>>>)  # Not a line starting with PS1\n                     .*$\\n?       # But any other line\n                  )*)\n        ', re.MULTILINE | re.VERBOSE)
    _EXCEPTION_RE = re.compile("\n        # Grab the traceback header.  Different versions of Python have\n        # said different things on the first traceback line.\n        ^(?P<hdr> Traceback\\ \\(\n            (?: most\\ recent\\ call\\ last\n            |   innermost\\ last\n            ) \\) :\n        )\n        \\s* $                # toss trailing whitespace on the header.\n        (?P<stack> .*?)      # don't blink: absorb stuff until...\n        ^ (?P<msg> \\w+ .*)   #     a line *starts* with alphanum.\n        ", re.VERBOSE | re.MULTILINE | re.DOTALL)
    _IS_BLANK_OR_COMMENT = re.compile('^[ ]*(#.*)?$').match

    def parse(self, string, name='<string>'):
        """
        Divide the given string into examples and intervening text,
        and return them as a list of alternating Examples and strings.
        Line numbers for the Examples are 0-based.  The optional
        argument `name` is a name identifying this string, and is only
        used for error messages.
        """
        string = string.expandtabs()
        min_indent = self._min_indent(string)
        if min_indent > 0:
            string = '\n'.join([ l[min_indent:] for l in string.split('\n') ])
        output = []
        charno, lineno = (0, 0)
        for m in self._EXAMPLE_RE.finditer(string):
            output.append(string[charno:m.start()])
            lineno += string.count('\n', charno, m.start())
            source, options, want, exc_msg = self._parse_example(m, name, lineno)
            if not self._IS_BLANK_OR_COMMENT(source):
                output.append(Example(source, want, exc_msg, lineno=lineno, indent=min_indent + len(m.group('indent')), options=options))
            lineno += string.count('\n', m.start(), m.end())
            charno = m.end()

        output.append(string[charno:])
        return output

    def get_doctest(self, string, globs, name, filename, lineno):
        """
        Extract all doctest examples from the given string, and
        collect them into a `DocTest` object.
        
        `globs`, `name`, `filename`, and `lineno` are attributes for
        the new `DocTest` object.  See the documentation for `DocTest`
        for more information.
        """
        return DocTest(self.get_examples(string, name), globs, name, filename, lineno, string)

    def get_examples(self, string, name='<string>'):
        """
        Extract all doctest examples from the given string, and return
        them as a list of `Example` objects.  Line numbers are
        0-based, because it's most common in doctests that nothing
        interesting appears on the same line as opening triple-quote,
        and so the first interesting line is called "line 1" then.
        
        The optional argument `name` is a name identifying this
        string, and is only used for error messages.
        """
        return [ x for x in self.parse(string, name) if isinstance(x, Example)
               ]

    def _parse_example(self, m, name, lineno):
        """
        Given a regular expression match from `_EXAMPLE_RE` (`m`),
        return a pair `(source, want)`, where `source` is the matched
        example's source code (with prompts and indentation stripped);
        and `want` is the example's expected output (with indentation
        stripped).
        
        `name` is the string's name, and `lineno` is the line number
        where the example starts; both are used for error messages.
        """
        indent = len(m.group('indent'))
        source_lines = m.group('source').split('\n')
        self._check_prompt_blank(source_lines, indent, name, lineno)
        self._check_prefix(source_lines[1:], ' ' * indent + '.', name, lineno)
        source = '\n'.join([ sl[indent + 4:] for sl in source_lines ])
        want = m.group('want')
        want_lines = want.split('\n')
        if len(want_lines) > 1 and re.match(' *$', want_lines[-1]):
            del want_lines[-1]
        self._check_prefix(want_lines, ' ' * indent, name, lineno + len(source_lines))
        want = '\n'.join([ wl[indent:] for wl in want_lines ])
        m = self._EXCEPTION_RE.match(want)
        if m:
            exc_msg = m.group('msg')
        else:
            exc_msg = None
        options = self._find_options(source, name, lineno)
        return (
         source, options, want, exc_msg)

    _OPTION_DIRECTIVE_RE = re.compile('#\\s*doctest:\\s*([^\\n\\\'"]*)$', re.MULTILINE)

    def _find_options(self, source, name, lineno):
        """
        Return a dictionary containing option overrides extracted from
        option directives in the given source string.
        
        `name` is the string's name, and `lineno` is the line number
        where the example starts; both are used for error messages.
        """
        options = {}
        for m in self._OPTION_DIRECTIVE_RE.finditer(source):
            option_strings = m.group(1).replace(',', ' ').split()
            for option in option_strings:
                if option[0] not in '+-' or option[1:] not in OPTIONFLAGS_BY_NAME:
                    raise ValueError('line %r of the doctest for %s has an invalid option: %r' % (
                     lineno + 1, name, option))
                flag = OPTIONFLAGS_BY_NAME[option[1:]]
                options[flag] = option[0] == '+'

        if options and self._IS_BLANK_OR_COMMENT(source):
            raise ValueError('line %r of the doctest for %s has an option directive on a line with no example: %r' % (
             lineno, name, source))
        return options

    _INDENT_RE = re.compile('^([ ]*)(?=\\S)', re.MULTILINE)

    def _min_indent(self, s):
        """Return the minimum indentation of any non-blank line in `s`"""
        indents = [ len(indent) for indent in self._INDENT_RE.findall(s) ]
        if len(indents) > 0:
            return min(indents)
        else:
            return 0

    def _check_prompt_blank(self, lines, indent, name, lineno):
        """
        Given the lines of a source string (including prompts and
        leading indentation), check to make sure that every prompt is
        followed by a space character.  If any line is not followed by
        a space character, then raise ValueError.
        """
        for i, line in enumerate(lines):
            if len(line) >= indent + 4 and line[indent + 3] != ' ':
                raise ValueError('line %r of the docstring for %s lacks blank after %s: %r' % (
                 lineno + i + 1, name,
                 line[indent:indent + 3], line))

    def _check_prefix(self, lines, prefix, name, lineno):
        """
        Check that every line in the given list starts with the given
        prefix; if any line does not, then raise a ValueError.
        """
        for i, line in enumerate(lines):
            if line and not line.startswith(prefix):
                raise ValueError('line %r of the docstring for %s has inconsistent leading whitespace: %r' % (
                 lineno + i + 1, name, line))


class DocTestFinder():
    """
    A class used to extract the DocTests that are relevant to a given
    object, from its docstring and the docstrings of its contained
    objects.  Doctests can currently be extracted from the following
    object types: modules, functions, classes, methods, staticmethods,
    classmethods, and properties.
    """

    def __init__(self, verbose=False, parser=DocTestParser(), recurse=True, exclude_empty=True):
        """
        Create a new doctest finder.
        
        The optional argument `parser` specifies a class or
        function that should be used to create new DocTest objects (or
        objects that implement the same interface as DocTest).  The
        signature for this factory function should match the signature
        of the DocTest constructor.
        
        If the optional argument `recurse` is false, then `find` will
        only examine the given object, and not any contained objects.
        
        If the optional argument `exclude_empty` is false, then `find`
        will include tests for objects with empty docstrings.
        """
        self._parser = parser
        self._verbose = verbose
        self._recurse = recurse
        self._exclude_empty = exclude_empty

    def find(self, obj, name=None, module=None, globs=None, extraglobs=None):
        """
        Return a list of the DocTests that are defined by the given
        object's docstring, or by any of its contained objects'
        docstrings.
        
        The optional parameter `module` is the module that contains
        the given object.  If the module is not specified or is None, then
        the test finder will attempt to automatically determine the
        correct module.  The object's module is used:
        
            - As a default namespace, if `globs` is not specified.
            - To prevent the DocTestFinder from extracting DocTests
              from objects that are imported from other modules.
            - To find the name of the file containing the object.
            - To help find the line number of the object within its
              file.
        
        Contained objects whose module does not match `module` are ignored.
        
        If `module` is False, no attempt to find the module will be made.
        This is obscure, of use mostly in tests:  if `module` is False, or
        is None but cannot be found automatically, then all objects are
        considered to belong to the (non-existent) module, so all contained
        objects will (recursively) be searched for doctests.
        
        The globals for each DocTest is formed by combining `globs`
        and `extraglobs` (bindings in `extraglobs` override bindings
        in `globs`).  A new copy of the globals dictionary is created
        for each DocTest.  If `globs` is not specified, then it
        defaults to the module's `__dict__`, if specified, or {}
        otherwise.  If `extraglobs` is not specified, then it defaults
        to {}.
        
        """
        if name is None:
            name = getattr(obj, '__name__', None)
            if name is None:
                raise ValueError("DocTestFinder.find: name must be given when obj.__name__ doesn't exist: %r" % (
                 type(obj),))
        if module is False:
            module = None
        elif module is None:
            module = inspect.getmodule(obj)
        try:
            file = inspect.getsourcefile(obj) or inspect.getfile(obj)
            if module is not None:
                source_lines = linecache.getlines(file, module.__dict__)
            else:
                source_lines = linecache.getlines(file)
            if not source_lines:
                source_lines = None
        except TypeError:
            source_lines = None

        if globs is None:
            if module is None:
                globs = {}
            else:
                globs = module.__dict__.copy()
        else:
            globs = globs.copy()
        if extraglobs is not None:
            globs.update(extraglobs)
        if '__name__' not in globs:
            globs['__name__'] = '__main__'
        tests = []
        self._find(tests, obj, name, module, source_lines, globs, {})
        tests.sort()
        return tests

    def _from_module(self, module, object):
        """
        Return true if the given object is defined in the given
        module.
        """
        if module is None:
            return True
        else:
            if inspect.getmodule(object) is not None:
                return module is inspect.getmodule(object)
            if inspect.isfunction(object):
                return module.__dict__ is object.func_globals
            if inspect.isclass(object):
                return module.__name__ == object.__module__
            if hasattr(object, '__module__'):
                return module.__name__ == object.__module__
            if isinstance(object, property):
                return True
            raise ValueError('object must be a class or function')
            return

    def _find(self, tests, obj, name, module, source_lines, globs, seen):
        """
        Find tests for the given object and any contained objects, and
        add them to `tests`.
        """
        if self._verbose:
            print 'Finding tests in %s' % name
        if id(obj) in seen:
            return
        else:
            seen[id(obj)] = 1
            test = self._get_test(obj, name, module, globs, source_lines)
            if test is not None:
                tests.append(test)
            if inspect.ismodule(obj) and self._recurse:
                for valname, val in obj.__dict__.items():
                    valname = '%s.%s' % (name, valname)
                    if (inspect.isfunction(val) or inspect.isclass(val)) and self._from_module(module, val):
                        self._find(tests, val, valname, module, source_lines, globs, seen)

            if inspect.ismodule(obj) and self._recurse:
                for valname, val in getattr(obj, '__test__', {}).items():
                    if not isinstance(valname, basestring):
                        raise ValueError('DocTestFinder.find: __test__ keys must be strings: %r' % (
                         type(valname),))
                    if not (inspect.isfunction(val) or inspect.isclass(val) or inspect.ismethod(val) or inspect.ismodule(val) or isinstance(val, basestring)):
                        raise ValueError('DocTestFinder.find: __test__ values must be strings, functions, methods, classes, or modules: %r' % (
                         type(val),))
                    valname = '%s.__test__.%s' % (name, valname)
                    self._find(tests, val, valname, module, source_lines, globs, seen)

            if inspect.isclass(obj) and self._recurse:
                for valname, val in obj.__dict__.items():
                    if isinstance(val, staticmethod):
                        val = getattr(obj, valname)
                    if isinstance(val, classmethod):
                        val = getattr(obj, valname).im_func
                    if (inspect.isfunction(val) or inspect.isclass(val) or isinstance(val, property)) and self._from_module(module, val):
                        valname = '%s.%s' % (name, valname)
                        self._find(tests, val, valname, module, source_lines, globs, seen)

            return

    def _get_test(self, obj, name, module, globs, source_lines):
        """
        Return a DocTest for the given object, if it defines a docstring;
        otherwise, return None.
        """
        if isinstance(obj, basestring):
            docstring = obj
        else:
            try:
                if obj.__doc__ is None:
                    docstring = ''
                else:
                    docstring = obj.__doc__
                    if not isinstance(docstring, basestring):
                        docstring = str(docstring)
            except (TypeError, AttributeError):
                docstring = ''

        lineno = self._find_lineno(obj, source_lines)
        if self._exclude_empty and not docstring:
            return
        else:
            if module is None:
                filename = None
            else:
                filename = getattr(module, '__file__', module.__name__)
                if filename[-4:] in ('.pyc', '.pyo'):
                    filename = filename[:-1]
            return self._parser.get_doctest(docstring, globs, name, filename, lineno)

    def _find_lineno(self, obj, source_lines):
        """
        Return a line number of the given object's docstring.  Note:
        this method assumes that the object has a docstring.
        """
        lineno = None
        if inspect.ismodule(obj):
            lineno = 0
        if inspect.isclass(obj):
            if source_lines is None:
                return
            pat = re.compile('^\\s*class\\s*%s\\b' % getattr(obj, '__name__', '-'))
            for i, line in enumerate(source_lines):
                if pat.match(line):
                    lineno = i
                    break

        if inspect.ismethod(obj):
            obj = obj.im_func
        if inspect.isfunction(obj):
            obj = obj.func_code
        if inspect.istraceback(obj):
            obj = obj.tb_frame
        if inspect.isframe(obj):
            obj = obj.f_code
        if inspect.iscode(obj):
            lineno = getattr(obj, 'co_firstlineno', None) - 1
        if lineno is not None:
            if source_lines is None:
                return lineno + 1
            pat = re.compile('(^|.*:)\\s*\\w*("|\')')
            for lineno in range(lineno, len(source_lines)):
                if pat.match(source_lines[lineno]):
                    return lineno

        return


class DocTestRunner():
    """
    A class used to run DocTest test cases, and accumulate statistics.
    The `run` method is used to process a single DocTest case.  It
    returns a tuple `(f, t)`, where `t` is the number of test cases
    tried, and `f` is the number of test cases that failed.
    
        >>> tests = DocTestFinder().find(_TestClass)
        >>> runner = DocTestRunner(verbose=False)
        >>> tests.sort(key = lambda test: test.name)
        >>> for test in tests:
        ...     print test.name, '->', runner.run(test)
        _TestClass -> TestResults(failed=0, attempted=2)
        _TestClass.__init__ -> TestResults(failed=0, attempted=2)
        _TestClass.get -> TestResults(failed=0, attempted=2)
        _TestClass.square -> TestResults(failed=0, attempted=1)
    
    The `summarize` method prints a summary of all the test cases that
    have been run by the runner, and returns an aggregated `(f, t)`
    tuple:
    
        >>> runner.summarize(verbose=1)
        4 items passed all tests:
           2 tests in _TestClass
           2 tests in _TestClass.__init__
           2 tests in _TestClass.get
           1 tests in _TestClass.square
        7 tests in 4 items.
        7 passed and 0 failed.
        Test passed.
        TestResults(failed=0, attempted=7)
    
    The aggregated number of tried examples and failed examples is
    also available via the `tries` and `failures` attributes:
    
        >>> runner.tries
        7
        >>> runner.failures
        0
    
    The comparison between expected outputs and actual outputs is done
    by an `OutputChecker`.  This comparison may be customized with a
    number of option flags; see the documentation for `testmod` for
    more information.  If the option flags are insufficient, then the
    comparison may also be customized by passing a subclass of
    `OutputChecker` to the constructor.
    
    The test runner's display output can be controlled in two ways.
    First, an output function (`out) can be passed to
    `TestRunner.run`; this function will be called with strings that
    should be displayed.  It defaults to `sys.stdout.write`.  If
    capturing the output is not sufficient, then the display output
    can be also customized by subclassing DocTestRunner, and
    overriding the methods `report_start`, `report_success`,
    `report_unexpected_exception`, and `report_failure`.
    """
    DIVIDER = '*' * 70

    def __init__(self, checker=None, verbose=None, optionflags=0):
        """
        Create a new test runner.
        
        Optional keyword arg `checker` is the `OutputChecker` that
        should be used to compare the expected outputs and actual
        outputs of doctest examples.
        
        Optional keyword arg 'verbose' prints lots of stuff if true,
        only failures if false; by default, it's true iff '-v' is in
        sys.argv.
        
        Optional argument `optionflags` can be used to control how the
        test runner compares expected output to actual output, and how
        it displays failures.  See the documentation for `testmod` for
        more information.
        """
        self._checker = checker or OutputChecker()
        if verbose is None:
            verbose = '-v' in sys.argv
        self._verbose = verbose
        self.optionflags = optionflags
        self.original_optionflags = optionflags
        self.tries = 0
        self.failures = 0
        self._name2ft = {}
        self._fakeout = _SpoofOut()
        return

    def report_start(self, out, test, example):
        """
        Report that the test runner is about to process the given
        example.  (Only displays a message if verbose=True)
        """
        if self._verbose:
            if example.want:
                out('Trying:\n' + _indent(example.source) + 'Expecting:\n' + _indent(example.want))
            else:
                out('Trying:\n' + _indent(example.source) + 'Expecting nothing\n')

    def report_success(self, out, test, example, got):
        """
        Report that the given example ran successfully.  (Only
        displays a message if verbose=True)
        """
        if self._verbose:
            out('ok\n')

    def report_failure(self, out, test, example, got):
        """
        Report that the given example failed.
        """
        out(self._failure_header(test, example) + self._checker.output_difference(example, got, self.optionflags))

    def report_unexpected_exception(self, out, test, example, exc_info):
        """
        Report that the given example raised an unexpected exception.
        """
        out(self._failure_header(test, example) + 'Exception raised:\n' + _indent(_exception_traceback(exc_info)))

    def _failure_header(self, test, example):
        out = [
         self.DIVIDER]
        if test.filename:
            if test.lineno is not None and example.lineno is not None:
                lineno = test.lineno + example.lineno + 1
            else:
                lineno = '?'
            out.append('File "%s", line %s, in %s' % (
             test.filename, lineno, test.name))
        else:
            out.append('Line %s, in %s' % (example.lineno + 1, test.name))
        out.append('Failed example:')
        source = example.source
        out.append(_indent(source))
        return '\n'.join(out)

    def __run(self, test, compileflags, out):
        """
        Run the examples in `test`.  Write the outcome of each example
        with one of the `DocTestRunner.report_*` methods, using the
        writer function `out`.  `compileflags` is the set of compiler
        flags that should be used to execute examples.  Return a tuple
        `(f, t)`, where `t` is the number of examples tried, and `f`
        is the number of examples that failed.  The examples are run
        in the namespace `test.globs`.
        """
        failures = tries = 0
        original_optionflags = self.optionflags
        SUCCESS, FAILURE, BOOM = range(3)
        check = self._checker.check_output
        for examplenum, example in enumerate(test.examples):
            quiet = self.optionflags & REPORT_ONLY_FIRST_FAILURE and failures > 0
            self.optionflags = original_optionflags
            if example.options:
                for optionflag, val in example.options.items():
                    if val:
                        self.optionflags |= optionflag
                    else:
                        self.optionflags &= ~optionflag

            if self.optionflags & SKIP:
                continue
            tries += 1
            if not quiet:
                self.report_start(out, test, example)
            filename = '<doctest %s[%d]>' % (test.name, examplenum)
            try:
                exec compile(example.source, filename, 'single', compileflags, 1) in test.globs
                self.debugger.set_continue()
                exception = None
            except KeyboardInterrupt:
                raise
            except:
                exception = sys.exc_info()
                self.debugger.set_continue()

            got = self._fakeout.getvalue()
            self._fakeout.truncate(0)
            outcome = FAILURE
            if exception is None:
                if check(example.want, got, self.optionflags):
                    outcome = SUCCESS
            else:
                exc_info = sys.exc_info()
                exc_msg = traceback.format_exception_only(*exc_info[:2])[-1]
                if not quiet:
                    got += _exception_traceback(exc_info)
                if example.exc_msg is None:
                    outcome = BOOM
                elif check(example.exc_msg, exc_msg, self.optionflags):
                    outcome = SUCCESS
                elif self.optionflags & IGNORE_EXCEPTION_DETAIL:
                    m1 = re.match('(?:[^:]*\\.)?([^:]*:)', example.exc_msg)
                    m2 = re.match('(?:[^:]*\\.)?([^:]*:)', exc_msg)
                    if m1 and m2 and check(m1.group(1), m2.group(1), self.optionflags):
                        outcome = SUCCESS
            if outcome is SUCCESS:
                if not quiet:
                    self.report_success(out, test, example, got)
            elif outcome is FAILURE:
                if not quiet:
                    self.report_failure(out, test, example, got)
                failures += 1
            elif outcome is BOOM:
                if not quiet:
                    self.report_unexpected_exception(out, test, example, exc_info)
                failures += 1

        self.optionflags = original_optionflags
        self.__record_outcome(test, failures, tries)
        return TestResults(failures, tries)

    def __record_outcome(self, test, f, t):
        """
        Record the fact that the given DocTest (`test`) generated `f`
        failures out of `t` tried examples.
        """
        f2, t2 = self._name2ft.get(test.name, (0, 0))
        self._name2ft[test.name] = (f + f2, t + t2)
        self.failures += f
        self.tries += t

    __LINECACHE_FILENAME_RE = re.compile('<doctest (?P<name>.+)\\[(?P<examplenum>\\d+)\\]>$')

    def __patched_linecache_getlines(self, filename, module_globals=None):
        m = self.__LINECACHE_FILENAME_RE.match(filename)
        if m and m.group('name') == self.test.name:
            example = self.test.examples[int(m.group('examplenum'))]
            source = example.source
            if isinstance(source, unicode):
                source = source.encode('ascii', 'backslashreplace')
            return source.splitlines(True)
        else:
            return self.save_linecache_getlines(filename, module_globals)

    def run(self, test, compileflags=None, out=None, clear_globs=True):
        """
        Run the examples in `test`, and display the results using the
        writer function `out`.
        
        The examples are run in the namespace `test.globs`.  If
        `clear_globs` is true (the default), then this namespace will
        be cleared after the test runs, to help with garbage
        collection.  If you would like to examine the namespace after
        the test completes, then use `clear_globs=False`.
        
        `compileflags` gives the set of flags that should be used by
        the Python compiler when running the examples.  If not
        specified, then it will default to the set of future-import
        flags that apply to `globs`.
        
        The output of each example is checked using
        `DocTestRunner.check_output`, and the results are formatted by
        the `DocTestRunner.report_*` methods.
        """
        self.test = test
        if compileflags is None:
            compileflags = _extract_future_flags(test.globs)
        save_stdout = sys.stdout
        if out is None:
            out = save_stdout.write
        sys.stdout = self._fakeout
        save_set_trace = pdb.set_trace
        self.debugger = _OutputRedirectingPdb(save_stdout)
        self.debugger.reset()
        pdb.set_trace = self.debugger.set_trace
        self.save_linecache_getlines = linecache.getlines
        linecache.getlines = self.__patched_linecache_getlines
        save_displayhook = sys.displayhook
        sys.displayhook = sys.__displayhook__
        try:
            return self.__run(test, compileflags, out)
        finally:
            sys.stdout = save_stdout
            pdb.set_trace = save_set_trace
            linecache.getlines = self.save_linecache_getlines
            sys.displayhook = save_displayhook
            if clear_globs:
                test.globs.clear()

        return

    def summarize(self, verbose=None):
        """
        Print a summary of all the test cases that have been run by
        this DocTestRunner, and return a tuple `(f, t)`, where `f` is
        the total number of failed examples, and `t` is the total
        number of tried examples.
        
        The optional `verbose` argument controls how detailed the
        summary is.  If the verbosity is not specified, then the
        DocTestRunner's verbosity is used.
        """
        if verbose is None:
            verbose = self._verbose
        notests = []
        passed = []
        failed = []
        totalt = totalf = 0
        for x in self._name2ft.items():
            name, (f, t) = x
            totalt += t
            totalf += f
            if t == 0:
                notests.append(name)
            elif f == 0:
                passed.append((name, t))
            else:
                failed.append(x)

        if verbose:
            if notests:
                print len(notests), 'items had no tests:'
                notests.sort()
                for thing in notests:
                    print '   ', thing

            if passed:
                print len(passed), 'items passed all tests:'
                passed.sort()
                for thing, count in passed:
                    print ' %3d tests in %s' % (count, thing)

        if failed:
            print self.DIVIDER
            print len(failed), 'items had failures:'
            failed.sort()
            for thing, (f, t) in failed:
                print ' %3d of %3d in %s' % (f, t, thing)

        if verbose:
            print totalt, 'tests in', len(self._name2ft), 'items.'
            print totalt - totalf, 'passed and', totalf, 'failed.'
        if totalf:
            print '***Test Failed***', totalf, 'failures.'
        elif verbose:
            print 'Test passed.'
        return TestResults(totalf, totalt)

    def merge(self, other):
        d = self._name2ft
        for name, (f, t) in other._name2ft.items():
            if name in d:
                f2, t2 = d[name]
                f = f + f2
                t = t + t2
            d[name] = (
             f, t)


class OutputChecker():
    """
    A class used to check the whether the actual output from a doctest
    example matches the expected output.  `OutputChecker` defines two
    methods: `check_output`, which compares a given pair of outputs,
    and returns true if they match; and `output_difference`, which
    returns a string describing the differences between two outputs.
    """

    def check_output(self, want, got, optionflags):
        """
        Return True iff the actual output from an example (`got`)
        matches the expected output (`want`).  These strings are
        always considered to match if they are identical; but
        depending on what option flags the test runner is using,
        several non-exact match types are also possible.  See the
        documentation for `TestRunner` for more information about
        option flags.
        """
        if got == want:
            return True
        if not optionflags & DONT_ACCEPT_TRUE_FOR_1:
            if (
             got, want) == ('True\n', '1\n'):
                return True
            if (
             got, want) == ('False\n', '0\n'):
                return True
        if not optionflags & DONT_ACCEPT_BLANKLINE:
            want = re.sub('(?m)^%s\\s*?$' % re.escape(BLANKLINE_MARKER), '', want)
            got = re.sub('(?m)^\\s*?$', '', got)
            if got == want:
                return True
        if optionflags & NORMALIZE_WHITESPACE:
            got = ' '.join(got.split())
            want = ' '.join(want.split())
            if got == want:
                return True
        if optionflags & ELLIPSIS:
            if _ellipsis_match(want, got):
                return True
        return False

    def _do_a_fancy_diff(self, want, got, optionflags):
        if not optionflags & (REPORT_UDIFF | REPORT_CDIFF | REPORT_NDIFF):
            return False
        if optionflags & REPORT_NDIFF:
            return True
        return want.count('\n') > 2 and got.count('\n') > 2

    def output_difference(self, example, got, optionflags):
        """
        Return a string describing the differences between the
        expected output for a given example (`example`) and the actual
        output (`got`).  `optionflags` is the set of option flags used
        to compare `want` and `got`.
        """
        want = example.want
        if not optionflags & DONT_ACCEPT_BLANKLINE:
            got = re.sub('(?m)^[ ]*(?=\n)', BLANKLINE_MARKER, got)
        if self._do_a_fancy_diff(want, got, optionflags):
            want_lines = want.splitlines(True)
            got_lines = got.splitlines(True)
            if optionflags & REPORT_UDIFF:
                diff = difflib.unified_diff(want_lines, got_lines, n=2)
                diff = list(diff)[2:]
                kind = 'unified diff with -expected +actual'
            elif optionflags & REPORT_CDIFF:
                diff = difflib.context_diff(want_lines, got_lines, n=2)
                diff = list(diff)[2:]
                kind = 'context diff with expected followed by actual'
            elif optionflags & REPORT_NDIFF:
                engine = difflib.Differ(charjunk=difflib.IS_CHARACTER_JUNK)
                diff = list(engine.compare(want_lines, got_lines))
                kind = 'ndiff with -expected +actual'
            diff = [ line.rstrip() + '\n' for line in diff ]
            return 'Differences (%s):\n' % kind + _indent(''.join(diff))
        else:
            if want and got:
                return 'Expected:\n%sGot:\n%s' % (_indent(want), _indent(got))
            if want:
                return 'Expected:\n%sGot nothing\n' % _indent(want)
            if got:
                return 'Expected nothing\nGot:\n%s' % _indent(got)
            return 'Expected nothing\nGot nothing\n'


class DocTestFailure(Exception):
    """A DocTest example has failed in debugging mode.
    
    The exception instance has variables:
    
    - test: the DocTest object being run
    
    - example: the Example object that failed
    
    - got: the actual output
    """

    def __init__(self, test, example, got):
        self.test = test
        self.example = example
        self.got = got

    def __str__(self):
        return str(self.test)


class UnexpectedException(Exception):
    """A DocTest example has encountered an unexpected exception
    
    The exception instance has variables:
    
    - test: the DocTest object being run
    
    - example: the Example object that failed
    
    - exc_info: the exception info
    """

    def __init__(self, test, example, exc_info):
        self.test = test
        self.example = example
        self.exc_info = exc_info

    def __str__(self):
        return str(self.test)


class DebugRunner(DocTestRunner):
    r"""Run doc tests but raise an exception as soon as there is a failure.
    
    If an unexpected exception occurs, an UnexpectedException is raised.
    It contains the test, the example, and the original exception:
    
      >>> runner = DebugRunner(verbose=False)
      >>> test = DocTestParser().get_doctest('>>> raise KeyError\n42',
      ...                                    {}, 'foo', 'foo.py', 0)
      >>> try:
      ...     runner.run(test)
      ... except UnexpectedException, failure:
      ...     pass
    
      >>> failure.test is test
      True
    
      >>> failure.example.want
      '42\n'
    
      >>> exc_info = failure.exc_info
      >>> raise exc_info[0], exc_info[1], exc_info[2]
      Traceback (most recent call last):
      ...
      KeyError
    
    We wrap the original exception to give the calling application
    access to the test and example information.
    
    If the output doesn't match, then a DocTestFailure is raised:
    
      >>> test = DocTestParser().get_doctest('''
      ...      >>> x = 1
      ...      >>> x
      ...      2
      ...      ''', {}, 'foo', 'foo.py', 0)
    
      >>> try:
      ...    runner.run(test)
      ... except DocTestFailure, failure:
      ...    pass
    
    DocTestFailure objects provide access to the test:
    
      >>> failure.test is test
      True
    
    As well as to the example:
    
      >>> failure.example.want
      '2\n'
    
    and the actual output:
    
      >>> failure.got
      '1\n'
    
    If a failure or error occurs, the globals are left intact:
    
      >>> del test.globs['__builtins__']
      >>> test.globs
      {'x': 1}
    
      >>> test = DocTestParser().get_doctest('''
      ...      >>> x = 2
      ...      >>> raise KeyError
      ...      ''', {}, 'foo', 'foo.py', 0)
    
      >>> runner.run(test)
      Traceback (most recent call last):
      ...
      UnexpectedException: <DocTest foo from foo.py:0 (2 examples)>
    
      >>> del test.globs['__builtins__']
      >>> test.globs
      {'x': 2}
    
    But the globals are cleared if there is no error:
    
      >>> test = DocTestParser().get_doctest('''
      ...      >>> x = 2
      ...      ''', {}, 'foo', 'foo.py', 0)
    
      >>> runner.run(test)
      TestResults(failed=0, attempted=1)
    
      >>> test.globs
      {}
    
    """

    def run(self, test, compileflags=None, out=None, clear_globs=True):
        r = DocTestRunner.run(self, test, compileflags, out, False)
        if clear_globs:
            test.globs.clear()
        return r

    def report_unexpected_exception(self, out, test, example, exc_info):
        raise UnexpectedException(test, example, exc_info)

    def report_failure(self, out, test, example, got):
        raise DocTestFailure(test, example, got)


master = None

def testmod(m=None, name=None, globs=None, verbose=None, report=True, optionflags=0, extraglobs=None, raise_on_error=False, exclude_empty=False):
    """m=None, name=None, globs=None, verbose=None, report=True,
       optionflags=0, extraglobs=None, raise_on_error=False,
       exclude_empty=False
    
    Test examples in docstrings in functions and classes reachable
    from module m (or the current module if m is not supplied), starting
    with m.__doc__.
    
    Also test examples reachable from dict m.__test__ if it exists and is
    not None.  m.__test__ maps names to functions, classes and strings;
    function and class docstrings are tested even if the name is private;
    strings are tested directly, as if they were docstrings.
    
    Return (#failures, #tests).
    
    See help(doctest) for an overview.
    
    Optional keyword arg "name" gives the name of the module; by default
    use m.__name__.
    
    Optional keyword arg "globs" gives a dict to be used as the globals
    when executing examples; by default, use m.__dict__.  A copy of this
    dict is actually used for each docstring, so that each docstring's
    examples start with a clean slate.
    
    Optional keyword arg "extraglobs" gives a dictionary that should be
    merged into the globals that are used to execute examples.  By
    default, no extra globals are used.  This is new in 2.4.
    
    Optional keyword arg "verbose" prints lots of stuff if true, prints
    only failures if false; by default, it's true iff "-v" is in sys.argv.
    
    Optional keyword arg "report" prints a summary at the end when true,
    else prints nothing at the end.  In verbose mode, the summary is
    detailed, else very brief (in fact, empty if all tests passed).
    
    Optional keyword arg "optionflags" or's together module constants,
    and defaults to 0.  This is new in 2.3.  Possible values (see the
    docs for details):
    
        DONT_ACCEPT_TRUE_FOR_1
        DONT_ACCEPT_BLANKLINE
        NORMALIZE_WHITESPACE
        ELLIPSIS
        SKIP
        IGNORE_EXCEPTION_DETAIL
        REPORT_UDIFF
        REPORT_CDIFF
        REPORT_NDIFF
        REPORT_ONLY_FIRST_FAILURE
    
    Optional keyword arg "raise_on_error" raises an exception on the
    first unexpected exception or failure. This allows failures to be
    post-mortem debugged.
    
    Advanced tomfoolery:  testmod runs methods of a local instance of
    class doctest.Tester, then merges the results into (or creates)
    global Tester instance doctest.master.  Methods of doctest.master
    can be called directly too, if you want to do something unusual.
    Passing report=0 to testmod is especially useful then, to delay
    displaying a summary.  Invoke doctest.master.summarize(verbose)
    when you're done fiddling.
    """
    global master
    if m is None:
        m = sys.modules.get('__main__')
    if not inspect.ismodule(m):
        raise TypeError('testmod: module required; %r' % (m,))
    if name is None:
        name = m.__name__
    finder = DocTestFinder(exclude_empty=exclude_empty)
    if raise_on_error:
        runner = DebugRunner(verbose=verbose, optionflags=optionflags)
    else:
        runner = DocTestRunner(verbose=verbose, optionflags=optionflags)
    for test in finder.find(m, name, globs=globs, extraglobs=extraglobs):
        runner.run(test)

    if report:
        runner.summarize()
    if master is None:
        master = runner
    else:
        master.merge(runner)
    return TestResults(runner.failures, runner.tries)


def testfile(filename, module_relative=True, name=None, package=None, globs=None, verbose=None, report=True, optionflags=0, extraglobs=None, raise_on_error=False, parser=DocTestParser(), encoding=None):
    """
    Test examples in the given file.  Return (#failures, #tests).
    
    Optional keyword arg "module_relative" specifies how filenames
    should be interpreted:
    
      - If "module_relative" is True (the default), then "filename"
         specifies a module-relative path.  By default, this path is
         relative to the calling module's directory; but if the
         "package" argument is specified, then it is relative to that
         package.  To ensure os-independence, "filename" should use
         "/" characters to separate path segments, and should not
         be an absolute path (i.e., it may not begin with "/").
    
      - If "module_relative" is False, then "filename" specifies an
        os-specific path.  The path may be absolute or relative (to
        the current working directory).
    
    Optional keyword arg "name" gives the name of the test; by default
    use the file's basename.
    
    Optional keyword argument "package" is a Python package or the
    name of a Python package whose directory should be used as the
    base directory for a module relative filename.  If no package is
    specified, then the calling module's directory is used as the base
    directory for module relative filenames.  It is an error to
    specify "package" if "module_relative" is False.
    
    Optional keyword arg "globs" gives a dict to be used as the globals
    when executing examples; by default, use {}.  A copy of this dict
    is actually used for each docstring, so that each docstring's
    examples start with a clean slate.
    
    Optional keyword arg "extraglobs" gives a dictionary that should be
    merged into the globals that are used to execute examples.  By
    default, no extra globals are used.
    
    Optional keyword arg "verbose" prints lots of stuff if true, prints
    only failures if false; by default, it's true iff "-v" is in sys.argv.
    
    Optional keyword arg "report" prints a summary at the end when true,
    else prints nothing at the end.  In verbose mode, the summary is
    detailed, else very brief (in fact, empty if all tests passed).
    
    Optional keyword arg "optionflags" or's together module constants,
    and defaults to 0.  Possible values (see the docs for details):
    
        DONT_ACCEPT_TRUE_FOR_1
        DONT_ACCEPT_BLANKLINE
        NORMALIZE_WHITESPACE
        ELLIPSIS
        SKIP
        IGNORE_EXCEPTION_DETAIL
        REPORT_UDIFF
        REPORT_CDIFF
        REPORT_NDIFF
        REPORT_ONLY_FIRST_FAILURE
    
    Optional keyword arg "raise_on_error" raises an exception on the
    first unexpected exception or failure. This allows failures to be
    post-mortem debugged.
    
    Optional keyword arg "parser" specifies a DocTestParser (or
    subclass) that should be used to extract tests from the files.
    
    Optional keyword arg "encoding" specifies an encoding that should
    be used to convert the file to unicode.
    
    Advanced tomfoolery:  testmod runs methods of a local instance of
    class doctest.Tester, then merges the results into (or creates)
    global Tester instance doctest.master.  Methods of doctest.master
    can be called directly too, if you want to do something unusual.
    Passing report=0 to testmod is especially useful then, to delay
    displaying a summary.  Invoke doctest.master.summarize(verbose)
    when you're done fiddling.
    """
    global master
    if package and not module_relative:
        raise ValueError('Package may only be specified for module-relative paths.')
    text, filename = _load_testfile(filename, package, module_relative)
    if name is None:
        name = os.path.basename(filename)
    if globs is None:
        globs = {}
    else:
        globs = globs.copy()
    if extraglobs is not None:
        globs.update(extraglobs)
    if '__name__' not in globs:
        globs['__name__'] = '__main__'
    if raise_on_error:
        runner = DebugRunner(verbose=verbose, optionflags=optionflags)
    else:
        runner = DocTestRunner(verbose=verbose, optionflags=optionflags)
    if encoding is not None:
        text = text.decode(encoding)
    test = parser.get_doctest(text, globs, name, filename, 0)
    runner.run(test)
    if report:
        runner.summarize()
    if master is None:
        master = runner
    else:
        master.merge(runner)
    return TestResults(runner.failures, runner.tries)


def run_docstring_examples(f, globs, verbose=False, name='NoName', compileflags=None, optionflags=0):
    """
    Test examples in the given object's docstring (`f`), using `globs`
    as globals.  Optional argument `name` is used in failure messages.
    If the optional argument `verbose` is true, then generate output
    even if there are no failures.
    
    `compileflags` gives the set of flags that should be used by the
    Python compiler when running the examples.  If not specified, then
    it will default to the set of future-import flags that apply to
    `globs`.
    
    Optional keyword arg `optionflags` specifies options for the
    testing and output.  See the documentation for `testmod` for more
    information.
    """
    finder = DocTestFinder(verbose=verbose, recurse=False)
    runner = DocTestRunner(verbose=verbose, optionflags=optionflags)
    for test in finder.find(f, name, globs=globs):
        runner.run(test, compileflags=compileflags)


class Tester():

    def __init__(self, mod=None, globs=None, verbose=None, optionflags=0):
        warnings.warn('class Tester is deprecated; use class doctest.DocTestRunner instead', DeprecationWarning, stacklevel=2)
        if mod is None and globs is None:
            raise TypeError('Tester.__init__: must specify mod or globs')
        if mod is not None and not inspect.ismodule(mod):
            raise TypeError('Tester.__init__: mod must be a module; %r' % (
             mod,))
        if globs is None:
            globs = mod.__dict__
        self.globs = globs
        self.verbose = verbose
        self.optionflags = optionflags
        self.testfinder = DocTestFinder()
        self.testrunner = DocTestRunner(verbose=verbose, optionflags=optionflags)
        return

    def runstring(self, s, name):
        test = DocTestParser().get_doctest(s, self.globs, name, None, None)
        if self.verbose:
            print 'Running string', name
        f, t = self.testrunner.run(test)
        if self.verbose:
            print f, 'of', t, 'examples failed in string', name
        return TestResults(f, t)

    def rundoc(self, object, name=None, module=None):
        f = t = 0
        tests = self.testfinder.find(object, name, module=module, globs=self.globs)
        for test in tests:
            f2, t2 = self.testrunner.run(test)
            f, t = f + f2, t + t2

        return TestResults(f, t)

    def rundict(self, d, name, module=None):
        import types
        m = types.ModuleType(name)
        m.__dict__.update(d)
        if module is None:
            module = False
        return self.rundoc(m, name, module)

    def run__test__(self, d, name):
        import types
        m = types.ModuleType(name)
        m.__test__ = d
        return self.rundoc(m, name)

    def summarize(self, verbose=None):
        return self.testrunner.summarize(verbose)

    def merge(self, other):
        self.testrunner.merge(other.testrunner)


_unittest_reportflags = 0

def set_unittest_reportflags(flags):
    """Sets the unittest option flags.
    
    The old flag is returned so that a runner could restore the old
    value if it wished to:
    
      >>> import doctest
      >>> old = doctest._unittest_reportflags
      >>> doctest.set_unittest_reportflags(REPORT_NDIFF |
      ...                          REPORT_ONLY_FIRST_FAILURE) == old
      True
    
      >>> doctest._unittest_reportflags == (REPORT_NDIFF |
      ...                                   REPORT_ONLY_FIRST_FAILURE)
      True
    
    Only reporting flags can be set:
    
      >>> doctest.set_unittest_reportflags(ELLIPSIS)
      Traceback (most recent call last):
      ...
      ValueError: ('Only reporting flags allowed', 8)
    
      >>> doctest.set_unittest_reportflags(old) == (REPORT_NDIFF |
      ...                                   REPORT_ONLY_FIRST_FAILURE)
      True
    """
    global _unittest_reportflags
    if flags & REPORTING_FLAGS != flags:
        raise ValueError('Only reporting flags allowed', flags)
    old = _unittest_reportflags
    _unittest_reportflags = flags
    return old


class DocTestCase(unittest.TestCase):

    def __init__(self, test, optionflags=0, setUp=None, tearDown=None, checker=None):
        unittest.TestCase.__init__(self)
        self._dt_optionflags = optionflags
        self._dt_checker = checker
        self._dt_test = test
        self._dt_setUp = setUp
        self._dt_tearDown = tearDown

    def setUp(self):
        test = self._dt_test
        if self._dt_setUp is not None:
            self._dt_setUp(test)
        return

    def tearDown(self):
        test = self._dt_test
        if self._dt_tearDown is not None:
            self._dt_tearDown(test)
        test.globs.clear()
        return

    def runTest(self):
        test = self._dt_test
        old = sys.stdout
        new = StringIO()
        optionflags = self._dt_optionflags
        if not optionflags & REPORTING_FLAGS:
            optionflags |= _unittest_reportflags
        runner = DocTestRunner(optionflags=optionflags, checker=self._dt_checker, verbose=False)
        try:
            runner.DIVIDER = '-' * 70
            failures, tries = runner.run(test, out=new.write, clear_globs=False)
        finally:
            sys.stdout = old

        if failures:
            raise self.failureException(self.format_failure(new.getvalue()))

    def format_failure(self, err):
        test = self._dt_test
        if test.lineno is None:
            lineno = 'unknown line number'
        else:
            lineno = '%s' % test.lineno
        lname = '.'.join(test.name.split('.')[-1:])
        return 'Failed doctest test for %s\n  File "%s", line %s, in %s\n\n%s' % (
         test.name, test.filename, lineno, lname, err)

    def debug(self):
        r"""Run the test case without results and without catching exceptions
        
        The unit test framework includes a debug method on test cases
        and test suites to support post-mortem debugging.  The test code
        is run in such a way that errors are not caught.  This way a
        caller can catch the errors and initiate post-mortem debugging.
        
        The DocTestCase provides a debug method that raises
        UnexpectedException errors if there is an unexpected
        exception:
        
          >>> test = DocTestParser().get_doctest('>>> raise KeyError\n42',
          ...                {}, 'foo', 'foo.py', 0)
          >>> case = DocTestCase(test)
          >>> try:
          ...     case.debug()
          ... except UnexpectedException, failure:
          ...     pass
        
        The UnexpectedException contains the test, the example, and
        the original exception:
        
          >>> failure.test is test
          True
        
          >>> failure.example.want
          '42\n'
        
          >>> exc_info = failure.exc_info
          >>> raise exc_info[0], exc_info[1], exc_info[2]
          Traceback (most recent call last):
          ...
          KeyError
        
        If the output doesn't match, then a DocTestFailure is raised:
        
          >>> test = DocTestParser().get_doctest('''
          ...      >>> x = 1
          ...      >>> x
          ...      2
          ...      ''', {}, 'foo', 'foo.py', 0)
          >>> case = DocTestCase(test)
        
          >>> try:
          ...    case.debug()
          ... except DocTestFailure, failure:
          ...    pass
        
        DocTestFailure objects provide access to the test:
        
          >>> failure.test is test
          True
        
        As well as to the example:
        
          >>> failure.example.want
          '2\n'
        
        and the actual output:
        
          >>> failure.got
          '1\n'
        
        """
        self.setUp()
        runner = DebugRunner(optionflags=self._dt_optionflags, checker=self._dt_checker, verbose=False)
        runner.run(self._dt_test, clear_globs=False)
        self.tearDown()

    def id(self):
        return self._dt_test.name

    def __repr__(self):
        name = self._dt_test.name.split('.')
        return '%s (%s)' % (name[-1], '.'.join(name[:-1]))

    __str__ = __repr__

    def shortDescription(self):
        return 'Doctest: ' + self._dt_test.name


class SkipDocTestCase(DocTestCase):

    def __init__(self):
        DocTestCase.__init__(self, None)
        return

    def setUp(self):
        self.skipTest('DocTestSuite will not work with -O2 and above')

    def test_skip(self):
        pass

    def shortDescription(self):
        return 'Skipping tests from %s' % module.__name__


def DocTestSuite(module=None, globs=None, extraglobs=None, test_finder=None, **options):
    """
    Convert doctest tests for a module to a unittest test suite.
    
    This converts each documentation string in a module that
    contains doctest tests to a unittest test case.  If any of the
    tests in a doc string fail, then the test case fails.  An exception
    is raised showing the name of the file containing the test and a
    (sometimes approximate) line number.
    
    The `module` argument provides the module to be tested.  The argument
    can be either a module or a module name.
    
    If no argument is given, the calling module is used.
    
    A number of options may be provided as keyword arguments:
    
    setUp
      A set-up function.  This is called before running the
      tests in each file. The setUp function will be passed a DocTest
      object.  The setUp function can access the test globals as the
      globs attribute of the test passed.
    
    tearDown
      A tear-down function.  This is called after running the
      tests in each file.  The tearDown function will be passed a DocTest
      object.  The tearDown function can access the test globals as the
      globs attribute of the test passed.
    
    globs
      A dictionary containing initial global variables for the tests.
    
    optionflags
       A set of doctest option flags expressed as an integer.
    """
    if test_finder is None:
        test_finder = DocTestFinder()
    module = _normalize_module(module)
    tests = test_finder.find(module, globs=globs, extraglobs=extraglobs)
    if not tests and sys.flags.optimize >= 2:
        suite = unittest.TestSuite()
        suite.addTest(SkipDocTestCase())
        return suite
    else:
        if not tests:
            raise ValueError(module, 'has no tests')
        tests.sort()
        suite = unittest.TestSuite()
        for test in tests:
            if len(test.examples) == 0:
                continue
            if not test.filename:
                filename = module.__file__
                if filename[-4:] in ('.pyc', '.pyo'):
                    filename = filename[:-1]
                test.filename = filename
            suite.addTest(DocTestCase(test, **options))

        return suite


class DocFileCase(DocTestCase):

    def id(self):
        return '_'.join(self._dt_test.name.split('.'))

    def __repr__(self):
        return self._dt_test.filename

    __str__ = __repr__

    def format_failure(self, err):
        return 'Failed doctest test for %s\n  File "%s", line 0\n\n%s' % (
         self._dt_test.name, self._dt_test.filename, err)


def DocFileTest(path, module_relative=True, package=None, globs=None, parser=DocTestParser(), encoding=None, **options):
    if globs is None:
        globs = {}
    else:
        globs = globs.copy()
    if package and not module_relative:
        raise ValueError('Package may only be specified for module-relative paths.')
    doc, path = _load_testfile(path, package, module_relative)
    if '__file__' not in globs:
        globs['__file__'] = path
    name = os.path.basename(path)
    if encoding is not None:
        doc = doc.decode(encoding)
    test = parser.get_doctest(doc, globs, name, path, 0)
    return DocFileCase(test, **options)


def DocFileSuite(*paths, **kw):
    """A unittest suite for one or more doctest files.
    
    The path to each doctest file is given as a string; the
    interpretation of that string depends on the keyword argument
    "module_relative".
    
    A number of options may be provided as keyword arguments:
    
    module_relative
      If "module_relative" is True, then the given file paths are
      interpreted as os-independent module-relative paths.  By
      default, these paths are relative to the calling module's
      directory; but if the "package" argument is specified, then
      they are relative to that package.  To ensure os-independence,
      "filename" should use "/" characters to separate path
      segments, and may not be an absolute path (i.e., it may not
      begin with "/").
    
      If "module_relative" is False, then the given file paths are
      interpreted as os-specific paths.  These paths may be absolute
      or relative (to the current working directory).
    
    package
      A Python package or the name of a Python package whose directory
      should be used as the base directory for module relative paths.
      If "package" is not specified, then the calling module's
      directory is used as the base directory for module relative
      filenames.  It is an error to specify "package" if
      "module_relative" is False.
    
    setUp
      A set-up function.  This is called before running the
      tests in each file. The setUp function will be passed a DocTest
      object.  The setUp function can access the test globals as the
      globs attribute of the test passed.
    
    tearDown
      A tear-down function.  This is called after running the
      tests in each file.  The tearDown function will be passed a DocTest
      object.  The tearDown function can access the test globals as the
      globs attribute of the test passed.
    
    globs
      A dictionary containing initial global variables for the tests.
    
    optionflags
      A set of doctest option flags expressed as an integer.
    
    parser
      A DocTestParser (or subclass) that should be used to extract
      tests from the files.
    
    encoding
      An encoding that will be used to convert the files to unicode.
    """
    suite = unittest.TestSuite()
    if kw.get('module_relative', True):
        kw['package'] = _normalize_module(kw.get('package'))
    for path in paths:
        suite.addTest(DocFileTest(path, **kw))

    return suite


def script_from_examples(s):
    """Extract script from text with examples.
    
    Converts text with examples to a Python script.  Example input is
    converted to regular code.  Example output and all other words
    are converted to comments:
    
    >>> text = '''
    ...       Here are examples of simple math.
    ...
    ...           Python has super accurate integer addition
    ...
    ...           >>> 2 + 2
    ...           5
    ...
    ...           And very friendly error messages:
    ...
    ...           >>> 1/0
    ...           To Infinity
    ...           And
    ...           Beyond
    ...
    ...           You can use logic if you want:
    ...
    ...           >>> if 0:
    ...           ...    blah
    ...           ...    blah
    ...           ...
    ...
    ...           Ho hum
    ...           '''
    
    >>> print script_from_examples(text)
    # Here are examples of simple math.
    #
    #     Python has super accurate integer addition
    #
    2 + 2
    # Expected:
    ## 5
    #
    #     And very friendly error messages:
    #
    1/0
    # Expected:
    ## To Infinity
    ## And
    ## Beyond
    #
    #     You can use logic if you want:
    #
    if 0:
       blah
       blah
    #
    #     Ho hum
    <BLANKLINE>
    """
    output = []
    for piece in DocTestParser().parse(s):
        if isinstance(piece, Example):
            output.append(piece.source[:-1])
            want = piece.want
            if want:
                output.append('# Expected:')
                output += [ '## ' + l for l in want.split('\n')[:-1] ]
        else:
            output += [ _comment_line(l) for l in piece.split('\n')[:-1]
                      ]

    while output and output[-1] == '#':
        output.pop()

    while output and output[0] == '#':
        output.pop(0)

    return '\n'.join(output) + '\n'


def testsource(module, name):
    """Extract the test sources from a doctest docstring as a script.
    
    Provide the module (or dotted name of the module) containing the
    test to be debugged and the name (within the module) of the object
    with the doc string with tests to be debugged.
    """
    module = _normalize_module(module)
    tests = DocTestFinder().find(module)
    test = [ t for t in tests if t.name == name ]
    if not test:
        raise ValueError(name, 'not found in tests')
    test = test[0]
    testsrc = script_from_examples(test.docstring)
    return testsrc


def debug_src(src, pm=False, globs=None):
    """Debug a single doctest docstring, in argument `src`'"""
    testsrc = script_from_examples(src)
    debug_script(testsrc, pm, globs)


def debug_script(src, pm=False, globs=None):
    """Debug a test script.  `src` is the script, as a string."""
    import pdb
    srcfilename = tempfile.mktemp('.py', 'doctestdebug')
    f = open(srcfilename, 'w')
    f.write(src)
    f.close()
    try:
        if globs:
            globs = globs.copy()
        else:
            globs = {}
        if pm:
            try:
                execfile(srcfilename, globs, globs)
            except:
                print sys.exc_info()[1]
                pdb.post_mortem(sys.exc_info()[2])

        else:
            pdb.run('execfile(%r)' % srcfilename, globs, globs)
    finally:
        os.remove(srcfilename)


def debug(module, name, pm=False):
    """Debug a single doctest docstring.
    
    Provide the module (or dotted name of the module) containing the
    test to be debugged and the name (within the module) of the object
    with the docstring with tests to be debugged.
    """
    module = _normalize_module(module)
    testsrc = testsource(module, name)
    debug_script(testsrc, pm, module.__dict__)


class _TestClass():
    """
    A pointless class, for sanity-checking of docstring testing.
    
    Methods:
        square()
        get()
    
    >>> _TestClass(13).get() + _TestClass(-12).get()
    1
    >>> hex(_TestClass(13).square().get())
    '0xa9'
    """

    def __init__(self, val):
        """val -> _TestClass object with associated value val.
        
        >>> t = _TestClass(123)
        >>> print t.get()
        123
        """
        self.val = val

    def square(self):
        """square() -> square TestClass's associated value
        
        >>> _TestClass(13).square().get()
        169
        """
        self.val = self.val ** 2
        return self

    def get(self):
        """get() -> return TestClass's associated value.
        
        >>> x = _TestClass(-42)
        >>> print x.get()
        -42
        """
        return self.val


__test__ = {'_TestClass': _TestClass,'string': '\n                      Example of a string object, searched as-is.\n                      >>> x = 1; y = 2\n                      >>> x + y, x * y\n                      (3, 2)\n                      ',
   'bool-int equivalence': '\n                                    In 2.2, boolean expressions displayed\n                                    0 or 1.  By default, we still accept\n                                    them.  This can be disabled by passing\n                                    DONT_ACCEPT_TRUE_FOR_1 to the new\n                                    optionflags argument.\n                                    >>> 4 == 4\n                                    1\n                                    >>> 4 == 4\n                                    True\n                                    >>> 4 > 4\n                                    0\n                                    >>> 4 > 4\n                                    False\n                                    ',
   'blank lines': "\n                Blank lines can be marked with <BLANKLINE>:\n                    >>> print 'foo\\n\\nbar\\n'\n                    foo\n                    <BLANKLINE>\n                    bar\n                    <BLANKLINE>\n            ",
   'ellipsis': "\n                If the ellipsis flag is used, then '...' can be used to\n                elide substrings in the desired output:\n                    >>> print range(1000) #doctest: +ELLIPSIS\n                    [0, 1, 2, ..., 999]\n            ",
   'whitespace normalization': '\n                If the whitespace normalization flag is used, then\n                differences in whitespace are ignored.\n                    >>> print range(30) #doctest: +NORMALIZE_WHITESPACE\n                    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,\n                     15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,\n                     27, 28, 29]\n            '
   }

def _test():
    testfiles = [ arg for arg in sys.argv[1:] if arg and arg[0] != '-' ]
    if not testfiles:
        name = os.path.basename(sys.argv[0])
        if '__loader__' in globals():
            name, _ = os.path.splitext(name)
        print 'usage: {0} [-v] file ...'.format(name)
        return 2
    for filename in testfiles:
        if filename.endswith('.py'):
            dirname, filename = os.path.split(filename)
            sys.path.insert(0, dirname)
            m = __import__(filename[:-3])
            del sys.path[0]
            failures, _ = testmod(m)
        else:
            failures, _ = testfile(filename, module_relative=False)
        if failures:
            return 1

    return 0


if __name__ == '__main__':
    sys.exit(_test())