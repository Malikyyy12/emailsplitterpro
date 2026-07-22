import customtkinter as ctk
from tkinter import filedialog, messagebox
from pathlib import Path
import threading
import os


class EmailSplitter:

    def __init__(self, root):
        self.root = root
        self.root.title("Email Splitter Pro")
        self.root.geometry("650x400")

        self.file_path = None

        ctk.CTkLabel(root, text="Email Splitter", font=("Arial", 24)).pack(pady=15)

        self.file_label = ctk.CTkLabel(root, text="No file selected")
        self.file_label.pack()

        ctk.CTkButton(
            root,
            text="Select Email File",
            command=self.select_file
        ).pack(pady=10)

        ctk.CTkLabel(root, text="Number of Groups").pack()

        self.groups = ctk.CTkEntry(root)
        self.groups.insert(0, "50")
        self.groups.pack()

        self.progress = ctk.CTkProgressBar(root, width=400)
        self.progress.pack(pady=20)
        self.progress.set(0)

        self.status = ctk.CTkLabel(root, text="")
        self.status.pack()

        ctk.CTkButton(
            root,
            text="Split Emails",
            command=self.start
        ).pack(pady=20)

    def select_file(self):
     print("Button clicked")

     self.file_path = filedialog.askopenfilename(
        title="Select Email File",
        filetypes=[
            ("All Files", "*.*"),
            ("Text Files", "*.txt"),
            ("ZIP Files", "*.zip"),
        ]
    )

     print("Selected:", self.file_path)

     if self.file_path:
        self.file_label.configure(text=self.file_path)

    def start(self):

        if not self.file_path:
            messagebox.showerror("Error", "Choose a file first")
            return

        thread = threading.Thread(target=self.split)
        thread.start()

    def split(self):

        groups = int(self.groups.get())

        self.status.configure(text="Counting emails...")

        total = 0

        with open(self.file_path, "r", encoding="utf8") as f:
            for _ in f:
                total += 1

        per_group = total // groups
        remainder = total % groups

        output_folder = Path(self.file_path).parent / "Output"

        output_folder.mkdir(exist_ok=True)

        self.status.configure(text="Writing files...")

        with open(self.file_path, "r", encoding="utf8") as infile:

            for group in range(groups):

                size = per_group

                if group < remainder:
                    size += 1

                outfile = open(
                    output_folder / f"Group_{group+1}.txt",
                    "w",
                    encoding="utf8"
                )

                for _ in range(size):
                    line = infile.readline()
                    if not line:
                        break
                    outfile.write(line)

                outfile.close()

                self.progress.set((group + 1) / groups)

                self.status.configure(
                    text=f"Finished Group {group+1} of {groups}"
                )

        self.status.configure(text="Completed!")


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()

EmailSplitter(root)

root.mainloop()