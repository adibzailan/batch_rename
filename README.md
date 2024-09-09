# Batch File Renaming Tool

The Batch File Renaming Tool is a user-friendly application that allows you to rename multiple files in a folder quickly and easily. It provides a graphical user interface for easy configuration and execution of batch file renaming operations.

## Features

- Select source folder through a graphical interface
- Two main renaming options:
  1. Add prefix and/or suffix
  2. Swap characters in file names
- Real-time preview of file name changes
- Select specific files for renaming or apply to all files in the folder
- Undo functionality to revert changes
- Dark mode interface for comfortable usage
- Studio Merpati branding elements

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

This will launch the graphical user interface. From here, you can:

1. Select the source folder by clicking the "Browse" button
2. Choose a renaming option: "Add prefix and/or suffix" or "Swap characters"
3. Enter the necessary information for the chosen renaming option
4. Select the files you want to rename
5. Preview the changes in the preview list
6. Click "Rename Files" to execute the renaming operation
7. Use "Undo Rename" if you need to revert the changes

## Packaging the Application

To create a standalone executable that can be run on systems without Python installed, you can use PyInstaller. There are two methods to package the application:

### Method 1: Using the PyInstaller script

Run the following command:

```
python pyinstaller_script.py
```

### Method 2: Running PyInstaller directly

Run the following command:

```
pyinstaller --onefile --windowed ui_main.py
```

Both methods will create an executable file in the `dist` folder. You can distribute this executable to run the application on other systems without requiring Python or the dependencies to be installed.

## File Structure

The project is organized into two main components: the frontend (ui) and the backend (core).

- `ui_main.py`: The main entry point of the application
- `ui/`: Frontend (UI) components
  - `main_window.py`: Contains the main BatchRenameUI class
  - `rename_worker.py`: Contains the RenameWorker class for background processing
  - `ui_components/`: Individual UI components
    - `folder_selection.py`: FolderSelectionWidget
    - `file_list.py`: FileListWidget
    - `rename_options.py`: RenameOptionsWidget
    - `action_buttons.py`: ActionButtonsWidget
    - `progress_bar.py`: ProgressBarWidget
    - `footer.py`: FooterWidget
  - `utils/`
    - `theme.py`: Contains theme-related functions
- `core/`: Backend (logic) components
  - `file_operations.py`: File-related operations
  - `rename_logic.py`: Core renaming logic
  - `rename_functions.py`: Specific renaming functions
- `pyinstaller_script.py`: Script for packaging the application with PyInstaller

### Frontend (UI) vs Backend (Core)

- **Frontend (ui)**: This directory contains all the user interface components. It handles the presentation layer, user interactions, and coordinates with the backend to perform operations. The frontend is responsible for displaying information to the user and capturing user input.

- **Backend (core)**: This directory contains the core logic and functionality of the application. It handles file operations, renaming logic, and other backend processes. The backend doesn't deal with user interfaces directly but provides the necessary functions and classes that the frontend uses to perform operations.

This separation of concerns between frontend and backend allows for better organization, maintainability, and potential reusability of code. The frontend can be updated or replaced without affecting the core functionality, and vice versa.

## How It Works

1. **User Interface**: The GUI provides an easy way to select the source folder, choose renaming options, and select files for renaming.

2. **Rename Options**: Users can choose to add prefixes/suffixes or swap characters in file names.

3. **Preview**: The application shows a real-time preview of the renamed files before applying changes.

4. **Renaming Process**: When the user clicks "Rename Files," the application renames the selected files according to the chosen options.

5. **Undo Functionality**: The "Undo Rename" feature allows users to revert the last renaming operation.

## Troubleshooting

If you encounter any issues:

1. Ensure that you have the correct permissions to read from and write to the source folder.
2. Check for any error messages displayed by the application.
3. Make sure that all required dependencies are installed correctly.
4. If the application doesn't start, try running it from the command line to see any error messages that might not be visible otherwise.

## License

This project is open-source and available under the MIT License.

## Contributing

Contributions to the Batch File Renaming Tool project are welcome! Please feel free to submit pull requests, create issues or spread the word.