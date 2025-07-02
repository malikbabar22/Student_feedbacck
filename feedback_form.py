import tkinter as tk
import os

def submit_data():
    name = name_entry.get()
    course = course_entry.get()
    rating = rating_entry.get()
    comment = comment_entry.get("1.0", tk.END).strip()

    if not name or not course or not rating:
        tk.messagebox.showwarning("Missing Info", "Please fill all fields.")
        return

    with open("temp.txt", "w") as f:
        f.write(f"{name}|{course}|{rating}|{comment}")

    os.system("python submit_feedback.py")

root = tk.Tk()
root.title("Feedback Form")
root.geometry("400x400")

tk.Label(root, text="Feedback Form", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Course:").pack()
course_entry = tk.Entry(root)
course_entry.pack()

tk.Label(root, text="Rating (1-5):").pack()
rating_entry = tk.Entry(root)
rating_entry.pack()

tk.Label(root, text="Comments:").pack()
comment_entry = tk.Text(root, height=5, width=30)
comment_entry.pack()

tk.Button(root, text="Submit", command=submit_data).pack(pady=10)

root.mainloop()

