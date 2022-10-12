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

    def __init__(self):
        super(Header, self).__init__()
        self.original_label = "Clear installed videos"

        self.clear_button = Gtk.Button(label=self.original_label)
        self.clear_button.connect("clicked", self.clear_videos)
        self.add(self.clear_button)
