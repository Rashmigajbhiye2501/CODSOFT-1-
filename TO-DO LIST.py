import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

def add_task():
    task = entry.get()
    if task:
        task_frame = ttk.Frame(listbox, relief="solid", borderwidth=1)
        task_frame.pack(fill=tk.X, pady=2)

        task_label = tk.Label(task_frame, text=task, width=30, anchor="w")
        task_label.pack(side=tk.LEFT)

        delete_button = tk.Button(task_frame, text="Delete", command=lambda frame=task_frame: delete_task(frame), bg="red")
        delete_button.pack(side=tk.LEFT, padx=5)

        edit_button = tk.Button(task_frame, text="Edit", command=lambda frame=task_frame, text=task: edit_task(frame, text), bg="green")
        edit_button.pack(side=tk.LEFT, padx=5)

        entry.delete(0, tk.END)

    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task(frame):
    frame.destroy()

def edit_task(frame, original_text):
    new_text = simpledialog.askstring("Edit Task", "Edit task:", initialvalue=original_text)
    if new_text is not None:
        frame.winfo_children()[0].config(text=new_text)

def clear_tasks():
    for widget in listbox.winfo_children():
        widget.destroy()

# Create the main window
root = tk.Tk()
root.title("ToDo List")

# Create and pack widgets
title_frame = tk.Frame(root, bg='green', padx=10, pady=10)
title_frame.pack(side=tk.TOP, fill=tk.X)

title_label = tk.Label(title_frame, text="ToDo List", font=("Arial", 17, "bold"), fg="black", bg='green')
title_label.pack(side=tk.LEFT)

frame = tk.Frame(root)
frame.pack(pady=10)

label = tk.Label(frame, text="Enter Task:", font=("Arial", 12, "bold"))
label.grid(row=0, column=0, padx=5)

entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=1, padx=5)

add_button = tk.Button(frame, text="Submit", command=add_task, bg="black", fg="white")
add_button.grid(row=0, column=2, padx=5)

tasks_title_label = tk.Label(root, text="Tasks:", font=("Arial", 12, "bold"))
tasks_title_label.pack(side=tk.TOP, padx=10)

listbox = tk.Frame(root)
listbox.pack(pady=10)

delete_button = tk.Button(root, text="Clear All", command=clear_tasks, bg="navy blue", fg="white")
delete_button.pack(pady=5)

# Start the main event loop
root.mainloop()
