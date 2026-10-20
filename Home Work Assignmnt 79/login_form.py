
import tkinter as tk
from tkinter import messagebox

# Predefined credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "12345"

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        result_label.config(text="Login Successful!", fg="green")
        messagebox.showinfo("Success", "Welcome! Login successful.")
    else:
        result_label.config(text="Invalid username or password.",
                            fg="red")
        messagebox.showerror("Login Failed",
                             "Invalid username or password.")

root = tk.Tk()
root.title("Basic Login Form")
root.geometry("350x250")

tk.Label(root, text="Login Form",
         font=("Arial", 16, "bold")).pack(pady=15)

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Login", command=login).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 10))
result_label.pack()

root.mainloop()
