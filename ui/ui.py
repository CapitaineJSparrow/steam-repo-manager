import gi

gi.require_version("Gtk", "3.0")
gi.require_version('Gst', '1.0')

from ui.widgets.main_window import MainWindow
from gi.repository import Gtk, Gdk, Gst

Gst.init(None)
Gst.init_check(None)


def build_ui():
    Gdk.threads_init()
    MainWindow()
    Gtk.main()
