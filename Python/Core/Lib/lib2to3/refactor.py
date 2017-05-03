# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: refactor.py
"""Refactoring framework.

Used as a main program, this can refactor any number of files and/or
recursively descend down directories.  Imported as a module, this
provides infrastructure to write your own refactoring tool.
"""
from __future__ import with_statement
__author__ = 'Guido van Rossum <guido@python.org>'
import os
import sys
import logging
import operator
import collections
import StringIO
from itertools import chain
from .pgen2 import driver, tokenize, token
from .fixer_util import find_root
from . import pytree, pygram
from . import btm_utils as bu
from . import btm_matcher as bm

def get_all_fix_names(fixer_pkg, remove_prefix=True):
    """Return a sorted list of all available fix names in the given package."""
    pkg = __import__(fixer_pkg, [], [], ['*'])
    fixer_dir = os.path.dirname(pkg.__file__)
    fix_names = []
    for name in sorted(os.listdir(fixer_dir)):
        if name.startswith('fix_') and name.endswith('.py'):
            if remove_prefix:
                name = name[4:]
            fix_names.append(name[:-3])

    return fix_names


class _EveryNode(Exception):
    pass


def _get_head_types(pat):
    """ Accepts a pytree Pattern Node and returns a set
    of the pattern types which will match first. """
    if isinstance(pat, (pytree.NodePattern, pytree.LeafPattern)):
        if pat.type is None:
            raise _EveryNode
        return set([pat.type])
    else:
        if isinstance(pat, pytree.NegatedPattern):
            if pat.content:
                return _get_head_types(pat.content)
            raise _EveryNode
        if isinstance(pat, pytree.WildcardPattern):
            r = set()
            for p in pat.content:
                for x in p:
                    r.update(_get_head_types(x))

            return r
        raise Exception("Oh no! I don't understand pattern %s" % pat)
        return


def _get_headnode_dict(fixer_list):
    """ Accepts a list of fixers and returns a dictionary
    of head node type --> fixer list.  """
    head_nodes = collections.defaultdict(list)
    every = []
    for fixer in fixer_list:
        if fixer.pattern:
            try:
                heads = _get_head_types(fixer.pattern)
            except _EveryNode:
                every.append(fixer)
            else:
                for node_type in heads:
                    head_nodes[node_type].append(fixer)

        elif fixer._accept_type is not None:
            head_nodes[fixer._accept_type].append(fixer)
        else:
            every.append(fixer)

    for node_type in chain(pygram.python_grammar.symbol2number.itervalues(), pygram.python_grammar.tokens):
        head_nodes[node_type].extend(every)

    return dict(head_nodes)


def get_fixers_from_package(pkg_name):
    """
    Return the fully qualified names for fixers in the package pkg_name.
    """
    return [ pkg_name + '.' + fix_name for fix_name in get_all_fix_names(pkg_name, False)
           ]


def _identity(obj):
    return obj


if sys.version_info < (3, 0):
    import codecs
    _open_with_encoding = codecs.open

    def _from_system_newlines(input):
        return input.replace(u'\r\n', u'\n')


    def _to_system_newlines(input):
        if os.linesep != '\n':
            return input.replace(u'\n', os.linesep)
        else:
            return input


else:
    _open_with_encoding = open
    _from_system_newlines = _identity
    _to_system_newlines = _identity

def _detect_future_features(source):
    have_docstring = False
    gen = tokenize.generate_tokens(StringIO.StringIO(source).readline)

    def advance():
        tok = gen.next()
        return (
         tok[0], tok[1])

    ignore = frozenset((token.NEWLINE, tokenize.NL, token.COMMENT))
    features = set()
    try:
        while True:
            tp, value = advance()
            if tp in ignore:
                continue
            elif tp == token.STRING:
                if have_docstring:
                    break
                have_docstring = True
            elif tp == token.NAME and value == u'from':
                tp, value = advance()
                if tp != token.NAME or value != u'__future__':
                    break
                tp, value = advance()
                if tp != token.NAME or value != u'import':
                    break
                tp, value = advance()
                if tp == token.OP and value == u'(':
                    tp, value = advance()
                while tp == token.NAME:
                    features.add(value)
                    tp, value = advance()
                    if tp != token.OP or value != u',':
                        break
                    tp, value = advance()

            else:
                break

    except StopIteration:
        pass

    return frozenset(features)


