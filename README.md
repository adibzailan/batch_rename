# Batch File Renaming Tool

The Batch File Renaming Tool is a user-friendly application that allows you to rename multiple files in a folder quickly and easily. It provides a graphical user interface for easy configuration and execution of batch file renaming operations.

## Features

- Select source folder through a graphical interface
- Two main renaming options:
  1. Add prefix and/or suffix
  2. Swap characters in file names
- Real-time preview of file name changes
- Intuitive multi-file selection using CTRL+Click and Shift+Click
- Undo functionality to revert changes
- Modern, Swiss Design-inspired color scheme for improved readability and aesthetics
- Error reporting for easier troubleshooting
- Splash screen for a polished startup experience
- Detailed logging for better diagnostics and troubleshooting

## Latest Updates (v1.3.0)

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
2. Select the source folder by clicking the "Browse" button
3. Use CTRL+Click and Shift+Click to select multiple files in the file list
4. Choose a renaming option: "Add prefix and/or suffix" or "Swap characters"
5. Enter the necessary information for the chosen renaming option
6. Preview the changes in real-time in the preview list
7. Click "Rename Files" to execute the renaming operation
8. Use "Undo Rename" if you need to revert the changes

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

## License

This project is open-source and available under the MIT License.

## Contributing

Contributions to the Batch File Renaming Tool project are welcome! Please feel free to submit pull requests, create issues or spread the word.
