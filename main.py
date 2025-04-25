import tkinter as tk
from tkinter import messagebox

# Caesar Cipher Function
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

# Cipher Button Function
def perform_cipher():
    text = message_entry.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        status_label.config(text="❌ Please enter a valid number for shift!", fg="red")
        return

    mode = mode_var.get()
    result = caesar_cipher(text, shift, mode)
    result_var.set(result)
    status_label.config(text="✅ Done!", fg="green")

# Clear All Fields
def clear_all():
    message_entry.delete("1.0", tk.END)
    shift_entry.delete(0, tk.END)
    result_var.set("")
    status_label.config(text="")

# Main GUI Window
root = tk.Tk()
root.title("🔐 Caesar Cipher - Encrypt & Decrypt")
root.geometry("550x500")
root.configure(bg="#E6E6FA")  # Lavender background color
root.resizable(False, False)

# Title
tk.Label(root, text="Caesar Cipher", font=("Arial", 18, "bold"), bg="#E6E6FA", fg="#333").pack(pady=10)

# Frame for message input
msg_frame = tk.Frame(root, bg="#E6E6FA")
msg_frame.pack(pady=5)
tk.Label(msg_frame, text="Enter Message:", font=("Arial", 12), bg="#E6E6FA").pack(anchor="w")
message_entry = tk.Text(msg_frame, height=5, width=60, font=("Arial", 12))
message_entry.pack()

# Frame for shift input
shift_frame = tk.Frame(root, bg="#E6E6FA")
shift_frame.pack(pady=5)
tk.Label(shift_frame, text="Shift Key (Number):", font=("Arial", 12), bg="#E6E6FA").pack(anchor="w")
shift_entry = tk.Entry(shift_frame, font=("Arial", 12), width=10)
shift_entry.pack()

# Mode selection
mode_var = tk.StringVar(value="encrypt")
mode_frame = tk.Frame(root, bg="#E6E6FA")
mode_frame.pack(pady=5)
tk.Label(mode_frame, text="Mode:", font=("Arial", 12), bg="#E6E6FA").pack(anchor="w")
tk.Radiobutton(mode_frame, text="Encrypt", variable=mode_var, value="encrypt", font=("Arial", 11), bg="#E6E6FA").pack(anchor="w")
tk.Radiobutton(mode_frame, text="Decrypt", variable=mode_var, value="decrypt", font=("Arial", 11), bg="#E6E6FA").pack(anchor="w")

# Buttons
btn_frame = tk.Frame(root, bg="#E6E6FA")
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="🔄 Do Cipher", command=perform_cipher, font=("Arial", 12), bg="#4CAF50", fg="white", width=15).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="🧹 Clear", command=clear_all, font=("Arial", 12), bg="#f44336", fg="white", width=10).grid(row=0, column=1)

# Result field
result_var = tk.StringVar()
tk.Label(root, text="Result:", font=("Arial", 12), bg="#E6E6FA").pack()
tk.Entry(root, textvariable=result_var, font=("Arial", 12), width=60, justify="center", state="readonly").pack(pady=5)

# Status label
status_label = tk.Label(root, text="", font=("Arial", 11), bg="#E6E6FA", fg="green")
status_label.pack(pady=5)

root.mainloop()
