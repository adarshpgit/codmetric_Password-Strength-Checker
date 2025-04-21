import tkinter as tk
from tkinter import messagebox
import re

def check_strength(password):
    length_error = len(password) < 8
    upper_error = re.search(r"[A-Z]", password) is None
    lower_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"[0-9]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Minimum 8 characters": length_error,
        "At least one uppercase letter": upper_error,
        "At least one lowercase letter": lower_error,
        "At least one digit": digit_error,
        "At least one special character": symbol_error
    }

    score = 5 - sum(errors.values())
    if score == 5:
        strength = "Strong 💪"
    elif 3 <= score < 5:
        strength = "Moderate ⚠️"
    else:
        strength = "Weak ❌"

    return strength, [msg for msg, failed in errors.items() if failed]

def evaluate_password():
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Empty", "Please enter a password.")
        return

    strength, suggestions = check_strength(password)
    result_label.config(text=f"Strength: {strength}", fg="#155724" if strength == "Strong 💪" else "#856404")

    suggestions_text.delete(1.0, tk.END)
    if suggestions:
        suggestions_text.insert(tk.END, "Suggestions:\n" + "\n".join(f"- {s}" for s in suggestions))
    else:
        suggestions_text.insert(tk.END, "Your password looks great! 🔒")

def toggle_password():
    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("420x330")
root.configure(bg="#eafaf1")
root.resizable(False, False)

frame = tk.Frame(root, bg="#eafaf1", padx=20, pady=20)
frame.pack(fill="both", expand=True)

tk.Label(frame, text="Enter Password:", bg="#eafaf1", font=("Segoe UI", 11)).pack(anchor="w")
password_entry = tk.Entry(frame, show="*", width=30, font=("Segoe UI", 11))
password_entry.pack(pady=5)

# Show password checkbox
show_var = tk.BooleanVar()
show_checkbox = tk.Checkbutton(frame, text="Show Password", variable=show_var, onvalue=True, offvalue=False,
                               command=toggle_password, bg="#eafaf1", font=("Segoe UI", 10))
show_checkbox.pack()

tk.Button(frame, text="Check Strength", bg="#28a745", fg="white", activebackground="#218838",
          font=("Segoe UI", 10, "bold"), command=evaluate_password).pack(pady=10)

result_label = tk.Label(frame, text="", font=("Segoe UI", 11, "bold"), bg="#eafaf1")
result_label.pack()

suggestions_text = tk.Text(frame, height=6, width=40, bg="#f8f9fa", font=("Segoe UI", 10))
suggestions_text.pack(pady=10)

root.mainloop()
