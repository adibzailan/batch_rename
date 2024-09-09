import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QMessageBox
from PyQt6.QtCore import Qt
from .rename_worker import RenameWorker
from .ui_components.folder_selection import FolderSelectionWidget
from .ui_components.file_list import FileListWidget
from .ui_components.rename_options import RenameOptionsWidget
from .ui_components.action_buttons import ActionButtonsWidget
from .ui_components.progress_bar import ProgressBarWidget
from .ui_components.footer import FooterWidget
from .utils.theme import apply_theme
from core.file_operations import FileOperations

class BatchRenameUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Batch Rename Files")
        self.setGeometry(100, 100, 800, 600)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        
        self.original_names = []
        self.setup_ui()
        apply_theme(self)
        
    def setup_ui(self):
        self.folder_selection = FolderSelectionWidget(self)
        self.file_list = FileListWidget(self)
        self.rename_options = RenameOptionsWidget(self)
        self.action_buttons = ActionButtonsWidget(self)
        self.progress_bar = ProgressBarWidget(self)
        self.footer = FooterWidget(self)
        
        self.layout.addWidget(self.folder_selection)
        self.layout.addWidget(self.file_list)
        self.layout.addWidget(self.rename_options)
        self.layout.addWidget(self.action_buttons)
        self.layout.addWidget(self.progress_bar)
        self.layout.addWidget(self.footer)
        
        # Connect signals
        self.action_buttons.rename_button.clicked.connect(self.batch_rename_files)
        self.action_buttons.undo_button.clicked.connect(self.undo_rename)
        self.file_list.file_list.itemSelectionChanged.connect(self.update_preview)
        
    def update_file_list(self):
        folder_path = self.folder_selection.get_folder_path()
        if folder_path:
            files = FileOperations.get_files_in_folder(folder_path)
            self.file_list.clear_and_add_files(files)
    
    def update_preview(self):
        self.file_list.clear_preview()
        selected_items = self.file_list.get_selected_items()
        for item in selected_items:
            filename = item.text()
            new_filename = self.apply_rename_operation(filename)
            if new_filename != filename:
                self.file_list.add_preview_item(f"{filename} -> {new_filename}")
            else:
                self.file_list.add_preview_item(f"{filename} (no change)")
    
    def apply_rename_operation(self, filename):
        operation, param1, param2 = self.rename_options.get_rename_operation()
        if operation == "prefix_suffix":
            name, ext = os.path.splitext(filename)
            return f"{param1}{name}{param2}{ext}"
        else:
            return filename.replace(param1, param2)
    
    def batch_rename_files(self):
        folder_path = self.folder_selection.get_folder_path()
        if not folder_path:
            QMessageBox.warning(self, "Error", "Please select a folder.")
            return
        
        selected_items = self.file_list.get_selected_items()
        if not selected_items:
            QMessageBox.warning(self, "Error", "Please select at least one file.")
            return
        
        self.original_names = [item.text() for item in selected_items]
        self.progress_bar.set_maximum(len(self.original_names))
        self.progress_bar.set_value(0)
        
        self.rename_worker = RenameWorker(folder_path, self.original_names, self.apply_rename_operation)
        self.rename_worker.progress.connect(self.update_progress)
        self.rename_worker.finished.connect(self.rename_finished)
        self.rename_worker.error.connect(self.show_error)
        self.rename_worker.start()
        
        self.action_buttons.enable_rename_button(False)
        self.action_buttons.enable_undo_button(False)
    
    def update_progress(self, value):
        self.progress_bar.set_value(value)
    
    def rename_finished(self):
        self.action_buttons.enable_rename_button(True)
        self.action_buttons.enable_undo_button(True)
        self.update_file_list()
        QMessageBox.information(self, "Success", "Files renamed successfully!")
    
    def show_error(self, error_message):
        QMessageBox.critical(self, "Error", f"An error occurred: {error_message}")
        self.action_buttons.enable_rename_button(True)
    
    def undo_rename(self):
        folder_path = self.folder_selection.get_folder_path()
        current_files = os.listdir(folder_path)
        
        for original, current in zip(self.original_names, current_files):
            if original != current:
                try:
                    FileOperations.rename_file(folder_path, current, original)
                except Exception as e:
                    QMessageBox.critical(self, "Undo Error", f"Error reverting {current} to {original}: {str(e)}")
        
        self.action_buttons.enable_undo_button(False)
        self.update_file_list()
        QMessageBox.information(self, "Undo Complete", "Files have been reverted to their original names.")