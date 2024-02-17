import tkinter as tk
from tkinter import filedialog

def abrir_archivo():
    # Abrir el cuadro de diálogo de selección de archivo
    archivo = filedialog.askopenfilename()
    
    # Verificar si se seleccionó un archivo
    if archivo:
        # Si se seleccionó un archivo, intenta abrirlo
        try:
            with open(archivo, 'r') as f:
                contenido = f.read()
                # Aquí puedes hacer lo que desees con el contenido del archivo
                print("Contenido del archivo:")
                print(contenido)
        except Exception as e:
            # Manejo de errores si no se puede abrir el archivo
            print("Error al abrir el archivo:", e)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Seleccionar Archivo")

# Botón para abrir el seleccionador de archivos
boton = tk.Button(ventana, text="Seleccionar Archivo", command=abrir_archivo, width=40, height=5)
boton.pack(pady=1)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
