import customtkinter as ctk
from tkinter import messagebox, Listbox, END, SINGLE, Scrollbar, VERTICAL

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
        display_contacts()
    else:
        messagebox.showerror("Error", "Name and phone number are required!")

def display_contacts():
    contacts_listbox.delete(0, END)
    for contact in contacts:
        contacts_listbox.insert(END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    query = search_entry.get().lower()
    search_results = [contact for contact in contacts if query in contact['name'].lower() or query in contact['phone']]
    
    contacts_listbox.delete(0, END)
    for contact in search_results:
        contacts_listbox.insert(END, f"{contact['name']} - {contact['phone']}")

def select_contact(event):
    try:
        selected_index = contacts_listbox.curselection()[0]
        selected_contact = contacts[selected_index]

        name_entry.delete(0, END)
        name_entry.insert(0, selected_contact['name'])
        
        phone_entry.delete(0, END)
        phone_entry.insert(0, selected_contact['phone'])

        email_entry.delete(0, END)
        email_entry.insert(0, selected_contact['email'])

        address_entry.delete(0, END)
        address_entry.insert(0, selected_contact['address'])

        update_button.configure(state="normal")
        delete_button.configure(state="normal")
    except IndexError:
        pass

def update_contact():
    selected_index = contacts_listbox.curselection()[0]
    contacts[selected_index] = {
        "name": name_entry.get(),
        "phone": phone_entry.get(),
        "email": email_entry.get(),
        "address": address_entry.get()
    }
    messagebox.showinfo("Success", "Contact updated successfully!")
    clear_entries()
    display_contacts()

def delete_contact():
    selected_index = contacts_listbox.curselection()[0]
    del contacts[selected_index]
    messagebox.showinfo("Success", "Contact deleted successfully!")
    clear_entries()
    display_contacts()

def clear_entries():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)
    update_button.configure(state="disabled")
    delete_button.configure(state="disabled")

def create_main_window():
    global name_entry, phone_entry, email_entry, address_entry, search_entry, contacts_listbox, update_button, delete_button

    window = ctk.CTk()
    window.title("Contact Book")
    window.geometry("700x600")
    window.resizable(True, True)

    main_frame = ctk.CTkFrame(window, corner_radius=15, bg_color="#1e1e1e")
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    for i in range(9):
        main_frame.grid_rowconfigure(i, weight=1)
    for i in range(2):
        main_frame.grid_columnconfigure(i, weight=1)

    ctk.CTkLabel(main_frame, text="Name:", font=("Arial", 12, "bold"), text_color="#ffffff").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    name_entry = ctk.CTkEntry(main_frame, width=350, placeholder_text="Enter name")
    name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    ctk.CTkLabel(main_frame, text="Phone:", font=("Arial", 12, "bold"), text_color="#ffffff").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    phone_entry = ctk.CTkEntry(main_frame, width=350, placeholder_text="Enter phone number")
    phone_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    ctk.CTkLabel(main_frame, text="Email:", font=("Arial", 12, "bold"), text_color="#ffffff").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    email_entry = ctk.CTkEntry(main_frame, width=350, placeholder_text="Enter email")
    email_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

    ctk.CTkLabel(main_frame, text="Address:", font=("Arial", 12, "bold"), text_color="#ffffff").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    address_entry = ctk.CTkEntry(main_frame, width=350, placeholder_text="Enter address")
    address_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

    add_button = ctk.CTkButton(main_frame, text="Add Contact", command=add_contact, width=180)
    add_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")

    update_button = ctk.CTkButton(main_frame, text="Update Contact", state="disabled", command=update_contact, width=180)
    update_button.grid(row=5, column=0, columnspan=2, pady=5, sticky="nsew")

    delete_button = ctk.CTkButton(main_frame, text="Delete Contact", state="disabled", command=delete_contact, width=180)
    delete_button.grid(row=6, column=0, columnspan=2, pady=5, sticky="nsew")

    search_entry = ctk.CTkEntry(main_frame, placeholder_text="Search by name or phone", width=350)
    search_entry.grid(row=7, column=0, padx=10, pady=10, sticky="ew")

    search_button = ctk.CTkButton(main_frame, text="Search", command=search_contact, width=180)
    search_button.grid(row=7, column=1, padx=10, pady=10, sticky="ew")

    listbox_frame = ctk.CTkFrame(main_frame)
    listbox_frame.grid(row=8, column=0, columnspan=2, pady=10, sticky="nsew")

    scrollbar = Scrollbar(listbox_frame, orient=VERTICAL)
    contacts_listbox = Listbox(listbox_frame, selectmode=SINGLE, width=60, height=15, bg="#2e2e2e", fg="#ffffff", borderwidth=2, relief="solid", yscrollcommand=scrollbar.set)
    contacts_listbox.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=contacts_listbox.yview)
    scrollbar.pack(side="right", fill="y")

    contacts_listbox.bind('<<ListboxSelect>>', select_contact)

    return window

if __name__ == "__main__":
    main_window = create_main_window()
    main_window.mainloop()
