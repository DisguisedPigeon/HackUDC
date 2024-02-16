import tkinter as tk
from tkinter import filedialog

def abrir_seleccionador():
    archivo = filedialog.askopenfilename(filetypes=[("Facturas de luz", "*.csv"), ("Todos los archivos", "*.*")])

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Ana Rosa Quintana")
ventana.geometry("600x300")  # Tamaño de la ventana (ancho x alto)

# Color de fondo para la ventana
ventana.configure(bg="#f0f0f0")

# Título para la ventana
titulo = tk.Label(ventana, text="Seleccione su factura", font=("Helvetica", 32), bg="#f0f0f0")
titulo.pack(pady=20)

# Etiqueta para mostrar el archivo seleccionado
etiqueta = tk.Label(ventana, text="", font=("Helvetica", 24), bg="#f0f0f0")
etiqueta.pack(pady=10)

# Botón para abrir el seleccionador de archivos
boton = tk.Button(ventana, text="Seleccionar Archivo", command=abrir_seleccionador, width=40, height=5)
boton.pack(pady=1)

ventana.mainloop()

