from gi.repository import Gtk
from gi.repository import Gst


class PlaybackInterface:
    def __init__(self, url):
        self.url = url
        window = Gtk.Window()
        window.set_title("Video-Player")
        window.set_default_size(300, 300)
        window.connect("destroy", Gtk.main_quit, "WM destroy")
        self.movie_window = Gtk.DrawingArea()
        window.add(self.movie_window)
        window.show_all()
        window.hide()

        self.player = Gst.ElementFactory.make("playbin", "player")
        bus = self.player.get_bus()
        bus.add_signal_watch()
        bus.enable_sync_message_emission()
        bus.connect("message", self.on_message)
        bus.connect("sync-message::element", self.on_sync_message)
        self.start_stop()

    def start_stop(self):
        self.player.set_property("uri", self.url)
        self.player.set_state(Gst.State.PLAYING)

    def on_message(self, _, message):
        t = message.type
        if t == Gst.MessageType.EOS:
            self.player.set_state(Gst.State.NULL)
        elif t == Gst.MessageType.ERROR:
            self.player.set_state(Gst.State.NULL)
            err, debug = message.parse_error()
            print(err, debug)

    def on_sync_message(self, _, message):
        if message.get_structure().get_name() == 'prepare-window-handle':
            imagesink = message.src
            imagesink.set_property("force-aspect-ratio", True)
