from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton

class ActionButtonsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout(self)
        self.rename_button = QPushButton("Rename Files")
        self.undo_button = QPushButton("Undo Rename")
        self.undo_button.setEnabled(False)

        layout.addWidget(self.rename_button)
        layout.addWidget(self.undo_button)

    def enable_rename_button(self, enabled):
        self.rename_button.setEnabled(enabled)

    def enable_undo_button(self, enabled):
        self.undo_button.setEnabled(enabled)