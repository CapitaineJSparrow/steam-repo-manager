from gi.repository import Gtk, GLib
from threading import Timer
from ui.utils import clear_installed_videos


class Header(Gtk.Box):
    def reset_label(self):
        self.clear_button.set_label(self.original_label)

    def reset_label_idle(self):
        GLib.idle_add(self.reset_label)

    def clear_videos(self, _=None):
        clear_installed_videos()
        self.clear_button.set_label("Done !")
        Timer(3.0, self.reset_label_idle).start()

    def __init__(self):
        super(Header, self).__init__()
        self.original_label = "Clear installed videos"

        self.clear_button = Gtk.Button(label=self.original_label)
        self.clear_button.connect("clicked", self.clear_videos)
        self.add(self.clear_button)
