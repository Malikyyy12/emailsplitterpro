from tkinter import filedialog


class EmailSplitter:

    ...

    def select_file(self):
        print("Button clicked")

        file_path = filedialog.askopenfilename(
            title="Select Email File",
            filetypes=[
                ("Text Files", "*.txt"),
                ("CSV Files", "*.csv"),
                ("All Files", "*.*")
            ]
        )

        print(file_path)

        if file_path:
            self.file_path = file_path
            self.file_label.configure(text=file_path)