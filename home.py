import tkinter as tk
import os

root = tk.Tk()
root.title("Student Feedback System")
root.geometry("400x300")

tk.Label(root, text="Welcome to Feedback System", font=("Arial", 16)).pack(pady=20)

tk.Button(root, text="Give Feedback", width=20, command=lambda: os.system("python feedback_form.py")).pack(pady=10)
tk.Button(root, text="View Feedback", width=20, command=lambda: os.system("python view_feedback.py")).pack(pady=10)
tk.Button(root, text="Exit", width=20, command=lambda: os.system("python exit_page.py")).pack(pady=10)

root.mainloop()
