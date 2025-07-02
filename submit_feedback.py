import sqlite3
import tkinter as tk
import os

# Read data from temp file
with open("temp.txt", "r") as f:
    content = f.read().split("|")
    name, course, rating, comment = content

# Save to SQLite DB
conn = sqlite3.connect("feedback.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        course TEXT,
        rating INTEGER,
        comment TEXT
    )
""")
cursor.execute("INSERT INTO feedback (name, course, rating, comment) VALUES (?, ?, ?, ?)",
               (name, course, int(rating), comment))
conn.commit()
conn.close()

# Show success window
root = tk.Tk()
root.title("Submitted")
root.geometry("300x150")

tk.Label(root, text="Feedback Submitted!", font=("Arial", 14)).pack(pady=30)
tk.Button(root, text="Back to Home", command=lambda: os.system("python home.py")).pack()

root.mainloop()
