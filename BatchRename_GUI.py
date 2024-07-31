
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def batch_rename_files():
    # Create a new tkinter window
    window = tk.Tk()
    window.title("Batch Rename Files")

    # Introduction label
    intro_label = tk.Label(window, text="# made with love in Singapore; 2024; Adib Zailan")
    intro_label.pack(pady=10)

    # Function to select folder
    def select_folder():
        folder_path = filedialog.askdirectory()
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_path)

    # Function to rename files
    def rename_files():
        folder_path = folder_entry.get()
        option = option_var.get()

        if option == "1":
            prefix_suffix_option = prefix_suffix_var.get()
            if prefix_suffix_option == "1":
                prefix = prefix_entry.get()
                suffix = ""
            elif prefix_suffix_option == "2":
                prefix = ""
                suffix = suffix_entry.get()
            elif prefix_suffix_option == "3":
                prefix = prefix_entry.get()
                suffix = suffix_entry.get()

            for filename in os.listdir(folder_path):
                file_ext = os.path.splitext(filename)[1]
                new_filename = f"{prefix}{filename}{suffix}{file_ext}"
                os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

        elif option == "2":
            swap_from = swap_from_entry.get()
            swap_to = swap_to_entry.get()
            for filename in os.listdir(folder_path):
                new_filename = filename.replace(swap_from, swap_to)
                os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

        messagebox.showinfo("Batch Rename", "Batch rename has been completed.")

    # Create folder selection frame
    folder_frame = tk.Frame(window)
    folder_label = tk.Label(folder_frame, text="Select Folder:")
    folder_label.pack(side=tk.LEFT)
    folder_entry = tk.Entry(folder_frame, width=50)
    folder_entry.pack(side=tk.LEFT)
    folder_button = tk.Button(folder_frame, text="Browse", command=select_folder)
    folder_button.pack(side=tk.LEFT)
    folder_frame.pack(pady=10)

    # Create option frame
    option_frame = tk.Frame(window)
    option_label = tk.Label(option_frame, text="Select Option:")
    option_label.pack(side=tk.LEFT)
    option_var = tk.StringVar()
    option_var.set("1")
    option_radio1 = tk.Radiobutton(option_frame, text="Add prefix and/or suffix", variable=option_var, value="1")
    option_radio1.pack(side=tk.LEFT)
    option_radio2 = tk.Radiobutton(option_frame, text="Swap characters", variable=option_var, value="2")
    option_radio2.pack(side=tk.LEFT)
    option_frame.pack(pady=10)

    # Create prefix and suffix frame
    prefix_suffix_frame = tk.Frame(window)
    prefix_suffix_label = tk.Label(prefix_suffix_frame, text="Select Prefix/Suffix Option:")
    prefix_suffix_label.pack(side=tk.LEFT)
    prefix_suffix_var = tk.StringVar()
    prefix_suffix_var.set("1")
    prefix_suffix_radio1 = tk.Radiobutton(prefix_suffix_frame, text="Add prefix", variable=prefix_suffix_var, value="1")
    prefix_suffix_radio1.pack(side=tk.LEFT)
    prefix_suffix_radio2 = tk.Radiobutton(prefix_suffix_frame, text="Add suffix", variable=prefix_suffix_var, value="2")
    prefix_suffix_radio2.pack(side=tk.LEFT)
    prefix_suffix_radio3 = tk.Radiobutton(prefix_suffix_frame, text="Add both prefix and suffix", variable=prefix_suffix_var, value="3")
    prefix_suffix_radio3.pack(side=tk.LEFT)
    prefix_suffix_frame.pack(pady=10)

    # Create prefix and suffix entry frame
    prefix_suffix_entry_frame = tk.Frame(window)
    prefix_label = tk.Label(prefix_suffix_entry_frame, text="Prefix:")
    prefix_label.pack(side=tk.LEFT)
    prefix_entry = tk.Entry(prefix_suffix_entry_frame, width=20)
    prefix_entry.pack(side=tk.LEFT)
    suffix_label = tk.Label(prefix_suffix_entry_frame, text="Suffix:")
    suffix_label.pack(side=tk.LEFT)
    suffix_entry = tk.Entry(prefix_suffix_entry_frame, width=20)
    suffix_entry.pack(side=tk.LEFT)
    prefix_suffix_entry_frame.pack(pady=10)

    # Create swap characters frame
    swap_frame = tk.Frame(window)
    swap_from_label = tk.Label(swap_frame, text="Swap from:")
    swap_from_label.pack(side=tk.LEFT)
    swap_from_entry = tk.Entry(swap_frame, width=20)
    swap_from_entry.pack(side=tk.LEFT)
    swap_to_label = tk.Label(swap_frame, text="Swap to:")
    swap_to_label.pack(side=tk.LEFT)
    swap_to_entry = tk.Entry(swap_frame, width=20)
    swap_to_entry.pack(side=tk.LEFT)
    swap_frame.pack(pady=10)

    # Create rename files button
    rename_button = tk.Button(window, text="Rename Files", command=rename_files)
    rename_button.pack(pady=10)

    # Start Tkinter event loop
    window.mainloop()

batch_rename_files()