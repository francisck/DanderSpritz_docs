# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: argparse.py
"""Command-line parsing library

This module is an optparse-inspired command-line parsing library that:

    - handles both optional and positional arguments
    - produces highly informative usage messages
    - supports parsers that dispatch to sub-parsers

The following is a simple usage example that sums integers from the
command-line and writes the result to a file::

    parser = argparse.ArgumentParser(
        description='sum the integers at the command line')
    parser.add_argument(
        'integers', metavar='int', nargs='+', type=int,
        help='an integer to be summed')
    parser.add_argument(
        '--log', default=sys.stdout, type=argparse.FileType('w'),
        help='the file where the sum should be written')
    args = parser.parse_args()
    args.log.write('%s' % sum(args.integers))
    args.log.close()

The module contains the following public classes:

    - ArgumentParser -- The main entry point for command-line parsing. As the
        example above shows, the add_argument() method is used to populate
        the parser with actions for optional and positional arguments. Then
        the parse_args() method is invoked to convert the args at the
        command-line into an object with attributes.

    - ArgumentError -- The exception raised by ArgumentParser objects when
        there are errors with the parser's actions. Errors raised while
        parsing the command-line are caught by ArgumentParser and emitted
        as command-line messages.

    - FileType -- A factory for defining types of files to be created. As the
        example above shows, instances of FileType are typically passed as
        the type= argument of add_argument() calls.

    - Action -- The base class for parser actions. Typically actions are
        selected by passing strings like 'store_true' or 'append_const' to
        the action= argument of add_argument(). However, for greater
        customization of ArgumentParser actions, subclasses of Action may
        be defined and passed as the action= argument.

    - HelpFormatter, RawDescriptionHelpFormatter, RawTextHelpFormatter,
        ArgumentDefaultsHelpFormatter -- Formatter classes which
        may be passed as the formatter_class= argument to the
        ArgumentParser constructor. HelpFormatter is the default,
        RawDescriptionHelpFormatter and RawTextHelpFormatter tell the parser
        not to change the formatting for help text, and
        ArgumentDefaultsHelpFormatter adds information about argument defaults
        to the help.

All other classes in this module are considered implementation details.
(Also note that HelpFormatter and RawDescriptionHelpFormatter are only
considered public as object names -- the API of the formatter objects is
still considered an implementation detail.)
"""
__version__ = '1.1'
__all__ = [
 'ArgumentParser',
 'ArgumentError',
 'ArgumentTypeError',
 'FileType',
 'HelpFormatter',
 'ArgumentDefaultsHelpFormatter',
 'RawDescriptionHelpFormatter',
 'RawTextHelpFormatter',
 'Namespace',
 'Action',
 'ONE_OR_MORE',
 'OPTIONAL',
 'PARSER',
 'REMAINDER',
 'SUPPRESS',
 'ZERO_OR_MORE']
import collections as _collections
import copy as _copy
import os as _os
import re as _re
import sys as _sys
import textwrap as _textwrap
from gettext import gettext as _

def _callable(obj):
    return hasattr(obj, '__call__') or hasattr(obj, '__bases__')


SUPPRESS = '==SUPPRESS=='
OPTIONAL = '?'
ZERO_OR_MORE = '*'
ONE_OR_MORE = '+'
PARSER = 'A...'
REMAINDER = '...'
_UNRECOGNIZED_ARGS_ATTR = '_unrecognized_args'

class _AttributeHolder(object):
    """Abstract base class that provides __repr__.
    
    The __repr__ method returns a string in the format::
        ClassName(attr=name, attr=name, ...)
    The attributes are determined either by a class-level attribute,
    '_kwarg_names', or by inspecting the instance __dict__.
    """

    def __repr__(self):
        type_name = type(self).__name__
        arg_strings = []
        for arg in self._get_args():
            arg_strings.append(repr(arg))

        for name, value in self._get_kwargs():
            arg_strings.append('%s=%r' % (name, value))

        return '%s(%s)' % (type_name, ', '.join(arg_strings))

    def _get_kwargs(self):
        return sorted(self.__dict__.items())

    def _get_args(self):
        return []


def _ensure_value(namespace, name, value):
    if getattr(namespace, name, None) is None:
        setattr(namespace, name, value)
    return getattr(namespace, name)


