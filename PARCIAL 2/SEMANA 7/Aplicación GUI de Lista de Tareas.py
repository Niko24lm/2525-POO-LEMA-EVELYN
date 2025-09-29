import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x500")

        # Lista interna de tareas: cada tarea es un diccionario {'text': str, 'completed': bool}
        self.tasks = []

        # Campo de entrada
        self.entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda event: self.add_task())

        # Botón Añadir
        add_btn = tk.Button(root, text="Añadir Tarea", command=self.add_task, bg="lightgreen")
        add_btn.pack(pady=5)

        # Listbox para mostrar tareas
        self.listbox = tk.Listbox(root, font=("Arial", 10), height=20, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        self.listbox.bind("<Double-1>", lambda event: self.toggle_complete())

        # Botones para completar y eliminar
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        complete_btn = tk.Button(btn_frame, text="Marcar como Completada", command=self.toggle_complete, bg="lightblue")
        complete_btn.pack(side=tk.LEFT, padx=5)

        delete_btn = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task, bg="lightcoral")
        delete_btn.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text:
            self.tasks.append({'text': task_text, 'completed': False})
            self.update_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            prefix = "[X] " if task['completed'] else "[ ] "
            self.listbox.insert(tk.END, prefix + task['text'])

    def toggle_complete(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self.tasks[index]['completed'] = not self.tasks[index]['completed']
            self.update_listbox()
            # Deseleccionar después de la acción
            self.listbox.selection_clear(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcarla.")

    def delete_task(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            del self.tasks[index]
            self.update_listbox()
            # Deseleccionar después de la acción
            self.listbox.selection_clear(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminarla.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()