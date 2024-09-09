from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLabel, QPushButton

class FileListWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        file_list_layout = QHBoxLayout()
        self.file_list = QListWidget()
        self.file_list.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        self.preview_list = QListWidget()

        file_list_layout.addWidget(QLabel("Files:"))
        file_list_layout.addWidget(self.file_list)
        file_list_layout.addWidget(QLabel("Preview:"))
        file_list_layout.addWidget(self.preview_list)

        layout.addLayout(file_list_layout)

        button_layout = QHBoxLayout()
        select_all_button = QPushButton("Select All")
        select_all_button.clicked.connect(self.select_all_files)
        select_none_button = QPushButton("Select None")
        select_none_button.clicked.connect(self.select_no_files)

        button_layout.addWidget(select_all_button)
        button_layout.addWidget(select_none_button)

        layout.addLayout(button_layout)

    def select_all_files(self):
        for i in range(self.file_list.count()):
            self.file_list.item(i).setSelected(True)
        if self.parent():
            self.parent().update_preview()

    def select_no_files(self):
        for i in range(self.file_list.count()):
            self.file_list.item(i).setSelected(False)
        if self.parent():
            self.parent().update_preview()

    def get_selected_items(self):
        return self.file_list.selectedItems()

    def clear_and_add_files(self, files):
        self.file_list.clear()
        self.file_list.addItems(files)

    def clear_preview(self):
        self.preview_list.clear()

    def add_preview_item(self, item):
        self.preview_list.addItem(item)