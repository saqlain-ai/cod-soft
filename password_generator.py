import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation

    if length < 8:
        messagebox.showerror("Error", "Password length should be at least 8 characters.")
        return None

    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def generate_password_callback():
    length = int(length_entry.get())

    password = generate_password(length)

    if password:
        password_text.delete(1.0, tk.END)
        password_text.insert(tk.END, password) 
        password_text.tag_config('center', justify='center')
        password_text.tag_add('center', 1.0, tk.END)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300") 

length_label = tk.Label(root, text="Enter the desired length of the password:")
length_label.pack(pady=20)  

length_entry = tk.Entry(root, width=20)
length_entry.pack(pady=10)  

generate_button = tk.Button(root, text="Generate Password", command=generate_password_callback)
generate_button.pack(pady=10)  

password_text = tk.Text(root, height=5, width=40, font=("Arial", 24))
password_text.pack(pady=20)  

root.mainloop()