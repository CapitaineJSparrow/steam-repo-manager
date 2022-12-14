from typing import Callable
from gi.repository import Gtk
from utils import clear_installed_videos


class Header(Gtk.Box):
    def clear_videos(self, _=None):
        clear_installed_videos()
        dialog = Gtk.MessageDialog(
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="Success ! Reboot your device, default boot video should be back.",
        )
        dialog.run()
        dialog.destroy()

    def __init__(self, on_search: Callable, on_duration_filter: Callable):
        super(Header, self).__init__()
        self.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.set_spacing(8)

        search_entry = Gtk.SearchEntry()
        search_entry.set_hexpand(True)
        search_entry.set_placeholder_text("Search for videos")

        def on_search_changed(_):
            on_search(search_entry.get_text())

        search_entry.connect("search-changed", on_search_changed)

        clear_button = Gtk.Button(label="Clear installed videos")
        clear_button.connect("clicked", self.clear_videos)

        filter_duration_button = Gtk.Button(label="Filter by duration")
        filter_duration_button.connect("clicked", on_duration_filter)

        self.add(search_entry)
        self.add(clear_button)
        # self.add(filter_duration_button)

