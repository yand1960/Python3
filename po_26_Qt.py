from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setFixedHeight(150)
        self.setFixedWidth(300)
        # Сделать так, чтобы надпись в заголовке окна была "Demo" (11:17)
        self.setWindowTitle("Demo")

        self.button = QPushButton(parent=self)
        self.button.setText("Click me")
        self.button.setGeometry(10, 10, 280, 130)
        self.button.clicked.connect(self.button_click)

        self.show()

    def button_click(self):
        # print("Hello, world!")
        # Как сделать так, чтобы надпись появлялась на самой кнопке
        self.button.setText("Hello, world!")

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    app.exec()
