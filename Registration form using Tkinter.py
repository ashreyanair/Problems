import tkinter as tk
from tkinter import messagebox

# File to store registrations
DATA_FILE = "registrations.txt"

def submit_form():
    name = name_var.get().strip()
    email = email_var.get().strip()
    gender = gender_var.get().strip()
    country = country_var.get().strip()

    if not name or not email:
        messagebox.showerror("Input Error", "Name and Email are required!")
        return

    # Prepare and write data
    entry = f"Name: {name} | Email: {email} | Gender: {gender} | Country: {country}\n"
    with open(DATA_FILE, "a") as file:
        file.write(entry)

    messagebox.showinfo("Success", "Registration saved!")

    # Clear form
    name_var.set("")
    email_var.set("")
    gender_var.set("")
    country_var.set("")

# GUI Setup
root = tk.Tk()
root.title("Registration Form")
root.geometry("450x300")
root.resizable(False, False)

# Variables
name_var = tk.StringVar()
email_var = tk.StringVar()
gender_var = tk.StringVar()
country_var = tk.StringVar()

# Labels and Entry widgets (side by side)
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root, textvariable=name_var, width=30).grid(row=0, column=1)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root, textvariable=email_var, width=30).grid(row=1, column=1)

tk.Label(root, text="Gender:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root, textvariable=gender_var, width=30).grid(row=2, column=1)

tk.Label(root, text="Country:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root, textvariable=country_var, width=30).grid(row=3, column=1)

tk.Button(root, text="Submit", command=submit_form).grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()