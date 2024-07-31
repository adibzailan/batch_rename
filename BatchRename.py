# made with love in Singapore, Adib Zailan, 2024

import os

def batch_rename_files():
    """
    Batch rename files in a specified folder with a prefix or suffix, or swap characters.
    """

    while True:
        # Prompt for folder path
        folder_path = input("Enter the path to the folder containing files to rename: ")

        # Check if folder exists
        if not os.path.exists(folder_path):
            print(f"Folder '{folder_path}' does not exist.")
            continue

        # Prompt for rename option
        print("Select a rename option:")
        print("1. Add prefix and/or suffix")
        print("2. Swap characters")
        option = input("Enter option number: ")

        if option == "1":
            # Prompt for prefix and suffix option
            print("Select an option:")
            print("1. Add prefix")
            print("2. Add suffix")
            print("3. Add both prefix and suffix")
            prefix_suffix_option = input("Enter option number: ")

            if prefix_suffix_option == "1":
                prefix = input("Enter prefix to add to file names: ")
                suffix = ""
            elif prefix_suffix_option == "2":
                prefix = ""
                suffix = input("Enter suffix to add to file names: ")
            elif prefix_suffix_option == "3":
                prefix = input("Enter prefix to add to file names: ")
                suffix = input("Enter suffix to add to file names: ")
            else:
                print("Invalid option. Please try again.")
                continue

            # Loop through files in folder
            for filename in os.listdir(folder_path):
                # Get file extension
                file_ext = os.path.splitext(filename)[1]

                # Construct new file name
                new_filename = f"{prefix}{filename}{suffix}{file_ext}"

                # Rename file
                os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

                print(f"Renamed '{filename}' to '{new_filename}'")

        elif option == "2":
            # Prompt for swap characters
            swap_from = input("Enter characters to swap from: ")
            swap_to = input("Enter characters to swap to: ")

            # Loop through files in folder
            for filename in os.listdir(folder_path):
                # Construct new file name
                new_filename = filename.replace(swap_from, swap_to)

                # Rename file
                os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

                print(f"Renamed '{filename}' to '{new_filename}'")

        else:
            print("Invalid option. Please try again.")

        # Ask if user wants to continue or exit
        print("\nBatch rename has been completed.")
        print("Select an option:")
        print("1. Continue")
        print("2. Exit")
        response = input("Enter option number: ")

        if response == "2":
            print("Exiting script. Goodbye!")
            break

# Run the script
batch_rename_files()