class HelpFormatter(object):
    """Formatter for generating usage messages and argument help strings.
    
    Only the name of this class is considered a public API. All the methods
    provided by the class are considered an implementation detail.
    """

    def __init__(self, prog, indent_increment=2, max_help_position=24, width=None):
        if width is None:
            try:
                width = int(_os.environ['COLUMNS'])
            except (KeyError, ValueError):
                width = 80

            width -= 2
        self._prog = prog
        self._indent_increment = indent_increment
        self._max_help_position = max_help_position
        self._width = width
        self._current_indent = 0
        self._level = 0
        self._action_max_length = 0
        self._root_section = self._Section(self, None)
        self._current_section = self._root_section
        self._whitespace_matcher = _re.compile('\\s+')
        self._long_break_matcher = _re.compile('\\n\\n\\n+')
        return

    def _indent(self):
        self._current_indent += self._indent_increment
        self._level += 1

    def _dedent(self):
        self._current_indent -= self._indent_increment
        self._level -= 1

    class _Section(object):

        def __init__(self, formatter, parent, heading=None):
            self.formatter = formatter
            self.parent = parent
            self.heading = heading
            self.items = []

        def format_help(self):
            if self.parent is not None:
                self.formatter._indent()
            join = self.formatter._join_parts
            for func, args in self.items:
                func(*args)

            item_help = join([ func(*args) for func, args in self.items ])
            if self.parent is not None:
                self.formatter._dedent()
            if not item_help:
                return ''
            else:
                if self.heading is not SUPPRESS and self.heading is not None:
                    current_indent = self.formatter._current_indent
                    heading = '%*s%s:\n' % (current_indent, '', self.heading)
                else:
                    heading = ''
                return join(['\n', heading, item_help, '\n'])

    def _add_item(self, func, args):
        self._current_section.items.append((func, args))

    def start_section(self, heading):
        self._indent()
        section = self._Section(self, self._current_section, heading)
        self._add_item(section.format_help, [])
        self._current_section = section

    def end_section(self):
        self._current_section = self._current_section.parent
        self._dedent()

    def add_text(self, text):
        if text is not SUPPRESS and text is not None:
            self._add_item(self._format_text, [text])
        return

    def add_usage(self, usage, actions, groups, prefix=None):
        if usage is not SUPPRESS:
            args = (
             usage, actions, groups, prefix)
            self._add_item(self._format_usage, args)

    def add_argument(self, action):
        if action.help is not SUPPRESS:
            get_invocation = self._format_action_invocation
            invocations = [get_invocation(action)]
            for subaction in self._iter_indented_subactions(action):
                invocations.append(get_invocation(subaction))

            invocation_length = max([ len(s) for s in invocations ])
            action_length = invocation_length + self._current_indent
            self._action_max_length = max(self._action_max_length, action_length)
            self._add_item(self._format_action, [action])

    def add_arguments(self, actions):
        for action in actions:
            self.add_argument(action)

    def format_help(self):
        help = self._root_section.format_help()
        if help:
            help = self._long_break_matcher.sub('\n\n', help)
            help = help.strip('\n') + '\n'
        return help

    def _join_parts(self, part_strings):
        return ''.join([ part for part in part_strings if part and part is not SUPPRESS
                       ])

    def _format_usage(self, usage, actions, groups, prefix):
        if prefix is None:
            prefix = _('usage: ')
        if usage is not None:
            usage = usage % dict(prog=self._prog)
        elif usage is None and not actions:
            usage = '%(prog)s' % dict(prog=self._prog)
        elif usage is None:
            prog = '%(prog)s' % dict(prog=self._prog)
            optionals = []
            positionals = []
            for action in actions:
                if action.option_strings:
                    optionals.append(action)
                else:
                    positionals.append(action)

            format = self._format_actions_usage
            action_usage = format(optionals + positionals, groups)
            usage = ' '.join([ s for s in [prog, action_usage] if s ])
            text_width = self._width - self._current_indent
            if len(prefix) + len(usage) > text_width:
                part_regexp = '\\(.*?\\)+|\\[.*?\\]+|\\S+'
                opt_usage = format(optionals, groups)
                pos_usage = format(positionals, groups)
                opt_parts = _re.findall(part_regexp, opt_usage)
                pos_parts = _re.findall(part_regexp, pos_usage)

                def get_lines(parts, indent, prefix=None):
                    lines = []
                    line = []
                    if prefix is not None:
                        line_len = len(prefix) - 1
                    else:
                        line_len = len(indent) - 1
                    for part in parts:
                        if line_len + 1 + len(part) > text_width:
                            lines.append(indent + ' '.join(line))
                            line = []
                            line_len = len(indent) - 1
                        line.append(part)
                        line_len += len(part) + 1

                    if line:
                        lines.append(indent + ' '.join(line))
                    if prefix is not None:
                        lines[0] = lines[0][len(indent):]
                    return lines

                if len(prefix) + len(prog) <= 0.75 * text_width:
                    indent = ' ' * (len(prefix) + len(prog) + 1)
                    if opt_parts:
                        lines = get_lines([prog] + opt_parts, indent, prefix)
                        lines.extend(get_lines(pos_parts, indent))
                    elif pos_parts:
                        lines = get_lines([prog] + pos_parts, indent, prefix)
                    else:
                        lines = [
                         prog]
                else:
                    indent = ' ' * len(prefix)
                    parts = opt_parts + pos_parts
                    lines = get_lines(parts, indent)
                    if len(lines) > 1:
                        lines = []
                        lines.extend(get_lines(opt_parts, indent))
                        lines.extend(get_lines(pos_parts, indent))
                    lines = [
                     prog] + lines
                usage = '\n'.join(lines)
        return '%s%s\n\n' % (prefix, usage)

    def _format_actions_usage(self, actions, groups):
        group_actions = set()
        inserts = {}
        for group in groups:
            try:
                start = actions.index(group._group_actions[0])
            except ValueError:
                continue
            else:
                end = start + len(group._group_actions)
                if actions[start:end] == group._group_actions:
                    for action in group._group_actions:
                        group_actions.add(action)

                    if not group.required:
                        if start in inserts:
                            inserts[start] += ' ['
                        else:
                            inserts[start] = '['
                        inserts[end] = ']'
                    else:
                        if start in inserts:
                            inserts[start] += ' ('
                        else:
                            inserts[start] = '('
                        inserts[end] = ')'
                    for i in range(start + 1, end):
                        inserts[i] = '|'

        parts = []
        for i, action in enumerate(actions):
            if action.help is SUPPRESS:
                parts.append(None)
                if inserts.get(i) == '|':
                    inserts.pop(i)
                elif inserts.get(i + 1) == '|':
                    inserts.pop(i + 1)
            elif not action.option_strings:
                part = self._format_args(action, action.dest)
                if action in group_actions:
                    if part[0] == '[' and part[-1] == ']':
                        part = part[1:-1]
                parts.append(part)
            else:
                option_string = action.option_strings[0]
                if action.nargs == 0:
                    part = '%s' % option_string
                else:
                    default = action.dest.upper()
                    args_string = self._format_args(action, default)
                    part = '%s %s' % (option_string, args_string)
                if not action.required and action not in group_actions:
                    part = '[%s]' % part
                parts.append(part)

        for i in sorted(inserts, reverse=True):
            parts[i:i] = [
             inserts[i]]

        text = ' '.join([ item for item in parts if item is not None ])
        open = '[\\[(]'
        close = '[\\])]'
        text = _re.sub('(%s) ' % open, '\\1', text)
        text = _re.sub(' (%s)' % close, '\\1', text)
        text = _re.sub('%s *%s' % (open, close), '', text)
        text = _re.sub('\\(([^|]*)\\)', '\\1', text)
        text = text.strip()
        return text

    def _format_text(self, text):
        if '%(prog)' in text:
            text = text % dict(prog=self._prog)
        text_width = self._width - self._current_indent
        indent = ' ' * self._current_indent
        return self._fill_text(text, text_width, indent) + '\n\n'

    def _format_action(self, action):
        help_position = min(self._action_max_length + 2, self._max_help_position)
        help_width = self._width - help_position
        action_width = help_position - self._current_indent - 2
        action_header = self._format_action_invocation(action)
        if not action.help:
            tup = (
             self._current_indent, '', action_header)
            action_header = '%*s%s\n' % tup
        elif len(action_header) <= action_width:
            tup = (
             self._current_indent, '', action_width, action_header)
            action_header = '%*s%-*s  ' % tup
            indent_first = 0
        else:
            tup = (self._current_indent, '', action_header)
            action_header = '%*s%s\n' % tup
            indent_first = help_position
        parts = [
         action_header]
        if action.help:
            help_text = self._expand_help(action)
            help_lines = self._split_lines(help_text, help_width)
            parts.append('%*s%s\n' % (indent_first, '', help_lines[0]))
            for line in help_lines[1:]:
                parts.append('%*s%s\n' % (help_position, '', line))

        elif not action_header.endswith('\n'):
            parts.append('\n')
        for subaction in self._iter_indented_subactions(action):
            parts.append(self._format_action(subaction))

        return self._join_parts(parts)

    def _format_action_invocation(self, action):
        if not action.option_strings:
            metavar, = self._metavar_formatter(action, action.dest)(1)
            return metavar
        else:
            parts = []
            if action.nargs == 0:
                parts.extend(action.option_strings)
            else:
                default = action.dest.upper()
                args_string = self._format_args(action, default)
                for option_string in action.option_strings:
                    parts.append('%s %s' % (option_string, args_string))

            return ', '.join(parts)

    def _metavar_formatter(self, action, default_metavar):
        if action.metavar is not None:
            result = action.metavar
        elif action.choices is not None:
            choice_strs = [ str(choice) for choice in action.choices ]
            result = '{%s}' % ','.join(choice_strs)
        else:
            result = default_metavar

        def format(tuple_size):
            if isinstance(result, tuple):
                return result
            else:
                return (
                 result,) * tuple_size

        return format

    def _format_args(self, action, default_metavar):
        get_metavar = self._metavar_formatter(action, default_metavar)
        if action.nargs is None:
            result = '%s' % get_metavar(1)
        elif action.nargs == OPTIONAL:
            result = '[%s]' % get_metavar(1)
        elif action.nargs == ZERO_OR_MORE:
            result = '[%s [%s ...]]' % get_metavar(2)
        elif action.nargs == ONE_OR_MORE:
            result = '%s [%s ...]' % get_metavar(2)
        elif action.nargs == REMAINDER:
            result = '...'
        elif action.nargs == PARSER:
            result = '%s ...' % get_metavar(1)
        else:
            formats = [ '%s' for _ in range(action.nargs) ]
            result = ' '.join(formats) % get_metavar(action.nargs)
        return result

    def _expand_help(self, action):
        params = dict(vars(action), prog=self._prog)
        for name in list(params):
            if params[name] is SUPPRESS:
                del params[name]

        for name in list(params):
            if hasattr(params[name], '__name__'):
                params[name] = params[name].__name__

        if params.get('choices') is not None:
            choices_str = ', '.join([ str(c) for c in params['choices'] ])
            params['choices'] = choices_str
        return self._get_help_string(action) % params

    def _iter_indented_subactions(self, action):
        try:
            get_subactions = action._get_subactions
        except AttributeError:
            pass
        else:
            self._indent()
            for subaction in get_subactions():
                yield subaction

            self._dedent()

    def _split_lines(self, text, width):
        text = self._whitespace_matcher.sub(' ', text).strip()
        return _textwrap.wrap(text, width)

    def _fill_text(self, text, width, indent):
        text = self._whitespace_matcher.sub(' ', text).strip()
        return _textwrap.fill(text, width, initial_indent=indent, subsequent_indent=indent)

    def _get_help_string(self, action):
        return action.help


