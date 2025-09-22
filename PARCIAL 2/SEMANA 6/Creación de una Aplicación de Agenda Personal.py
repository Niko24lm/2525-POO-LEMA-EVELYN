# Importación de módulos necesarios
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime  # Para validaciones básicas de fecha y hora (opcional)


# Clase principal de la aplicación de Agenda Personal
class AgendaPersonal:
    def __init__(self, root):
        # Configuración de la ventana principal
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x500")

        # Lista para almacenar los eventos (en memoria)
        self.eventos = []
        self.evento_id = 0  # Contador para IDs únicos

        # Crear frames para organizar la interfaz
        self.crear_frames()

        # Inicializar la lista de eventos en el TreeView
        self.actualizar_lista()

    def crear_frames(self):
        # Frame superior para la visualización de eventos (TreeView)
        self.frame_lista = tk.Frame(self.root)
        self.frame_lista.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # TreeView para mostrar los eventos
        columnas = ("ID", "Fecha", "Hora", "Descripción")
        self.tree = ttk.Treeview(self.frame_lista, columns=columnas, show="headings", height=10)

        # Configurar encabezados de columnas
        self.tree.heading("ID", text="ID")
        self.tree.heading("Fecha", text="Fecha (YYYY-MM-DD)")
        self.tree.heading("Hora", text="Hora (HH:MM)")
        self.tree.heading("Descripción", text="Descripción")

        # Configurar anchos de columnas
        self.tree.column("ID", width=50)
        self.tree.column("Fecha", width=120)
        self.tree.column("Hora", width=80)
        self.tree.column("Descripción", width=250)

        # Scrollbar para el TreeView
        scrollbar = ttk.Scrollbar(self.frame_lista, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Empaquetar TreeView y scrollbar
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Frame medio para entrada de datos
        self.frame_entrada = tk.Frame(self.root)
        self.frame_entrada.pack(pady=10, padx=10, fill=tk.X)

        # Labels y Entries para los campos de entrada
        # Nota: Para el DatePicker, usamos un Entry simple con formato sugerido.
        # Un método alternativo sería usar la librería tkcalendar (instalar con pip install tkcalendar),
        # pero para simplicidad sin dependencias externas, validamos el formato en la función agregar.

        tk.Label(self.frame_entrada, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_fecha = tk.Entry(self.frame_entrada, width=15)
        self.entry_fecha.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_entrada, text="Hora (HH:MM):").grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)
        self.entry_hora = tk.Entry(self.frame_entrada, width=10)
        self.entry_hora.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(self.frame_entrada, text="Descripción:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_descripcion = tk.Entry(self.frame_entrada, width=50)
        self.entry_descripcion.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky=tk.W + tk.E)

        # Frame inferior para botones de acciones
        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack(pady=10, padx=10)

        # Botones
        self.btn_agregar = tk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.pack(side=tk.LEFT, padx=5)

        self.btn_eliminar = tk.Button(self.frame_botones, text="Eliminar Evento Seleccionado",
                                      command=self.eliminar_evento)
        self.btn_eliminar.pack(side=tk.LEFT, padx=5)

        self.btn_salir = tk.Button(self.frame_botones, text="Salir", command=self.salir)
        self.btn_salir.pack(side=tk.LEFT, padx=5)

    def agregar_evento(self):
        # Obtener valores de los campos de entrada
        fecha = self.entry_fecha.get().strip()
        hora = self.entry_hora.get().strip()
        descripcion = self.entry_descripcion.get().strip()

        # Validación básica: campos no vacíos y formatos aproximados
        if not fecha or not hora or not descripcion:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        # Validación simple de formato de fecha (YYYY-MM-DD) y hora (HH:MM)
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Error", "Formato inválido. Usa YYYY-MM-DD para fecha y HH:MM para hora.")
            return

        # Crear nuevo evento
        self.evento_id += 1
        evento = (self.evento_id, fecha, hora, descripcion)
        self.eventos.append(evento)

        # Limpiar campos
        self.entry_fecha.delete(0, tk.END)
        self.entry_hora.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)

        # Actualizar la lista visual
        self.actualizar_lista()

        messagebox.showinfo("Éxito", "Evento agregado correctamente.")

    def eliminar_evento(self):
        # Obtener selección del TreeView
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar.")
            return

        # Diálogo de confirmación (opcional, pero implementado)
        if messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres eliminar el evento seleccionado?"):
            # Obtener el ID del evento seleccionado
            item = self.tree.item(seleccion)
            evento_id = int(item['values'][0])

            # Remover de la lista de eventos
            self.eventos = [e for e in self.eventos if e[0] != evento_id]

            # Actualizar la lista visual
            self.actualizar_lista()

            messagebox.showinfo("Éxito", "Evento eliminado correctamente.")

    def actualizar_lista(self):
        # Limpiar TreeView
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar eventos en el TreeView
        for evento in self.eventos:
            self.tree.insert("", tk.END, values=evento)

    def salir(self):
        # Confirmar salida (opcional)
        if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?"):
            self.root.quit()


# Función principal para ejecutar la aplicación
def main():
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()


# Pruebas realizadas:
# - Agregar eventos: Ingresé datos válidos e inválidos; valida formatos y muestra mensajes.
# - Eliminar eventos: Seleccioné items, confirmó eliminación y actualizó la lista.
# - Visualización: TreeView muestra correctamente los eventos con scroll.
# - Salida: Cierra la aplicación tras confirmación.
# - Interfaz: Frames organizan bien los componentes; responsive en ventana de 600x500.
# No se detectaron errores en pruebas básicas.

if __name__ == "__main__":
    main()