class FixerError(Exception):
    """A fixer could not be loaded."""
    pass


class RefactoringTool(object):
    _default_options = {'print_function': False}
    CLASS_PREFIX = 'Fix'
    FILE_PREFIX = 'fix_'

    def __init__(self, fixer_names, options=None, explicit=None):
        """Initializer.
        
        Args:
            fixer_names: a list of fixers to import
            options: an dict with configuration.
            explicit: a list of fixers to run even if they are explicit.
        """
        self.fixers = fixer_names
        self.explicit = explicit or []
        self.options = self._default_options.copy()
        if options is not None:
            self.options.update(options)
        if self.options['print_function']:
            self.grammar = pygram.python_grammar_no_print_statement
        else:
            self.grammar = pygram.python_grammar
        self.errors = []
        self.logger = logging.getLogger('RefactoringTool')
        self.fixer_log = []
        self.wrote = False
        self.driver = driver.Driver(self.grammar, convert=pytree.convert, logger=self.logger)
        self.pre_order, self.post_order = self.get_fixers()
        self.files = []
        self.BM = bm.BottomMatcher()
        self.bmi_pre_order = []
        self.bmi_post_order = []
        for fixer in chain(self.post_order, self.pre_order):
            if fixer.BM_compatible:
                self.BM.add_fixer(fixer)
            elif fixer in self.pre_order:
                self.bmi_pre_order.append(fixer)
            elif fixer in self.post_order:
                self.bmi_post_order.append(fixer)

        self.bmi_pre_order_heads = _get_headnode_dict(self.bmi_pre_order)
        self.bmi_post_order_heads = _get_headnode_dict(self.bmi_post_order)
        return

    def get_fixers(self):
        """Inspects the options to load the requested patterns and handlers.
        
        Returns:
          (pre_order, post_order), where pre_order is the list of fixers that
          want a pre-order AST traversal, and post_order is the list that want
          post-order traversal.
        """
        pre_order_fixers = []
        post_order_fixers = []
        for fix_mod_path in self.fixers:
            mod = __import__(fix_mod_path, {}, {}, ['*'])
            fix_name = fix_mod_path.rsplit('.', 1)[-1]
            if fix_name.startswith(self.FILE_PREFIX):
                fix_name = fix_name[len(self.FILE_PREFIX):]
            parts = fix_name.split('_')
            class_name = self.CLASS_PREFIX + ''.join([ p.title() for p in parts ])
            try:
                fix_class = getattr(mod, class_name)
            except AttributeError:
                raise FixerError("Can't find %s.%s" % (fix_name, class_name))

            fixer = fix_class(self.options, self.fixer_log)
            if fixer.explicit and self.explicit is not True and fix_mod_path not in self.explicit:
                self.log_message('Skipping implicit fixer: %s', fix_name)
                continue
            self.log_debug('Adding transformation: %s', fix_name)
            if fixer.order == 'pre':
                pre_order_fixers.append(fixer)
            elif fixer.order == 'post':
                post_order_fixers.append(fixer)
            else:
                raise FixerError('Illegal fixer order: %r' % fixer.order)

        key_func = operator.attrgetter('run_order')
        pre_order_fixers.sort(key=key_func)
        post_order_fixers.sort(key=key_func)
        return (
         pre_order_fixers, post_order_fixers)

    def log_error(self, msg, *args, **kwds):
        """Called when an error occurs."""
        raise

    def log_message(self, msg, *args):
        """Hook to log a message."""
        if args:
            msg = msg % args
        self.logger.info(msg)

    def log_debug(self, msg, *args):
        if args:
            msg = msg % args
        self.logger.debug(msg)

    def print_output(self, old_text, new_text, filename, equal):
        """Called with the old version, new version, and filename of a
        refactored file."""
        pass

    def refactor(self, items, write=False, doctests_only=False):
        """Refactor a list of files and directories."""
        for dir_or_file in items:
            if os.path.isdir(dir_or_file):
                self.refactor_dir(dir_or_file, write, doctests_only)
            else:
                self.refactor_file(dir_or_file, write, doctests_only)

    def refactor_dir(self, dir_name, write=False, doctests_only=False):
        """Descends down a directory and refactor every Python file found.
        
        Python files are assumed to have a .py extension.
        
        Files and subdirectories starting with '.' are skipped.
        """
        py_ext = os.extsep + 'py'
        for dirpath, dirnames, filenames in os.walk(dir_name):
            self.log_debug('Descending into %s', dirpath)
            dirnames.sort()
            filenames.sort()
            for name in filenames:
                if not name.startswith('.') and os.path.splitext(name)[1] == py_ext:
                    fullname = os.path.join(dirpath, name)
                    self.refactor_file(fullname, write, doctests_only)

            dirnames[:] = [ dn for dn in dirnames if not dn.startswith('.') ]

    def _read_python_source(self, filename):
        """
        Do our best to decode a Python source file correctly.
        """
        try:
            f = open(filename, 'rb')
        except IOError as err:
            self.log_error("Can't open %s: %s", filename, err)
            return (None, None)

        try:
            encoding = tokenize.detect_encoding(f.readline)[0]
        finally:
            f.close()

        with _open_with_encoding(filename, 'r', encoding=encoding) as f:
            return (_from_system_newlines(f.read()), encoding)
        return

    def refactor_file(self, filename, write=False, doctests_only=False):
        """Refactors a file."""
        input, encoding = self._read_python_source(filename)
        if input is None:
            return
        else:
            input += u'\n'
            if doctests_only:
                self.log_debug('Refactoring doctests in %s', filename)
                output = self.refactor_docstring(input, filename)
                if output != input:
                    self.processed_file(output, filename, input, write, encoding)
                else:
                    self.log_debug('No doctest changes in %s', filename)
            else:
                tree = self.refactor_string(input, filename)
                if tree and tree.was_changed:
                    self.processed_file(unicode(tree)[:-1], filename, write=write, encoding=encoding)
                else:
                    self.log_debug('No changes in %s', filename)
            return

    def refactor_string(self, data, name):
        """Refactor a given input string.
        
        Args:
            data: a string holding the code to be refactored.
            name: a human-readable name for use in error/log messages.
        
        Returns:
            An AST corresponding to the refactored input stream; None if
            there were errors during the parse.
        """
        features = _detect_future_features(data)
        if 'print_function' in features:
            self.driver.grammar = pygram.python_grammar_no_print_statement
        try:
            try:
                tree = self.driver.parse_string(data)
            except Exception as err:
                self.log_error("Can't parse %s: %s: %s", name, err.__class__.__name__, err)
                return

        finally:
            self.driver.grammar = self.grammar

        tree.future_features = features
        self.log_debug('Refactoring %s', name)
        self.refactor_tree(tree, name)
        return tree

    def refactor_stdin(self, doctests_only=False):
        input = sys.stdin.read()
        if doctests_only:
            self.log_debug('Refactoring doctests in stdin')
            output = self.refactor_docstring(input, '<stdin>')
            if output != input:
                self.processed_file(output, '<stdin>', input)
            else:
                self.log_debug('No doctest changes in stdin')
        else:
            tree = self.refactor_string(input, '<stdin>')
            if tree and tree.was_changed:
                self.processed_file(unicode(tree), '<stdin>', input)
            else:
                self.log_debug('No changes in stdin')

    def refactor_tree(self, tree, name):
        """Refactors a parse tree (modifying the tree in place).
        
        For compatible patterns the bottom matcher module is
        used. Otherwise the tree is traversed node-to-node for
        matches.
        
        Args:
            tree: a pytree.Node instance representing the root of the tree
                  to be refactored.
            name: a human-readable name for this tree.
        
        Returns:
            True if the tree was modified, False otherwise.
        """
        for fixer in chain(self.pre_order, self.post_order):
            fixer.start_tree(tree, name)

        self.traverse_by(self.bmi_pre_order_heads, tree.pre_order())
        self.traverse_by(self.bmi_post_order_heads, tree.post_order())
        match_set = self.BM.run(tree.leaves())
        while any(match_set.values()):
            for fixer in self.BM.fixers:
                if fixer in match_set and match_set[fixer]:
                    match_set[fixer].sort(key=pytree.Base.depth, reverse=True)
                    if fixer.keep_line_order:
                        match_set[fixer].sort(key=pytree.Base.get_lineno)
                    for node in list(match_set[fixer]):
                        if node in match_set[fixer]:
                            match_set[fixer].remove(node)
                        try:
                            find_root(node)
                        except AssertionError:
                            continue

                        if node.fixers_applied and fixer in node.fixers_applied:
                            continue
                        results = fixer.match(node)
                        if results:
                            new = fixer.transform(node, results)
                            if new is not None:
                                node.replace(new)
                                for node in new.post_order():
                                    if not node.fixers_applied:
                                        node.fixers_applied = []
                                    node.fixers_applied.append(fixer)

                                new_matches = self.BM.run(new.leaves())
                                for fxr in new_matches:
                                    if fxr not in match_set:
                                        match_set[fxr] = []
                                    match_set[fxr].extend(new_matches[fxr])

        for fixer in chain(self.pre_order, self.post_order):
            fixer.finish_tree(tree, name)

        return tree.was_changed

    def traverse_by(self, fixers, traversal):
        """Traverse an AST, applying a set of fixers to each node.
        
        This is a helper method for refactor_tree().
        
        Args:
            fixers: a list of fixer instances.
            traversal: a generator that yields AST nodes.
        
        Returns:
            None
        """
        if not fixers:
            return
        else:
            for node in traversal:
                for fixer in fixers[node.type]:
                    results = fixer.match(node)
                    if results:
                        new = fixer.transform(node, results)
                        if new is not None:
                            node.replace(new)
                            node = new

            return

    def processed_file(self, new_text, filename, old_text=None, write=False, encoding=None):
        """
        Called when a file has been refactored, and there are changes.
        """
        self.files.append(filename)
        if old_text is None:
            old_text = self._read_python_source(filename)[0]
            if old_text is None:
                return
        equal = old_text == new_text
        self.print_output(old_text, new_text, filename, equal)
        if equal:
            self.log_debug('No changes to %s', filename)
            return
        else:
            if write:
                self.write_file(new_text, filename, old_text, encoding)
            else:
                self.log_debug('Not writing changes to %s', filename)
            return

    def write_file(self, new_text, filename, old_text, encoding=None):
        """Writes a string to a file.
        
        It first shows a unified diff between the old text and the new text, and
        then rewrites the file; the latter is only done if the write option is
        set.
        """
        try:
            f = _open_with_encoding(filename, 'w', encoding=encoding)
        except os.error as err:
            self.log_error("Can't create %s: %s", filename, err)
            return

        try:
            try:
                f.write(_to_system_newlines(new_text))
            except os.error as err:
                self.log_error("Can't write %s: %s", filename, err)

        finally:
            f.close()

        self.log_debug('Wrote changes to %s', filename)
        self.wrote = True

    PS1 = '>>> '
    PS2 = '... '

    def refactor_docstring(self, input, filename):
        """Refactors a docstring, looking for doctests.
        
        This returns a modified version of the input string.  It looks
        for doctests, which start with a ">>>" prompt, and may be
        continued with "..." prompts, as long as the "..." is indented
        the same as the ">>>".
        
        (Unfortunately we can't use the doctest module's parser,
        since, like most parsers, it is not geared towards preserving
        the original source.)
        """
        result = []
        block = None
        block_lineno = None
        indent = None
        lineno = 0
        for line in input.splitlines(True):
            lineno += 1
            if line.lstrip().startswith(self.PS1):
                if block is not None:
                    result.extend(self.refactor_doctest(block, block_lineno, indent, filename))
                block_lineno = lineno
                block = [line]
                i = line.find(self.PS1)
                indent = line[:i]
            elif indent is not None and (line.startswith(indent + self.PS2) or line == indent + self.PS2.rstrip() + u'\n'):
                block.append(line)
            else:
                if block is not None:
                    result.extend(self.refactor_doctest(block, block_lineno, indent, filename))
                block = None
                indent = None
                result.append(line)

        if block is not None:
            result.extend(self.refactor_doctest(block, block_lineno, indent, filename))
        return u''.join(result)

    def refactor_doctest(self, block, lineno, indent, filename):
        """Refactors one doctest.
        
        A doctest is given as a block of lines, the first of which starts
        with ">>>" (possibly indented), while the remaining lines start
        with "..." (identically indented).
        
        """
        try:
            tree = self.parse_block(block, lineno, indent)
        except Exception as err:
            if self.logger.isEnabledFor(logging.DEBUG):
                for line in block:
                    self.log_debug('Source: %s', line.rstrip(u'\n'))

            self.log_error("Can't parse docstring in %s line %s: %s: %s", filename, lineno, err.__class__.__name__, err)
            return block

        if self.refactor_tree(tree, filename):
            new = unicode(tree).splitlines(True)
            clipped, new = new[:lineno - 1], new[lineno - 1:]
            if not new[-1].endswith(u'\n'):
                new[-1] += u'\n'
            block = [
             indent + self.PS1 + new.pop(0)]
            if new:
                block += [ indent + self.PS2 + line for line in new ]
        return block

    def summarize(self):
        if self.wrote:
            were = 'were'
        else:
            were = 'need to be'
        if not self.files:
            self.log_message('No files %s modified.', were)
        else:
            self.log_message('Files that %s modified:', were)
            for file in self.files:
                self.log_message(file)

        if self.fixer_log:
            self.log_message('Warnings/messages while refactoring:')
            for message in self.fixer_log:
                self.log_message(message)

        if self.errors:
            if len(self.errors) == 1:
                self.log_message('There was 1 error:')
            else:
                self.log_message('There were %d errors:', len(self.errors))
            for msg, args, kwds in self.errors:
                self.log_message(msg, *args, **kwds)

    def parse_block(self, block, lineno, indent):
        """Parses a block into a tree.
        
        This is necessary to get correct line number / offset information
        in the parser diagnostics and embedded into the parse tree.
        """
        tree = self.driver.parse_tokens(self.wrap_toks(block, lineno, indent))
        tree.future_features = frozenset()
        return tree

    def wrap_toks(self, block, lineno, indent):
        """Wraps a tokenize stream to systematically modify start/end."""
        tokens = tokenize.generate_tokens(self.gen_lines(block, indent).next)
        for type, value, (line0, col0), (line1, col1), line_text in tokens:
            line0 += lineno - 1
            line1 += lineno - 1
            yield (
             type, value, (line0, col0), (line1, col1), line_text)

    def gen_lines(self, block, indent):
        """Generates lines as expected by tokenize from a list of lines.
        
        This strips the first len(indent + self.PS1) characters off each line.
        """
        prefix1 = indent + self.PS1
        prefix2 = indent + self.PS2
        prefix = prefix1
        for line in block:
            if line.startswith(prefix):
                yield line[len(prefix):]
            elif line == prefix.rstrip() + u'\n':
                yield u'\n'
            else:
                raise AssertionError('line=%r, prefix=%r' % (line, prefix))
            prefix = prefix2

        while True:
            yield ''


