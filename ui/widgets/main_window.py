import asyncio
import threading
from math import ceil
from gi.repository import Gtk, GLib, Gst

from main import get_videos
from ui.widgets.library_row import LibraryRow
from ui.widgets.header import Header
from ui.widgets.playback_interface import PlaybackInterface

GLOBAL_SPACING = 20
added = False
ROW_COUNT = 3


class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Steam Deck Repo Manager")
        default_width = 1180

        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_default_size(default_width, 680)
        self.current_page = 1

        # workaround for focus of first entry
        dummy_entry = Gtk.Entry()

        # Global Layout
        box = Gtk.Box()
        box.set_margin_top(GLOBAL_SPACING)
        box.set_margin_left(GLOBAL_SPACING)
        box.set_margin_right(GLOBAL_SPACING)
        box.set_margin_bottom(GLOBAL_SPACING)
        box.set_valign(Gtk.Align.START)
        box.set_orientation(Gtk.Orientation.VERTICAL)

        head = Header()

        box.add(dummy_entry)
        box.add(head)

        root_scroll = Gtk.ScrolledWindow()
        root_scroll.add(box)

        self.add(root_scroll)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        # head.hide()

        self.item_container = Gtk.Box()
        self.item_container.set_margin_top(GLOBAL_SPACING)
        self.item_container.set_margin_left(GLOBAL_SPACING)
        self.item_container.set_margin_right(GLOBAL_SPACING)
        self.item_container.set_margin_bottom(GLOBAL_SPACING)
        self.item_container.set_valign(Gtk.Align.START)
        self.item_container.set_orientation(Gtk.Orientation.VERTICAL)
        self.item_container.show()
        box.add(self.item_container)

        self.spinner = Gtk.Spinner()
        self.spinner.set_margin_bottom(GLOBAL_SPACING)
        box.add(self.spinner)

        self.more_button = Gtk.Button(label="More")
        self.more_button.set_margin_bottom(GLOBAL_SPACING)
        self.more_button.connect('clicked', self.download_more)
        box.add(self.more_button)

        footer = Gtk.Label(label="<span>Made with ♥ by Captain J. Sparrow built on top of <a href='https://steamdeckrepo.com/'>Steam Deck Repo</a></span>")
        footer.set_use_markup(True)
        footer.show()
        box.add(footer)

        # Dummy entry got focus, hide it now
        dummy_entry.destroy()

        # Get Videos in a new thread to prevent UI freeze
        threading.Thread(target=self.download_videos_async, daemon=True, kwargs={'page': 0}).start()

    def on_videos_downloaded(self, videos):
        self.spinner.stop()
        # head.show()
        for i in range(ceil(len(videos) / 3)):
            row = LibraryRow(videos[i * ROW_COUNT:(i + 1) * ROW_COUNT],
                             self.item_container.get_allocated_width(), ROW_COUNT)
            sep = Gtk.Box()
            sep.set_margin_bottom(GLOBAL_SPACING)
            self.item_container.add(row)
            self.item_container.add(sep)
            sep.show()
            row.show_all()
        if videos:
            self.more_button.show()

    def download_videos_async(self, page: int):
        self.spinner.start()
        self.spinner.show()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        videos = loop.run_until_complete(get_videos(page))
        GLib.idle_add(self.on_videos_downloaded, videos)

    def download_more(self, *args, **kwargs):
        self.more_button.hide()
        next_page = self.current_page + 1
        threading.Thread(target=self.download_videos_async, daemon=True, kwargs={'page': next_page}).start()
        self.current_page = next_page
