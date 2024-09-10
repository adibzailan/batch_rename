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

- Improved error handling and logging throughout the application
- Enhanced file listing and renaming functionality
- Updated UI components for better user interaction
- Integrated Cerebri Sans font for improved typography
- Further optimized startup process and main window display

## Recent Improvements (v1.2.0)

- Implemented a stylish splash screen adhering to Studio Merpati Design System
- Improved startup experience with a loading progress bar
- Enhanced error handling during application initialization
- Centered the main application window on the screen for better user experience

## Previous Improvements (v1.1.0)

- Redesigned UI adhering to Swiss Design principles and Studio Merpati brand guidelines
- Implemented an asymmetrical layout with controls on the left (30%) and content on the right (70%)
- Updated color scheme:
  - Living Coral (#FF6F61) as the primary accent color
  - Dark Gray (#333333) for text
  - Off-White (#F5F5F5) for backgrounds
  - Soft Teal (#4ECDC4) for selected items and links
- Updated typography to use Cerebri Sans font
- Improved white space usage for better visual separation and clarity
- Enhanced responsive design with a splitter for flexible resizing
- Updated footer with new layout and version number (Alpha 1.3.0)
- Streamlined the overall user experience with a cleaner, more minimalist layout

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
  - `splash_screen.py`: Contains the SplashScreen class for the startup screen
  - `ui_components/`: Individual UI components
    - `folder_selection.py`: FolderSelectionWidget
    - `file_list.py`: FileListWidget
    - `rename_options.py`: RenameOptionsWidget
    - `action_buttons.py`: ActionButtonsWidget
    - `progress_bar.py`: ProgressBarWidget
    - `footer.py`: FooterWidget
  - `utils/`
    - `theme.py`: Contains theme-related functions and styles
- `core/`: Backend (logic) components
  - `file_operations.py`: File-related operations
  - `rename_logic.py`: Core renaming logic
  - `rename_functions.py`: Specific renaming functions
- `pyinstaller_script.py`: Script for packaging the application with PyInstaller
- `resources/`: Contains application resources
  - `fonts/`: Custom fonts used in the application (including Cerebri Sans)
  - `images/`: Images used in the application, including the splash screen logo

### Frontend (UI) vs Backend (Core)

- **Frontend (ui)**: This directory contains all the user interface components. It handles the presentation layer, user interactions, and coordinates with the backend to perform operations. The frontend is responsible for displaying information to the user and capturing user input.

- **Backend (core)**: This directory contains the core logic and functionality of the application. It handles file operations, renaming logic, and other backend processes. The backend doesn't deal with user interfaces directly but provides the necessary functions and classes that the frontend uses to perform operations.

This separation of concerns between frontend and backend allows for better organization, maintainability, and potential reusability of code. The frontend can be updated or replaced without affecting the core functionality, and vice versa.

## How It Works

1. **Startup**: The application displays a splash screen while initializing components.

2. **User Interface**: The GUI provides an easy way to select the source folder, choose renaming options, and select files for renaming using standard multi-select functionality.

3. **Rename Options**: Users can choose to add prefixes/suffixes or swap characters in file names.

4. **Preview**: The application shows a real-time preview of the renamed files before applying changes.

5. **Renaming Process**: When the user clicks "Rename Files," the application renames the selected files according to the chosen options.

6. **Undo Functionality**: The "Undo Rename" feature allows users to revert the last renaming operation.

## Troubleshooting

If you encounter any issues:

1. Ensure that you have the correct permissions to read from and write to the source folder.
2. Check for any error messages displayed by the application.
3. Make sure that all required dependencies are installed correctly.
4. If the application doesn't start, try running it from the command line to see any error messages that might not be visible otherwise.
5. If an error occurs during operation, you will be given the option to create an error report. This report will be saved on your desktop and can be useful for diagnosing issues.
6. Check the application's log file located in your system's temporary directory for more detailed information about any errors.

## Known Issues and Limitations

1. The application may have difficulty renaming files if there are permission issues or if the files are currently in use by another program.
2. Renaming a large number of files simultaneously may take some time, especially on slower systems.
3. The undo functionality only works for the most recent renaming operation. Multiple levels of undo are not supported.
4. When packaging the application with PyInstaller, some antivirus software may flag the executable as suspicious. This is a false positive due to the way PyInstaller works.

## License

This project is open-source and available under the MIT License.

## Contributing

Contributions to the Batch File Renaming Tool project are welcome! Please feel free to submit pull requests, create issues or spread the word.

## Feedback and Support

If you encounter any bugs, have feature requests, or need assistance, please open an issue on the project's GitHub page. When reporting issues, please include the error report if one was generated, or provide as much detail as possible about the problem and the steps to reproduce it.