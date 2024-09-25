import tkinter as tk
from tkinter import font as tkFont

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("APLICACIÓN DE LISTAS DE TAREAS PENDIENTES")

        # Establecer el tamaño de la ventana
        self.root.geometry("600x400")

        # Cambiar el color de fondo de la ventana
        self.root.configure(bg="Blue")  # Puedes cambiar el color a tu preferencia

        self.tasks = []

        # Definir la fuente en negrilla
        bold_font = tkFont.Font(weight="bold")

        # Crear los componentes de la interfaz gráfica de usuario
        self.entry_field = tk.Entry(root, width=40, font=bold_font)
        self.entry_field.pack(fill="x", padx=10, pady=10)

        self.add_button = tk.Button(root, text="AÑADIR TAREA", command=self.add_task, bg="Black", fg="white",
                                    font=bold_font)
        self.add_button.pack(fill="x", padx=10, pady=5)

        self.mark_button = tk.Button(root, text="MARCAR COMO COMPLETADA", command=self.mark_task, state=tk.DISABLED,
                                     bg="white", fg="black", font=bold_font)
        self.mark_button.pack(fill="x", padx=10, pady=5)

        self.delete_button = tk.Button(root, text="ELIMINAR TAREA", command=self.delete_task, state=tk.DISABLED,
                                       bg="yellow", fg="black", font=bold_font)
        self.delete_button.pack(fill="x", padx=10, pady=5)

        self.task_list = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10, font=bold_font)
        self.task_list.pack(fill="both", expand=True, padx=10, pady=10)

        # Bind events
        self.entry_field.bind("<Return>", self.add_task)
        self.task_list.bind("<<ListboxSelect>>", self.update_buttons)

    def add_task(self, event=None):
        task = self.entry_field.get().strip()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.entry_field.delete(0, tk.END)

    def mark_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            index = selected_task[0]
            task = self.tasks[index]
            # Verificar si la tarea ya está marcada
            if not task.startswith("[X] "):
                self.tasks[index] = f"[X] {task}"
                self.task_list.delete(index)
                self.task_list.insert(index, self.tasks[index])

    def delete_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            index = selected_task[0]
            self.tasks.pop(index)
            self.task_list.delete(index)

    def update_buttons(self, event=None):
        # Habilitar o deshabilitar los botones en función de la selección de la tarea
        if self.task_list.curselection():
            self.mark_button.config(state=tk.NORMAL)
            self.delete_button.config(state=tk.NORMAL)
        else:
            self.mark_button.config(state=tk.DISABLED)
            self.delete_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
