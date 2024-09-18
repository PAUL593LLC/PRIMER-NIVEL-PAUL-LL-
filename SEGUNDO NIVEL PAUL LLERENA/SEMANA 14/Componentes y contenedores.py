import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class AgendaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MI AGENDA PERSONALIZADA")
        self.geometry("600x400")  # Tamaño de la ventana

        # Frame para la lista de eventos
        self.frame_eventos = ttk.Frame(self)
        self.frame_eventos.pack(fill="both", expand=True)

        # Treeview para mostrar los eventos
        self.tree = ttk.Treeview(self.frame_eventos, columns=("fecha", "hora", "descripcion"), show="headings")
        self.tree.heading("fecha", text="FECHA")
        self.tree.heading("hora", text="HORA")
        self.tree.heading("descripcion", text="DESCRIPCIÓN")
        self.tree.column("fecha", width=100)
        self.tree.column("hora", width=100)
        self.tree.column("descripcion", width=300)
        self.tree.pack(fill="both", expand=True)

        # Frame para los campos de entrada y botones
        self.frame_entrada = ttk.Frame(self)
        self.frame_entrada.pack(fill="x", pady=10)

        # Campos de entrada
        ttk.Label(self.frame_entrada, text="Fecha (dd/mm/aaaa):").grid(row=0, column=0, padx=5)
        self.entrada_fecha = ttk.Entry(self.frame_entrada)
        self.entrada_fecha.grid(row=0, column=1, padx=5)

        ttk.Label(self.frame_entrada, text="Hora (hh:mm):").grid(row=1, column=0, padx=5)
        self.entrada_hora = ttk.Entry(self.frame_entrada)
        self.entrada_hora.grid(row=1, column=1, padx=5)

        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5)
        self.entrada_descripcion = ttk.Entry(self.frame_entrada, width=50)
        self.entrada_descripcion.grid(row=2, column=1, padx=5)

        # Botones
        self.boton_agregar = ttk.Button(self.frame_entrada, text="Agregar Evento")
        self.boton_agregar.grid(row=3, column=0, columnspan=2, pady=5)
        self.boton_eliminar = ttk.Button(self.frame_entrada, text="Eliminar Evento")
        self.boton_eliminar.grid(row=4, column=0, columnspan=2, pady=5)

        # Asignar comandos a los botones
        self.boton_agregar.config(command=self.agregar_evento)
        self.boton_eliminar.config(command=self.eliminar_evento)

    def agregar_evento(self):
        # Obtener datos de los campos de entrada
        fecha = self.entrada_fecha.get()
        hora = self.entrada_hora.get()
        descripcion = self.entrada_descripcion.get()

        # Verificar que los campos no estén vacíos
        if fecha and hora and descripcion:
            # Agregar un nuevo evento al Treeview
            self.tree.insert("", "end", values=(fecha, hora, descripcion))

            # Limpiar campos de entrada
            self.entrada_fecha.delete(0, tk.END)
            self.entrada_hora.delete(0, tk.END)
            self.entrada_descripcion.delete(0, tk.END)
        else:
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")

    def eliminar_evento(self):
        # Obtener el evento seleccionado
        selected_item = self.tree.selection()

        if selected_item:
            # Mostrar un diálogo de confirmación
            confirm = messagebox.askyesno("Eliminar evento", "¿Está seguro de que desea eliminar este evento?")
            if confirm:
                # Eliminar el evento del Treeview
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Seleccionar evento", "Por favor, seleccione un evento para eliminar.")


# Crear una instancia de la aplicación y ejecutarla
app = AgendaApp()
app.mainloop()
