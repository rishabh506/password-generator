import tkinter as tk
from tkinter import messagebox
import random,string,pyperclip

def generate_password():
    length = length_slider.get()
    characters = ""

    if use_uppercase.get():
        characters += string.ascii_uppercase
    if use_lowercase.get():
        characters += string.ascii_lowercase
    if use_numbers.get():
        characters += string.digits 
    if use_symbols.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Error", "Please select at least one option!")
        return
    
    password = "".join(random.choice(characters) for _ in range (length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

    check_strentgth(password)

def check_strentgth(password):
    strength = "Weak"
    if len(password) >= 12 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password):
        strength = "Strong"
    elif len(password) >=8: 
        strength = "Medium"

    strength_label.config(text=f"Strength: {strength}")

root = tk.Tk()
root.title("🔑 Password Generator")
root.geometry("450x300")

use_uppercase = tk.BooleanVar(value=True)
use_lowercase = tk.BooleanVar(value=True)
use_numbers = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Uppercase(A-Z)", variable=use_uppercase).pack(anchor="w")
tk.Checkbutton(root, text="Lowercase(a-z)", variable=use_lowercase).pack(anchor="w")
tk.Checkbutton(root, text="Numbers(0-9)", variable=use_numbers).pack(anchor="w")
tk.Checkbutton(root, text="Symbols(!@#$)", variable=use_symbols).pack(anchor="w")

tk.Label(root, text="Password Length: ").pack()
length_slider = tk.Scale(root, from_=4, to=20, orient="horizontal")
length_slider.set(12)
length_slider.pack()


password_entry = tk.Entry(root, width=30, font=("Arial", 14))
password_entry.pack(pady=10)

strength_label = tk.Label(root, text="Strength:", font=("Arial", 12))
strength_label.pack()

tk.Button(root, text="Genrated Password", command=generate_password).pack(pady=5)

root.mainloop()