class RawDescriptionHelpFormatter(HelpFormatter):
    """Help message formatter which retains any formatting in descriptions.
    
    Only the name of this class is considered a public API. All the methods
    provided by the class are considered an implementation detail.
    """

    def _fill_text(self, text, width, indent):
        return ''.join([ indent + line for line in text.splitlines(True) ])


class RawTextHelpFormatter(RawDescriptionHelpFormatter):
    """Help message formatter which retains formatting of all help text.
    
    Only the name of this class is considered a public API. All the methods
    provided by the class are considered an implementation detail.
    """

    def _split_lines(self, text, width):
        return text.splitlines()


class ArgumentDefaultsHelpFormatter(HelpFormatter):
    """Help message formatter which adds default values to argument help.
    
    Only the name of this class is considered a public API. All the methods
    provided by the class are considered an implementation detail.
    """

    def _get_help_string(self, action):
        help = action.help
        if '%(default)' not in action.help:
            if action.default is not SUPPRESS:
                defaulting_nargs = [
                 OPTIONAL, ZERO_OR_MORE]
                if action.option_strings or action.nargs in defaulting_nargs:
                    help += ' (default: %(default)s)'
        return help


def _get_action_name(argument):
    if argument is None:
        return
    else:
        if argument.option_strings:
            return '/'.join(argument.option_strings)
        if argument.metavar not in (None, SUPPRESS):
            return argument.metavar
        if argument.dest not in (None, SUPPRESS):
            return argument.dest
        return
        return


class ArgumentError(Exception):
    """An error from creating or using an argument (optional or positional).
    
    The string value of this exception is the message, augmented with
    information about the argument that caused it.
    """

    def __init__(self, argument, message):
        self.argument_name = _get_action_name(argument)
        self.message = message

    def __str__(self):
        if self.argument_name is None:
            format = '%(message)s'
        else:
            format = 'argument %(argument_name)s: %(message)s'
        return format % dict(message=self.message, argument_name=self.argument_name)


class ArgumentTypeError(Exception):
    """An error from trying to convert a command line string to a type."""
    pass


class Action(_AttributeHolder):
    """Information about how to convert command line strings to Python objects.
    
    Action objects are used by an ArgumentParser to represent the information
    needed to parse a single argument from one or more strings from the
    command line. The keyword arguments to the Action constructor are also
    all attributes of Action instances.
    
    Keyword Arguments:
    
        - option_strings -- A list of command-line option strings which
            should be associated with this action.
    
        - dest -- The name of the attribute to hold the created object(s)
    
        - nargs -- The number of command-line arguments that should be
            consumed. By default, one argument will be consumed and a single
            value will be produced.  Other values include:
                - N (an integer) consumes N arguments (and produces a list)
                - '?' consumes zero or one arguments
                - '*' consumes zero or more arguments (and produces a list)
                - '+' consumes one or more arguments (and produces a list)
            Note that the difference between the default and nargs=1 is that
            with the default, a single value will be produced, while with
            nargs=1, a list containing a single value will be produced.
    
        - const -- The value to be produced if the option is specified and the
            option uses an action that takes no values.
    
        - default -- The value to be produced if the option is not specified.
    
        - type -- The type which the command-line arguments should be converted
            to, should be one of 'string', 'int', 'float', 'complex' or a
            callable object that accepts a single string argument. If None,
            'string' is assumed.
    
        - choices -- A container of values that should be allowed. If not None,
            after a command-line argument has been converted to the appropriate
            type, an exception will be raised if it is not a member of this
            collection.
    
        - required -- True if the action must always be specified at the
            command line. This is only meaningful for optional command-line
            arguments.
    
        - help -- The help string describing the argument.
    
        - metavar -- The name to be used for the option's argument with the
            help string. If None, the 'dest' value will be used as the name.
    """

    def __init__(self, option_strings, dest, nargs=None, const=None, default=None, type=None, choices=None, required=False, help=None, metavar=None):
        self.option_strings = option_strings
        self.dest = dest
        self.nargs = nargs
        self.const = const
        self.default = default
        self.type = type
        self.choices = choices
        self.required = required
        self.help = help
        self.metavar = metavar

    def _get_kwargs(self):
        names = [
         'option_strings',
         'dest',
         'nargs',
         'const',
         'default',
         'type',
         'choices',
         'help',
         'metavar']
        return [ (name, getattr(self, name)) for name in names ]

    def __call__(self, parser, namespace, values, option_string=None):
        raise NotImplementedError(_('.__call__() not defined'))


class _StoreAction(Action):

    def __init__(self, option_strings, dest, nargs=None, const=None, default=None, type=None, choices=None, required=False, help=None, metavar=None):
        if nargs == 0:
            raise ValueError('nargs for store actions must be > 0; if you have nothing to store, actions such as store true or store const may be more appropriate')
        if const is not None and nargs != OPTIONAL:
            raise ValueError('nargs must be %r to supply const' % OPTIONAL)
        super(_StoreAction, self).__init__(option_strings=option_strings, dest=dest, nargs=nargs, const=const, default=default, type=type, choices=choices, required=required, help=help, metavar=metavar)
        return

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values)


