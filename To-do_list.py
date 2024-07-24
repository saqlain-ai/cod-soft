import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if not task:
        messagebox.showwarning("Warning", "Please enter a task.")
        return
    task_listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)
    update_task_count()

def remove_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")
    update_task_count()

def clear_tasks():
    task_listbox.delete(0, tk.END)
    update_task_count()

def update_task():
    try:
        selected_index = task_listbox.curselection()[0]
        new_task = task_entry.get()
        if not new_task:
            messagebox.showwarning("Warning", "Please enter a task.")
            return
        task_listbox.delete(selected_index)
        task_listbox.insert(selected_index, new_task)
        task_entry.delete(0, tk.END)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

def search_task():
    search_term = search_entry.get().lower()
    if not search_term:
        messagebox.showwarning("Warning", "Please enter a search term.")
        return
    
    found_indices = []
    for index in range(task_listbox.size()):
        task = task_listbox.get(index).lower()
        if search_term in task:
            found_indices.append(index)
    
    if found_indices:
        task_listbox.selection_clear(0, tk.END)
        for index in found_indices:
            task_listbox.selection_set(index)
        task_listbox.activate(found_indices[0])
    else:
        messagebox.showinfo("Search Result", "No matching tasks found.")

def update_task_count():
    task_count_label.config(text=f"Total Tasks: {task_listbox.size()}")

def on_enter(event):
    event.widget.config(bg=event.widget.cget("activebackground"), fg=event.widget.cget("activeforeground"))

def on_leave(event):
    event.widget.config(bg=event.widget.cget("background"), fg=event.widget.cget("foreground"))

window = tk.Tk()
window.title("To-Do List")
window.geometry('500x500')
window.configure(bg='#121212')  

frame = tk.Frame(window, bg='#121212')
frame.pack(fill='both', expand=True)

font_large = ("Roboto", 16, "bold")  
font_medium = ("Roboto", 14, "bold")

search_label = tk.Label(frame, text="Search Task", bg='#121212', font=font_large, fg="#1E90FF")
search_entry = tk.Entry(frame, font=font_large, bg="#333333", fg="#FFFFFF", highlightthickness=1, highlightcolor="#1E90FF")
search_button = tk.Button(frame, text="Search", bg="#1E90FF", fg="#FFFFFF", font=font_large, command=search_task, activebackground="#0a74da", activeforeground="#FFFFFF", relief="flat", borderwidth=0)
search_button.bind("<Enter>", on_enter)
search_button.bind("<Leave>", on_leave)

task_label = tk.Label(frame, text="New Task", bg='#121212', font=font_large, fg="#32CD32")
task_entry = tk.Entry(frame, font=font_large, bg="#333333", fg="#FFFFFF", highlightthickness=1, highlightcolor="#32CD32")
add_task_button = tk.Button(frame, text="Add Task", bg="#32CD32", fg="#FFFFFF", font=font_large, command=add_task, activebackground="#228b22", activeforeground="#FFFFFF", relief="flat", borderwidth=0)
add_task_button.bind("<Enter>", on_enter)
add_task_button.bind("<Leave>", on_leave)

remove_task_button = tk.Button(frame, text="Remove Task", bg="#FF4500", fg="#FFFFFF", font=font_large, command=remove_task, activebackground="#e03b2c", activeforeground="#FFFFFF", relief="flat", borderwidth=0)
remove_task_button.bind("<Enter>", on_enter)
remove_task_button.bind("<Leave>", on_leave)

clear_tasks_button = tk.Button(frame, text="Clear Tasks", bg="#FFD700", fg="#000000", font=font_large, command=clear_tasks, activebackground="#ffbf00", activeforeground="#000000", relief="flat", borderwidth=0)
clear_tasks_button.bind("<Enter>", on_enter)
clear_tasks_button.bind("<Leave>", on_leave)

update_task_button = tk.Button(frame, text="Update Task", bg="#1E90FF", fg="#FFFFFF", font=font_large, command=update_task, activebackground="#0a74da", activeforeground="#FFFFFF", relief="flat", borderwidth=0)
update_task_button.bind("<Enter>", on_enter)
update_task_button.bind("<Leave>", on_leave)

task_listbox = tk.Listbox(frame, font=font_medium, width=50, height=15, bg='#333333', fg='#FFFFFF', selectmode=tk.SINGLE, highlightthickness=1, highlightcolor="#1E90FF")

task_count_label = tk.Label(frame, text="Total Tasks: 0", bg='#121212', font=font_medium, fg="#FFFFFF")

search_label.grid(row=0, column=0, pady=10, padx=10, sticky='w')
search_entry.grid(row=0, column=1, pady=5, padx=10, sticky='ew')
search_button.grid(row=0, column=2, pady=10, padx=10, sticky='ew')

task_listbox.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

task_label.grid(row=2, column=0, pady=10, padx=10, sticky='w')
task_entry.grid(row=2, column=1, pady=5, padx=10, sticky='ew')
add_task_button.grid(row=3, column=0, pady=10, columnspan=3, sticky='ew')
remove_task_button.grid(row=4, column=0, pady=10, columnspan=3, sticky='ew')
clear_tasks_button.grid(row=5, column=0, pady=10, columnspan=3, sticky='ew')
update_task_button.grid(row=6, column=0, pady=10, columnspan=3, sticky='ew')

task_count_label.grid(row=7, column=0, columnspan=3, pady=10, padx=10)

frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.rowconfigure(1, weight=1)

window.mainloop()
