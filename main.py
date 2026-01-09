import tkinter as tk
from tkinter import messagebox


def submit_form():
    # Retrieve data from entries
    name = name_entry.get()
    email = email_entry.get()

    if name and email:
        print(f"Form Submitted: Name: {name}, Email: {email}")
        messagebox.showinfo("Success", f"Hello {name}, your data was saved!")
        # Clear the fields
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill out all fields.")


# 1. Create the main window
root = tk.Tk()
root.title("User Registration Form")
root.geometry("300x200")

# 2. Add Name Label and Entry
tk.Label(root, text="Full Name").pack(pady=(10, 0), padx=30)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# 3. Add Email Label and Entry
tk.Label(root, text="Email Address").pack(pady=(10, 0))
email_entry = tk.Entry(root)
email_entry.pack(pady=5)

# 4. Add Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack(pady=20)

# 5. Run the application
root.mainloop()