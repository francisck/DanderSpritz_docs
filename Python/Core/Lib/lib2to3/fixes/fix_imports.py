# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_imports.py
"""Fix incompatible imports and module references."""
from .. import fixer_base
from ..fixer_util import Name, attr_chain
MAPPING = {'StringIO': 'io','cStringIO': 'io',
   'cPickle': 'pickle',
   '__builtin__': 'builtins',
   'copy_reg': 'copyreg',
   'Queue': 'queue',
   'SocketServer': 'socketserver',
   'ConfigParser': 'configparser',
   'repr': 'reprlib',
   'FileDialog': 'tkinter.filedialog',
   'tkFileDialog': 'tkinter.filedialog',
   'SimpleDialog': 'tkinter.simpledialog',
   'tkSimpleDialog': 'tkinter.simpledialog',
   'tkColorChooser': 'tkinter.colorchooser',
   'tkCommonDialog': 'tkinter.commondialog',
   'Dialog': 'tkinter.dialog',
   'Tkdnd': 'tkinter.dnd',
   'tkFont': 'tkinter.font',
   'tkMessageBox': 'tkinter.messagebox',
   'ScrolledText': 'tkinter.scrolledtext',
   'Tkconstants': 'tkinter.constants',
   'Tix': 'tkinter.tix',
   'ttk': 'tkinter.ttk',
   'Tkinter': 'tkinter',
   'markupbase': '_markupbase',
   '_winreg': 'winreg',
   'thread': '_thread',
   'dummy_thread': '_dummy_thread',
   'dbhash': 'dbm.bsd',
   'dumbdbm': 'dbm.dumb',
   'dbm': 'dbm.ndbm',
   'gdbm': 'dbm.gnu',
   'xmlrpclib': 'xmlrpc.client',
   'DocXMLRPCServer': 'xmlrpc.server',
   'SimpleXMLRPCServer': 'xmlrpc.server',
   'httplib': 'http.client',
   'htmlentitydefs': 'html.entities',
   'HTMLParser': 'html.parser',
   'Cookie': 'http.cookies',
   'cookielib': 'http.cookiejar',
   'BaseHTTPServer': 'http.server',
   'SimpleHTTPServer': 'http.server',
   'CGIHTTPServer': 'http.server',
   'commands': 'subprocess',
   'UserString': 'collections',
   'UserList': 'collections',
   'urlparse': 'urllib.parse',
   'robotparser': 'urllib.robotparser'
   }

def alternates(members):
    return '(' + '|'.join(map(repr, members)) + ')'


def build_pattern(mapping=MAPPING):
    mod_list = ' | '.join([ "module_name='%s'" % key for key in mapping ])
    bare_names = alternates(mapping.keys())
    yield "name_import=import_name< 'import' ((%s) |\n               multiple_imports=dotted_as_names< any* (%s) any* >) >\n          " % (mod_list, mod_list)
    yield "import_from< 'from' (%s) 'import' ['(']\n              ( any | import_as_name< any 'as' any > |\n                import_as_names< any* >)  [')'] >\n          " % mod_list
    yield "import_name< 'import' (dotted_as_name< (%s) 'as' any > |\n               multiple_imports=dotted_as_names<\n                 any* dotted_as_name< (%s) 'as' any > any* >) >\n          " % (mod_list, mod_list)
    yield "power< bare_with_attr=(%s) trailer<'.' any > any* >" % bare_names


class FixImports(fixer_base.BaseFix):
    BM_compatible = True
    keep_line_order = True
    mapping = MAPPING
    run_order = 6

    def build_pattern(self):
        return '|'.join(build_pattern(self.mapping))

    def compile_pattern(self):
        self.PATTERN = self.build_pattern()
        super(FixImports, self).compile_pattern()

    def match(self, node):
        match = super(FixImports, self).match
        results = match(node)
        if results:
            if 'bare_with_attr' not in results and any((match(obj) for obj in attr_chain(node, 'parent'))):
                return False
            return results
        return False

    def start_tree(self, tree, filename):
        super(FixImports, self).start_tree(tree, filename)
        self.replace = {}

    def transform(self, node, results):
        import_mod = results.get('module_name')
        if import_mod:
            mod_name = import_mod.value
            new_name = unicode(self.mapping[mod_name])
            import_mod.replace(Name(new_name, prefix=import_mod.prefix))
            if 'name_import' in results:
                self.replace[mod_name] = new_name
            if 'multiple_imports' in results:
                results = self.match(node)
                if results:
                    self.transform(node, results)
        else:
            bare_name = results['bare_with_attr'][0]
            new_name = self.replace.get(bare_name.value)
            if new_name:
                bare_name.replace(Name(new_name, prefix=bare_name.prefix))