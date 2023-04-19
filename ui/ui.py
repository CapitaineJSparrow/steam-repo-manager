import platform
import gi

gi.require_version("Gtk", "3.0")
gi.require_version('Gst', '1.0')

from ui.widgets.main_window import MainWindow
from gi.repository import Gtk, Gdk, Gst
from utils import is_windows

gtksettings = Gtk.Settings.get_default()
gtksettings.set_property(
    "gtk-application-prefer-dark-theme", False
)

Gst.init(None)
Gst.init_check(None)

def build_ui():
    if not is_windows:
        Gdk.threads_init()
    MainWindow()
    Gtk.main()