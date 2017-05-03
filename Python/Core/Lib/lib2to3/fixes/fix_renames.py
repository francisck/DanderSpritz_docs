# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_renames.py
"""Fix incompatible renames

Fixes:
  * sys.maxint -> sys.maxsize
"""
from .. import fixer_base
from ..fixer_util import Name, attr_chain
MAPPING = {'sys': {'maxint': 'maxsize'}}
LOOKUP = {}

def alternates(members):
    return '(' + '|'.join(map(repr, members)) + ')'


def build_pattern():
    for module, replace in MAPPING.items():
        for old_attr, new_attr in replace.items():
            LOOKUP[module, old_attr] = new_attr
            yield "\n                  import_from< 'from' module_name=%r 'import'\n                      ( attr_name=%r | import_as_name< attr_name=%r 'as' any >) >\n                  " % (module, old_attr, old_attr)
            yield "\n                  power< module_name=%r trailer< '.' attr_name=%r > any* >\n                  " % (module, old_attr)


class FixRenames(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = '|'.join(build_pattern())
    order = 'pre'

    def match(self, node):
        match = super(FixRenames, self).match
        results = match(node)
        if results:
            if any((match(obj) for obj in attr_chain(node, 'parent'))):
                return False
            return results
        return False

    def transform(self, node, results):
        mod_name = results.get('module_name')
        attr_name = results.get('attr_name')
        if mod_name and attr_name:
            new_attr = unicode(LOOKUP[mod_name.value, attr_name.value])
            attr_name.replace(Name(new_attr, prefix=attr_name.prefix))