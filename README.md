# Batch File Renaming Tool

The Batch File Renaming Tool is a user-friendly application that allows you to rename multiple files in a folder quickly and easily. It provides a graphical user interface for easy configuration and execution of batch file renaming operations.

## Features

- Select source folder through a graphical interface
- Two main renaming options:
  1. Add prefix and/or suffix
  2. Swap characters in file names
- Real-time preview of file name changes
- Intuitive file selection with checkboxes and Select All/Deselect All buttons
- Resizable sections for better file management
- Undo functionality to revert changes
- Modern, Swiss Design-inspired color scheme for improved readability and aesthetics
- Error reporting for easier troubleshooting
- Splash screen for a polished startup experience
- Detailed logging for better diagnostics and troubleshooting

## Latest Updates (v1.3.5)

- Enhanced UI with resizable file list and preview sections
- Improved file selection with intuitive checkboxes
- Added Select All/Deselect All buttons for faster file selection
- Updated button styles for better visibility and contrast
- Optimized UI layout for improved usability
- Added visual feedback for interactive elements
- Added standalone executable packaging with PyInstaller
- Optimized packaging configuration for reduced file size
- Improved application startup performance
- Fixed PyQt6 dependency handling in packaged version
- Enhanced error handling for file system operations

## Requirements

- Python 3.6 or higher
- PyQt6

## Installation

1. Clone this repository or download the source code.

2. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

To run the Batch File Renaming Tool, execute the following command in the project directory:

```
python ui_main.py
```

This will launch the application with a splash screen, followed by the main graphical user interface. From here, you can:

1. Wait for the splash screen to complete its initialization process
2. Click "Browse" to select a folder containing files to rename
3. Use checkboxes to select files for renaming
4. Choose your renaming option:
   - Add prefix/suffix: Enter text to add before or after file names
   - Swap characters: Replace specific characters in file names
5. Preview changes in real-time
6. Click "Rename Files" to apply changes
7. Use "Undo Rename" if needed to revert changes

### Running the Packaged Application

1. Navigate to the `dist` folder
2. Run `BatchRename.exe`

The packaged application includes all necessary dependencies and will run on any compatible Windows system without requiring Python or additional installations.

## How It Works

1. **Startup**: The application displays a splash screen while initializing components.

2. **User Interface**: The GUI provides an easy way to select the source folder, choose renaming options, and select files for renaming using standard multi-select functionality.

3. **Rename Options**: Users can choose to add prefixes/suffixes or swap characters in file names.

4. **Preview**: The application shows a real-time preview of the renamed files before applying changes.

5. **Renaming Process**: When the user clicks "Rename Files," the application renames the selected files according to the chosen options.

6. **Undo Functionality**: The "Undo Rename" feature allows users to revert the last renaming operation.

## Known Issues and Limitations

1. The application may have difficulty renaming files if there are permission issues or if the files are currently in use by another program.
2. Renaming a large number of files simultaneously may take some time, especially on slower systems.
3. The undo functionality only works for the most recent renaming operation. Multiple levels of undo are not supported.
4. When packaging the application with PyInstaller, some antivirus software may flag the executable as suspicious. This is a false positive due to the way PyInstaller works.

## Contributing

Contributions to the Batch File Renaming Tool project are welcome! Please feel free to submit pull requests, create issues or spread the word.

## License

This project is open-source and available under the MIT License.
