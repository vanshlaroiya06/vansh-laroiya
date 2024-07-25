import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

# Define the main application window
class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.create_widgets()

    def create_widgets(self):
        # Label and entry for password length
        self.length_label = ttk.Label(self.root, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)
        self.length_entry = ttk.Entry(self.root, width=10)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        # Checkbuttons for password complexity options
        self.lower_var = tk.IntVar()
        self.lower_check = ttk.Checkbutton(self.root, text="Include lowercase letters (a-z)", variable=self.lower_var)
        self.lower_check.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

        self.upper_var = tk.IntVar()
        self.upper_check = ttk.Checkbutton(self.root, text="Include uppercase letters (A-Z)", variable=self.upper_var)
        self.upper_check.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

        self.digits_var = tk.IntVar()
        self.digits_check = ttk.Checkbutton(self.root, text="Include digits (0-9)", variable=self.digits_var)
        self.digits_check.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

        self.punctuation_var = tk.IntVar()
        self.punctuation_check = ttk.Checkbutton(self.root, text="Include punctuation (!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~)", variable=self.punctuation_var)
        self.punctuation_check.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

        # Button to generate password
        self.generate_button = ttk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Text area to display generated password
        self.password_display = tk.Text(self.root, height=5, width=40)
        self.password_display.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for password length.")
            return

        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than zero.")
            return

        include_lower = bool(self.lower_var.get())
        include_upper = bool(self.upper_var.get())
        include_digits = bool(self.digits_var.get())
        include_punctuation = bool(self.punctuation_var.get())

        if not (include_lower or include_upper or include_digits or include_punctuation):
            messagebox.showerror("Error", "Please select at least one option for password generation.")
            return

        characters = ''
        if include_lower:
            characters += string.ascii_lowercase
        if include_upper:
            characters += string.ascii_uppercase
        if include_digits:
            characters += string.digits
        if include_punctuation:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_display.delete(1.0, tk.END)  # Clear previous content
        self.password_display.insert(tk.END, password)

# Main function to run the application
def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
