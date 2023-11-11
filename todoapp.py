import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.style = Style(theme="superhero")  # Use the superhero theme

        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        # Task Entry
        self.task_entry = ttk.Entry(self.root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W+tk.E)

        # Add Task Button
        self.add_task_button = ttk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=1, column=0, pady=5, padx=10, sticky=tk.W)

        # Task Listbox
        self.task_listbox = tk.Listbox(self.root, width=40, height=10, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W+tk.E)

        # Mark as Completed Button
        self.mark_completed_button = ttk.Button(self.root, text="Mark as Completed", command=self.mark_completed)
        self.mark_completed_button.grid(row=3, column=0, pady=5, padx=10, sticky=tk.W)

        # Remove Task Button
        self.remove_task_button = ttk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_task_button.grid(row=3, column=1, pady=5, padx=10, sticky=tk.W)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()

    def mark_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            if selected_task_index < len(self.tasks):
                self.tasks[selected_task_index] = f"[Completed] {self.tasks[selected_task_index]}"
                self.update_task_list()

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            if selected_task_index < len(self.tasks):
                del self.tasks[selected_task_index]
                self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
        self.task_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
