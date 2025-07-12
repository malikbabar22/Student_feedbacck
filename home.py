import tkinter as tk
import os

root = tk.Tk()
root.title("Student Feedback System")
root.geometry("400x300")

# Use grid instead of pack for better layout control
tk.Label(root, text="Welcome to Feedback System", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=20)

tk.Button(root, text="Give Feedback", width=20, command=lambda: os.system("python feedback_form.py")).grid(row=1, column=0, columnspan=2, pady=10)
tk.Button(root, text="View Feedback", width=20, command=lambda: os.system("python view_feedback.py")).grid(row=2, column=0, columnspan=2, pady=10)
tk.Button(root, text="Exit", width=20, command=lambda: os.system("python exit_page.py")).grid(row=3, column=0, columnspan=2, pady=10)

# Center everything
root.grid_columnconfigure(0, weight=1)
root.mainloop()
