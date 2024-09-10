from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QLabel, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt

class FileListWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # File list
        self.file_list = QListWidget()
        self.file_list.setSelectionMode(QListWidget.SelectionMode.ExtendedSelection)

        # Preview list
        self.preview_list = QListWidget()
        self.preview_list.setSelectionMode(QListWidget.SelectionMode.NoSelection)

        # Select/Deselect All buttons
        button_layout = QHBoxLayout()
        self.select_all_button = QPushButton("Select All")
        self.select_all_button.clicked.connect(self.select_all_files)
        self.deselect_all_button = QPushButton("Deselect All")
        self.deselect_all_button.clicked.connect(self.deselect_all_files)
        button_layout.addWidget(self.select_all_button)
        button_layout.addWidget(self.deselect_all_button)

        # Labels
        file_list_label = QLabel("Files:")
        preview_label = QLabel("Preview:")

        # Add widgets to layout
        layout.addWidget(file_list_label)
        layout.addWidget(self.file_list)
        layout.addLayout(button_layout)
        layout.addWidget(preview_label)
        layout.addWidget(self.preview_list)

    def clear_and_add_files(self, files):
        self.file_list.clear()
        for file in files:
            item = QListWidgetItem(file)
            self.file_list.addItem(item)

    def get_selected_items(self):
        return self.file_list.selectedItems()

    def clear_preview(self):
        self.preview_list.clear()

    def add_preview_item(self, text):
        self.preview_list.addItem(text)

    def select_all_files(self):
        self.file_list.selectAll()

    def deselect_all_files(self):
        self.file_list.clearSelection()