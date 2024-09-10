from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLineEdit, QListWidget

def apply_theme(widget):
    widget.setStyleSheet("""
        QWidget {
            background-color: #F5F5F5;
            color: #333333;
            font-family: 'Helvetica Neue', 'Open Sans', sans-serif;
            font-size: 14px;
        }
        QPushButton {
            background-color: #FF6F61;
            color: #FFFFFF;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            font-size: 14px;
            margin: 4px 2px;
            border-radius: 4px;
        }
        QPushButton:hover {
            background-color: #E5635C;
        }
        QPushButton:pressed {
            background-color: #CC5750;
        }
        QLineEdit {
            background-color: #FFFFFF;
            color: #333333;
            border: 1px solid #CCCCCC;
            padding: 8px;
            border-radius: 4px;
        }
        QListWidget {
            background-color: #FFFFFF;
            color: #333333;
            border: 1px solid #CCCCCC;
            border-radius: 4px;
        }
        QListWidget::item {
            padding: 8px;
        }
        QListWidget::item:selected {
            background-color: #4ECDC4;
            color: #FFFFFF;
        }
        QProgressBar {
            background-color: #FFFFFF;
            border: 1px solid #CCCCCC;
            border-radius: 4px;
            text-align: center;
        }
        QProgressBar::chunk {
            background-color: #4ECDC4;
            width: 10px;
            margin: 0.5px;
        }
        QRadioButton::indicator {
            width: 18px;
            height: 18px;
        }
        QRadioButton::indicator::unchecked {
            border: 2px solid #4ECDC4;
            background-color: #FFFFFF;
            border-radius: 9px;
        }
        QRadioButton::indicator::checked {
            border: 2px solid #4ECDC4;
            background-color: #4ECDC4;
            border-radius: 9px;
        }
        QLabel {
            color: #333333;
            font-weight: bold;
        }
        QSplitter::handle {
            background-color: #F7E8D5;
        }
    """)
    
    # Set bold font for specific widgets
    bold_font = QFont("Helvetica Neue")
    bold_font.setBold(True)
    widget.setFont(bold_font)

    # Apply regular font to QLineEdit and QListWidget
    regular_font = QFont("Open Sans")
    regular_font.setBold(False)
    for child in widget.findChildren(QLineEdit):
        child.setFont(regular_font)
    for child in widget.findChildren(QListWidget):
        child.setFont(regular_font)