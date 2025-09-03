import tkinter as tk
from tkinter import messagebox
import re

def check_strength():
    password = entry.get()
    if len(password) == 0:
        strength = "Please enter a password!"
    elif len(password) < 6:
        strength = "Weak"
    elif not re.search("[a-z]", password):
        strength = "Weak (no lowercase)"
    elif not re.search("[A-Z]", password):
        strength = "Weak (no uppercase)"
    elif not re.search("[0-9]", password):
        strength = "Moderate (add digits)"
    elif not re.search("[@#$%^&*!]", password):
        strength = "Moderate (add special char)"
    else:
        strength = "Strong"
    messagebox.showinfo("Password Strength", f"Your password is: {strength}")

root = tk.Tk()
root.title("Password Strength Checker")

label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

btn = tk.Button(root, text="Check Strength", command=check_strength)
btn.pack(pady=10)

root.mainloop()
