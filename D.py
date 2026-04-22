import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class App(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Квадратное уравнение")

        self.input_a = QLineEdit()
        self.input_a.setPlaceholderText("a")

        self.input_b = QLineEdit()
        self.input_b.setPlaceholderText("b")

        self.input_c = QLineEdit()
        self.input_c.setPlaceholderText("c")

        self.btn = QPushButton("Решить")
        self.btn.clicked.connect(self.solve)

        self.result = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.input_a)
        layout.addWidget(self.input_b)
        layout.addWidget(self.input_c)
        layout.addWidget(self.btn)
        layout.addWidget(self.result)

        self.setLayout(layout)

    def solve(self):
        try:
            a = float(self.input_a.text())
            b = float(self.input_b.text())
            c = float(self.input_c.text())
        except:
            self.result.setText("Ошибка ввода")
            return

        if a == 0:
            self.result.setText("a = 0 нельзя")
            return

        D = b**2 - 4*a*c

        answer = "D = " + str(D) + "\n"

        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            answer += "x1 = " + str(x1) + "\n"
            answer += "x2 = " + str(x2)
        elif D == 0:
            x = -b / (2 * a)
            answer += "x = " + str(x)
        else:
            answer += "нет корней"

        self.result.setText(answer)


app = QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec_())