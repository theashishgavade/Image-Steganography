import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from stegano import encode, FileError, DataError, PasswordError


class EncodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Encode File")

        self.input_path = tk.StringVar()
        self.text = tk.StringVar()
        self.password = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0)

        ttk.Label(main_frame, text="Input Image File:").grid(row=0, column=0, sticky="w")
        self.input_entry = ttk.Entry(main_frame, textvariable=self.input_path, width=50)
        self.input_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(main_frame, text="Choose File", command=self.choose_file).grid(row=0, column=2, padx=5)

        ttk.Label(main_frame, text="Enter text to hide:").grid(row=1, column=0, sticky="w")
        self.text_entry = ttk.Entry(main_frame, textvariable=self.text, width=50)
        self.text_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(main_frame, text="Enter Password:").grid(row=2, column=0, sticky="w")
        self.password_entry = ttk.Entry(main_frame, textvariable=self.password, show="*", width=50)
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)

        self.encode_button = ttk.Button(main_frame, text="Encode and Save", command=self.encode)
        self.encode_button.grid(row=3, column=1, pady=10)

    def choose_file(self):
        file_path = filedialog.askopenfilename(title="Choose Input Image File", filetypes=(("Image files", "*.jpg *.png *.bmp"),))
        if file_path:
            self.input_path.set(file_path)

    def encode(self):
        input_path = self.input_path.get()
        text = self.text.get()
        password = self.password.get()

        if not input_path:
            messagebox.showerror("Error: No file chosen", "You must select input image file!")
            return
        elif not text:
            messagebox.showerror("Text is empty", "Please enter some text to hide!")
            return
        elif not password:
            messagebox.showerror("Error: No password given", "Please enter a password!")
            return

        output_path = filedialog.asksaveasfilename(title="Save encoded file", defaultextension=".png",
                                                   filetypes=(("PNG files", "*.png"),))
        if not output_path:
            messagebox.showinfo("Operation cancelled", "Operation cancelled by user!")
            return

        try:
            loss = encode(input_path, text, output_path, password)
            messagebox.showinfo("Success", f"Encoded Successfully!\n\nImage Data Loss = {loss:.5f} %")
        except FileError as fe:
            messagebox.showerror("File Error", str(fe))
        except DataError as de:
            messagebox.showerror("Data Error", str(de))


if __name__ == "__main__":
    root = tk.Tk()
    app = EncodeApp(root)
    root.mainloop()



