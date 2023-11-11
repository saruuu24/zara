import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

# Morse Code Dictionary
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                  'C': '-.-.', 'D': '-..', 'E': '.',
                  'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-',
                  'L': '.-..', 'M': '--', 'N': '-.',
                  'O': '---', 'P': '.--.', 'Q': '--.-',
                  'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--',
                  'X': '-..-', 'Y': '-.--', 'Z': '--..',
                  '1': '.----', '2': '..---', '3': '...--',
                  '4': '....-', '5': '.....', '6': '-....',
                  '7': '--...', '8': '---..', '9': '----.',
                  '0': '-----', ',': '--..--', '.': '.-.-.-',
                  '?': '..--..', '/': '-..-.', '-': '-....-',
                  '(': '-.--.', ')': '-.--.-', ' ': '/'}

# Invert the dictionary for decoding
MORSE_CODE_DICT_REVERSE = {value: key for key, value in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += char
    return morse_code

def morse_to_text(morse_code):
    words = morse_code.split(' / ')
    decoded_text = ''
    for word in words:
        chars = word.split(' ')
        for char in chars:
            if char in MORSE_CODE_DICT_REVERSE:
                decoded_text += MORSE_CODE_DICT_REVERSE[char]
            else:
                decoded_text += char
        decoded_text += ' '
    return decoded_text.strip()

class MorseCodeTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Morse Code Translator")
        self.style = Style(theme="superhero")  # You can choose a different theme if you like

        self.create_widgets()

    def create_widgets(self):
        # Input Label and Entry (Text to Morse)
        self.input_label_text_to_morse = ttk.Label(self.root, text="Enter Text:")
        self.input_label_text_to_morse.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.input_entry_text_to_morse = ttk.Entry(self.root, width=30)
        self.input_entry_text_to_morse.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        # Output Label and Entry (Text to Morse)
        self.output_label_text_to_morse = ttk.Label(self.root, text="Morse Code:")
        self.output_label_text_to_morse.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.output_entry_text_to_morse = ttk.Entry(self.root, width=30, state="readonly")
        self.output_entry_text_to_morse.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        # Translate Button (Text to Morse)
        self.translate_button_text_to_morse = ttk.Button(self.root, text="Translate to Morse", command=self.translate_text_to_morse)
        self.translate_button_text_to_morse.grid(row=2, column=0, columnspan=2, pady=10)

        # Input Label and Entry (Morse to Text)
        self.input_label_morse_to_text = ttk.Label(self.root, text="Enter Morse Code:")
        self.input_label_morse_to_text.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

        self.input_entry_morse_to_text = ttk.Entry(self.root, width=30)
        self.input_entry_morse_to_text.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        # Output Label and Entry (Morse to Text)
        self.output_label_morse_to_text = ttk.Label(self.root, text="Decoded Text:")
        self.output_label_morse_to_text.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

        self.output_entry_morse_to_text = ttk.Entry(self.root, width=30, state="readonly")
        self.output_entry_morse_to_text.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)

        # Translate Button (Morse to Text)
        self.translate_button_morse_to_text = ttk.Button(self.root, text="Translate to Text", command=self.translate_morse_to_text)
        self.translate_button_morse_to_text.grid(row=5, column=0, columnspan=2, pady=10)

    def translate_text_to_morse(self):
        input_text = self.input_entry_text_to_morse.get()
        morse_code = text_to_morse(input_text)
        self.output_entry_text_to_morse.config(state="normal")
        self.output_entry_text_to_morse.delete(0, tk.END)
        self.output_entry_text_to_morse.insert(0, morse_code)
        self.output_entry_text_to_morse.config(state="readonly")

    def translate_morse_to_text(self):
        input_morse_code = self.input_entry_morse_to_text.get()
        decoded_text = morse_to_text(input_morse_code)
        self.output_entry_morse_to_text.config(state="normal")
        self.output_entry_morse_to_text.delete(0, tk.END)
        self.output_entry_morse_to_text.insert(0, decoded_text)
        self.output_entry_morse_to_text.config(state="readonly")

if __name__ == "__main__":
    root = tk.Tk()
    app = MorseCodeTranslatorApp(root)
    root.mainloop()
