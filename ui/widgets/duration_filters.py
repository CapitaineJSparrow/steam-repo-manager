from gi.repository import Gtk, Gdk


class DurationFilters(Gtk.Expander):
    def __init__(self):
        super(DurationFilters, self).__init__()
        container = Gtk.Box()
        container.set_orientation(Gtk.Orientation.HORIZONTAL)

        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(
            screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        css = b"""
        expander arrow {
            -gtk-icon-source: none;
        }
        """
        provider.load_from_data(css)

        start_label = Gtk.Label(label="Filter by duration from")
        start_label.set_margin_right(8)

        start_values = [
            "0",
            "5",
            "10",
            "15",
            "20",
            "30",
        ]
        start_combo = Gtk.ComboBoxText()
        start_combo.set_entry_text_column(0)

        end_combo = Gtk.ComboBoxText()
        end_combo.set_entry_text_column(0)
        end_combo.set_margin_left(8)

        for value in start_values:
            start_combo.append_text(value)
            end_combo.append_text(value)

        start_combo.set_active(0)
        end_combo.append_text("any")
        end_combo.set_active(len(start_values))
        start_combo.set_margin_right(8)

        container.add(start_label)
        container.add(start_combo)
        container.add(Gtk.Label(label="to"))
        container.add(end_combo)
        container.add(Gtk.Label(label="  seconds  "))
        container.add(Gtk.Button(label="apply filters"))
        self.add(container)
