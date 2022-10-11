import asyncio
import threading
from math import ceil
from gi.repository import Gtk, Gdk, GLib

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

        spinner = Gtk.Spinner()
        spinner.start()

        head = Header()

        box.add(dummy_entry)
        box.add(head)
        box.add(spinner)

        root_scroll = Gtk.ScrolledWindow()
        root_scroll.add(box)

        self.add(root_scroll)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        head.hide()

        # Dummy entry got focus, hide it now
        dummy_entry.destroy()

        def on_videos_downloaded(videos):
            spinner.stop()
            head.show()
            for i in range(ceil(len(videos) / 3)):
                row = LibraryRow(videos[i * ROW_COUNT:(i + 1) * ROW_COUNT], box.get_allocated_width(), ROW_COUNT)
                sep = Gtk.Box()
                sep.set_margin_bottom(GLOBAL_SPACING)
                box.add(row)
                box.add(sep)
                sep.show()
                row.show_all()
            footer = Gtk.Label(label="<span>Made with ♥ by Captain J. Sparrow built on top of <a href='https://steamdeckrepo.com/'>Steam Deck Repo</a></span>")
            footer.set_use_markup(True)
            footer.show()
            box.add(footer)

        def download_videos_async():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            videos = loop.run_until_complete(get_videos())
            GLib.idle_add(on_videos_downloaded, videos)

        # Get Videos in a new thread to prevent UI freeze
        threading.Thread(target=download_videos_async, daemon=True).start()
