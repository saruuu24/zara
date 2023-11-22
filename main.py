import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
class FileOpenerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set up the layout
        main_layout = QVBoxLayout()

        # Add an icon for the program
        self.setWindowIcon(QIcon("logo.png"))

        # Add a QLabel for displaying a GIF
        gif_label = QLabel(self)
        gif_pixmap = QPixmap("zara.gif")
        gif_label.setPixmap(gif_pixmap)
        gif_label.setAlignment(Qt.AlignCenter)

        # Define the button names, icons, and file names
        button_info = [
            ("Button 1", "icon1.png", "script1.py"),
            ("Button 2", "icon2.png", "script2.py"),
            ("Button 3", "icon3.png", "script3.py"),
            ("Button 4", "icon4.png", "script4.py"),
            ("Button 5", "icon5.png", "script5.py"),
            ("Button 6", "icon6.png", "script6.py"),
            ("Button 7", "icon7.png", "script7.py"),
            ("Button 8", "icon8.png", "script8.py"),
        ]

        for name, icon_file, file_name in button_info:
            button = QPushButton(name, self)
            icon = QIcon(icon_file)
            button.setIcon(icon)
            button.setIconSize(icon.actualSize(icon.availableSizes()[0]))  # Set the icon size
            button.clicked.connect(lambda _, file=file_name: self.openFile(file))
            main_layout.addWidget(button)

        # Add the GIF label above the first row of buttons
        main_layout.addWidget(gif_label)

        self.setLayout(main_layout)

        # Set up the main window
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('File Opener App')
        self.show()

    def openFile(self, file_name):
        # Check if the file exists in the program directory
        if os.path.isfile(file_name):
            os.system(f"python {file_name}")
        else:
            print(f"File '{file_name}' not found in the program directory.")

if __name__ == '__main__':
    app = QApplication([])
    ex = FileOpenerApp()
    app.exec_()