class _StoreConstAction(Action):

    def __init__(self, option_strings, dest, const, default=None, required=False, help=None, metavar=None):
        super(_StoreConstAction, self).__init__(option_strings=option_strings, dest=dest, nargs=0, const=const, default=default, required=required, help=help)

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, self.const)


class _StoreTrueAction(_StoreConstAction):

    def __init__(self, option_strings, dest, default=False, required=False, help=None):
        super(_StoreTrueAction, self).__init__(option_strings=option_strings, dest=dest, const=True, default=default, required=required, help=help)


class _StoreFalseAction(_StoreConstAction):

    def __init__(self, option_strings, dest, default=True, required=False, help=None):
        super(_StoreFalseAction, self).__init__(option_strings=option_strings, dest=dest, const=False, default=default, required=required, help=help)


class _AppendAction(Action):

    def __init__(self, option_strings, dest, nargs=None, const=None, default=None, type=None, choices=None, required=False, help=None, metavar=None):
        if nargs == 0:
            raise ValueError('nargs for append actions must be > 0; if arg strings are not supplying the value to append, the append const action may be more appropriate')
        if const is not None and nargs != OPTIONAL:
            raise ValueError('nargs must be %r to supply const' % OPTIONAL)
        super(_AppendAction, self).__init__(option_strings=option_strings, dest=dest, nargs=nargs, const=const, default=default, type=type, choices=choices, required=required, help=help, metavar=metavar)
        return

    def __call__(self, parser, namespace, values, option_string=None):
        items = _copy.copy(_ensure_value(namespace, self.dest, []))
        items.append(values)
        setattr(namespace, self.dest, items)


class _AppendConstAction(Action):

    def __init__(self, option_strings, dest, const, default=None, required=False, help=None, metavar=None):
        super(_AppendConstAction, self).__init__(option_strings=option_strings, dest=dest, nargs=0, const=const, default=default, required=required, help=help, metavar=metavar)

    def __call__(self, parser, namespace, values, option_string=None):
        items = _copy.copy(_ensure_value(namespace, self.dest, []))
        items.append(self.const)
        setattr(namespace, self.dest, items)


class _CountAction(Action):

    def __init__(self, option_strings, dest, default=None, required=False, help=None):
        super(_CountAction, self).__init__(option_strings=option_strings, dest=dest, nargs=0, default=default, required=required, help=help)

    def __call__(self, parser, namespace, values, option_string=None):
        new_count = _ensure_value(namespace, self.dest, 0) + 1
        setattr(namespace, self.dest, new_count)


class _HelpAction(Action):

    def __init__(self, option_strings, dest=SUPPRESS, default=SUPPRESS, help=None):
        super(_HelpAction, self).__init__(option_strings=option_strings, dest=dest, default=default, nargs=0, help=help)

    def __call__(self, parser, namespace, values, option_string=None):
        parser.print_help()
        parser.exit()


class _VersionAction(Action):

    def __init__(self, option_strings, version=None, dest=SUPPRESS, default=SUPPRESS, help="show program's version number and exit"):
        super(_VersionAction, self).__init__(option_strings=option_strings, dest=dest, default=default, nargs=0, help=help)
        self.version = version

    def __call__(self, parser, namespace, values, option_string=None):
        version = self.version
        if version is None:
            version = parser.version
        formatter = parser._get_formatter()
        formatter.add_text(version)
        parser.exit(message=formatter.format_help())
        return


class _SubParsersAction(Action):

    class _ChoicesPseudoAction(Action):

        def __init__(self, name, help):
            sup = super(_SubParsersAction._ChoicesPseudoAction, self)
            sup.__init__(option_strings=[], dest=name, help=help)

    def __init__(self, option_strings, prog, parser_class, dest=SUPPRESS, help=None, metavar=None):
        self._prog_prefix = prog
        self._parser_class = parser_class
        self._name_parser_map = _collections.OrderedDict()
        self._choices_actions = []
        super(_SubParsersAction, self).__init__(option_strings=option_strings, dest=dest, nargs=PARSER, choices=self._name_parser_map, help=help, metavar=metavar)

    def add_parser(self, name, **kwargs):
        if kwargs.get('prog') is None:
            kwargs['prog'] = '%s %s' % (self._prog_prefix, name)
        if 'help' in kwargs:
            help = kwargs.pop('help')
            choice_action = self._ChoicesPseudoAction(name, help)
            self._choices_actions.append(choice_action)
        parser = self._parser_class(**kwargs)
        self._name_parser_map[name] = parser
        return parser

    def _get_subactions(self):
        return self._choices_actions

    def __call__(self, parser, namespace, values, option_string=None):
        parser_name = values[0]
        arg_strings = values[1:]
        if self.dest is not SUPPRESS:
            setattr(namespace, self.dest, parser_name)
        try:
            parser = self._name_parser_map[parser_name]
        except KeyError:
            tup = (
             parser_name, ', '.join(self._name_parser_map))
            msg = _('unknown parser %r (choices: %s)') % tup
            raise ArgumentError(self, msg)

        namespace, arg_strings = parser.parse_known_args(arg_strings, namespace)
        if arg_strings:
            vars(namespace).setdefault(_UNRECOGNIZED_ARGS_ATTR, [])
            getattr(namespace, _UNRECOGNIZED_ARGS_ATTR).extend(arg_strings)


class FileType(object):
    """Factory for creating file object types
    
    Instances of FileType are typically passed as type= arguments to the
    ArgumentParser add_argument() method.
    
    Keyword Arguments:
        - mode -- A string indicating how the file is to be opened. Accepts the
            same values as the builtin open() function.
        - bufsize -- The file's desired buffer size. Accepts the same values as
            the builtin open() function.
    """

    def __init__(self, mode='r', bufsize=-1):
        self._mode = mode
        self._bufsize = bufsize

    def __call__(self, string):
        if string == '-':
            if 'r' in self._mode:
                return _sys.stdin
            if 'w' in self._mode:
                return _sys.stdout
            msg = _('argument "-" with mode %r') % self._mode
            raise ValueError(msg)
        try:
            return open(string, self._mode, self._bufsize)
        except IOError as e:
            message = _("can't open '%s': %s")
            raise ArgumentTypeError(message % (string, e))

    def __repr__(self):
        args = (self._mode, self._bufsize)
        args_str = ', '.join((repr(arg) for arg in args if arg != -1))
        return '%s(%s)' % (type(self).__name__, args_str)


class Namespace(_AttributeHolder):
    """Simple object for storing attributes.
    
    Implements equality by attribute names and values, and provides a simple
    string representation.
    """

    def __init__(self, **kwargs):
        for name in kwargs:
            setattr(self, name, kwargs[name])

    __hash__ = None

    def __eq__(self, other):
        return vars(self) == vars(other)

    def __ne__(self, other):
        return not self == other

    def __contains__(self, key):
        return key in self.__dict__


