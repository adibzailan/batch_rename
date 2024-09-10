import sys
import os
import logging
import tempfile
import shutil
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QFileDialog, QSplitter
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

# Set up logging
log_dir = tempfile.gettempdir()
log_path = os.path.join(log_dir, 'batch_rename.log')
logging.basicConfig(filename=log_path, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class BatchRenameUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Batch Rename Files")
        self.setGeometry(100, 100, 1000, 600)
        
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
        
        # Create a splitter for file list and preview
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.addWidget(self.file_list)
        splitter.addWidget(self.file_list.preview_list)
        splitter.setSizes([int(self.width() * 0.6), int(self.width() * 0.4)])

        # Main layout
        self.layout.addWidget(self.folder_selection)
        self.layout.addWidget(splitter)
        self.layout.addWidget(self.rename_options)
        
        # Action buttons and progress bar in a horizontal layout
        action_layout = QHBoxLayout()
        action_layout.addWidget(self.action_buttons)
        action_layout.addWidget(self.progress_bar)
        self.layout.addLayout(action_layout)
        
        self.layout.addWidget(self.footer)
        
        # Set layout spacing and margins
        self.layout.setSpacing(20)
        self.layout.setContentsMargins(20, 20, 20, 20)
        
        # Connect signals
        self.folder_selection.folder_selected.connect(self.update_file_list)
        self.action_buttons.rename_button.clicked.connect(self.batch_rename_files)
        self.action_buttons.undo_button.clicked.connect(self.undo_rename)
        self.file_list.file_list.itemSelectionChanged.connect(self.update_preview)
        self.rename_options.options_changed.connect(self.update_preview)
        
    def update_file_list(self, folder_path=None):
        if folder_path is None:
            folder_path = self.folder_selection.get_folder_path()
        if folder_path and os.path.isdir(folder_path):
            try:
                files = FileOperations.get_files_in_folder(folder_path)
                self.file_list.clear_and_add_files(files)
                self.update_preview()
            except PermissionError:
                logging.error(f"Permission denied when accessing folder: {folder_path}")
                self.show_error(f"Permission denied when accessing folder: {folder_path}")
            except Exception as e:
                logging.error(f"Error updating file list: {str(e)}")
                self.show_error(f"An error occurred while updating the file list: {str(e)}")
        else:
            logging.warning(f"Invalid folder path: {folder_path}")
            self.show_error("Please select a valid folder.")
    
    def update_preview(self):
        self.file_list.clear_preview()
        selected_items = self.file_list.get_selected_items()
        for item in selected_items:
            filename = item.text()
            new_filename = self.apply_rename_operation(filename)
            if new_filename != filename:
                self.file_list.add_preview_item(f"{filename} → {new_filename}")
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
        if not folder_path or not os.path.isdir(folder_path):
            logging.warning(f"Invalid folder path: {folder_path}")
            self.show_error("Please select a valid folder.")
            return
        
        selected_items = self.file_list.get_selected_items()
        if not selected_items:
            logging.warning("No files selected for renaming")
            self.show_error("Please select at least one file.")
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
        logging.info("Files renamed successfully")
        QMessageBox.information(self, "Success", "Files renamed successfully!")
    
    def show_error(self, error_message):
        logging.error(f"Error: {error_message}")
        reply = QMessageBox.critical(self, "Error", f"{error_message}\n\nWould you like to report this error?", 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.report_error()
        self.action_buttons.enable_rename_button(True)
    
    def report_error(self):
        try:
            desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
            error_report_path = os.path.join(desktop_path, 'batch_rename_error_report.txt')
            
            with open(log_path, 'r') as log_file, open(error_report_path, 'w') as report_file:
                report_file.write("Batch Rename Error Report\n\n")
                report_file.write("Log contents:\n\n")
                report_file.write(log_file.read())
            
            QMessageBox.information(self, "Error Report", f"Error report saved to:\n{error_report_path}")
        except Exception as e:
            logging.error(f"Failed to create error report: {str(e)}")
            QMessageBox.warning(self, "Error", f"Failed to create error report: {str(e)}")
    
    def undo_rename(self):
        folder_path = self.folder_selection.get_folder_path()
        if not folder_path or not os.path.isdir(folder_path):
            logging.warning(f"Invalid folder path for undo operation: {folder_path}")
            self.show_error("Please select a valid folder.")
            return
        
        try:
            current_files = os.listdir(folder_path)
        except PermissionError:
            logging.error(f"Permission denied when accessing folder for undo: {folder_path}")
            self.show_error(f"Permission denied when accessing folder: {folder_path}")
            return
        except Exception as e:
            logging.error(f"Error listing files for undo: {str(e)}")
            self.show_error(f"An error occurred while listing files: {str(e)}")
            return
        
        for original, current in zip(self.original_names, current_files):
            if original != current:
                try:
                    FileOperations.rename_file(folder_path, current, original)
                except Exception as e:
                    logging.error(f"Error reverting {current} to {original}: {str(e)}")
                    self.show_error(f"Error reverting {current} to {original}: {str(e)}")
        
        self.action_buttons.enable_undo_button(False)
        self.update_file_list()
        logging.info("Undo operation completed")
        QMessageBox.information(self, "Undo Complete", "Files have been reverted to their original names.")

    def closeEvent(self, event):
        try:
            # Clean up temporary files
            temp_dir = tempfile.gettempdir()
            for filename in os.listdir(temp_dir):
                if filename.startswith('_MEI'):
                    file_path = os.path.join(temp_dir, filename)
                    if os.path.isdir(file_path):
                        shutil.rmtree(file_path, ignore_errors=True)
        except Exception as e:
            logging.error(f"Error cleaning up temporary files: {str(e)}")
        event.accept()