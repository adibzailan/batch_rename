import os

class RenameFunctions:
    @staticmethod
    def apply_rename_operation(filename, rename_type, prefix="", suffix="", swap_from="", swap_to=""):
        if rename_type == "prefix_suffix":
            name, ext = os.path.splitext(filename)
            return f"{prefix}{name}{suffix}{ext}"
        elif rename_type == "swap":
            return filename.replace(swap_from, swap_to)
        else:
            return filename  # No change if invalid rename_type