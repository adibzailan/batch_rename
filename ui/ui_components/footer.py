from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel

class FooterWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout(self)
        footer_text = QLabel("Alpha 1.0.0 | Built in Singapore, ")
        footer_link = QLabel('<a href="https://www.linkedin.com/in/adibzailan/">AZ</a>')
        footer_link.setOpenExternalLinks(True)

        layout.addWidget(footer_text)
        layout.addWidget(footer_link)
        layout.addStretch()