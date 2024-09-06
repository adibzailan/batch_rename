import os
import logging
from typing import List

class FileOperations:
    @staticmethod
    def rename_file(folder_path: str, old_name: str, new_name: str) -> None:
        try:
            os.rename(os.path.join(folder_path, old_name), os.path.join(folder_path, new_name))
        except OSError as e:
            logging.error(f"Error renaming file {old_name}: {e}")
            raise

    @staticmethod
    def get_files_in_folder(folder_path: str) -> List[str]:
        return os.listdir(folder_path)