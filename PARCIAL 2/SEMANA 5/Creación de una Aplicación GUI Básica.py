import tkinter as tk
from tkinter import messagebox

class AplicacionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Información Básico")

        # --- Diseño de la interfaz ---

        # Etiqueta instructiva
        self.label = tk.Label(root, text="Ingrese información:")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Campo de texto para ingresar datos
        self.entry = tk.Entry(root, width=40)
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        # Botón para agregar la información ingresada a la lista
        self.btn_agregar = tk.Button(root, text="Agregar", command=self.agregar_info)
        self.btn_agregar.grid(row=0, column=2, padx=10, pady=10)

        # Lista para mostrar la información agregada
        self.lista = tk.Listbox(root, width=60, height=10)
        self.lista.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Botón para limpiar la entrada o la selección en la lista
        self.btn_limpiar = tk.Button(root, text="Limpiar", command=self.limpiar)
        self.btn_limpiar.grid(row=2, column=1, pady=10)

    def agregar_info(self):
        """
        Función que se ejecuta al presionar el botón 'Agregar'.
        Toma el texto del campo de entrada y lo agrega a la lista si no está vacío.
        """
        texto = self.entry.get().strip()
        if texto:
            self.lista.insert(tk.END, texto)
            self.entry.delete(0, tk.END)  # Limpiar campo de texto después de agregar
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, ingrese algún texto antes de agregar.")

    def limpiar(self):
        """
        Función que se ejecuta al presionar el botón 'Limpiar'.
        Si hay un elemento seleccionado en la lista, lo elimina.
        Si no hay selección, limpia el campo de texto.
        """
        seleccion = self.lista.curselection()
        if seleccion:
            # Eliminar el elemento seleccionado
            for index in reversed(seleccion):  # Reversed para evitar problemas al eliminar múltiples
                self.lista.delete(index)
        else:
            # Si no hay selección, limpiar el campo de texto
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()