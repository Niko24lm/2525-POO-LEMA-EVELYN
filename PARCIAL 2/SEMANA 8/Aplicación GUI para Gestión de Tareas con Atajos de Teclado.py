import tkinter as tk
from tkinter import messagebox


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x500")

        # Lista de tareas (usaremos un Listbox para mostrarlas)
        self.task_listbox = tk.Listbox(root, height=15, width=50)
        self.task_listbox.pack(pady=10)

        # Campo de entrada para nuevas tareas
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=5)
        self.entry.bind('<Return>', lambda event: self.add_task())

        # Frame para botones
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        # Botones
        add_button = tk.Button(button_frame, text="Añadir Tarea", command=self.add_task)
        add_button.pack(side=tk.LEFT, padx=5)

        complete_button = tk.Button(button_frame, text="Marcar Completada", command=self.complete_task)
        complete_button.pack(side=tk.LEFT, padx=5)

        delete_button = tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task)
        delete_button.pack(side=tk.LEFT, padx=5)

        # Atajos de teclado
        self.root.bind('<c>', lambda event: self.complete_task())
        self.root.bind('<C>', lambda event: self.complete_task())  # Para mayúscula también
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('<d>', lambda event: self.delete_task())
        self.root.bind('<D>', lambda event: self.delete_task())
        self.root.bind('<Escape>', lambda event: self.root.quit())

        # Enfocar el entry al inicio
        self.entry.focus()

    def add_task(self):
        task_text = self.entry.get().strip()
        if task_text:
            # Añadir con prefijo "[ ]" para pendiente
            display_text = f"[ ] {task_text}"
            self.task_listbox.insert(tk.END, display_text)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

    def complete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            current_text = self.task_listbox.get(index)
            if current_text.startswith("[ ]"):
                # Cambiar a "[X]" para completada
                new_text = current_text.replace("[ ]", "[X]")
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, new_text)
            else:
                messagebox.showinfo("Info", "La tarea ya está marcada como completada.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

    def delete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            self.task_listbox.delete(index)
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()