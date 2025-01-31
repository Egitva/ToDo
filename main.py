import tkinter as tk
class TaskManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ToDo Manager")
        self.geometry(400x400)
        self.tasks = []
        self.task_label = ()
        self.task_entry = ()
        self.task_button = ()
        self.task_Listbox =tk.Listbox(self, height=10)
        self.delete_button =tk.Button(self, text="", command=self.delete_task)