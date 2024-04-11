import tkinter as tk
from tkinter import filedialog, messagebox, Menu
from stegano import decode, FileError, PasswordError


class DecodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganography Software - Decode")
        self.root.geometry("410x500")  # Set the application window size

        # Create a menu bar and add it to the root window
        self.create_menu()

        # Set consistent width for text entry fields
        entry_width = 60

        # Label for input encrypted file path
        self.label_input_image = tk.Label(root, text="Enter Encrypted File Path Or Click DERIVE FILE Button:")
        self.label_input_image.grid(row=0, column=0, sticky='w', padx=5, pady=5)

        # Entry widget for encrypted file path
        self.entry_input_image = tk.Entry(root, width=entry_width)
        self.entry_input_image.grid(row=1, column=0, sticky='w', padx=5, pady=5)

        # Button for file selection
        self.btn_choose_file = tk.Button(root, text="DERIVE ENCRYPTED FILE", command=self.choose_file)
        self.btn_choose_file.grid(row=2, column=0, padx=5, pady=5, ipadx=8, ipady=5)

        # Label for password entry
        self.label_password = tk.Label(root, text="Enter Secret key:")
        self.label_password.grid(row=3, column=0, sticky='w', padx=5, pady=5)

        # Entry widget for password entry (hidden by default)
        self.entry_password = tk.Entry(root, width=entry_width, show="*")
        self.entry_password.grid(row=4, column=0, sticky='w', padx=5, pady=5)

        # Password visibility toggle checkbutton
        self.show_password_var = tk.BooleanVar()
        self.show_password_checkbutton = tk.Checkbutton(root, text="Show Secret key",
                                                        variable=self.show_password_var,
                                                        command=self.toggle_password_visibility)
        self.show_password_checkbutton.grid(row=5, column=0, padx=5, pady=5)

        # Button for decoding and viewing hidden data
        self.btn_decode = tk.Button(root, text="Decode & view Hidden Data", command=self.decode)
        self.btn_decode.grid(row=6, column=0, padx=5, pady=5, ipadx=8, ipady=5)

        # Reset button to reset all input fields
        self.btn_reset = tk.Button(root, text="Reset", command=self.reset_fields)
        self.btn_reset.grid(row=7, column=0, padx=5, pady=5, ipadx=8, ipady=5)

        # Text widget to display decoded data
        self.text_decoded_data = tk.Text(root, height=10, width=46)
        self.text_decoded_data.grid(row=8, column=0, padx=5, pady=5)

        # Status label at the bottom for live status updates
        self.status_label = tk.Label(root, text="Live Status Report: ", foreground="green")
        self.status_label.grid(row=9, column=0, sticky='w', padx=5, pady=5)

        # Update status on application start
        self.update_status("Choose an image file")

    def create_menu(self):
        """Create and configure a menu bar with Help and Exit options."""
        # Create a menu bar
        menubar = Menu(self.root)

        # Create a Help menu and add it to the menu bar
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="Help", command=self.show_help)
        menubar.add_cascade(label="Help", menu=help_menu)

        # Add an Exit option to the menu bar
        menubar.add_command(label="Exit", command=self.exit_app)

        # Add the menu bar to the root window
        self.root.config(menu=menubar)

    def show_help(self):
        """Show a Help message with the creator's information."""
        help_text = "Created by: Ashish Gavade\nInstagram: @theashishgavade\nGitHub: https://github.com/theashishgavade/"
        messagebox.showinfo("Help", help_text)

    def exit_app(self):
        """Close the application."""
        self.root.quit()

    def choose_file(self):
        """Open a file dialog to allow the user to choose an encrypted file."""
        file_path = filedialog.askopenfilename(title="Open file", filetypes=[("Image files", "*.jpg *.png *.bmp")])
        if file_path:
            # Set the selected file path in the entry widget
            self.entry_input_image.delete(0, tk.END)
            self.entry_input_image.insert(tk.END, file_path)
            self.update_status("File selected")

    def decode(self):
        """Decode the chosen file using the secret key and display the hidden data."""
        input_path = self.entry_input_image.get()
        password = self.entry_password.get()

        # Validate user input
        if not input_path:
            messagebox.showerror("Error: No file chosen", "You must select an input image file!")
            self.update_status("Error: No file chosen")
            return
        if not password:
            messagebox.showerror("Error: No secret key given", "Please enter a secret key!")
            self.update_status("Error: No secret key given")
            return

        try:
            # Decode the image file using the secret key
            data = decode(input_path, password)
            # Clear the previous decoded data and insert the new decoded data into the text widget
            self.text_decoded_data.delete(1.0, tk.END)
            self.text_decoded_data.insert(tk.END, data)
            messagebox.showinfo("Success", "Decoded successfully!")
            self.update_status("Decoded successfully")
        except FileError as fe:
            # Handle file error exceptions
            messagebox.showerror("File Error", str(fe))
            self.update_status(f"File Error: {fe}")
        except PasswordError as pe:
            # Handle password error exceptions
            messagebox.showerror("Secret key Error", str(pe))
            self.update_status(f"Secret key Error: {pe}")

    def toggle_password_visibility(self):
        """Toggle secret key visibility based on the state of the checkbutton."""
        if self.show_password_var.get():
            # If checkbox is selected, show the secret key
            self.entry_password.config(show="")
            self.show_password_checkbutton.config(text="Hide Secret key")
            self.update_status("Showing Secret key")
        else:
            # If checkbox is deselected, hide the secret key
            self.entry_password.config(show="*")
            self.show_password_checkbutton.config(text="Show Secret key")
            self.update_status("Hiding Secret key")

    def reset_fields(self):
        """Reset all input fields to their initial state."""
        self.entry_input_image.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.text_decoded_data.delete(1.0, tk.END)
        self.show_password_var.set(False)
        self.entry_password.config(show="*")
        self.update_status("All fields have been reset")

    def update_status(self, status_text):
        """Update the status label text."""
        self.status_label.config(text=f"{status_text}")


if __name__ == "__main__":
    root = tk.Tk()
    app = DecodeApp(root)
    root.mainloop()
