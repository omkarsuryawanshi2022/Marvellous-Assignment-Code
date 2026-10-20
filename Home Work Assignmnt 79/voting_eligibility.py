
import tkinter as tk
from tkinter import messagebox

def check_eligibility():
    name = name_entry.get().strip()

    try:
        age = int(age_entry.get())

        if not name:
            messagebox.showerror("Error", "Please enter your name.")
            return

        if age < 0:
            messagebox.showerror("Error", "Age cannot be negative.")
            return

        if age >= 18:
            result_label.config(
                text=f"{name}, you are eligible to vote.",
                fg="green"
            )
        else:
            result_label.config(
                text=f"{name}, you are not eligible to vote.",
                fg="red"
            )

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid age.")

root = tk.Tk()
root.title("Voting Eligibility Checker")
root.geometry("400x250")

tk.Label(root, text="Voting Eligibility Checker",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter Your Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="Enter Your Age:").pack()
age_entry = tk.Entry(root)
age_entry.pack(pady=5)

tk.Button(root, text="Check Eligibility",
          command=check_eligibility).pack(pady=10)

result_label = tk.Label(root, text="",
                        font=("Arial", 11))
result_label.pack()

root.mainloop()
