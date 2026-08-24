import sys
import random

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QPushButton,
    QFrame,
)
from PySide6.QtCore import Qt

def generate_5_plus_1():
    numbers = sorted(random.sample(range(1, 35), 5))
    bonus = random.randint(1, 14)

    return (
        "   ".join(f"{n:02d}" for n in numbers)
        + f"\n\n★ {bonus:02d}"
    )


def generate_sayisal():
    first_six = sorted(random.sample(range(1, 91), 6))

    seventh = random.randint(1, 90)

    return (
        "   ".join(f"{n:02d}" for n in first_six)
        + f"\n\n7. SAYI: {seventh:02d}"
    )


def generate_6_60():
    numbers = sorted(random.sample(range(1, 61), 6))

    return "   ".join(f"{n:02d}" for n in numbers)


def generate_10_80():
    numbers = sorted(random.sample(range(1, 81), 10))

    return "   ".join(f"{n:02d}" for n in numbers)


# ============================================================
# PANEL
# ============================================================

class LotteryPanel(QFrame):

    def __init__(self, title, generator):
        super().__init__()

        self.generator = generator

        self.setObjectName("lotteryPanel")

        layout = QVBoxLayout()
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(20)

        # Başlık
        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setObjectName("panelTitle")

        # Sonuç
        self.result = QLabel("—")
        self.result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result.setWordWrap(True)
        self.result.setObjectName("result")

        # Buton
        button = QPushButton("SAYI ÜRET")
        button.setCursor(Qt.CursorShape.PointingHandCursor)
        button.setMinimumHeight(55)
        button.setObjectName("generateButton")

        button.clicked.connect(self.generate)

        layout.addWidget(title_label)
        layout.addStretch()
        layout.addWidget(self.result)
        layout.addStretch()
        layout.addWidget(button)

        self.setLayout(layout)

    def generate(self):
        self.result.setText(self.generator())


# ============================================================
# ANA PENCERE
# ============================================================

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rastgele Sayı Üretici")
        self.resize(1100, 700)

        main_layout = QVBoxLayout()

        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(25)

        # Ana başlık
        title = QLabel("RASTGELE SAYI ÜRETİCİ")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setObjectName("mainTitle")

        main_layout.addWidget(title)

        # 2x2 grid
        grid = QGridLayout()
        grid.setSpacing(20)

        panel1 = LotteryPanel(
            "5 + 1 LOTO",
            generate_5_plus_1
        )

        panel2 = LotteryPanel(
            "SAYISAL LOTO",
            generate_sayisal
        )

        panel3 = LotteryPanel(
            "6 / 60",
            generate_6_60
        )

        panel4 = LotteryPanel(
            "10 / 80",
            generate_10_80
        )

        grid.addWidget(panel1, 0, 0)
        grid.addWidget(panel2, 0, 1)
        grid.addWidget(panel3, 1, 0)
        grid.addWidget(panel4, 1, 1)

        main_layout.addLayout(grid)

        self.setLayout(main_layout)


# ============================================================
# STİL
# ============================================================

app = QApplication(sys.argv)

app.setStyle("Fusion")

app.setStyleSheet("""
    QWidget {
        background-color: #f4f4f4;
        color: #202020;
        font-family: Arial;
    }

    #mainTitle {
        font-size: 30px;
        font-weight: bold;
        padding: 10px;
    }

    #lotteryPanel {
        background-color: white;
        border: 1px solid #d0d0d0;
        border-radius: 15px;
    }

    #panelTitle {
        font-size: 23px;
        font-weight: bold;
    }

    #result {
        font-size: 26px;
        font-weight: bold;
        min-height: 80px;
    }

    #generateButton {
        background-color: #222222;
        color: white;
        border: none;
        border-radius: 8px;
        font-size: 17px;
        font-weight: bold;
    }

    #generateButton:hover {
        background-color: #444444;
    }

    #generateButton:pressed {
        background-color: #111111;
    }
""")


window = MainWindow()
window.show()

sys.exit(app.exec())