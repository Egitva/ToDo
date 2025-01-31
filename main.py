import tkinter as tk
class TaskManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ToDo Manager")
        self.geometry('400x400')
        self.tasks = []
        self.task_label = tk.Label(self, text="")
        self.task_entry = tk.Entry(self)
        self.task_button = tk.Button(self, text="", command=self.add_task)
        self.task_Listbox =tk.Listbox(self, height=10)
        self.delete_button =tk.Button(self, text="", command=self.delete_task)
        self.edit_button =tk.Button()
        self.mark_coplete_button =tk.Button()
    def delete_task(self):
        try:
            selected_task_index =