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
        try:
            for i, filename in enumerate(self.files):
                new_filename = self.rename_function(filename)
                if new_filename != filename:
                    FileOperations.rename_file(self.folder_path, filename, new_filename)
                self.progress.emit(i + 1)
            self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))