class _ActionsContainer(object):

    def __init__(self, description, prefix_chars, argument_default, conflict_handler):
        super(_ActionsContainer, self).__init__()
        self.description = description
        self.argument_default = argument_default
        self.prefix_chars = prefix_chars
        self.conflict_handler = conflict_handler
        self._registries = {}
        self.register('action', None, _StoreAction)
        self.register('action', 'store', _StoreAction)
        self.register('action', 'store_const', _StoreConstAction)
        self.register('action', 'store_true', _StoreTrueAction)
        self.register('action', 'store_false', _StoreFalseAction)
        self.register('action', 'append', _AppendAction)
        self.register('action', 'append_const', _AppendConstAction)
        self.register('action', 'count', _CountAction)
        self.register('action', 'help', _HelpAction)
        self.register('action', 'version', _VersionAction)
        self.register('action', 'parsers', _SubParsersAction)
        self._get_handler()
        self._actions = []
        self._option_string_actions = {}
        self._action_groups = []
        self._mutually_exclusive_groups = []
        self._defaults = {}
        self._negative_number_matcher = _re.compile('^-\\d+$|^-\\d*\\.\\d+$')
        self._has_negative_number_optionals = []
        return

    def register(self, registry_name, value, object):
        registry = self._registries.setdefault(registry_name, {})
        registry[value] = object

    def _registry_get(self, registry_name, value, default=None):
        return self._registries[registry_name].get(value, default)

    def set_defaults(self, **kwargs):
        self._defaults.update(kwargs)
        for action in self._actions:
            if action.dest in kwargs:
                action.default = kwargs[action.dest]

    def get_default(self, dest):
        for action in self._actions:
            if action.dest == dest and action.default is not None:
                return action.default

        return self._defaults.get(dest, None)

    def add_argument(self, *args, **kwargs):
        """
        add_argument(dest, ..., name=value, ...)
        add_argument(option_string, option_string, ..., name=value, ...)
        """
        chars = self.prefix_chars
        if not args or len(args) == 1 and args[0][0] not in chars:
            if args and 'dest' in kwargs:
                raise ValueError('dest supplied twice for positional argument')
            kwargs = self._get_positional_kwargs(*args, **kwargs)
        else:
            kwargs = self._get_optional_kwargs(*args, **kwargs)
        if 'default' not in kwargs:
            dest = kwargs['dest']
            if dest in self._defaults:
                kwargs['default'] = self._defaults[dest]
            elif self.argument_default is not None:
                kwargs['default'] = self.argument_default
        action_class = self._pop_action_class(kwargs)
        if not _callable(action_class):
            raise ValueError('unknown action "%s"' % (action_class,))
        action = action_class(**kwargs)
        type_func = self._registry_get('type', action.type, action.type)
        if not _callable(type_func):
            raise ValueError('%r is not callable' % (type_func,))
        if hasattr(self, '_get_formatter'):
            try:
                self._get_formatter()._format_args(action, None)
            except TypeError:
                raise ValueError('length of metavar tuple does not match nargs')

        return self._add_action(action)

    def add_argument_group(self, *args, **kwargs):
        group = _ArgumentGroup(self, *args, **kwargs)
        self._action_groups.append(group)
        return group

    def add_mutually_exclusive_group(self, **kwargs):
        group = _MutuallyExclusiveGroup(self, **kwargs)
        self._mutually_exclusive_groups.append(group)
        return group

    def _add_action(self, action):
        self._check_conflict(action)
        self._actions.append(action)
        action.container = self
        for option_string in action.option_strings:
            self._option_string_actions[option_string] = action

        for option_string in action.option_strings:
            if self._negative_number_matcher.match(option_string):
                if not self._has_negative_number_optionals:
                    self._has_negative_number_optionals.append(True)

        return action

    def _remove_action(self, action):
        self._actions.remove(action)

    def _add_container_actions(self, container):
        title_group_map = {}
        for group in self._action_groups:
            if group.title in title_group_map:
                msg = _('cannot merge actions - two groups are named %r')
                raise ValueError(msg % group.title)
            title_group_map[group.title] = group

        group_map = {}
        for group in container._action_groups:
            if group.title not in title_group_map:
                title_group_map[group.title] = self.add_argument_group(title=group.title, description=group.description, conflict_handler=group.conflict_handler)
            for action in group._group_actions:
                group_map[action] = title_group_map[group.title]

        for group in container._mutually_exclusive_groups:
            mutex_group = self.add_mutually_exclusive_group(required=group.required)
            for action in group._group_actions:
                group_map[action] = mutex_group

        for action in container._actions:
            group_map.get(action, self)._add_action(action)

    def _get_positional_kwargs(self, dest, **kwargs):
        if 'required' in kwargs:
            msg = _("'required' is an invalid argument for positionals")
            raise TypeError(msg)
        if kwargs.get('nargs') not in [OPTIONAL, ZERO_OR_MORE]:
            kwargs['required'] = True
        if kwargs.get('nargs') == ZERO_OR_MORE and 'default' not in kwargs:
            kwargs['required'] = True
        return dict(kwargs, dest=dest, option_strings=[])

    def _get_optional_kwargs(self, *args, **kwargs):
        option_strings = []
        long_option_strings = []
        for option_string in args:
            if option_string[0] not in self.prefix_chars:
                msg = _('invalid option string %r: must start with a character %r')
                tup = (
                 option_string, self.prefix_chars)
                raise ValueError(msg % tup)
            option_strings.append(option_string)
            if option_string[0] in self.prefix_chars:
                if len(option_string) > 1:
                    if option_string[1] in self.prefix_chars:
                        long_option_strings.append(option_string)

        dest = kwargs.pop('dest', None)
        if dest is None:
            if long_option_strings:
                dest_option_string = long_option_strings[0]
            else:
                dest_option_string = option_strings[0]
            dest = dest_option_string.lstrip(self.prefix_chars)
            if not dest:
                msg = _('dest= is required for options like %r')
                raise ValueError(msg % option_string)
            dest = dest.replace('-', '_')
        return dict(kwargs, dest=dest, option_strings=option_strings)

    def _pop_action_class(self, kwargs, default=None):
        action = kwargs.pop('action', default)
        return self._registry_get('action', action, action)

    def _get_handler(self):
        handler_func_name = '_handle_conflict_%s' % self.conflict_handler
        try:
            return getattr(self, handler_func_name)
        except AttributeError:
            msg = _('invalid conflict_resolution value: %r')
            raise ValueError(msg % self.conflict_handler)

    def _check_conflict(self, action):
        confl_optionals = []
        for option_string in action.option_strings:
            if option_string in self._option_string_actions:
                confl_optional = self._option_string_actions[option_string]
                confl_optionals.append((option_string, confl_optional))

        if confl_optionals:
            conflict_handler = self._get_handler()
            conflict_handler(action, confl_optionals)

    def _handle_conflict_error(self, action, conflicting_actions):
        message = _('conflicting option string(s): %s')
        conflict_string = ', '.join([ option_string for option_string, action in conflicting_actions
                                    ])
        raise ArgumentError(action, message % conflict_string)

    def _handle_conflict_resolve(self, action, conflicting_actions):
        for option_string, action in conflicting_actions:
            action.option_strings.remove(option_string)
            self._option_string_actions.pop(option_string, None)
            if not action.option_strings:
                action.container._remove_action(action)

        return


