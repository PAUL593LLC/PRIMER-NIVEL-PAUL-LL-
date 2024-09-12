import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
# Tamaño de mi pantalla
root.geometry("300x600")
root.configure(background="blue")

class ApplicationGUI:
    def __init__(self, master):
        self.master = master
        master.title("Aplicación GUI Básica Semana 13")

        # Crear celda de ingreso de información
        self.label = tk.Label(master, text="Ingrese información")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        # Creamos un  botón de agregar
        self.add_button = tk.Button(master, text="Agregar", command=self.add_info)
        self.add_button.pack()
        self.add_button.config(font=("Comic sans", 16, "bold"), bg="dark grey", fg="yellow")

        # Creamos un  botón de limpiar
        self.clear_button = tk.Button(master, text="Limpiar", command=self.clear_info)
        self.clear_button.pack()
        self.clear_button.config(font=("Comic sans", 16, "bold"), bg="dark grey", fg="yellow")

        self.listbox = tk.Listbox(master)
        self.listbox.pack()

    def add_info(self):
        info = self.entry.get()
        self.listbox.insert(tk.END, info)
        self.entry.delete(0, tk.END)

    def clear_info(self):
        self.listbox.delete(0, tk.END)
        self.entry.delete(0, tk.END)

app = ApplicationGUI(root)
root.mainloop()