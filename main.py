import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QComboBox, QTextEdit
from PyQt5.QtCore import Qt
import pyttsx3
from gtts import gTTS
import os

class TTSApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Set up the main layout
        main_layout = QVBoxLayout()

        # Text input area
        self.text_edit = QTextEdit(self)
        main_layout.addWidget(self.text_edit)

        # Voice selection
        voice_layout = QHBoxLayout()
        voice_label = QLabel("Select Voice:")
        self.voice_combobox = QComboBox(self)
        self.populate_voices()
        voice_layout.addWidget(voice_label)
        voice_layout.addWidget(self.voice_combobox)
        main_layout.addLayout(voice_layout)

        # Buttons
        button_layout = QHBoxLayout()
        self.speak_button = QPushButton("Speak", self)
        self.speak_button.clicked.connect(self.speak_text)
        button_layout.addWidget(self.speak_button)

        # Add layouts to the main layout
        main_layout.addLayout(button_layout)

        # Set the main layout
        self.setLayout(main_layout)

        # Set the window properties
        self.setWindowTitle('Text-to-Speech App')
        self.setGeometry(100, 100, 600, 400)

        # Show the window
        self.show()

    def populate_voices(self):
        # Clear the combobox before populating
        self.voice_combobox.clear()

        # Use pyttsx3 to get available voices
        engine = pyttsx3.init()
        pyttsx3_voices = engine.getProperty('voices')

        # Use gTTS to get available voices
        gtts_voices = ['en', 'es', 'fr']  # Add language codes as needed

        # Populate the ComboBox with pyttsx3 voices
        for voice in pyttsx3_voices:
            self.voice_combobox.addItem(f"pyttsx3: {voice.name}")

        # Populate the ComboBox with gTTS voices
        for voice in gtts_voices:
            self.voice_combobox.addItem(f"gTTS: {voice}")

    def speak_text(self):
        # Get the selected voice
        selected_voice = self.voice_combobox.currentText()

        # Determine the TTS engine based on the voice selection
        if selected_voice.startswith("pyttsx3"):
            engine = pyttsx3.init()
            engine.setProperty('voice', selected_voice.split(":")[1].strip())
            text_to_speak = self.text_edit.toPlainText()
            engine.say(text_to_speak)
            engine.runAndWait()
        elif selected_voice.startswith("gTTS"):
            language_code = selected_voice.split(":")[1].strip()
            text_to_speak = self.text_edit.toPlainText()
            tts = gTTS(text=text_to_speak, lang=language_code, slow=False)
            tts.save("temp.mp3")
            os.system("start temp.mp3")  # Open the default media player to play the audio
        else:
            print("Unknown TTS engine")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tts_app = TTSApp()
    sys.exit(app.exec_())
