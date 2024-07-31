import tkinter as tk
from tkinter import filedialog, ttk
import os
import threading
import time

def batch_rename_files():
    window = tk.Tk()
    window.title("Batch Rename Files")
    window.geometry("600x400")
    
    style = ttk.Style()
    style.theme_use('clam')

    # Create styles for normal and underlined radiobuttons
    style.configure("TRadiobutton", font=("TkDefaultFont", 10))
    style.configure("Underline.TRadiobutton", font=("TkDefaultFont", 10, "underline"))

    # Create a style for disabled Entry widgets
    style.map("TEntry",
        fieldbackground=[("disabled", "light gray"), ("!disabled", "white")],
        foreground=[("disabled", "gray"), ("!disabled", "black")]
    )

    main_frame = ttk.Frame(window, padding="10")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Header
    header_label = ttk.Label(main_frame, text="Batch File Renaming Tool", font=("Arial", 16, "bold"))
    header_label.pack(pady=(0, 10))

    def select_folder():
        folder_path = filedialog.askdirectory()
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_path)

    def rename_files():
        folder_path = folder_entry.get()
        option = option_var.get()

        if not folder_path:
            show_error("Please select a folder.")
            return

        if option == "1":
            prefix_suffix_option = prefix_suffix_var.get()
            prefix = prefix_entry.get()
            suffix = suffix_entry.get()

            if prefix_suffix_option == "1" and not prefix:
                show_error("Please enter a prefix.")
                return
            elif prefix_suffix_option == "2" and not suffix:
                show_error("Please enter a suffix.")
                return
            elif prefix_suffix_option == "3" and not (prefix and suffix):
                show_error("Please enter both prefix and suffix.")
                return

            for filename in os.listdir(folder_path):
                name, ext = os.path.splitext(filename)
                if prefix_suffix_option in ["1", "3"]:
                    name = prefix + name
                if prefix_suffix_option in ["2", "3"]:
                    name = name + suffix
                new_filename = name + ext
                os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

        elif option == "2":
            swap_from = swap_from_entry.get()
            swap_to = swap_to_entry.get()

            if not swap_from:
                show_error("Please enter the text to swap from.")
                return

            for filename in os.listdir(folder_path):
                new_filename = filename.replace(swap_from, swap_to)
                os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

        update_button("Files renamed!")
        threading.Thread(target=reset_button).start()

    def update_button(text):
        rename_button.config(text=text, bg='#FF6F61')  # Updated color as requested

    def reset_button():
        time.sleep(2)  # Wait for 2 seconds
        rename_button.config(text="Rename files", bg='SystemButtonFace')  # Updated text case

    def show_error(message):
        error_label.config(text=message)
        error_label.pack(pady=(0, 10))
        window.after(3000, lambda: error_label.pack_forget())

    def update_ui():
        option = option_var.get()
        if option == "2":
            prefix_suffix_var.set("0")
            prefix_suffix_radio0.state(['!disabled', 'selected'])
            prefix_suffix_radio1.state(['disabled'])
            prefix_suffix_radio2.state(['disabled'])
            prefix_suffix_radio3.state(['disabled'])
            prefix_entry.state(['disabled'])
            suffix_entry.state(['disabled'])
            swap_from_entry.state(['!disabled'])
            swap_to_entry.state(['!disabled'])
            option_radio2.configure(style="Underline.TRadiobutton")
            prefix_suffix_radio0.configure(style="Underline.TRadiobutton")
            option_radio1.configure(style="TRadiobutton")
            prefix_suffix_radio1.configure(style="TRadiobutton")
            prefix_suffix_radio2.configure(style="TRadiobutton")
            prefix_suffix_radio3.configure(style="TRadiobutton")
        else:
            prefix_suffix_radio0.state(['!disabled'])
            prefix_suffix_radio1.state(['!disabled'])
            prefix_suffix_radio2.state(['!disabled'])
            prefix_suffix_radio3.state(['!disabled'])
            swap_from_entry.state(['disabled'])
            swap_to_entry.state(['disabled'])
            option_radio1.configure(style="Underline.TRadiobutton")
            option_radio2.configure(style="TRadiobutton")
            prefix_suffix_radio0.configure(style="TRadiobutton")
            update_prefix_suffix_ui()

    def update_prefix_suffix_ui():
        prefix_suffix_option = prefix_suffix_var.get()
        if prefix_suffix_option == "0":
            prefix_entry.state(['disabled'])
            suffix_entry.state(['disabled'])
            prefix_suffix_radio0.configure(style="Underline.TRadiobutton")
            prefix_suffix_radio1.configure(style="TRadiobutton")
            prefix_suffix_radio2.configure(style="TRadiobutton")
            prefix_suffix_radio3.configure(style="TRadiobutton")
        elif prefix_suffix_option == "1":
            prefix_entry.state(['!disabled'])
            suffix_entry.state(['disabled'])
            prefix_suffix_radio0.configure(style="TRadiobutton")
            prefix_suffix_radio1.configure(style="Underline.TRadiobutton")
            prefix_suffix_radio2.configure(style="TRadiobutton")
            prefix_suffix_radio3.configure(style="TRadiobutton")
        elif prefix_suffix_option == "2":
            prefix_entry.state(['disabled'])
            suffix_entry.state(['!disabled'])
            prefix_suffix_radio0.configure(style="TRadiobutton")
            prefix_suffix_radio1.configure(style="TRadiobutton")
            prefix_suffix_radio2.configure(style="Underline.TRadiobutton")
            prefix_suffix_radio3.configure(style="TRadiobutton")
        elif prefix_suffix_option == "3":
            prefix_entry.state(['!disabled'])
            suffix_entry.state(['!disabled'])
            prefix_suffix_radio0.configure(style="TRadiobutton")
            prefix_suffix_radio1.configure(style="TRadiobutton")
            prefix_suffix_radio2.configure(style="TRadiobutton")
            prefix_suffix_radio3.configure(style="Underline.TRadiobutton")

    folder_frame = ttk.Frame(main_frame)
    folder_frame.pack(fill=tk.X, pady=5)

    folder_label = ttk.Label(folder_frame, text="Select Folder:")
    folder_label.pack(side=tk.LEFT, padx=(0, 5))

    folder_entry = ttk.Entry(folder_frame, width=50)
    folder_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

    folder_button = ttk.Button(folder_frame, text="Browse", command=select_folder)
    folder_button.pack(side=tk.LEFT)

    option_frame = ttk.Frame(main_frame)
    option_frame.pack(fill=tk.X, pady=10)

    option_label = ttk.Label(option_frame, text="Select Renaming Option:")
    option_label.pack(side=tk.LEFT, padx=(0, 5))

    option_var = tk.StringVar(value="1")
    option_radio1 = ttk.Radiobutton(option_frame, text="Add prefix and/or suffix", variable=option_var, value="1", command=update_ui, style="TRadiobutton")
    option_radio1.pack(side=tk.LEFT, padx=(0, 10))
    option_radio2 = ttk.Radiobutton(option_frame, text="Swap characters", variable=option_var, value="2", command=update_ui, style="TRadiobutton")
    option_radio2.pack(side=tk.LEFT)

    prefix_suffix_frame = ttk.Frame(main_frame)
    prefix_suffix_frame.pack(fill=tk.X, pady=5)

    prefix_suffix_label = ttk.Label(prefix_suffix_frame, text="Select Prefix/Suffix Option:")
    prefix_suffix_label.pack(side=tk.LEFT, padx=(0, 5))

    prefix_suffix_var = tk.StringVar(value="0")
    prefix_suffix_radio0 = ttk.Radiobutton(prefix_suffix_frame, text="None", variable=prefix_suffix_var, value="0", command=update_prefix_suffix_ui, style="TRadiobutton")
    prefix_suffix_radio0.pack(side=tk.LEFT, padx=(0, 5))
    prefix_suffix_radio1 = ttk.Radiobutton(prefix_suffix_frame, text="Add prefix", variable=prefix_suffix_var, value="1", command=update_prefix_suffix_ui, style="TRadiobutton")
    prefix_suffix_radio1.pack(side=tk.LEFT, padx=(0, 5))
    prefix_suffix_radio2 = ttk.Radiobutton(prefix_suffix_frame, text="Add suffix", variable=prefix_suffix_var, value="2", command=update_prefix_suffix_ui, style="TRadiobutton")
    prefix_suffix_radio2.pack(side=tk.LEFT, padx=(0, 5))
    prefix_suffix_radio3 = ttk.Radiobutton(prefix_suffix_frame, text="Add both", variable=prefix_suffix_var, value="3", command=update_prefix_suffix_ui, style="TRadiobutton")
    prefix_suffix_radio3.pack(side=tk.LEFT)

    prefix_suffix_entry_frame = ttk.Frame(main_frame)
    prefix_suffix_entry_frame.pack(fill=tk.X, pady=5)

    prefix_label = ttk.Label(prefix_suffix_entry_frame, text="Prefix:")
    prefix_label.pack(side=tk.LEFT, padx=(0, 5))
    prefix_entry = ttk.Entry(prefix_suffix_entry_frame, width=20)
    prefix_entry.pack(side=tk.LEFT, padx=(0, 10))

    suffix_label = ttk.Label(prefix_suffix_entry_frame, text="Suffix:")
    suffix_label.pack(side=tk.LEFT, padx=(0, 5))
    suffix_entry = ttk.Entry(prefix_suffix_entry_frame, width=20)
    suffix_entry.pack(side=tk.LEFT)

    swap_frame = ttk.Frame(main_frame)
    swap_frame.pack(fill=tk.X, pady=5)

    swap_from_label = ttk.Label(swap_frame, text="Swap from:")
    swap_from_label.pack(side=tk.LEFT, padx=(0, 5))
    swap_from_entry = ttk.Entry(swap_frame, width=20)
    swap_from_entry.pack(side=tk.LEFT, padx=(0, 10))

    swap_to_label = ttk.Label(swap_frame, text="Swap to:")
    swap_to_label.pack(side=tk.LEFT, padx=(0, 5))
    swap_to_entry = ttk.Entry(swap_frame, width=20)
    swap_to_entry.pack(side=tk.LEFT)

    error_label = ttk.Label(main_frame, foreground="red")

    rename_button = tk.Button(main_frame, text="Rename files", command=rename_files)  # Updated text case
    rename_button.pack(pady=10)

    # Footer
    footer_label = ttk.Label(main_frame, text="Beta v0.1 / Made with love in Singapore, Adib Zailan, 2024", font=("Arial", 8, "italic"))
    footer_label.pack(side=tk.BOTTOM, pady=(10, 0))

    # Initialize UI
    update_ui()

    window.mainloop()

if __name__ == "__main__":
    batch_rename_files()