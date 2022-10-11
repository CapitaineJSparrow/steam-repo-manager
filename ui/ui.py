import gi
gi.require_version("Gtk", "3.0")

from ui.widgets.main_window import MainWindow
from gi.repository import Gtk, Gdk


def build_ui():
    Gdk.threads_init()
    MainWindow()
    Gtk.main()
