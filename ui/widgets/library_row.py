from math import floor
from gi.repository import GLib, Gtk, GdkPixbuf, Pango
from ui.utils import download_video
from ui.widgets.info_box import InfoBox

GUTTER = 16
IMAGE_RATIO = 1.6


class LibraryRow(Gtk.Box):
    def on_video_dl(self, _, url):
        download_video(_, url)
        dialog = Gtk.MessageDialog(
            flags=0,
            message_type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            text="Success ! Video is installed on your Steam Deck, reboot your device.",
        )
        dialog.run()
        dialog.destroy()

    def compute_image_size(self, width):
        new_width = floor(width * (1 / self.row_count))
        new_size = new_width - (GUTTER * (self.row_count - 1) / self.row_count)

        return {
            "width": floor(new_size),
            "height": floor(new_size / IMAGE_RATIO)
        }

    def resize_images(self, __, _, window):
        size = self.compute_image_size(window.get_allocated_width())
        for index, buffer in enumerate(self.original_buffers):
            pixbuf = buffer.scale_simple(size["width"], size["height"], GdkPixbuf.InterpType.BILINEAR)
            self.original_images[index].set_from_pixbuf(pixbuf)

    def __init__(self, images, default_width, row_count):
        super(LibraryRow, self).__init__()

        self.temp_height = 0
        self.event_count = 0
        self.temp_width = 0
        self.original_buffers = []
        self.original_images = []
        self.row_count = row_count

        scroll = Gtk.ScrolledWindow()
        scroll.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.NEVER)
        scroll.set_hexpand(True)
        boot_video_container = Gtk.Box()
        boot_video_container.set_orientation(Gtk.Orientation.HORIZONTAL)

        for index, boot_video in enumerate(images):
            content = boot_video["content"]

            loader = GdkPixbuf.PixbufLoader()
            loader.write_bytes(GLib.Bytes.new(content))
            loader.close()

            container = Gtk.Box()
            container.set_orientation(Gtk.Orientation.VERTICAL)
            container.set_margin_bottom(8)
            container.set_margin_top(0)
            container.set_margin_left(0 if index == 0 else GUTTER)

            pixbuf = loader.get_pixbuf()
            self.original_buffers.append(pixbuf)
            size = self.compute_image_size(default_width)
            pixbuf = pixbuf.scale_simple(size["width"], size["height"], GdkPixbuf.InterpType.BILINEAR)

            img = Gtk.Image.new_from_pixbuf(pixbuf)
            label = Gtk.Label(label=boot_video["title"])
            label.set_margin_bottom(8)
            label.set_ellipsize(Pango.EllipsizeMode.END)
            label.set_tooltip_text(boot_video["title"])

            actions = Gtk.Box()
            actions.set_homogeneous(True)
            actions.set_spacing(6)

            download_button = Gtk.Button(label="Download")
            download_button.connect('clicked', self.on_video_dl, boot_video["video"])
            preview_button = Gtk.LinkButton(boot_video["video"], label="Preview")

            actions.add(download_button)
            actions.add(preview_button)

            container.add(label)
            container.add(img)
            container.add(InfoBox(author=boot_video["author"], downloads=boot_video["downloads"]))
            container.add(actions)

            boot_video_container.add(container)
            self.original_images.append(img)

        scroll.add(boot_video_container)
        self.add(scroll)
        self.connect('size-allocate', self.resize_images, self)
