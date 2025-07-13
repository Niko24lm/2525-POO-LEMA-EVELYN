"""
Autor: Nicole
Fecha: 13‑jul‑2025
Descripción:
    Ejemplo educativo de uso de constructores y destructores en Python.
    - La clase Logger abre un archivo y escribe eventos.
    - El constructor __init__ se encarga de configurar el recurso.
    - El destructor __del__ cierra el recurso si sigue abierto.
    - Se añaden mensajes en consola para observar cuándo se disparan.
"""

from datetime import datetime
from pathlib import Path


class Logger:
    """
    Logger sencillo que escribe mensajes con marca de tiempo en un archivo.

    Uso:
        with Logger("log.txt") as log:
            log.write("Hola mundo")

        # o sin context manager (NO recomendado, pero sirve para ver __del__):
        log = Logger("log.txt")
        log.write("Algo")
        del log  # fuerza la llamada a __del__ si no hay más referencias
    """

    def __init__(self, filename: str):
        """
        Constructor: abre (o crea) el archivo y deja listo el manejador.

        :param filename: ruta del archivo de log
        """
        self.file_path: Path = Path(filename).expanduser().resolve()
        self._fh = open(self.file_path, mode="a", encoding="utf‑8")
        print(f"[__init__] Archivo abierto: {self.file_path}")

    def write(self, message: str) -> None:
        """Escribe un mensaje con fecha y hora."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._fh.write(f"{timestamp} | {message}\n")
        self._fh.flush()  # aseguramos escritura inmediata

    # --- soporte para "with" -------------------------------------------------

    def __enter__(self):
        """Devuelve el propio objeto para usarlo en un bloque with."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Se llama al salir del with; cerramos el archivo."""
        self.close()

    # --- limpieza explícita y destructor ------------------------------------

    def close(self):
        """Cierra el archivo de forma explícita (buena práctica)."""
        if not self._fh.closed:
            self._fh.close()
            print(f"[close] Archivo cerrado: {self.file_path}")

    def __del__(self):
        """
        Destructor: se invoca cuando el objeto se elimina / GC recupera memoria.
        No confíes ciegamente en él: puede tardar en ejecutarse.
        """
        if hasattr(self, "_fh") and not self._fh.closed:
            self._fh.close()
            print(f"[__del__] Archivo cerrado automáticamente: {self.file_path}")


# -------------------------- Prueba de funcionamiento ------------------------

def main():
    # Ejemplo con contexto (recomendado)
    with Logger("demo_log.txt") as log:
        log.write("Primer mensaje con contexto.")

    # Ejemplo sin contexto, para ver explícitamente __del__
    log2 = Logger("demo_log_2.txt")
    log2.write("Mensaje sin with.")
    # No llamamos a close() a propósito
    # Cuando log2 quede sin referencias, __del__ cerrará el archivo


if __name__ == "__main__":
    main()
