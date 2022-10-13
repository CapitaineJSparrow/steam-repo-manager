import os
from gi.repository import Gtk, GdkPixbuf, Pango


def get_resource_path(rel_path):
    dir_of_py_file = os.path.dirname(__file__)
    rel_path_to_resource = os.path.join(dir_of_py_file, rel_path)
    abs_path_to_resource = os.path.abspath(rel_path_to_resource)
    return abs_path_to_resource


class InfoBox(Gtk.Box):
    def __init__(self, video):
        super(InfoBox, self).__init__()

        self.set_orientation(Gtk.Orientation.HORIZONTAL)
        self.set_margin_top(6)
        self.set_margin_bottom(6)

        author = video["author"]
        downloads = video["downloads"]
        likes = video["likes"]
        duration = video["duration"]

        author = Gtk.Label(label=f"<b>{author}</b>")
        author.set_ellipsize(Pango.EllipsizeMode.END)
        author.set_use_markup(True)

        download_img = Gtk.Image()
        download_img.set_from_file(get_resource_path("../icons/download.svg"))
        pixbuf = download_img.get_pixbuf()
        pixbuf = pixbuf.scale_simple(20, 20, GdkPixbuf.InterpType.BILINEAR)
        download_img.set_from_pixbuf(pixbuf)
        download_img.set_margin_left(6)

        likes_img = Gtk.Image()
        likes_img.set_from_file(get_resource_path("../icons/like.svg"))
        pixbuf = likes_img.get_pixbuf()
        pixbuf = pixbuf.scale_simple(20, 20, GdkPixbuf.InterpType.BILINEAR)
        likes_img.set_from_pixbuf(pixbuf)
        likes_img.set_margin_left(6)

        duration_img = Gtk.Image()
        duration_img.set_from_file(get_resource_path("../icons/time.svg"))
        pixbuf = duration_img.get_pixbuf()
        pixbuf = pixbuf.scale_simple(20, 20, GdkPixbuf.InterpType.BILINEAR)
        duration_img.set_from_pixbuf(pixbuf)
        duration_img.set_margin_left(6)

        actions_container = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        actions_container.set_hexpand(True)
        actions_container.set_halign(Gtk.Align.END)

        downloads = Gtk.Label(label=f"{str(downloads)}")
        likes = Gtk.Label(label=f"{str(likes)}")
        likes.set_margin_left(8)
        duration = Gtk.Label(label=f"{str(duration)}s")
        duration.set_margin_left(8)

        self.add(author)
        actions_container.add(downloads)
        actions_container.add(download_img)
        actions_container.add(likes)
        actions_container.add(likes_img)
        actions_container.add(duration)
        actions_container.add(duration_img)
        self.add(actions_container)
        self.set_margin_bottom(10)
        self.set_margin_top(10)
