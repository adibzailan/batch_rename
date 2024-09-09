import os

class FileOperations:
    @staticmethod
    def rename_file(folder_path, old_name, new_name):
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)

    @staticmethod
    def get_files_in_folder(folder_path):
        return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]