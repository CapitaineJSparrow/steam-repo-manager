import asyncio
import threading
from math import ceil
from gi.repository import Gtk, GLib

from main import get_videos
from ui.widgets.library_row import LibraryRow
from ui.widgets.header import Header

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

        self.head = Header()
        box.add(dummy_entry)
        box.add(self.head)

        root_scroll = Gtk.ScrolledWindow()
        root_scroll.add(box)

        self.add(root_scroll)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        self.head.hide()

        self.item_container = Gtk.Box()
        self.item_container.set_margin_top(GLOBAL_SPACING)
        self.item_container.set_margin_left(GLOBAL_SPACING)
        self.item_container.set_margin_right(GLOBAL_SPACING)
        self.item_container.set_valign(Gtk.Align.START)
        self.item_container.set_orientation(Gtk.Orientation.VERTICAL)
        self.item_container.show()
        box.add(self.item_container)

        self.spinner = Gtk.Spinner()
        box.add(self.spinner)

        self.more_button = Gtk.Button(label="Load more")
        self.more_button.set_margin_bottom(GLOBAL_SPACING)
        self.more_button.set_margin_left(GLOBAL_SPACING)
        self.more_button.set_margin_right(GLOBAL_SPACING)
        self.more_button.connect('clicked', self.download_more)
        box.add(self.more_button)

        self.footer = Gtk.Label(
            label="<span>Made with ♥ by Captain J. Sparrow built on top of <a href='https://steamdeckrepo.com/'>Steam Deck Repo</a></span>")
        self.footer.set_use_markup(True)
        box.add(self.footer)

        # Dummy entry got focus, hide it now
        dummy_entry.destroy()

        # Get Videos in a new thread to prevent UI freeze
        threading.Thread(target=self.download_videos_async, daemon=True, kwargs={'page': 0}).start()

    def on_videos_downloaded(self, videos):
        self.spinner.stop()
        self.head.show()  # Show clear video button
        self.footer.show()  # Show credits
        for i in range(ceil(len(videos) / ROW_COUNT)):
            row = LibraryRow(
                videos[i * ROW_COUNT:(i + 1) * ROW_COUNT],
                self.item_container.get_allocated_width(), ROW_COUNT
            )
            sep = Gtk.Box()
            sep.set_margin_bottom(GLOBAL_SPACING)
            self.item_container.add(row)
            self.item_container.add(sep)
            sep.show()
            row.show_all()

            if len(videos) > 0:
                self.more_button.set_label("Load more")
                self.more_button.set_sensitive(True)
                self.more_button.show()
            else:
                self.more_button.hide()

    def download_videos_async(self, page: int):
        if page == 0:  # Do not show spinner when using pagination since it's not spinning due to threading issues
            self.spinner.start()
            self.spinner.show()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        videos = loop.run_until_complete(get_videos(page))
        GLib.idle_add(self.on_videos_downloaded, videos)

    def download_more(self, *args, **kwargs):
        self.more_button.set_label("Loading ...")
        self.more_button.set_sensitive(False)
        self.current_page = self.current_page + 1
        threading.Thread(target=self.download_videos_async, daemon=True, kwargs={'page': self.current_page}).start()
