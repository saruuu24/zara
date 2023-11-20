import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageDraw, ImageTk


class TimetableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zara Timetable Generator")

        self.style = Style(theme="flatly")

        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        self.periods = ["1", "2", "3", "4", "5", "6", "7", "8"]

        self.class_info = {day: {period: "" for period in self.periods} for day in self.days}

        self.create_widgets()

    def create_widgets(self):
        # Day and Period Labels
        ttk.Label(self.root, text="Day").grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(self.root, text="Period").grid(row=0, column=2, padx=5, pady=5)
        ttk.Label(self.root, text="Class").grid(row=0, column=3, padx=5, pady=5)

        # Entry widgets for class information
        self.day_var = tk.StringVar()
        self.period_var = tk.StringVar()
        self.class_var = tk.StringVar()

        self.day_combobox = ttk.Combobox(self.root, textvariable=self.day_var, values=self.days)
        self.period_combobox = ttk.Combobox(self.root, textvariable=self.period_var, values=self.periods)
        self.class_entry = ttk.Entry(self.root, textvariable=self.class_var)

        self.day_combobox.grid(row=1, column=1, padx=5, pady=5)
        self.period_combobox.grid(row=1, column=2, padx=5, pady=5)
        self.class_entry.grid(row=1, column=3, padx=5, pady=5)

        # Button to add class information
        ttk.Button(self.root, text="Add Class", command=self.add_class).grid(row=1, column=4, padx=5, pady=5)

        # Button to generate and save timetable as PNG
        ttk.Button(self.root, text="Generate Timetable", command=self.generate_timetable).grid(row=2, column=1,
                                                                                               columnspan=4, pady=10)

        # Labels to display messages
        self.add_class_label = ttk.Label(self.root, text="")
        self.add_class_label.grid(row=3, column=1, columnspan=4, pady=5)

        self.save_label = ttk.Label(self.root, text="")
        self.save_label.grid(row=4, column=1, columnspan=4, pady=5)

    def add_class(self):
        day = self.day_var.get()
        period = self.period_var.get()
        class_info = self.class_var.get()

        if day and period and class_info:
            self.class_info[day][period] = class_info
            self.class_var.set("")
            print(f"Added class: {class_info} on {day}, Period {period}")

            # Update the label when a class is added
            self.add_class_label["text"] = f"Added class: {class_info} on {day}, Period {period}"

    def generate_timetable(self):
        image = self.create_timetable_image()
        image.show()  # Display the generated timetable (optional)
        image.save("timetable.png", "png")
        print("Timetable saved as 'timetable.png'")

        # Update the label when the timetable is saved
        self.save_label["text"] = "Timetable saved as 'timetable.png'"

    def create_timetable_image(self):
        cell_width = 120
        cell_height = 40

        image_width = cell_width * (len(self.days) + 1)
        image_height = cell_height * (len(self.periods) + 1)

        image = Image.new("RGB", (image_width, image_height), "white")
        draw = ImageDraw.Draw(image)

        # Draw day labels
        for i, day in enumerate([""] + self.days):
            draw.rectangle([i * cell_width, 0, (i + 1) * cell_width, cell_height], outline="black", width=2)
            draw.text(((i + 0.5) * cell_width, cell_height // 2), day, fill="black", anchor="mm")

        # Draw period labels and class information
        for i, period in enumerate(self.periods):
            draw.rectangle([0, (i + 1) * cell_height, cell_width, (i + 2) * cell_height], outline="black", width=2)
            draw.text((cell_width // 2, (i + 1.5) * cell_height), period, fill="black", anchor="mm")

            for j, day in enumerate(self.days):
                class_info = self.class_info[day][period]
                draw.rectangle(
                    [(j + 1) * cell_width, (i + 1) * cell_height, (j + 2) * cell_width, (i + 2) * cell_height],
                    outline="black", width=2)
                draw.text(((j + 1.5) * cell_width, (i + 1.5) * cell_height), class_info, fill="black", anchor="mm")

        return image


if __name__ == "__main__":
    root = tk.Tk()
    app = TimetableApp(root)
    root.mainloop()
