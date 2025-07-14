import tkinter as tk
from tkinter import messagebox
import os

def submit_data():
    name = name_entry.get()
    course = course_entry.get()
    rating = rating_entry.get()
    comment = comment_entry.get("1.0", tk.END).strip()

    if not name or not course or not rating:
        messagebox.showwarning("Missing Info", "Please fill all fields.")
        return

    with open("temp.txt", "w") as f:
        f.write(f"{name}|{course}|{rating}|{comment}")

    os.system("python submit_feedback.py")

root = tk.Tk()
root.title("Feedback Form")
root.geometry("400x400")

# Unified font
FONT = ("Segoe UI", 11)

tk.Label(root, text="Feedback Form", font=("Segoe UI", 16, "bold")).pack(pady=10)

tk.Label(root, text="Name:", font=FONT).pack(pady=5)
name_entry = tk.Entry(root, font=FONT)
name_entry.pack()

tk.Label(root, text="Course:", font=FONT).pack(pady=5)
course_entry = tk.Entry(root, font=FONT)
course_entry.pack()

tk.Label(root, text="Rating (1-5):", font=FONT).pack(pady=5)
rating_entry = tk.Entry(root, font=FONT)
rating_entry.pack()

tk.Label(root, text="Comments:", font=FONT).pack(pady=5)
comment_entry = tk.Text(root, height=5, width=30, font=FONT)
comment_entry.pack(pady=5)

tk.Button(root, text="Submit", font=FONT, command=submit_data).pack(pady=10)

root.mainloop()
