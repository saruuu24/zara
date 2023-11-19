import tkinter as tk
import time
from math import cos, sin, pi
from tkinter import ttk, messagebox
from ttkbootstrap import Style
from PIL import Image, ImageTk

class AnimatedClock(tk.Label):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.angle = 0
        self.image_sequence = [ImageTk.PhotoImage(Image.open(f"clock{i}.gif")) for i in range(1,29)]
        self.after_id = None
        self.current_frame = 0

    def start_animation(self):
        self.after_id = self.after(50, self.update_clock)

    def stop_animation(self):
        if self.after_id:
            self.after_cancel(self.after_id)
            self.after_id = None

    def update_clock(self):
        self.current_frame = (self.current_frame + 1) % len(self.image_sequence)
        self.config(image=self.image_sequence[self.current_frame])
        self.after_id = self.after(50, self.update_clock)

class FocusTimerApp:
    def __init__(self, master):
        self.master = master
        master.title("Focus Timer")

        style = Style('flatly')  # You can choose a different theme from ttkbootstrap

        self.minutes_label = ttk.Label(master, text="Minutes:")
        self.minutes_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        self.minutes_entry = ttk.Entry(master, width=5)
        self.minutes_entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        self.start_button = ttk.Button(master, text="Start", command=self.start_timer)
        self.start_button.grid(row=0, column=2, pady=10, padx=10)

        self.timer_label = ttk.Label(master, text="Timer: 00:00")
        self.timer_label.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

        self.animated_clock = AnimatedClock(master)
        self.animated_clock.grid(row=2, column=1, pady=10)

        self.running = False
        self.remaining_time = 0
        self.end_time = 0

    def start_timer(self):
        if self.running:
            self.show_message("Timer is already running.")
            return

        try:
            minutes = int(self.minutes_entry.get())
            if minutes <= 0:
                raise ValueError("Please enter a valid positive number of minutes.")

            self.remaining_time = minutes * 60
            self.end_time = time.time() + self.remaining_time

            self.running = True
            self.update_timer()
            self.animated_clock.start_animation()
        except ValueError as e:
            self.show_message(f"Error: {e}")

    def update_timer(self):
        if self.running:
            current_time = int(self.end_time - time.time())
            if current_time <= 0:
                self.running = False
                self.show_message("Focus time is over!")
                self.animated_clock.stop_animation()

            minutes = current_time // 60
            seconds = current_time % 60
            timer_text = f"Timer: {minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=timer_text)
            self.master.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Timer: 00:00")

    def show_message(self, message):
        messagebox.showinfo("Message", message)

def main():
    root = tk.Tk()
    style = Style('vapor')  # You can choose a different theme from ttkbootstrap
    app = FocusTimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