class _ArgumentGroup(_ActionsContainer):

    def __init__(self, container, title=None, description=None, **kwargs):
        update = kwargs.setdefault
        update('conflict_handler', container.conflict_handler)
        update('prefix_chars', container.prefix_chars)
        update('argument_default', container.argument_default)
        super_init = super(_ArgumentGroup, self).__init__
        super_init(description=description, **kwargs)
        self.title = title
        self._group_actions = []
        self._registries = container._registries
        self._actions = container._actions
        self._option_string_actions = container._option_string_actions
        self._defaults = container._defaults
        self._has_negative_number_optionals = container._has_negative_number_optionals
        self._mutually_exclusive_groups = container._mutually_exclusive_groups

    def _add_action(self, action):
        action = super(_ArgumentGroup, self)._add_action(action)
        self._group_actions.append(action)
        return action

    def _remove_action(self, action):
        super(_ArgumentGroup, self)._remove_action(action)
        self._group_actions.remove(action)


class _MutuallyExclusiveGroup(_ArgumentGroup):

    def __init__(self, container, required=False):
        super(_MutuallyExclusiveGroup, self).__init__(container)
        self.required = required
        self._container = container

    def _add_action(self, action):
        if action.required:
            msg = _('mutually exclusive arguments must be optional')
            raise ValueError(msg)
        action = self._container._add_action(action)
        self._group_actions.append(action)
        return action

    def _remove_action(self, action):
        self._container._remove_action(action)
        self._group_actions.remove(action)


