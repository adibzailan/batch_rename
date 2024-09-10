from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLineEdit, QLabel, QFileDialog
from PyQt6.QtCore import pyqtSignal

class FolderSelectionWidget(QWidget):
    folder_selected = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.folder_label = QLabel("Select Folder:")
        self.folder_entry = QLineEdit()
        self.folder_entry.setPlaceholderText("Choose a folder...")
        self.browse_button = QPushButton("Browse")
        self.browse_button.setFixedWidth(100)
        self.browse_button.clicked.connect(self.select_folder)

        layout.addWidget(self.folder_label)
        layout.addWidget(self.folder_entry, 1)  # Give more space to the line edit
        layout.addWidget(self.browse_button)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.folder_entry.setText(folder)
            self.folder_selected.emit(folder)

    def get_folder_path(self):
        return self.folder_entry.text()