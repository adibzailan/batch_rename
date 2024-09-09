def apply_theme(widget):
    widget.setStyleSheet("""
        QWidget {
            background-color: #121212;
            color: #E0E0E0;
            font-family: 'Helvetica', 'Arial', sans-serif;
            font-size: 14px;
        }
        QPushButton {
            background-color: #FF6F61;
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
            background-color: #FF8A80;
        }
        QPushButton:pressed {
            background-color: #FF5252;
        }
        QLineEdit {
            background-color: #333333;
            color: #E0E0E0;
            border: 1px solid #555555;
            padding: 5px;
            border-radius: 4px;
        }
        QListWidget {
            background-color: #333333;
            color: #E0E0E0;
            border: 1px solid #555555;
            border-radius: 4px;
        }
        QProgressBar {
            background-color: #333333;
            border: 1px solid #555555;
            border-radius: 4px;
            text-align: center;
        }
        QProgressBar::chunk {
            background-color: #FF6F61;
            width: 10px;
            margin: 0.5px;
        }
        QRadioButton::indicator {
            width: 13px;
            height: 13px;
        }
        QRadioButton::indicator::unchecked {
            border: 2px solid #FF6F61;
            background-color: #121212;
            border-radius: 7px;
        }
        QRadioButton::indicator::checked {
            border: 2px solid #FF6F61;
            background-color: #FF6F61;
            border-radius: 7px;
        }
    """)