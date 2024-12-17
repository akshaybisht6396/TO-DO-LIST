import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x500")

        # Title Label
        tk.Label(self.root, text="To-Do List", font=("Arial", 24), pady=10).pack()

        # Entry widget for adding tasks
        self.task_entry = tk.Entry(self.root, font=("Arial", 16), width=30)
        self.task_entry.pack(pady=10)

        # Button to add tasks
        tk.Button(
            self.root, text="Add Task", font=("Arial", 14), command=self.add_task
        ).pack(pady=5)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(
            self.root, font=("Arial", 14), width=35, height=15, selectmode=tk.SINGLE
        )
        self.task_listbox.pack(pady=10)

        # Buttons to delete and clear tasks
        tk.Button(
            self.root, text="Delete Task", font=("Arial", 14), command=self.delete_task
        ).pack(pady=5)
        tk.Button(
            self.root, text="Clear All", font=("Arial", 14), command=self.clear_all
        ).pack(pady=5)

    def add_task(self):
        """Adds a task to the listbox."""
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        """Deletes the selected task from the listbox."""
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Warning", "No task selected to delete!")

    def clear_all(self):
        """Clears all tasks from the listbox."""
        if self.task_listbox.size() > 0:
            confirm = messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?")
            if confirm:
                self.task_listbox.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "No tasks to clear!")

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