class ArgumentParser(_AttributeHolder, _ActionsContainer):
    """Object for parsing command line strings into Python objects.
    
    Keyword Arguments:
        - prog -- The name of the program (default: sys.argv[0])
        - usage -- A usage message (default: auto-generated from arguments)
        - description -- A description of what the program does
        - epilog -- Text following the argument descriptions
        - parents -- Parsers whose arguments should be copied into this one
        - formatter_class -- HelpFormatter class for printing help messages
        - prefix_chars -- Characters that prefix optional arguments
        - fromfile_prefix_chars -- Characters that prefix files containing
            additional arguments
        - argument_default -- The default value for all arguments
        - conflict_handler -- String indicating how to handle conflicts
        - add_help -- Add a -h/-help option
    """

    def __init__(self, prog=None, usage=None, description=None, epilog=None, version=None, parents=[], formatter_class=HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True):
        if version is not None:
            import warnings
            warnings.warn('The "version" argument to ArgumentParser is deprecated. Please use "add_argument(..., action=\'version\', version="N", ...)" instead', DeprecationWarning)
        superinit = super(ArgumentParser, self).__init__
        superinit(description=description, prefix_chars=prefix_chars, argument_default=argument_default, conflict_handler=conflict_handler)
        if prog is None:
            prog = _os.path.basename(_sys.argv[0])
        self.prog = prog
        self.usage = usage
        self.epilog = epilog
        self.version = version
        self.formatter_class = formatter_class
        self.fromfile_prefix_chars = fromfile_prefix_chars
        self.add_help = add_help
        add_group = self.add_argument_group
        self._positionals = add_group(_('positional arguments'))
        self._optionals = add_group(_('optional arguments'))
        self._subparsers = None

        def identity(string):
            return string

        self.register('type', None, identity)
        default_prefix = '-' if '-' in prefix_chars else prefix_chars[0]
        if self.add_help:
            self.add_argument(default_prefix + 'h', default_prefix * 2 + 'help', action='help', default=SUPPRESS, help=_('show this help message and exit'))
        if self.version:
            self.add_argument(default_prefix + 'v', default_prefix * 2 + 'version', action='version', default=SUPPRESS, version=self.version, help=_("show program's version number and exit"))
        for parent in parents:
            self._add_container_actions(parent)
            try:
                defaults = parent._defaults
            except AttributeError:
                pass
            else:
                self._defaults.update(defaults)

        return

    def _get_kwargs(self):
        names = [
         'prog',
         'usage',
         'description',
         'version',
         'formatter_class',
         'conflict_handler',
         'add_help']
        return [ (name, getattr(self, name)) for name in names ]

    def add_subparsers(self, **kwargs):
        if self._subparsers is not None:
            self.error(_('cannot have multiple subparser arguments'))
        kwargs.setdefault('parser_class', type(self))
        if 'title' in kwargs or 'description' in kwargs:
            title = _(kwargs.pop('title', 'subcommands'))
            description = _(kwargs.pop('description', None))
            self._subparsers = self.add_argument_group(title, description)
        else:
            self._subparsers = self._positionals
        if kwargs.get('prog') is None:
            formatter = self._get_formatter()
            positionals = self._get_positional_actions()
            groups = self._mutually_exclusive_groups
            formatter.add_usage(self.usage, positionals, groups, '')
            kwargs['prog'] = formatter.format_help().strip()
        parsers_class = self._pop_action_class(kwargs, 'parsers')
        action = parsers_class(option_strings=[], **kwargs)
        self._subparsers._add_action(action)
        return action

    def _add_action(self, action):
        if action.option_strings:
            self._optionals._add_action(action)
        else:
            self._positionals._add_action(action)
        return action

    def _get_optional_actions(self):
        return [ action for action in self._actions if action.option_strings
               ]

    def _get_positional_actions(self):
        return [ action for action in self._actions if not action.option_strings
               ]

    def parse_args(self, args=None, namespace=None):
        args, argv = self.parse_known_args(args, namespace)
        if argv:
            msg = _('unrecognized arguments: %s')
            self.error(msg % ' '.join(argv))
        return args

    def parse_known_args(self, args=None, namespace=None):
        if args is None:
            args = _sys.argv[1:]
        if namespace is None:
            namespace = Namespace()
        for action in self._actions:
            if action.dest is not SUPPRESS:
                if not hasattr(namespace, action.dest):
                    if action.default is not SUPPRESS:
                        default = action.default
                        if isinstance(action.default, basestring):
                            default = self._get_value(action, default)
                        setattr(namespace, action.dest, default)

        for dest in self._defaults:
            if not hasattr(namespace, dest):
                setattr(namespace, dest, self._defaults[dest])

        try:
            namespace, args = self._parse_known_args(args, namespace)
            if hasattr(namespace, _UNRECOGNIZED_ARGS_ATTR):
                args.extend(getattr(namespace, _UNRECOGNIZED_ARGS_ATTR))
                delattr(namespace, _UNRECOGNIZED_ARGS_ATTR)
            return (namespace, args)
        except ArgumentError:
            err = _sys.exc_info()[1]
            self.error(str(err))

        return

    def _parse_known_args(self, arg_strings, namespace):
        if self.fromfile_prefix_chars is not None:
            arg_strings = self._read_args_from_files(arg_strings)
        action_conflicts = {}
        for mutex_group in self._mutually_exclusive_groups:
            group_actions = mutex_group._group_actions
            for i, mutex_action in enumerate(mutex_group._group_actions):
                conflicts = action_conflicts.setdefault(mutex_action, [])
                conflicts.extend(group_actions[:i])
                conflicts.extend(group_actions[i + 1:])

        option_string_indices = {}
        arg_string_pattern_parts = []
        arg_strings_iter = iter(arg_strings)
        for i, arg_string in enumerate(arg_strings_iter):
            if arg_string == '--':
                arg_string_pattern_parts.append('-')
                for arg_string in arg_strings_iter:
                    arg_string_pattern_parts.append('A')

            else:
                option_tuple = self._parse_optional(arg_string)
                if option_tuple is None:
                    pattern = 'A'
                else:
                    option_string_indices[i] = option_tuple
                    pattern = 'O'
                arg_string_pattern_parts.append(pattern)

        arg_strings_pattern = ''.join(arg_string_pattern_parts)
        seen_actions = set()
        seen_non_default_actions = set()

        def take_action(action, argument_strings, option_string=None):
            seen_actions.add(action)
            argument_values = self._get_values(action, argument_strings)
            if argument_values is not action.default:
                seen_non_default_actions.add(action)
                for conflict_action in action_conflicts.get(action, []):
                    if conflict_action in seen_non_default_actions:
                        msg = _('not allowed with argument %s')
                        action_name = _get_action_name(conflict_action)
                        raise ArgumentError(action, msg % action_name)

            if argument_values is not SUPPRESS:
                action(self, namespace, argument_values, option_string)

        def consume_optional(start_index):
            option_tuple = option_string_indices[start_index]
            action, option_string, explicit_arg = option_tuple
            match_argument = self._match_argument
            action_tuples = []
            while True:
                if action is None:
                    extras.append(arg_strings[start_index])
                    return start_index + 1
                if explicit_arg is not None:
                    arg_count = match_argument(action, 'A')
                    chars = self.prefix_chars
                    if arg_count == 0 and option_string[1] not in chars:
                        action_tuples.append((action, [], option_string))
                        char = option_string[0]
                        option_string = char + explicit_arg[0]
                        new_explicit_arg = explicit_arg[1:] or None
                        optionals_map = self._option_string_actions
                        if option_string in optionals_map:
                            action = optionals_map[option_string]
                            explicit_arg = new_explicit_arg
                        else:
                            msg = _('ignored explicit argument %r')
                            raise ArgumentError(action, msg % explicit_arg)
                    elif arg_count == 1:
                        stop = start_index + 1
                        args = [explicit_arg]
                        action_tuples.append((action, args, option_string))
                        break
                    else:
                        msg = _('ignored explicit argument %r')
                        raise ArgumentError(action, msg % explicit_arg)
                else:
                    start = start_index + 1
                    selected_patterns = arg_strings_pattern[start:]
                    arg_count = match_argument(action, selected_patterns)
                    stop = start + arg_count
                    args = arg_strings[start:stop]
                    action_tuples.append((action, args, option_string))
                    break

            for action, args, option_string in action_tuples:
                take_action(action, args, option_string)

            return stop

        positionals = self._get_positional_actions()

        def consume_positionals(start_index):
            match_partial = self._match_arguments_partial
            selected_pattern = arg_strings_pattern[start_index:]
            arg_counts = match_partial(positionals, selected_pattern)
            for action, arg_count in zip(positionals, arg_counts):
                args = arg_strings[start_index:start_index + arg_count]
                start_index += arg_count
                take_action(action, args)

            positionals[:] = positionals[len(arg_counts):]
            return start_index

        extras = []
        start_index = 0
        if option_string_indices:
            max_option_string_index = max(option_string_indices)
        else:
            max_option_string_index = -1
        while start_index <= max_option_string_index:
            next_option_string_index = min([ index for index in option_string_indices if index >= start_index
                                           ])
            if start_index != next_option_string_index:
                positionals_end_index = consume_positionals(start_index)
                if positionals_end_index > start_index:
                    start_index = positionals_end_index
                    continue
                else:
                    start_index = positionals_end_index
            if start_index not in option_string_indices:
                strings = arg_strings[start_index:next_option_string_index]
                extras.extend(strings)
                start_index = next_option_string_index
            start_index = consume_optional(start_index)

        stop_index = consume_positionals(start_index)
        extras.extend(arg_strings[stop_index:])
        if positionals:
            self.error(_('too few arguments'))
        for action in self._actions:
            if action.required:
                if action not in seen_actions:
                    name = _get_action_name(action)
                    self.error(_('argument %s is required') % name)

        for group in self._mutually_exclusive_groups:
            if group.required:
                for action in group._group_actions:
                    if action in seen_non_default_actions:
                        break
                else:
                    names = [ _get_action_name(action) for action in group._group_actions if action.help is not SUPPRESS ]
                    msg = _('one of the arguments %s is required')
                    self.error(msg % ' '.join(names))

        return (namespace, extras)

    def _read_args_from_files(self, arg_strings):
        new_arg_strings = []
        for arg_string in arg_strings:
            if arg_string[0] not in self.fromfile_prefix_chars:
                new_arg_strings.append(arg_string)
            else:
                try:
                    args_file = open(arg_string[1:])
                    try:
                        arg_strings = []
                        for arg_line in args_file.read().splitlines():
                            for arg in self.convert_arg_line_to_args(arg_line):
                                arg_strings.append(arg)

                        arg_strings = self._read_args_from_files(arg_strings)
                        new_arg_strings.extend(arg_strings)
                    finally:
                        args_file.close()

                except IOError:
                    err = _sys.exc_info()[1]
                    self.error(str(err))

        return new_arg_strings

    def convert_arg_line_to_args(self, arg_line):
        return [
         arg_line]

    def _match_argument(self, action, arg_strings_pattern):
        nargs_pattern = self._get_nargs_pattern(action)
        match = _re.match(nargs_pattern, arg_strings_pattern)
        if match is None:
            nargs_errors = {None: _('expected one argument'),OPTIONAL: _('expected at most one argument'),
               ONE_OR_MORE: _('expected at least one argument')
               }
            default = _('expected %s argument(s)') % action.nargs
            msg = nargs_errors.get(action.nargs, default)
            raise ArgumentError(action, msg)
        return len(match.group(1))

    def _match_arguments_partial(self, actions, arg_strings_pattern):
        result = []
        for i in range(len(actions), 0, -1):
            actions_slice = actions[:i]
            pattern = ''.join([ self._get_nargs_pattern(action) for action in actions_slice
                              ])
            match = _re.match(pattern, arg_strings_pattern)
            if match is not None:
                result.extend([ len(string) for string in match.groups() ])
                break

        return result

    def _parse_optional(self, arg_string):
        if not arg_string:
            return None
        else:
            if arg_string[0] not in self.prefix_chars:
                return None
            if arg_string in self._option_string_actions:
                action = self._option_string_actions[arg_string]
                return (
                 action, arg_string, None)
            if len(arg_string) == 1:
                return None
            if '=' in arg_string:
                option_string, explicit_arg = arg_string.split('=', 1)
                if option_string in self._option_string_actions:
                    action = self._option_string_actions[option_string]
                    return (
                     action, option_string, explicit_arg)
            option_tuples = self._get_option_tuples(arg_string)
            if len(option_tuples) > 1:
                options = ', '.join([ option_string for action, option_string, explicit_arg in option_tuples
                                    ])
                tup = (arg_string, options)
                self.error(_('ambiguous option: %s could match %s') % tup)
            elif len(option_tuples) == 1:
                option_tuple, = option_tuples
                return option_tuple
            if self._negative_number_matcher.match(arg_string):
                if not self._has_negative_number_optionals:
                    return None
            if ' ' in arg_string:
                return None
            return (
             None, arg_string, None)

    def _get_option_tuples(self, option_string):
        result = []
        chars = self.prefix_chars
        if option_string[0] in chars and option_string[1] in chars:
            if '=' in option_string:
                option_prefix, explicit_arg = option_string.split('=', 1)
            else:
                option_prefix = option_string
                explicit_arg = None
            for option_string in self._option_string_actions:
                if option_string.startswith(option_prefix):
                    action = self._option_string_actions[option_string]
                    tup = (action, option_string, explicit_arg)
                    result.append(tup)

        elif option_string[0] in chars and option_string[1] not in chars:
            option_prefix = option_string
            explicit_arg = None
            short_option_prefix = option_string[:2]
            short_explicit_arg = option_string[2:]
            for option_string in self._option_string_actions:
                if option_string == short_option_prefix:
                    action = self._option_string_actions[option_string]
                    tup = (action, option_string, short_explicit_arg)
                    result.append(tup)
                elif option_string.startswith(option_prefix):
                    action = self._option_string_actions[option_string]
                    tup = (action, option_string, explicit_arg)
                    result.append(tup)

        else:
            self.error(_('unexpected option string: %s') % option_string)
        return result

    def _get_nargs_pattern(self, action):
        nargs = action.nargs
        if nargs is None:
            nargs_pattern = '(-*A-*)'
        elif nargs == OPTIONAL:
            nargs_pattern = '(-*A?-*)'
        elif nargs == ZERO_OR_MORE:
            nargs_pattern = '(-*[A-]*)'
        elif nargs == ONE_OR_MORE:
            nargs_pattern = '(-*A[A-]*)'
        elif nargs == REMAINDER:
            nargs_pattern = '([-AO]*)'
        elif nargs == PARSER:
            nargs_pattern = '(-*A[-AO]*)'
        else:
            nargs_pattern = '(-*%s-*)' % '-*'.join('A' * nargs)
        if action.option_strings:
            nargs_pattern = nargs_pattern.replace('-*', '')
            nargs_pattern = nargs_pattern.replace('-', '')
        return nargs_pattern

    def _get_values(self, action, arg_strings):
        if action.nargs not in [PARSER, REMAINDER]:
            arg_strings = [ s for s in arg_strings if s != '--' ]
        if not arg_strings and action.nargs == OPTIONAL:
            if action.option_strings:
                value = action.const
            else:
                value = action.default
            if isinstance(value, basestring):
                value = self._get_value(action, value)
                self._check_value(action, value)
        elif not arg_strings and action.nargs == ZERO_OR_MORE and not action.option_strings:
            if action.default is not None:
                value = action.default
            else:
                value = arg_strings
            self._check_value(action, value)
        elif len(arg_strings) == 1 and action.nargs in [None, OPTIONAL]:
            arg_string, = arg_strings
            value = self._get_value(action, arg_string)
            self._check_value(action, value)
        elif action.nargs == REMAINDER:
            value = [ self._get_value(action, v) for v in arg_strings ]
        elif action.nargs == PARSER:
            value = [ self._get_value(action, v) for v in arg_strings ]
            self._check_value(action, value[0])
        else:
            value = [ self._get_value(action, v) for v in arg_strings ]
            for v in value:
                self._check_value(action, v)

        return value

    def _get_value(self, action, arg_string):
        type_func = self._registry_get('type', action.type, action.type)
        if not _callable(type_func):
            msg = _('%r is not callable')
            raise ArgumentError(action, msg % type_func)
        try:
            result = type_func(arg_string)
        except ArgumentTypeError:
            name = getattr(action.type, '__name__', repr(action.type))
            msg = str(_sys.exc_info()[1])
            raise ArgumentError(action, msg)
        except (TypeError, ValueError):
            name = getattr(action.type, '__name__', repr(action.type))
            msg = _('invalid %s value: %r')
            raise ArgumentError(action, msg % (name, arg_string))

        return result

    def _check_value(self, action, value):
        if action.choices is not None and value not in action.choices:
            tup = (
             value, ', '.join(map(repr, action.choices)))
            msg = _('invalid choice: %r (choose from %s)') % tup
            raise ArgumentError(action, msg)
        return

    def format_usage(self):
        formatter = self._get_formatter()
        formatter.add_usage(self.usage, self._actions, self._mutually_exclusive_groups)
        return formatter.format_help()

    def format_help(self):
        formatter = self._get_formatter()
        formatter.add_usage(self.usage, self._actions, self._mutually_exclusive_groups)
        formatter.add_text(self.description)
        for action_group in self._action_groups:
            formatter.start_section(action_group.title)
            formatter.add_text(action_group.description)
            formatter.add_arguments(action_group._group_actions)
            formatter.end_section()

        formatter.add_text(self.epilog)
        return formatter.format_help()

    def format_version(self):
        import warnings
        warnings.warn('The format_version method is deprecated -- the "version" argument to ArgumentParser is no longer supported.', DeprecationWarning)
        formatter = self._get_formatter()
        formatter.add_text(self.version)
        return formatter.format_help()

    def _get_formatter(self):
        return self.formatter_class(prog=self.prog)

    def print_usage(self, file=None):
        if file is None:
            file = _sys.stdout
        self._print_message(self.format_usage(), file)
        return

    def print_help(self, file=None):
        if file is None:
            file = _sys.stdout
        self._print_message(self.format_help(), file)
        return

    def print_version(self, file=None):
        import warnings
        warnings.warn('The print_version method is deprecated -- the "version" argument to ArgumentParser is no longer supported.', DeprecationWarning)
        self._print_message(self.format_version(), file)

    def _print_message(self, message, file=None):
        if message:
            if file is None:
                file = _sys.stderr
            file.write(message)
        return

    def exit(self, status=0, message=None):
        if message:
            self._print_message(message, _sys.stderr)
        _sys.exit(status)

    def error(self, message):
        """error(message: string)
        
        Prints a usage message incorporating the message to stderr and
        exits.
        
        If you override this in a subclass, it should not return -- it
        should either exit or raise an exception.
        """
        self.print_usage(_sys.stderr)
        self.exit(2, _('%s: error: %s\n') % (self.prog, message))