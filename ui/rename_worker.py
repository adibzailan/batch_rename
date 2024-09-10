import os
import logging
from PyQt6.QtCore import QThread, pyqtSignal
from core.file_operations import FileOperations

class RenameWorker(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, folder_path, files, rename_function):
        super().__init__()
        self.folder_path = folder_path
        self.files = files
        self.rename_function = rename_function

    def run(self):
        for i, filename in enumerate(self.files):
            try:
                new_filename = self.rename_function(filename)
                if new_filename != filename:
                    old_path = os.path.join(self.folder_path, filename)
                    new_path = os.path.join(self.folder_path, new_filename)
                    
                    # Check if the source file exists
                    if not os.path.exists(old_path):
                        raise FileNotFoundError(f"Source file not found: {old_path}")
                    
                    # Check if we have permission to rename the file
                    if not os.access(old_path, os.W_OK):
                        raise PermissionError(f"No write permission for file: {old_path}")
                    
                    # Check if the destination file already exists
                    if os.path.exists(new_path):
                        raise FileExistsError(f"Destination file already exists: {new_path}")
                    
                    FileOperations.rename_file(self.folder_path, filename, new_filename)
                    logging.info(f"Renamed: {filename} to {new_filename}")
                
                self.progress.emit(i + 1)
            
            except FileNotFoundError as e:
                logging.error(f"File not found error: {str(e)}")
                self.error.emit(f"File not found: {filename}. It may have been moved or deleted.")
                return
            
            except PermissionError as e:
                logging.error(f"Permission error: {str(e)}")
                self.error.emit(f"Permission denied when trying to rename: {filename}. Check file permissions.")
                return
            
            except FileExistsError as e:
                logging.error(f"File exists error: {str(e)}")
                self.error.emit(f"Cannot rename {filename} to {new_filename} as it already exists.")
                return
            
            except Exception as e:
                logging.error(f"Unexpected error during renaming: {str(e)}")
                self.error.emit(f"An unexpected error occurred while renaming {filename}: {str(e)}")
                return

        self.finished.emit()
        logging.info("Rename operation completed successfully")