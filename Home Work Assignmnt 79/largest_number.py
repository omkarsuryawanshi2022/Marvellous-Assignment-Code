
import tkinter as tk
from tkinter import messagebox

def find_maximum():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())

        largest = max(num1, num2, num3)
        result_label.config(text=f"Largest Number: {largest}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Find the Largest Number")
root.geometry("350x300")

tk.Label(root, text="Find the Largest Number",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter First Number:").pack()
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Enter Second Number:").pack()
entry2 = tk.Entry(root)
entry2.pack(pady=5)

tk.Label(root, text="Enter Third Number:").pack()
entry3 = tk.Entry(root)
entry3.pack(pady=5)

tk.Button(root, text="Find Maximum",
          command=find_maximum).pack(pady=10)

result_label = tk.Label(root, text="Result will appear here",
                        font=("Arial", 12))
result_label.pack()

root.mainloop()
