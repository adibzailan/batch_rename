import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os
import threading
import time
import logging
import webbrowser
from typing import List

class FileOperations:
    @staticmethod
    def rename_file(folder_path: str, old_name: str, new_name: str) -> None:
        try:
            os.rename(os.path.join(folder_path, old_name), os.path.join(folder_path, new_name))
        except OSError as e:
            logging.error(f"Error renaming file {old_name}: {e}")
            raise

    @staticmethod
    def get_files_in_folder(folder_path: str) -> List[str]:
        return os.listdir(folder_path)

class BatchRenameUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Batch Rename Files")
        self.window.geometry("1000x600")
        
        self.option_var = tk.StringVar(value="1")
        self.prefix_suffix_var = tk.StringVar(value="1")
        self.folder_entry = None
        self.prefix_entry = None
        self.suffix_entry = None
        self.swap_from_entry = None
        self.swap_to_entry = None
        self.option_radio1 = None
        self.option_radio2 = None
        self.prefix_suffix_radio1 = None
        self.prefix_suffix_radio2 = None
        self.prefix_suffix_radio3 = None
        self.rename_button = None
        self.undo_button = None
        self.progress = None
        self.file_listbox = None
        self.preview_listbox = None
        self.file_vars = {}

        self.setup_ui()
        self.original_names = []

    def setup_ui(self):
        self.create_folder_frame()
        self.create_file_and_preview_listboxes()
        self.create_option_frame()
        self.create_prefix_suffix_frame()
        self.create_action_buttons()
        self.create_progress_bar()
        self.create_footer()

    def batch_rename_files(self):
        folder_path = self.folder_entry.get()
        option = self.option_var.get()

        if not folder_path:
            self.show_error("Please select a folder.")
            return

        try:
            selected_files = [file for file, var in self.file_vars.items() if var.get()]
            total_files = len(selected_files)
            self.original_names = selected_files.copy()

            self.progress['maximum'] = total_files
            self.progress['value'] = 0

            for i, filename in enumerate(selected_files):
                if option == "1":
                    new_filename = self.apply_prefix_suffix(filename)
                elif option == "2":
                    new_filename = self.apply_swap(filename)
                
                if new_filename != filename:
                    FileOperations.rename_file(folder_path, filename, new_filename)
                
                self.progress['value'] = i + 1
                self.window.update_idletasks()

            self.update_button("Files renamed!")
            threading.Thread(target=self.reset_button).start()
            self.undo_button.config(state=tk.NORMAL)
            self.update_file_listbox()
            
        except Exception as e:
            logging.error(f"Error during file renaming: {e}")
            messagebox.showerror("Error", f"An error occurred: {e}")

    def apply_prefix_suffix(self, filename):
        prefix_suffix_option = self.prefix_suffix_var.get()
        prefix = self.prefix_entry.get()
        suffix = self.suffix_entry.get()
        name, ext = os.path.splitext(filename)

        if prefix_suffix_option in ["1", "3"]:
            name = prefix + name
        if prefix_suffix_option in ["2", "3"]:
            name = name + suffix

        return name + ext

    def apply_swap(self, filename):
        swap_from = self.swap_from_entry.get()
        swap_to = self.swap_to_entry.get()
        return filename.replace(swap_from, swap_to)

    def undo_rename(self):
        folder_path = self.folder_entry.get()
        current_files = os.listdir(folder_path)
        
        for original, current in zip(self.original_names, current_files):
            if original != current:
                try:
                    FileOperations.rename_file(folder_path, current, original)
                except Exception as e:
                    logging.error(f"Error during undo operation: {e}")
                    messagebox.showerror("Undo Error", f"Error reverting {current} to {original}: {e}")

        self.undo_button.config(state=tk.DISABLED)
        messagebox.showinfo("Undo Complete", "Files have been reverted to their original names.")
        self.update_file_listbox()

    def update_preview(self, *args):
        self.preview_listbox.delete(0, tk.END)
        folder_path = self.folder_entry.get()
        option = self.option_var.get()
        selected_files = [file for file, var in self.file_vars.items() if var.get()]

        for filename in selected_files:
            if option == "1":
                new_filename = self.apply_prefix_suffix(filename)
            elif option == "2":
                new_filename = self.apply_swap(filename)
            
            if new_filename != filename:
                self.preview_listbox.insert(tk.END, f"{filename} -> {new_filename}")
            else:
                self.preview_listbox.insert(tk.END, f"{filename} (no change)")

    def update_button(self, text):
        self.rename_button.config(text=text, style='Accent.TButton')

    def reset_button(self):
        time.sleep(2)  # Wait for 2 seconds
        self.rename_button.config(text="Rename files", style='TButton')

    def show_error(self, message):
        error_label = ttk.Label(self.window, text=message, foreground="red")
        error_label.pack(pady=(0, 10))
        self.window.after(3000, error_label.destroy)

    def update_ui(self):
        option = self.option_var.get()
        if option == "2":
            self.prefix_suffix_var.set("1")  # Set to "Add prefix" as default
            self.prefix_suffix_radio1.state(['disabled'])
            self.prefix_suffix_radio2.state(['disabled'])
            self.prefix_suffix_radio3.state(['disabled'])
            self.prefix_entry.state(['disabled'])
            self.suffix_entry.state(['disabled'])
            self.swap_from_entry.state(['!disabled'])
            self.swap_to_entry.state(['!disabled'])
            self.option_radio2.configure(style="Underline.TRadiobutton")
            self.option_radio1.configure(style="TRadiobutton")
            self.prefix_suffix_radio1.configure(style="TRadiobutton")
            self.prefix_suffix_radio2.configure(style="TRadiobutton")
            self.prefix_suffix_radio3.configure(style="TRadiobutton")
        else:
            self.prefix_suffix_radio1.state(['!disabled'])
            self.prefix_suffix_radio2.state(['!disabled'])
            self.prefix_suffix_radio3.state(['!disabled'])
            self.swap_from_entry.state(['disabled'])
            self.swap_to_entry.state(['disabled'])
            self.option_radio1.configure(style="Underline.TRadiobutton")
            self.option_radio2.configure(style="TRadiobutton")
            self.update_prefix_suffix_ui()
        self.update_preview()

    def update_prefix_suffix_ui(self):
        prefix_suffix_option = self.prefix_suffix_var.get()
        if prefix_suffix_option == "1":
            self.prefix_entry.state(['!disabled'])
            self.suffix_entry.state(['disabled'])
            self.prefix_suffix_radio1.configure(style="Underline.TRadiobutton")
            self.prefix_suffix_radio2.configure(style="TRadiobutton")
            self.prefix_suffix_radio3.configure(style="TRadiobutton")
        elif prefix_suffix_option == "2":
            self.prefix_entry.state(['disabled'])
            self.suffix_entry.state(['!disabled'])
            self.prefix_suffix_radio1.configure(style="TRadiobutton")
            self.prefix_suffix_radio2.configure(style="Underline.TRadiobutton")
            self.prefix_suffix_radio3.configure(style="TRadiobutton")
        elif prefix_suffix_option == "3":
            self.prefix_entry.state(['!disabled'])
            self.suffix_entry.state(['!disabled'])
            self.prefix_suffix_radio1.configure(style="TRadiobutton")
            self.prefix_suffix_radio2.configure(style="TRadiobutton")
            self.prefix_suffix_radio3.configure(style="Underline.TRadiobutton")
        self.update_preview()

    def create_folder_frame(self):
        folder_frame = ttk.Frame(self.window)
        folder_frame.pack(fill=tk.X, padx=10, pady=10)

        folder_label = ttk.Label(folder_frame, text="Select Folder:")
        folder_label.pack(side=tk.LEFT, padx=(0, 5))

        self.folder_entry = ttk.Entry(folder_frame, width=50)
        self.folder_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

        folder_button = ttk.Button(folder_frame, text="Browse", command=self.select_folder)
        folder_button.pack(side=tk.LEFT)

    def create_file_and_preview_listboxes(self):
        listbox_frame = ttk.Frame(self.window)
        listbox_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # File Listbox
        file_frame = ttk.Frame(listbox_frame)
        file_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        file_label = ttk.Label(file_frame, text="Files:")
        file_label.pack(side=tk.TOP, anchor=tk.W)

        select_buttons_frame = ttk.Frame(file_frame)
        select_buttons_frame.pack(side=tk.TOP, fill=tk.X, pady=(0, 5))

        select_all_button = ttk.Button(select_buttons_frame, text="Select All", command=self.select_all_files)
        select_all_button.pack(side=tk.LEFT, padx=(0, 5))

        select_none_button = ttk.Button(select_buttons_frame, text="Select None", command=self.select_no_files)
        select_none_button.pack(side=tk.LEFT)

        self.file_listbox = tk.Listbox(file_frame, selectmode=tk.MULTIPLE)
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        file_scrollbar = ttk.Scrollbar(file_frame, orient=tk.VERTICAL, command=self.file_listbox.yview)
        file_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.file_listbox.config(yscrollcommand=file_scrollbar.set)
        self.file_listbox.bind('<<ListboxSelect>>', self.on_file_select)

        # Preview Listbox
        preview_frame = ttk.Frame(listbox_frame)
        preview_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        preview_label = ttk.Label(preview_frame, text="Preview:")
        preview_label.pack(side=tk.TOP, anchor=tk.W)

        self.preview_listbox = tk.Listbox(preview_frame)
        self.preview_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        preview_scrollbar = ttk.Scrollbar(preview_frame, orient=tk.VERTICAL, command=self.preview_listbox.yview)
        preview_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.preview_listbox.config(yscrollcommand=preview_scrollbar.set)

    def select_all_files(self):
        self.file_listbox.select_set(0, tk.END)
        for var in self.file_vars.values():
            var.set(True)
        self.update_preview()

    def select_no_files(self):
        self.file_listbox.selection_clear(0, tk.END)
        for var in self.file_vars.values():
            var.set(False)
        self.update_preview()

    def on_file_select(self, event):
        selected_indices = self.file_listbox.curselection()
        for i, (file, var) in enumerate(self.file_vars.items()):
            var.set(i in selected_indices)
        self.update_preview()

    def update_file_listbox(self):
        self.file_listbox.delete(0, tk.END)
        self.file_vars.clear()
        folder_path = self.folder_entry.get()
        
        if folder_path:
            files = FileOperations.get_files_in_folder(folder_path)
            for file in files:
                self.file_vars[file] = tk.BooleanVar(value=True)
                self.file_listbox.insert(tk.END, file)
                self.file_listbox.select_set(tk.END)
        self.update_preview()

    def create_option_frame(self):
        option_frame = ttk.Frame(self.window)
        option_frame.pack(fill=tk.X, padx=10, pady=5)

        option_label = ttk.Label(option_frame, text="Select Renaming Option:")
        option_label.pack(side=tk.LEFT, padx=(0, 5))

        self.option_radio1 = ttk.Radiobutton(option_frame, text="Add prefix and/or suffix", variable=self.option_var, value="1", command=self.update_ui, style="TRadiobutton")
        self.option_radio1.pack(side=tk.LEFT, padx=(0, 10))
        self.option_radio2 = ttk.Radiobutton(option_frame, text="Swap characters", variable=self.option_var, value="2", command=self.update_ui, style="TRadiobutton")
        self.option_radio2.pack(side=tk.LEFT)

    def create_prefix_suffix_frame(self):
        prefix_suffix_frame = ttk.Frame(self.window)
        prefix_suffix_frame.pack(fill=tk.X, padx=10, pady=5)

        prefix_suffix_label = ttk.Label(prefix_suffix_frame, text="Select Prefix/Suffix Option:")
        prefix_suffix_label.pack(side=tk.LEFT, padx=(0, 5))

        self.prefix_suffix_radio1 = ttk.Radiobutton(prefix_suffix_frame, text="Add prefix", variable=self.prefix_suffix_var, value="1", command=self.update_prefix_suffix_ui, style="TRadiobutton")
        self.prefix_suffix_radio1.pack(side=tk.LEFT, padx=(0, 5))
        self.prefix_suffix_radio2 = ttk.Radiobutton(prefix_suffix_frame, text="Add suffix", variable=self.prefix_suffix_var, value="2", command=self.update_prefix_suffix_ui, style="TRadiobutton")
        self.prefix_suffix_radio2.pack(side=tk.LEFT, padx=(0, 5))
        self.prefix_suffix_radio3 = ttk.Radiobutton(prefix_suffix_frame, text="Add both", variable=self.prefix_suffix_var, value="3", command=self.update_prefix_suffix_ui, style="TRadiobutton")
        self.prefix_suffix_radio3.pack(side=tk.LEFT)

        prefix_suffix_entry_frame = ttk.Frame(self.window)
        prefix_suffix_entry_frame.pack(fill=tk.X, padx=10, pady=5)

        prefix_label = ttk.Label(prefix_suffix_entry_frame, text="Prefix:")
        prefix_label.pack(side=tk.LEFT, padx=(0, 5))
        self.prefix_entry = ttk.Entry(prefix_suffix_entry_frame, width=20)
        self.prefix_entry.pack(side=tk.LEFT, padx=(0, 10))
        self.prefix_entry.bind("<KeyRelease>", self.update_preview)

        suffix_label = ttk.Label(prefix_suffix_entry_frame, text="Suffix:")
        suffix_label.pack(side=tk.LEFT, padx=(0, 5))
        self.suffix_entry = ttk.Entry(prefix_suffix_entry_frame, width=20)
        self.suffix_entry.pack(side=tk.LEFT)
        self.suffix_entry.bind("<KeyRelease>", self.update_preview)

        swap_frame = ttk.Frame(self.window)
        swap_frame.pack(fill=tk.X, padx=10, pady=5)

        swap_from_label = ttk.Label(swap_frame, text="Swap from:")
        swap_from_label.pack(side=tk.LEFT, padx=(0, 5))
        self.swap_from_entry = ttk.Entry(swap_frame, width=20)
        self.swap_from_entry.pack(side=tk.LEFT, padx=(0, 10))
        self.swap_from_entry.bind("<KeyRelease>", self.update_preview)

        swap_to_label = ttk.Label(swap_frame, text="Swap to:")
        swap_to_label.pack(side=tk.LEFT, padx=(0, 5))
        self.swap_to_entry = ttk.Entry(swap_frame, width=20)
        self.swap_to_entry.pack(side=tk.LEFT)
        self.swap_to_entry.bind("<KeyRelease>", self.update_preview)

    def create_action_buttons(self):
        button_frame = ttk.Frame(self.window)
        button_frame.pack(pady=10)

        self.rename_button = ttk.Button(button_frame, text="Rename Files", command=self.batch_rename_files)
        self.rename_button.pack(side=tk.LEFT, padx=5)

        self.undo_button = ttk.Button(button_frame, text="Undo Rename", command=self.undo_rename, state=tk.DISABLED)
        self.undo_button.pack(side=tk.LEFT, padx=5)

    def create_progress_bar(self):
        self.progress = ttk.Progressbar(self.window, orient="horizontal", length=200, mode="determinate")
        self.progress.pack(pady=10)

    def create_footer(self):
        footer_frame = ttk.Frame(self.window)
        footer_frame.pack(side=tk.BOTTOM, pady=10)

        footer_text = "Beta 1.0 | Built in Singapore, "
        footer_label = ttk.Label(footer_frame, text=footer_text, font=("Arial", 8, "italic"))
        footer_label.pack(side=tk.LEFT)

        az_label = ttk.Label(footer_frame, text="AZ", font=("Arial", 8, "italic", "underline"), foreground="blue", cursor="hand2")
        az_label.pack(side=tk.LEFT)
        az_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.linkedin.com/in/adibzailan/"))

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        self.folder_entry.delete(0, tk.END)
        self.folder_entry.insert(0, folder_path)
        self.update_file_listbox()

    def run(self):
        self.update_ui()
        self.window.mainloop()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    app = BatchRenameUI()
    app.run()
