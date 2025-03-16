import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton
from PySide6.QtCore import Slot

@Slot()
def say_hello():
    print("Hellooo")

app = QApplication(sys.argv)

label = QLabel("Hello World!")
label.show()

button = QPushButton("Clicka")
button.clicked.connect(say_hello)
button.show()

app.exec()