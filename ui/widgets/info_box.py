from gi.repository import Gtk


class InfoBox(Gtk.Box):
    def __init__(self, author: str = '', downloads: str = ''):
        super(InfoBox, self).__init__()

        self.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.set_margin_top(6)
        self.set_margin_bottom(6)

        author = Gtk.Label(label=f"<b>{author}</b>")
        author.set_use_markup(True)

        downloads = Gtk.Label(label=f"<span size='10000'>Downloads: {str(downloads)}</span>")
        downloads.set_use_markup(True)
        downloads.set_alignment(1, 0)
        downloads.set_hexpand(True)

        self.add(author)
        self.add(downloads)
