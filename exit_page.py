import tkinter as tk
import sys
import os

def close():
    sys.exit()

root = tk.Tk()
root.title("Exit Confirmation")
root.geometry("300x150")

tk.Label(root, text="Are you sure you want to exit?", font=("Arial", 12)).pack(pady=30)

tk.Button(root, text="Yes, Exit", command=close).pack(side="left", padx=30)
tk.Button(root, text="No, Go Back", command=lambda: os.system("python home.py")).pack(side="right", padx=30)

root.mainloop()
