from gi.repository import Gtk
from packaging import version
from utils import CURRENT_VERSION, get_remote_version


class UpdateFrame(Gtk.Frame):
    def __init__(self):
        super(UpdateFrame, self).__init__()
        self.should_update = version.parse(CURRENT_VERSION) < version.parse(get_remote_version())
        self.set_label("Update available")
        self.set_margin_top(20)

        label = Gtk.Label(label="You are using version 1.0.7 but update 1.1.0 should be available in Discover. Please consider to update Steam Deck Repo Manager")
        label.set_margin_top(10)
        label.set_margin_bottom(10)
        self.add(label)
        get_remote_version()
