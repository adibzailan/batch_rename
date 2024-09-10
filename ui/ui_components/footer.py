from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QFrame
from PyQt6.QtCore import Qt

class FooterWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 10, 20, 10)
        layout.setSpacing(10)

        # Version label
        version_label = QLabel("Alpha 1.1.0")
        version_label.setObjectName("footerLabel")

        # Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.VLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        separator.setObjectName("footerSeparator")

        # Location and creator label with link
        footer_text = QLabel('Built in Singapore, <a href="https://www.linkedin.com/in/adibzailan/" style="color: #4ECDC4; text-decoration: none;">AZ</a>')
        footer_text.setOpenExternalLinks(True)
        footer_text.setObjectName("footerText")

        # Add widgets to layout
        layout.addWidget(version_label)
        layout.addWidget(separator)
        layout.addWidget(footer_text)
        layout.addStretch()

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
            #footerSeparator {
                background-color: #CCCCCC;
            }
            #footerText a {
                color: #4ECDC4;
            }
        """)

        self.setFixedHeight(40)  # Set a fixed height for the footer