import sys
import os
import logging
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QProgressBar
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFontDatabase

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        logging.info("Initializing SplashScreen")
        self.setWindowTitle('Studio Merpati')
        self.setFixedSize(400, 300)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.counter = 0
        self.n = 100  # total number of iterations for loading

        self.load_fonts()
        self.initUI()

        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(30)
        logging.info("SplashScreen initialization completed")

    def load_fonts(self):
        logging.info("Loading fonts")
        resources_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resources', 'fonts'))
        font_files = [
            'CEREBRI SANS BOLD.TTF',
            'CEREBRI SANS BOLD ITALIC.TTF',
            'CEREBRI SANS BOOK.TTF',
            'CEREBRI SANS ITALIC.TTF'
        ]
        
        for font_file in font_files:
            font_path = os.path.join(resources_path, font_file)
            if os.path.exists(font_path):
                font_id = QFontDatabase.addApplicationFont(font_path)
                if font_id == -1:
                    logging.warning(f"Failed to load font: {font_file}")
                else:
                    logging.info(f"Successfully loaded font: {font_file}")
            else:
                logging.warning(f"Font file not found: {font_file}")
        logging.info("Font loading completed")

    def initUI(self):
        logging.info("Initializing UI components")
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Wordmark
        self.wordmark = QLabel("STUDIO MERPATI")
        self.wordmark.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.wordmark.setStyleSheet("""
            font-family: 'Cerebri Sans', Arial, sans-serif;
            font-size: 32px;
            font-weight: bold;
            color: #FF6F61;
            letter-spacing: 2px;
        """)
        layout.addWidget(self.wordmark)

        # Spacer
        spacer = QLabel()
        spacer.setFixedHeight(20)
        layout.addWidget(spacer)

        # Loading Text
        self.loading_text = QLabel("Loading...")
        self.loading_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loading_text.setStyleSheet("""
            font-family: 'Cerebri Sans', Arial, sans-serif;
            font-size: 14px;
            color: #333333;
        """)
        layout.addWidget(self.loading_text)

        # Progress Bar
        self.progress = QProgressBar()
        self.progress.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progress.setFormat('%p%')
        self.progress.setStyleSheet("""
            QProgressBar {
                background-color: #F5F5F5;
                color: #333333;
                border-radius: 4px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #FF6F61;
                border-radius: 4px;
            }
        """)
        layout.addWidget(self.progress)

        self.setStyleSheet("""
            background-color: #F5F5F5;
            border-radius: 8px;
        """)

        logging.info("UI components initialized")

    def loading(self):
        self.progress.setValue(self.counter)

        if self.counter >= self.n:
            self.timer.stop()
            logging.info("Splash screen loading completed")
            self.close()

        self.counter += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()
    logging.info("Splash screen displayed")
    sys.exit(app.exec())