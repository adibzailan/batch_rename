from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLineEdit, QListWidget

def apply_theme(widget):
    widget.setStyleSheet("""
        QWidget {
            background-color: #F5F5F5;
            color: #333333;
            font-family: 'Segoe UI', 'Helvetica', 'Arial', sans-serif;
            font-size: 14px;
        }
        QPushButton {
            background-color: #4A90E2;
            color: #FFFFFF;
            border: none;
            padding: 8px 16px;
            text-align: center;
            text-decoration: none;
            font-size: 14px;
            margin: 4px 2px;
            border-radius: 4px;
        }
        QPushButton:hover {
            background-color: #357ABD;
        }
        QPushButton:pressed {
            background-color: #2A5F8E;
        }
        QLineEdit {
            background-color: #FFFFFF;
            color: #333333;
            border: 1px solid #CCCCCC;
            padding: 5px;
            border-radius: 4px;
        }
        QListWidget {
            background-color: #FFFFFF;
            color: #333333;
            border: 1px solid #CCCCCC;
            border-radius: 4px;
        }
        QListWidget::item {
            padding: 5px;
        }
        QListWidget::item:selected {
            background-color: #E1F0FF;
            color: #333333;
        }
        QProgressBar {
            background-color: #FFFFFF;
            border: 1px solid #CCCCCC;
            border-radius: 4px;
            text-align: center;
        }
        QProgressBar::chunk {
            background-color: #4A90E2;
            width: 10px;
            margin: 0.5px;
        }
        QRadioButton::indicator {
            width: 18px;
            height: 18px;
        }
        QRadioButton::indicator::unchecked {
            border: 2px solid #4A90E2;
            background-color: #FFFFFF;
            border-radius: 9px;
        }
        QRadioButton::indicator::checked {
            border: 2px solid #4A90E2;
            background-color: #4A90E2;
            border-radius: 9px;
        }
        QLabel {
            color: #333333;
            font-weight: bold;
        }
    """)
    
    # Set bold font for specific widgets
    bold_font = QFont()
    bold_font.setBold(True)
    widget.setFont(bold_font)

    # Apply regular font to QLineEdit and QListWidget
    regular_font = QFont()
    regular_font.setBold(False)
    for child in widget.findChildren(QLineEdit):
        child.setFont(regular_font)
    for child in widget.findChildren(QListWidget):
        child.setFont(regular_font)