import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, END

class TodoApp:
    """
    Aplicación GUI simple para gestionar una lista de tareas usando Tkinter.
    Permite añadir tareas, marcarlas como completadas (con cambio visual),
    eliminarlas y responder a eventos como Enter y doble clic.
    """

    def __init__(self, root):
        """
        Inicializa la aplicación.
        - Crea la ventana principal.
        - Configura los widgets: Entry para input, botones y Listbox para tareas.
        - Inicializa la lista de tareas en memoria.
        """
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x500")

        # Lista en memoria para almacenar tareas: cada tarea es un dict {'text': str, 'completed': bool}
        self.tasks = []

        # Campo de entrada para nuevas tareas
        self.entry = tk.Entry(root, width=40, font=('Arial', 12))
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', lambda event: self.add_task())  # Evento Enter para añadir tarea
        self.entry.focus()  # Enfocar el Entry al inicio

        # Frame para botones
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        # Botón Añadir Tarea
        add_btn = tk.Button(button_frame, text="Añadir Tarea", command=self.add_task, bg='lightgreen')
        add_btn.pack(side=tk.LEFT, padx=5)

        # Botón Marcar como Completada (toggle)
        complete_btn = tk.Button(button_frame, text="Marcar Completada", command=self.toggle_complete, bg='lightblue')
        complete_btn.pack(side=tk.LEFT, padx=5)

        # Botón Eliminar Tarea
        delete_btn = tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task, bg='lightcoral')
        delete_btn.pack(side=tk.LEFT, padx=5)

        # Listbox para mostrar tareas con scrollbar
        list_frame = tk.Frame(root)
        list_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        scrollbar = Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = Listbox(list_frame, width=50, height=20, font=('Arial', 11), yscrollcommand=scrollbar.set)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)

        # Evento opcional: Doble clic en una tarea para togglear completada
        self.listbox.bind('<Double-Button-1>', lambda event: self.toggle_complete())

        # Mensaje inicial
        self.update_listbox()

    def add_task(self):
        """
        Añade una nueva tarea desde el Entry a la lista.
        - Obtiene el texto del Entry.
        - Si no está vacío, añade la tarea como no completada.
        - Limpia el Entry y actualiza la visualización.
        - Muestra error si está vacío.
        """
        task_text = self.entry.get().strip()
        if not task_text:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")
            return

        self.tasks.append({'text': task_text, 'completed': False})
        self.entry.delete(0, END)  # Limpiar Entry
        self.update_listbox()

    def toggle_complete(self):
        """
        Marca/Desmarca una tarea como completada.
        - Obtiene el índice seleccionado en el Listbox.
        - Si hay selección, toggles el estado 'completed' de la tarea.
        - Actualiza la visualización.
        - Maneja caso sin selección.
        """
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar.")
            return

        index = selection[0]
        self.tasks[index]['completed'] = not self.tasks[index]['completed']
        self.update_listbox()
        # Opcional: Mantener selección después del toggle
        self.listbox.selection_set(index)

    def delete_task(self):
        """
        Elimina la tarea seleccionada.
        - Obtiene el índice seleccionado.
        - Si hay selección, remueve la tarea de la lista.
        - Actualiza la visualización.
        - Maneja caso sin selección.
        """
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")
            return

        index = selection[0]
        del self.tasks[index]
        self.update_listbox()

    def update_listbox(self):
        """
        Actualiza el Listbox con las tareas actuales.
        - Limpia el Listbox.
        - Para cada tarea, muestra símbolo visual: ✓ para completada, □ para pendiente.
        - El texto se muestra con el símbolo al inicio.
        """
        self.listbox.delete(0, END)
        for task in self.tasks:
            symbol = "✓" if task['completed'] else "□"
            display_text = f"{symbol} {task['text']}"
            self.listbox.insert(END, display_text)


if __name__ == "__main__":
    # Crear y ejecutar la aplicación
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()