class MultiprocessingUnsupported(Exception):
    pass


class MultiprocessRefactoringTool(RefactoringTool):

    def __init__(self, *args, **kwargs):
        super(MultiprocessRefactoringTool, self).__init__(*args, **kwargs)
        self.queue = None
        self.output_lock = None
        return

    def refactor(self, items, write=False, doctests_only=False, num_processes=1):
        if num_processes == 1:
            return super(MultiprocessRefactoringTool, self).refactor(items, write, doctests_only)
        else:
            try:
                import multiprocessing
            except ImportError:
                raise MultiprocessingUnsupported

            if self.queue is not None:
                raise RuntimeError('already doing multiple processes')
            self.queue = multiprocessing.JoinableQueue()
            self.output_lock = multiprocessing.Lock()
            processes = [ multiprocessing.Process(target=self._child) for i in xrange(num_processes)
                        ]
            try:
                for p in processes:
                    p.start()

                super(MultiprocessRefactoringTool, self).refactor(items, write, doctests_only)
            finally:
                self.queue.join()
                for i in xrange(num_processes):
                    self.queue.put(None)

                for p in processes:
                    if p.is_alive():
                        p.join()

                self.queue = None

            return

    def _child(self):
        task = self.queue.get()
        while task is not None:
            args, kwargs = task
            try:
                super(MultiprocessRefactoringTool, self).refactor_file(*args, **kwargs)
            finally:
                self.queue.task_done()

            task = self.queue.get()

        return

    def refactor_file(self, *args, **kwargs):
        if self.queue is not None:
            self.queue.put((args, kwargs))
        else:
            return super(MultiprocessRefactoringTool, self).refactor_file(*args, **kwargs)
        return