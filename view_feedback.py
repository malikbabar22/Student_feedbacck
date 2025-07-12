import sqlite3
import tkinter as tk
import os

conn = sqlite3.connect("feedback.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS feedback (id INTEGER PRIMARY KEY, name TEXT, course TEXT, rating INTEGER, comment TEXT)")
cursor.execute("SELECT name, course, rating, comment FROM feedback")
data = cursor.fetchall()
conn.close()

root = tk.Tk()
root.title("View Feedback")
root.geometry("500x400")

tk.Label(root, text="All Feedback", font=("Arial", 16)).pack(pady=10)

box = tk.Text(root, wrap=tk.WORD)
box.pack(expand=True, fill="both")

# ✅ 1st Change: Use tuple unpacking for readability
if data:
    for name, course, rating, comment in data:
        box.insert(tk.END, f"Name: {name}\nCourse: {course}\nRating: {rating}\nComment: {comment}\n{'-'*40}\n")
else:
    box.insert(tk.END, "No feedback submitted yet.")

# ✅ 2nd Change: Moved button command to a named function
def go_home():
    os.system("python home.py")

tk.Button(root, text="Back to Home", command=go_home).pack(pady=10)

root.mainloop()
