import tkinter as tk

def open_feedback_form():
    import feedback_form
    feedback_form.main()

def open_view_feedback():
    import view_feedback
    view_feedback.main()

def open_exit_page():
    import exit_page
    exit_page.main()

root = tk.Tk()
root.title("Student Feedback System - Modified UI")
root.geometry("600x400")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(expand=True)

title_label = tk.Label(
    frame,
    text="Welcome to the Feedback System",
    font=("Helvetica", 18, "bold"),
    bg="#f0f0f0",
    fg="#333"
)
title_label.pack(pady=20)

btn_style = {
    "width": 25,
    "height": 2,
    "font": ("Arial", 12, "bold"),
    "bg": "#007BFF",       # Blue background
    "fg": "white",         # White text
    "activebackground": "#0056b3",  # Darker blue on hover
    "bd": 0
}

feedback_btn = tk.Button(frame, text="Give Feedback", command=open_feedback_form, **btn_style)
feedback_btn.pack(pady=10)

view_btn = tk.Button(frame, text="View Feedback", command=open_view_feedback, **btn_style)
view_btn.pack(pady=10)

exit_btn = tk.Button(frame, text="Exit", command=open_exit_page, **btn_style)
exit_btn.pack(pady=10)

root.mainloop()
