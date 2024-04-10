import tkinter as tk
from tkinter import filedialog, messagebox
from stegano import decode, FileError, PasswordError


class DecodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganography Software - Decode")

        self.label_step1 = tk.Label(root, text="Step 1:", font=('Arial', 12, 'bold'))
        self.label_step1.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.label_input_image = tk.Label(root, text="Input Image File:")
        self.label_input_image.grid(row=0, column=1, padx=5, pady=5)

        self.entry_input_image = tk.Entry(root, width=40)
        self.entry_input_image.grid(row=0, column=2, padx=5, pady=5)

        self.btn_choose_file = tk.Button(root, text="Choose File", command=self.choose_file)
        self.btn_choose_file.grid(row=0, column=3, padx=5, pady=5)

        self.label_step2 = tk.Label(root, text="Step 2:", font=('Arial', 12, 'bold'))
        self.label_step2.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.label_password = tk.Label(root, text="Enter Password:")
        self.label_password.grid(row=1, column=1, padx=5, pady=5)

        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.grid(row=1, column=2, padx=5, pady=5)

        self.btn_decode = tk.Button(root, text="Decode", command=self.decode)
        self.btn_decode.grid(row=1, column=3, padx=5, pady=5)

        self.label_step3 = tk.Label(root, text="Decoded Data:", font=('Arial', 12, 'bold'))
        self.label_step3.grid(row=2, column=0, padx=5, pady=5, sticky="e")

        self.text_decoded_data = tk.Text(root, height=10, width=50)
        self.text_decoded_data.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

    def choose_file(self):
        file_path = filedialog.askopenfilename(title="Open file", filetypes=[("Image files", "*.jpg *.png *.bmp")])
        if file_path:
            self.entry_input_image.delete(0, tk.END)
            self.entry_input_image.insert(tk.END, file_path)

    def decode(self):
        input_path = self.entry_input_image.get()
        password = self.entry_password.get()

        if not input_path:
            messagebox.showerror("Error: No file chosen", "You must select input image file!")
            return
        if not password:
            messagebox.showerror("Error: No password given", "Please enter a password!")
            return

        try:
            data = decode(input_path, password)
            self.text_decoded_data.delete(1.0, tk.END)
            self.text_decoded_data.insert(tk.END, data)
            messagebox.showinfo("Success", "Decoded successfully!")
        except FileError as fe:
            messagebox.showerror("File Error", str(fe))
        except PasswordError as pe:
            messagebox.showerror("Password Error", str(pe))


if __name__ == "__main__":
    root = tk.Tk()
    app = DecodeApp(root)
    root.mainloop()


