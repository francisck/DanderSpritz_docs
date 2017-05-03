# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: ElementPath.py
import re
xpath_tokenizer_re = re.compile('(\'[^\']*\'|"[^"]*"|::|//?|\\.\\.|\\(\\)|[/.*:\\[\\]\\(\\)@=])|((?:\\{[^}]+\\})?[^/\\[\\]\\(\\)@=\\s]+)|\\s+')

def xpath_tokenizer(pattern, namespaces=None):
    for token in xpath_tokenizer_re.findall(pattern):
        tag = token[1]
        if tag and tag[0] != '{' and ':' in tag:
            try:
                prefix, uri = tag.split(':', 1)
                if not namespaces:
                    raise KeyError
                yield (
                 token[0], '{%s}%s' % (namespaces[prefix], uri))
            except KeyError:
                raise SyntaxError('prefix %r not found in prefix map' % prefix)

        else:
            yield token


def get_parent_map(context):
    parent_map = context.parent_map
    if parent_map is None:
        context.parent_map = parent_map = {}
        for p in context.root.iter():
            for e in p:
                parent_map[e] = p

    return parent_map


def prepare_child(next, token):
    tag = token[1]

    def select(context, result):
        for elem in result:
            for e in elem:
                if e.tag == tag:
                    yield e

    return select


def prepare_star(next, token):

    def select(context, result):
        for elem in result:
            for e in elem:
                yield e

    return select


def prepare_self(next, token):

    def select(context, result):
        for elem in result:
            yield elem

    return select


def prepare_descendant(next, token):
    token = next()
    if token[0] == '*':
        tag = '*'
    elif not token[0]:
        tag = token[1]
    else:
        raise SyntaxError('invalid descendant')

    def select(context, result):
        for elem in result:
            for e in elem.iter(tag):
                if e is not elem:
                    yield e

    return select


def prepare_parent(next, token):

    def select(context, result):
        parent_map = get_parent_map(context)
        result_map = {}
        for elem in result:
            if elem in parent_map:
                parent = parent_map[elem]
                if parent not in result_map:
                    result_map[parent] = None
                    yield parent

        return

    return select


def prepare_predicate(next, token):
    signature = []
    predicate = []
    while 1:
        token = next()
        if token[0] == ']':
            break
        if token[0] and token[0][:1] in '\'"':
            token = (
             "'", token[0][1:-1])
        signature.append(token[0] or '-')
        predicate.append(token[1])

    signature = ''.join(signature)
    if signature == '@-':
        key = predicate[1]

        def select(context, result):
            for elem in result:
                if elem.get(key) is not None:
                    yield elem

            return

        return select
    if signature == "@-='":
        key = predicate[1]
        value = predicate[-1]

        def select(context, result):
            for elem in result:
                if elem.get(key) == value:
                    yield elem

        return select
    if signature == '-' and not re.match('\\d+$', predicate[0]):
        tag = predicate[0]

        def select(context, result):
            for elem in result:
                if elem.find(tag) is not None:
                    yield elem

            return

        return select
    if signature == "-='" and not re.match('\\d+$', predicate[0]):
        tag = predicate[0]
        value = predicate[-1]

        def select(context, result):
            for elem in result:
                for e in elem.findall(tag):
                    if ''.join(e.itertext()) == value:
                        yield elem
                        break

        return select
    if signature == '-' or signature == '-()' or signature == '-()-':
        if signature == '-':
            index = int(predicate[0]) - 1
        else:
            if predicate[0] != 'last':
                raise SyntaxError('unsupported function')
            if signature == '-()-':
                try:
                    index = int(predicate[2]) - 1
                except ValueError:
                    raise SyntaxError('unsupported expression')

            else:
                index = -1

        def select(context, result):
            parent_map = get_parent_map(context)
            for elem in result:
                try:
                    parent = parent_map[elem]
                    elems = list(parent.findall(elem.tag))
                    if elems[index] is elem:
                        yield elem
                except (IndexError, KeyError):
                    pass

        return select
    raise SyntaxError('invalid predicate')


ops = {'': prepare_child,
   '*': prepare_star,
   '.': prepare_self,
   '..': prepare_parent,
   '//': prepare_descendant,
   '[': prepare_predicate
   }
_cache = {}

class _SelectorContext:
    parent_map = None

    def __init__(self, root):
        self.root = root


def iterfind(elem, path, namespaces=None):
    if path[-1:] == '/':
        path = path + '*'
    try:
        selector = _cache[path]
    except KeyError:
        if len(_cache) > 100:
            _cache.clear()
        if path[:1] == '/':
            raise SyntaxError('cannot use absolute path on element')
        next = iter(xpath_tokenizer(path, namespaces)).next
        token = next()
        selector = []
        while 1:
            try:
                selector.append(ops[token[0]](next, token))
            except StopIteration:
                raise SyntaxError('invalid path')

            try:
                token = next()
                if token[0] == '/':
                    token = next()
            except StopIteration:
                break

        _cache[path] = selector

    result = [elem]
    context = _SelectorContext(elem)
    for select in selector:
        result = select(context, result)

    return result


def find(elem, path, namespaces=None):
    try:
        return iterfind(elem, path, namespaces).next()
    except StopIteration:
        return None

    return None


def findall(elem, path, namespaces=None):
    return list(iterfind(elem, path, namespaces))


def findtext(elem, path, default=None, namespaces=None):
    try:
        elem = iterfind(elem, path, namespaces).next()
        return elem.text or ''
    except StopIteration:
        return default