import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import json
import os

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []

        self.setup_ui()
        self.load_tasks()

    def setup_ui(self):
        # Entry for adding tasks
        self.entry = tk.Entry(self.root, width=50, font=('Arial', 14))
        self.entry.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        tk.Button(button_frame, text="Add Task", width=15, command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Edit Task", width=15, command=self.edit_task).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Delete Task", width=15, command=self.delete_task).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Mark as Done", width=15, command=self.mark_done).grid(row=0, column=3, padx=5)
        tk.Button(button_frame, text="Save Tasks", width=15, command=self.save_tasks).grid(row=0, column=4, padx=5)

        # Listbox for tasks
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=80, height=15, font=('Courier New', 12))
        self.task_listbox.pack(pady=10)

        # Scrollbar
        scrollbar = tk.Scrollbar(self.root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.tasks.append({'task': task, 'done': False})
            self.update_task_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def edit_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            current_task = self.tasks[index]['task']
            new_task = simpledialog.askstring("Edit Task", "Modify task:", initialvalue=current_task)
            if new_task:
                self.tasks[index]['task'] = new_task
                self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to edit.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            confirm = messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?")
            if confirm:
                del self.tasks[index]
                self.update_task_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def mark_done(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks[index]['done'] = not self.tasks[index]['done']
            self.update
