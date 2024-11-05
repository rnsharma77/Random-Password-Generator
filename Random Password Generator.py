import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGeneratorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Secure Password Generator")
        self.master.geometry("400x400")
        self.master.configure(bg="#34495E")  # Dark background for a sleek look
        
        # Title Label
        self.title_label = tk.Label(master, text="Secure Password Generator", font=("Helvetica", 16, "bold"),
                                    fg="#F1C40F", bg="#34495E")
        self.title_label.pack(pady=10)
        
        # Password Length Slider
        self.length_label = tk.Label(master, text="Password Length", font=("Helvetica", 12),
                                     fg="#ECF0F1", bg="#34495E")
        self.length_label.pack(pady=5)
        
        self.length_slider = tk.Scale(master, from_=8, to=32, orient="horizontal", length=250,
                                      font=("Helvetica", 10), bg="#1ABC9C", fg="white", troughcolor="#F39C12",
                                      highlightbackground="#34495E")
        self.length_slider.set(12)  # Default length
        self.length_slider.pack(pady=5)
        
        # Checkbox for password criteria
        self.include_numbers = tk.BooleanVar()
        self.include_symbols = tk.BooleanVar()
        self.include_uppercase = tk.BooleanVar()

        self.numbers_check = tk.Checkbutton(master, text="Include Numbers", font=("Helvetica", 10),
                                            variable=self.include_numbers, fg="#ECF0F1", bg="#34495E",
                                            activebackground="#34495E", activeforeground="#ECF0F1",
                                            selectcolor="#1ABC9C")
        self.numbers_check.pack()

        self.symbols_check = tk.Checkbutton(master, text="Include Symbols", font=("Helvetica", 10),
                                            variable=self.include_symbols, fg="#ECF0F1", bg="#34495E",
                                            activebackground="#34495E", activeforeground="#ECF0F1",
                                            selectcolor="#1ABC9C")
        self.symbols_check.pack()

        self.uppercase_check = tk.Checkbutton(master, text="Include Uppercase Letters", font=("Helvetica", 10),
                                              variable=self.include_uppercase, fg="#ECF0F1", bg="#34495E",
                                              activebackground="#34495E", activeforeground="#ECF0F1",
                                              selectcolor="#1ABC9C")
        self.uppercase_check.pack()

        # Generate Password Button
        self.generate_button = tk.Button(master, text="Generate Password", font=("Helvetica", 12, "bold"),
                                         bg="#3498DB", fg="white", command=self.generate_password)
        self.generate_button.pack(pady=15)
        
        # Display Generated Password
        self.password_display = tk.Entry(master, font=("Helvetica", 14), width=24, justify="center",
                                         bg="#1ABC9C", fg="#ECF0F1", bd=0)
        self.password_display.pack(pady=10)

        # Copy to Clipboard Button
        self.copy_button = tk.Button(master, text="Copy to Clipboard", font=("Helvetica", 10, "bold"),
                                     bg="#E74C3C", fg="white", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=5)

    def generate_password(self):
        length = self.length_slider.get()
        include_numbers = self.include_numbers.get()
        include_symbols = self.include_symbols.get()
        include_uppercase = self.include_uppercase.get()

        # Define character pools based on criteria
        lowercase_letters = string.ascii_lowercase
        numbers = string.digits if include_numbers else ''
        symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?/" if include_symbols else ''
        uppercase_letters = string.ascii_uppercase if include_uppercase else ''
        
        all_characters = lowercase_letters + numbers + symbols + uppercase_letters

        if len(all_characters) == 0:
            messagebox.showwarning("Selection Error", "Please select at least one character type!")
            return

        # Generate password
        password = ''.join(random.choice(all_characters) for _ in range(length))
        self.password_display.delete(0, tk.END)
        self.password_display.insert(0, password)

    def copy_to_clipboard(self):
        password = self.password_display.get()
        if password:
            self.master.clipboard_clear()
            self.master.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Copy Error", "No password to copy!")

# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()
