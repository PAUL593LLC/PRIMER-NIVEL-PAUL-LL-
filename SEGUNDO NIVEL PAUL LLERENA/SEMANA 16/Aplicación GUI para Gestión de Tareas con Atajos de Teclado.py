import tkinter as tk
from tkinter import messagebox, Listbox, END


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Botones
        self.add_task_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.complete_task_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        # Lista para mostrar tareas
        self.task_list = Listbox(root, width=50)
        self.task_list.pack(pady=10)

        # Atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<c>', lambda event: self.complete_task())
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('<Escape>', lambda event: root.quit())

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.insert(END, task)
            self.task_entry.delete(0, END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese una tarea.")

    def complete_task(self):
        try:
            selected_task_index = self.task_list.curselection()[0]
            completed_task = self.task_list.get(selected_task_index)
            self.task_list.delete(selected_task_index)
            completed_task += " (Completada)"
            self.task_list.insert(END, completed_task)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor seleccione una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_task_index = self.task_list.curselection()[0]
            self.task_list.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor seleccione una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()