from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QFrame
from PyQt6.QtCore import Qt

class FooterWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 5, 10, 5)
        layout.setSpacing(10)

        # Version label
        version_label = QLabel("v1.3.5")
        version_label.setObjectName("footerLabel")

        # Creator label with link
        creator_label = QLabel()
        creator_label.setText('<a href="https://github.com/adibzailan" style="color: #FF7F7F; text-decoration: none;">Adib Zailan</a>')
        creator_label.setOpenExternalLinks(True)
        creator_label.setObjectName("footerText")

        # Add widgets to layout
        layout.addWidget(version_label)
        layout.addStretch()
        layout.addWidget(creator_label)

        # Set overall widget style
        self.setStyleSheet("""
            QWidget {
                background-color: #F5F5F5;
                color: #333333;
                font-family: 'Helvetica Neue', 'Open Sans', sans-serif;
                font-size: 12px;
            }
            #footerLabel, #footerText {
                color: #333333;
            }
            #footerText a {
                color: #FF7F7F;
            }
        """)

        self.setFixedHeight(40)  # Set a fixed height for the footer