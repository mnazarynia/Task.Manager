import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

# Task Manager Class
class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.tasks = []

        # GUI Elements
        self.task_label = tk.Label(root, text="Enter Task:")
        self.task_label.pack()

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack()

        # Date Selection
        self.date_label = tk.Label(root, text="Due Date (YYYY-MM-DD):")
        self.date_label.pack()

        self.date_entry = tk.Entry(root, width=40)
        self.date_entry.pack()

        # Time Selection
        self.time_label = tk.Label(root, text="Due Time (HH:MM):")
        self.time_label.pack()

        self.time_entry = tk.Entry(root, width=40)
        self.time_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, height=10, width=60)
        self.task_listbox.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.clear_button = tk.Button(root, text="Clear All Tasks", command=self.clear_tasks)
        self.clear_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        due_date = self.date_entry.get()
        due_time = self.time_entry.get()

        if task and due_date and due_time:
            try:
                # Validate date and time
                due_datetime = datetime.strptime(f"{due_date} {due_time}", "%Y-%m-%d %H:%M")
                reminder_time = due_datetime - timedelta(hours=3)

                task_info = f"{task} (Due: {due_datetime.strftime('%Y-%m-%d %H:%M')})"
                self.tasks.append((task_info, due_datetime))

                # Schedule reminder
                time_until_reminder = (reminder_time - datetime.now()).total_seconds() * 1000
                if time_until_reminder > 0:
                    self.root.after(int(time_until_reminder), self.remind, task_info)

                self.task_listbox.insert(tk.END, task_info)
                self.task_entry.delete(0, tk.END)
                self.date_entry.delete(0, tk.END)
                self.time_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showwarning("Input Error", "Invalid date or time format!")
        else:
            messagebox.showwarning("Input Error", "All fields must be filled!")

    def remind(self, task_info):
        messagebox.showinfo("Reminder", f"Reminder: {task_info} is due soon!")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index]
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def clear_tasks(self):
        self.task_listbox.delete(0, tk.END)
        self.tasks.clear()

# Main window setup
if __name__ == "__main__":
    root = tk.Tk()
    task_manager = TaskManager(root)
    root.mainloop()


# In[ ]:




