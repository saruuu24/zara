import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize

class FileOpenerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # Set up the layout
        main_layout = QVBoxLayout()

        # Add a centered title
        title_label = QLabel("Zara - A simple app for students", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont("Gabriola", 20, QFont.Bold)
        title_label.setFont(title_font)
        main_layout.addWidget(title_label)

        # Add buttons in rows of four
        button_grid_layout = QGridLayout()

        # Define the button names, icons, and file names
        button_info = [
            ("Locally save videos", "icon1.png", "script1.py"),
            ("Focus Mode", "icon2.png", "script2.py"),
            ("Sticky notes", "icon3.png", "script3.py"),
            ("Timetable generator", "icon4.png", "script4.py"),
            ("Summarize news articles", "icon5.png", "script5.py"),
            ("Create todo list", "icon6.png", "script6.py"),
            ("Voice assistant", "icon7.png", "script7.py"),
            ("Morse Code decrypter (its useless)", "icon8.png", "script8.py"),
        ]
        row, col = 0, 0
        for name, icon_file, file_name in button_info:
            button = QPushButton(self)
            icon = QIcon(icon_file)
            button.setIcon(icon)
            button.setIconSize(QSize(256, 256))  # Set the custom icon size
            button.clicked.connect(lambda _, file=file_name: self.openFile(file))

            # Set up a QLabel for the button text below the icon
            label = QLabel(name, self)
            label.setAlignment(Qt.AlignCenter)

            # Remove the border around the button
            button.setStyleSheet("border: none;")

            # Add the icon and text to the layout
            button_layout = QVBoxLayout()
            button_layout.addWidget(button)
            button_layout.addWidget(label)

            button_grid_layout.addLayout(button_layout, row, col)

            col += 1
            if col > 3:
                col = 0
                row += 1

        main_layout.addLayout(button_grid_layout)

        self.setLayout(main_layout)

        # Set up the main window
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Zara')
        self.setWindowIcon(QIcon('zara.png'))
        # Apply the "Windows" style theme
        QApplication.setStyle("Windows")

        import ctypes
        myappid = 'saru.app.zara.0.1'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    def openFile(self, file_name):
        # Check if the file exists in the program directory
        if os.path.isfile(file_name):
            os.system(f"python {file_name}")
        else:
            print(f"File '{file_name}' not found in the program directory.")
if __name__ == '__main__':
    app = QApplication([])
    ex = FileOpenerApp()
    ex.show()
    app.exec_()