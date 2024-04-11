import tkinter as tk
from tkinter import ttk, messagebox, filedialog, Menu, Text
from stegano import encode, FileError, DataError, PasswordError

class EncodeApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Steganography Software - Encode")
        self.root.geometry("410x450")

        # Create variables to hold input values
        self.input_path = tk.StringVar()
        self.text = tk.StringVar()
        self.password = tk.StringVar()

        # Create the UI widgets
        self.create_widgets()

        # Create the menu bar
        self.create_menu()

    def create_widgets(self):
        # Create the main frame to hold all widgets
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0)

        # Input Image File section
        ttk.Label(main_frame, text="Enter File Path Or Click DERIVE FILE Button:").grid(row=0, column=0, sticky="w", padx=5)
        self.input_entry = ttk.Entry(main_frame, textvariable=self.input_path, width=60)
        self.input_entry.grid(row=1, column=0, sticky='w', padx=5, pady=5)
        # Button to open a file dialog to choose the input file
        ttk.Button(main_frame, text="DERIVE FILE", command=self.choose_file, width=40).grid(row=2, column=0, padx=5, pady=5, ipadx=5, ipady=6)

        # Password section
        ttk.Label(main_frame, text="Enter Secret Key:").grid(row=3, column=0, sticky="w", padx=5)
        self.password_entry = ttk.Entry(main_frame, textvariable=self.password, show="*", width=60)
        self.password_entry.grid(row=4, column=0, sticky='w', padx=5, pady=5)

        # Add password visibility toggle checkbutton
        self.show_password_var = tk.BooleanVar()
        self.show_password_checkbutton = ttk.Checkbutton(main_frame, text="Show Secret Key",
                                                         variable=self.show_password_var,
                                                         command=self.toggle_password_visibility)
        self.show_password_checkbutton.grid(row=5, column=0, padx=5, pady=5)

        # Text to hide section
        ttk.Label(main_frame, text="Enter text to hide:").grid(row=6, column=0, sticky="w", padx=5)
        # Create a Text widget for the text area
        self.text_area = Text(main_frame, height=5, width=46)
        self.text_area.grid(row=7, column=0, padx=5, pady=5)

        # Encode and Save Button
        self.encode_button = ttk.Button(main_frame, text="Encode and Save", command=self.encode, width=40)
        self.encode_button.grid(row=8, column=0, pady=5, padx=5, ipady=8, ipadx=5)

        # Reset button
        self.reset_button = ttk.Button(main_frame, text="Reset", command=self.reset_fields, width=40)
        self.reset_button.grid(row=9, column=0, pady=5, padx=5, ipady=8, ipadx=5)

        # Status label at the bottom
        self.status_label = ttk.Label(self.root, text="Live Status Report: ", foreground="green")
        self.status_label.grid(row=10, column=0, sticky="w", pady=10)

        # Initial status update
        self.update_status("Choose an image file")

        # Define a custom style for blue buttons
        style = ttk.Style()
        style.configure('blue.TButton', background='blue', foreground='white')

    def create_menu(self):
        # Create a menu bar
        menubar = Menu(self.root)

        # Create a Help menu
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="Help", command=self.show_help)
        menubar.add_cascade(label="Help", menu=help_menu)

        # Create an Exit menu
        menubar.add_command(label="Exit", command=self.exit_app)

        # Add the menu bar to the root window
        self.root.config(menu=menubar)

    def show_help(self):
        # Create a popup for Help menu item
        help_text = "Created by: Ashish Gavade \nInstagram: @theashishgavade\nGitHub: https://github.com/theashishgavade/"
        messagebox.showinfo("Help", f"{help_text}")

    def exit_app(self):
        # Exit the application
        self.root.quit()

    def choose_file(self):
        # Open a file dialog to choose an input image file
        file_path = filedialog.askopenfilename(title="Choose Input Image File",
                                               filetypes=(("Image files", "*.jpg *.png *.bmp"),))
        if file_path:
            self.input_path.set(file_path)
            self.update_status("File selected")

    def encode(self):
        # Retrieve input values from the UI
        input_path = self.input_path.get()
        text = self.text_area.get("1.0", "end-1c")  # Get the text from the Text widget
        password = self.password.get()

        # Check for empty fields
        if not input_path:
            messagebox.showerror("Error: No file chosen", "You must select input image file!")
            self.update_status("Error: No file chosen")
            return
        elif not text:
            messagebox.showerror("Text is empty", "Please enter some text to hide!")
            self.update_status("Error: Text is empty")
            return
        elif not password:
            messagebox.showerror("Error: No Secret key given", "Please enter a Secret key!")
            self.update_status("Error: No Secret key given")
            return

        # Ask for the output file path to save the encoded image
        output_path = filedialog.asksaveasfilename(title="Save encoded file", defaultextension=".png",
                                                   filetypes=(("PNG files", "*.png"),))
        if not output_path:
            messagebox.showinfo("Operation cancelled", "Operation cancelled by user!")
            self.update_status("Operation cancelled by user")
            return

        # Encode the text in the image
        try:
            loss = encode(input_path, text, output_path, password)
            messagebox.showinfo("Success", f"Encoded Successfully!\n\nImage Data Loss = {loss:.5%}")
            self.update_status("Encoding and saving successful")
        except FileError as fe:
            messagebox.showerror("File Error", str(fe))
            self.update_status(f"File Error: {fe}")
        except DataError as de:
            messagebox.showerror("Data Error", str(de))
            self.update_status(f"Data Error: {de}")

    def toggle_password_visibility(self):
        """Toggle password visibility based on the state of the checkbutton."""
        # Check if password should be shown or hidden based on the checkbutton state
        if self.show_password_var.get():
            # If the checkbox is selected, show the password
            self.password_entry.config(show="")
            self.show_password_checkbutton.config(text="Hide Secret Key")
        else:
            # If the checkbox is deselected, hide the password
            self.password_entry.config(show="*")
            self.show_password_checkbutton.config(text="Show Secret Key")

        # Update status based on password visibility toggle
        if self.show_password_var.get():
            self.update_status("Showing Secret key")
        else:
            self.update_status("Hiding Secret key")

    def reset_fields(self):
        # Reset all input fields to their default state
        self.input_path.set("")
        self.text_area.delete("1.0", "end")  # Clear the text area
        self.password.set("")
        self.password_entry.config(show="*")
        self.show_password_var.set(False)
        self.update_status("All fields have been reset")

    def update_status(self, status_text):
        # Update the status label text with the given status message
        self.status_label.config(text=f"{status_text}")

if __name__ == "__main__":
    # Create the main application window and initialize the app
    root = tk.Tk()
    app = EncodeApp(root)
    root.mainloop()
