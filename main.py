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
    QSizePolicy,
)
from PySide6.QtCore import Qt


# ============================================================
# SAYI ÜRETİCİLERİ
# ============================================================

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

        # Telefonda daha uygun boşluklar
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(12)

        # Başlık
        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setObjectName("panelTitle")

        # Sonuç
        self.result = QLabel("—")
        self.result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result.setWordWrap(True)
        self.result.setObjectName("result")

        # Sonucun paneli taşırmamasını sağla
        self.result.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )

        # Buton
        button = QPushButton("SAYI ÜRET")
        button.setMinimumHeight(52)
        button.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed
        )
        button.setObjectName("generateButton")

        button.clicked.connect(self.generate)

        layout.addWidget(title_label)
        layout.addStretch(1)
        layout.addWidget(self.result)
        layout.addStretch(1)
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

        # SABİT 1100x700 kaldırıldı.
        # Android pencereyi kendi ekranına göre boyutlandıracak.

        main_layout = QVBoxLayout()

        # Telefon için daha küçük kenar boşlukları
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(15)

        # ====================================================
        # ANA BAŞLIK
        # ====================================================

        title = QLabel("RASTGELE SAYI ÜRETİCİ")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setWordWrap(True)
        title.setObjectName("mainTitle")

        main_layout.addWidget(title)

        # ====================================================
        # 2x2 GRID
        # ====================================================

        self.grid = QGridLayout()
        self.grid.setSpacing(15)

        self.panel1 = LotteryPanel(
            "5 + 1 LOTO",
            generate_5_plus_1
        )

        self.panel2 = LotteryPanel(
            "SAYISAL LOTO",
            generate_sayisal
        )

        self.panel3 = LotteryPanel(
            "6 / 60",
            generate_6_60
        )

        self.panel4 = LotteryPanel(
            "10 / 80",
            generate_10_80
        )

        self.grid.addWidget(self.panel1, 0, 0)
        self.grid.addWidget(self.panel2, 0, 1)
        self.grid.addWidget(self.panel3, 1, 0)
        self.grid.addWidget(self.panel4, 1, 1)

        main_layout.addLayout(self.grid)

        self.setLayout(main_layout)

        # İlk açılışta telefon düzenini uygula
        self.update_layout()

    # ========================================================
    # EKRAN GENİŞLİĞİNE GÖRE DÜZEN
    # ========================================================

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_layout()

    def update_layout(self):

        width = self.width()

        # Telefon / dar ekran
        if width < 700:

            self.grid.addWidget(self.panel1, 0, 0, 1, 1)
            self.grid.addWidget(self.panel2, 1, 0, 1, 1)
            self.grid.addWidget(self.panel3, 2, 0, 1, 1)
            self.grid.addWidget(self.panel4, 3, 0, 1, 1)

        # Tablet / geniş ekran
        else:

            self.grid.addWidget(self.panel1, 0, 0)
            self.grid.addWidget(self.panel2, 0, 1)
            self.grid.addWidget(self.panel3, 1, 0)
            self.grid.addWidget(self.panel4, 1, 1)


# ============================================================
# UYGULAMA
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
        font-size: 26px;
        font-weight: bold;
        padding: 8px;
    }

    #lotteryPanel {
        background-color: white;
        border: 1px solid #d0d0d0;
        border-radius: 15px;
    }

    #panelTitle {
        font-size: 21px;
        font-weight: bold;
    }

    #result {
        font-size: 23px;
        font-weight: bold;
        min-height: 70px;
    }

    #generateButton {
        background-color: #222222;
        color: white;
        border: none;
        border-radius: 10px;
        font-size: 17px;
        font-weight: bold;
        min-height: 52px;
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
