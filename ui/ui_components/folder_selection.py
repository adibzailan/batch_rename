from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLineEdit, QLabel, QFileDialog

class FolderSelectionWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QHBoxLayout(self)
        self.folder_label = QLabel("Select Folder:")
        self.folder_entry = QLineEdit()
        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.select_folder)

        layout.addWidget(self.folder_label)
        layout.addWidget(self.folder_entry)
        layout.addWidget(self.browse_button)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.folder_entry.setText(folder)
            if self.parent():
                self.parent().update_file_list()

    def get_folder_path(self):
        return self.folder_entry.text()