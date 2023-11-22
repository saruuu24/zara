import tkinter as tk
from tkinter import ttk
import pyttsx3

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech App")
        self.root.geometry("400x250")

        # Available voices
        self.voices = self.get_available_voices()

        if not self.voices:
            tk.messagebox.showerror("Error", "No voices available.")
            self.root.destroy()
            return

        self.create_widgets()

    def create_widgets(self):
        # Text input
        self.text_label = ttk.Label(self.root, text="Enter Text:")
        self.text_label.pack(pady=10)

        self.text_entry = ttk.Entry(self.root, width=40)
        self.text_entry.pack(pady=10)

        # Voice selection
        self.voice_label = ttk.Label(self.root, text="Select Voice:")
        self.voice_label.pack(pady=5)

        self.voice_combobox = ttk.Combobox(self.root, values=self.voices, state="readonly")
        self.voice_combobox.pack(pady=10)
        self.voice_combobox.set(self.voices[0])  # Set the default voice

        # Speak button
        self.speak_button = ttk.Button(self.root, text="Speak", command=self.speak_text)
        self.speak_button.pack(pady=10)

    def get_available_voices(self):
        # Get the available voices
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        return [f"{voice.name} ({voice.languages[0]}, {voice.gender})" for voice in voices] if voices else []

    def speak_text(self):
        text_to_speak = self.text_entry.get()
        selected_voice_name = self.voice_combobox.get().split(" (")[0]

        # Initialize the text-to-speech engine
        engine = pyttsx3.init()

        # Set the selected voice
        for voice in engine.getProperty('voices'):
            if voice.name == selected_voice_name:
                engine.setProperty('voice', voice.id)
                break

        # Set properties (optional)
        engine.setProperty('rate', 150)  # Speed of speech

        # Speak the text
        engine.say(text_to_speak)

        # Wait for the speech to finish
        engine.runAndWait()

if __name__ == "__main__":
    root = tk.Tk()

    # Use a different theme (e.g., "clam")
    style = ttk.Style()
    style.theme_use("clam")

    app = TextToSpeechApp(root)
    root.mainloop()
