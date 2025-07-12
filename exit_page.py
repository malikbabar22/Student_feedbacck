import tkinter as tk
import sys
import subprocess  # Changed from os

def close():
    sys.exit()

def go_back():
    subprocess.Popen(["python", "home.py"])  # Changed from os.system
    root.destroy()  # Added to close the current window

root = tk.Tk()
root.title("Exit Confirmation")
root.geometry("300x150")

tk.Label(root, text="Are you sure you want to exit?", font=("Arial", 12)).pack(pady=30)

tk.Button(root, text="Yes, Exit", command=close).pack(side="left", padx=30)
tk.Button(root, text="No, Go Back", command=go_back).pack(side="right", padx=30)  # Changed command

root.mainloop()
