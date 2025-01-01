from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QLabel, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal

class FileListWidget(QWidget):
    selection_changed = pyqtSignal()  # Signal for selection changes
    
    def __init__(self, parent=None, is_preview=False):
        super().__init__(parent)
        self.is_preview = is_preview
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Add label
        self.label = QLabel("Preview:" if self.is_preview else "Files:")
        layout.addWidget(self.label)
        
        # File list
        self.file_list = QListWidget()
        if self.is_preview:
            self.file_list.setSelectionMode(QListWidget.SelectionMode.NoSelection)
        else:
            self.file_list.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
            self.file_list.itemChanged.connect(lambda: self.selection_changed.emit())
        layout.addWidget(self.file_list)
        
        # Only add buttons if this is not a preview widget
        if not self.is_preview:
            button_layout = QHBoxLayout()
            self.select_all_button = QPushButton("Select All")
            self.deselect_all_button = QPushButton("Deselect All")
            
            # Style buttons
            button_style = """
                QPushButton {
                    background: #FF7F7F;
                    color: black;
                    border: none;
                    padding: 6px 12px;
                    border-radius: 4px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background: #FF9999;
                }
                QPushButton:disabled {
                    background: #FFB3B3;
                    color: rgba(0, 0, 0, 0.5);
                }
            """
            self.select_all_button.setStyleSheet(button_style)
            self.deselect_all_button.setStyleSheet(button_style)
            
            self.select_all_button.clicked.connect(self.select_all_files)
            self.deselect_all_button.clicked.connect(self.deselect_all_files)
            button_layout.addWidget(self.select_all_button)
            button_layout.addWidget(self.deselect_all_button)
            layout.addLayout(button_layout)
        
    def clear(self):
        self.file_list.clear()
        
    def add_item(self, text):
        if self.is_preview:
            item = QListWidgetItem(text)
        else:
            item = QListWidgetItem(text)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Unchecked)
        self.file_list.addItem(item)
        
    def clear_and_add_files(self, files):
        self.clear()
        for file in files:
            self.add_item(file)
            
    def get_selected_items(self):
        if self.is_preview:
            return []
        return [
            self.file_list.item(i) for i in range(self.file_list.count())
            if self.file_list.item(i).checkState() == Qt.CheckState.Checked
        ]
        
    def get_all_items(self):
        return [self.file_list.item(i) for i in range(self.file_list.count())]
        
    def select_all_files(self):
        if not self.is_preview:
            for i in range(self.file_list.count()):
                self.file_list.item(i).setCheckState(Qt.CheckState.Checked)
            self.selection_changed.emit()
            
    def deselect_all_files(self):
        if not self.is_preview:
            for i in range(self.file_list.count()):
                self.file_list.item(i).setCheckState(Qt.CheckState.Unchecked)
            self.selection_changed.emit()