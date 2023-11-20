import gi
import os
import subprocess

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf, Gdk

class PythonFileOpener(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Zara - The Student's App")
        self.set_default_size(400, 300)
        # Set the icon for the window
        icon_path = "logo.png"  # Replace with the path to your icon file
        if os.path.exists(icon_path):
            self.set_icon_from_file(icon_path)

        # Set the layout
        grid = Gtk.Grid()
        grid.set_column_spacing(20)
        grid.set_row_spacing(20)
        grid.set_row_homogeneous(True)  # Make rows have equal height

        self.add(grid)

        # Create buttons
        buttons = [
            {"label": "Save videos locally", "icon": "icon1.png"},
            {"label": "Focus Mode", "icon": "icon2.png"},
            {"label": "Sticky Notes", "icon": "icon3.png"},
            {"label": "Generate a timetable", "icon": "icon4.png"},
            {"label": "Get summary from a news article", "icon": "icon5.png"},
            {"label": "Create a Todo list", "icon": "icon6.png"},
            {"label": "Video Summary", "icon": "icon7.png"},
            {"label": "Morse Code Decrypter (i know its useless)", "icon": "icon8.png"},
        ]

        for i, button_info in enumerate(buttons):
            button = Gtk.Button(label=button_info["label"])
            image = Gtk.Image.new_from_file(button_info["icon"])
            button.set_image(image)
            button.set_relief(Gtk.ReliefStyle.NONE)  # Remove button border

            button.connect("clicked", self.on_button_clicked, i + 1)
            grid.attach(button, i % 4, i // 4, 1, 1)

        # Center the grid in the window
        align = Gtk.Alignment.new(0.5, 0.5, 0, 0)
        align.add(grid)
        self.add(align)

        # Apply some additional styling
        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(b"""
            button {
                font-size: 14px;
                padding: 10px;
            }
        """)

        screen = Gdk.Screen.get_default()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def on_button_clicked(self, widget, button_number):
        py_file_path = f"script{button_number}.py"

        if os.path.exists(py_file_path):
            subprocess.Popen(["python3", py_file_path])
        else:
            print(f"Error: {py_file_path} not found.")

win = PythonFileOpener()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
