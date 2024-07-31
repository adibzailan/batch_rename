# Batch File Renaming Tool

## Overview

The Batch File Renaming Tool is a user-friendly desktop application that allows you to rename multiple files in a folder quickly and easily. It provides options to add prefixes, suffixes, or both to file names, as well as the ability to swap characters within file names.

## Features

- Simple and intuitive graphical user interface
- Two main renaming options:
  1. Add prefix and/or suffix
  2. Swap characters
- Ability to select a folder for batch renaming
- Real-time UI updates based on user selections
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
   python BatchRename.py
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

5. Click the "Rename files" button to start the renaming process.

6. A success message will appear briefly on the button when the process is complete. The button will change color to a shade of coral (#FF6F61), which is a nod to the Studio Merpati branding.

## Error Handling

The tool provides error messages in the following situations:
- No folder is selected
- No prefix/suffix is entered when required
- No "swap from" text is entered when using the swap characters option

## Development

This tool is developed using Python and the tkinter library for the graphical user interface. The main script is `BatchRename_GUI-v4.py`.

### Branding

The tool incorporates elements of Studio Merpati branding:
- The success message button color (#FF6F61) is inspired by Studio Merpati's color palette, adding a personal touch to the user interface.

### Future Improvements

- Add a preview feature to show how files will be renamed before applying changes
- Implement undo functionality
- Add support for renaming based on file attributes (e.g., creation date, file type)
- Create an executable version for easy distribution
- Further integrate Studio Merpati branding elements

## Contributing

Contributions to the Batch File Renaming Tool are welcome! Please feel free to submit pull requests, report bugs, or suggest new features.

## License

[Specify your chosen license here]

## Acknowledgments

Beta v0.1 / Made with love in Singapore, Adib Zailan, 2024
