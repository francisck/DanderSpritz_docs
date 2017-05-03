# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: macosxSupport.py
"""
A number of function that enhance IDLE on MacOSX when it used as a normal
GUI application (as opposed to an X11 application).
"""
import sys
import Tkinter
from os import path
_appbundle = None

def runningAsOSXApp():
    """
    Returns True if Python is running from within an app on OSX.
    If so, assume that Python was built with Aqua Tcl/Tk rather than
    X11 Tcl/Tk.
    """
    global _appbundle
    if _appbundle is None:
        _appbundle = sys.platform == 'darwin' and '.app' in sys.executable
    return _appbundle


_carbonaquatk = None

def isCarbonAquaTk(root):
    """
    Returns True if IDLE is using a Carbon Aqua Tk (instead of the
    newer Cocoa Aqua Tk).
    """
    global _carbonaquatk
    if _carbonaquatk is None:
        _carbonaquatk = runningAsOSXApp() and 'aqua' in root.tk.call('tk', 'windowingsystem') and 'AppKit' not in root.tk.call('winfo', 'server', '.')
    return _carbonaquatk


def tkVersionWarning(root):
    """
    Returns a string warning message if the Tk version in use appears to
    be one known to cause problems with IDLE.  The Apple Cocoa-based Tk 8.5
    that was shipped with Mac OS X 10.6.
    """
    if runningAsOSXApp() and 'AppKit' in root.tk.call('winfo', 'server', '.') and root.tk.call('info', 'patchlevel') == '8.5.7':
        return 'WARNING: The version of Tcl/Tk (8.5.7) in use may be unstable.\\nVisit http://www.python.org/download/mac/tcltk/ for current information.'
    else:
        return False


def addOpenEventSupport(root, flist):
    """
    This ensures that the application will respond to open AppleEvents, which
    makes is feasible to use IDLE as the default application for python files.
    """

    def doOpenFile(*args):
        for fn in args:
            flist.open(fn)

    root.createcommand('::tk::mac::OpenDocument', doOpenFile)


def hideTkConsole(root):
    try:
        root.tk.call('console', 'hide')
    except Tkinter.TclError:
        pass


def overrideRootMenu(root, flist):
    """
    Replace the Tk root menu by something that's more appropriate for
    IDLE.
    """
    from Tkinter import Menu, Text, Text
    from idlelib.EditorWindow import prepstr, get_accelerator
    from idlelib import Bindings
    from idlelib import WindowList
    from idlelib.MultiCall import MultiCallCreator
    menubar = Menu(root)
    root.configure(menu=menubar)
    menudict = {}
    menudict['windows'] = menu = Menu(menubar, name='windows')
    menubar.add_cascade(label='Window', menu=menu, underline=0)

    def postwindowsmenu(menu=menu):
        end = menu.index('end')
        if end is None:
            end = -1
        if end > 0:
            menu.delete(0, end)
        WindowList.add_windows_to_menu(menu)
        return

    WindowList.register_callback(postwindowsmenu)

    def about_dialog(event=None):
        from idlelib import aboutDialog
        aboutDialog.AboutDialog(root, 'About IDLE')

    def config_dialog(event=None):
        from idlelib import configDialog
        root.instance_dict = flist.inversedict
        configDialog.ConfigDialog(root, 'Settings')

    def help_dialog(event=None):
        from idlelib import textView
        fn = path.join(path.abspath(path.dirname(__file__)), 'help.txt')
        textView.view_file(root, 'Help', fn)

    root.bind('<<about-idle>>', about_dialog)
    root.bind('<<open-config-dialog>>', config_dialog)
    root.createcommand('::tk::mac::ShowPreferences', config_dialog)
    if flist:
        root.bind('<<close-all-windows>>', flist.close_all_callback)
        root.createcommand('exit', flist.close_all_callback)
    if isCarbonAquaTk(root):
        menudict['application'] = menu = Menu(menubar, name='apple')
        menubar.add_cascade(label='IDLE', menu=menu)
        Bindings.menudefs.insert(0, (
         'application',
         [
          ('About IDLE', '<<about-idle>>'),
          None]))
        tkversion = root.tk.eval('info patchlevel')
        if tuple(map(int, tkversion.split('.'))) < (8, 4, 14):
            Bindings.menudefs[0][1].append(('_Preferences....', '<<open-config-dialog>>'))
    else:
        root.createcommand('tkAboutDialog', about_dialog)
        root.createcommand('::tk::mac::ShowHelp', help_dialog)
        del Bindings.menudefs[-1][1][0]
    return


def setupApp(root, flist):
    """
    Perform setup for the OSX application bundle.
    """
    if not runningAsOSXApp():
        return
    hideTkConsole(root)
    overrideRootMenu(root, flist)
    addOpenEventSupport(root, flist)