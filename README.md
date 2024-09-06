# Batch File Renaming Tool

## Overview

The Batch File Renaming Tool is a user-friendly desktop application that allows you to rename multiple files in a folder quickly and easily. It provides options to add prefixes, suffixes, or both to file names, as well as the ability to swap characters within file names.

## Features

- Simple and intuitive graphical user interface
- Two main renaming options:
  1. Add prefix and/or suffix
  2. Swap characters
- Ability to select a folder for batch renaming
- Real-time preview of file name changes
- Undo functionality to revert changes
- Error handling and user feedback
- Studio Merpati branding elements

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Clone this repository or download the source code.
3. Install the required dependencies (if any) by running:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the script by executing:
   ```
   python main.py
   ```
2. The Batch File Renaming Tool window will appear.

### Renaming Files

1. Click the "Browse" button to select the folder containing the files you want to rename.
2. Choose a renaming option:
   - "Add prefix and/or suffix"
   - "Swap characters"

3. If you selected "Add prefix and/or suffix":
   - Choose whether to add a prefix, suffix, or both.
   - Enter the desired prefix and/or suffix in the provided input boxes.

4. If you selected "Swap characters":
   - Enter the text you want to replace in the "Swap from" box.
   - Enter the replacement text in the "Swap to" box.

5. Use the file list to select which files you want to rename. You can use the "Select All" and "Select None" buttons for convenience.

6. The preview list will show you how the selected files will be renamed.

7. Click the "Rename Files" button to start the renaming process.

8. A success message will appear briefly on the button when the process is complete.

9. If you need to undo the renaming, click the "Undo Rename" button.

## Error Handling

The tool provides error messages in the following situations:
- No folder is selected
- No files are selected for renaming
- An error occurs during the renaming process

## Development

This tool is developed using Python and the tkinter library for the graphical user interface. The project is structured as follows:

- `main.py`: The entry point of the application
- `batch_rename_ui.py`: Contains the `BatchRenameUI` class, which handles the user interface and main logic
- `file_operations.py`: Contains the `FileOperations` class, which handles file system operations

### Branding

The tool incorporates elements of Studio Merpati branding:
- The success message button color (#FF6F61) is inspired by Studio Merpati's color palette, adding a personal touch to the user interface.
- A footer with branding information is included in the main window.

### Future Improvements

- Add support for renaming based on file attributes (e.g., creation date, file type)
- Implement file name pattern matching and regular expressions for more advanced renaming options
- Create an executable version for easy distribution
- Add support for multiple languages
- Implement a dark mode option
- Add the ability to save and load renaming presets

## Contributing

Contributions to improve the Batch File Renaming Tool are welcome. Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.