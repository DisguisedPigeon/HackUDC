import tkinter as tk
from tkinter import filedialog
from parser_1 import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graficar():
    # Crear una figura de Matplotlib
    figura = Figure(figsize=(5, 4), dpi=100)
    # Agregar un subplot
    subplot = figura.add_subplot(111)
    # Graficar algo (aquí un ejemplo de una línea)
    subplot.plot([1, 2, 3, 4], [1, 4, 9, 16])

    # Crear un lienzo de Matplotlib para Tkinter
    lienzo = FigureCanvasTkAgg(figura, master=ventana)
    lienzo.draw()
    lienzo.get_tk_widget().pack()

def abrir_seleccionador():
    archivo = filedialog.askopenfilename(filetypes=[("Facturas de luz", "*.csv"), ("Todos los archivos", "*.*")])
    
    # Verificar si se seleccionó un archivo
    if archivo:
        # Si se seleccionó un archivo, intenta abrirlo
        try:
            with open(archivo, 'r') as f:
                contenido = print_data(archivo)
                #contenido = f.read()
                # Aquí puedes hacer lo que desees con el contenido del archivo
                print("Contenido del archivo:")
                # Limpiar el widget de texto
                texto.delete('1.0', tk.END)
                # Insertar el contenido del archivo en el widget de texto
                texto.insert(tk.END, contenido)
                #print(contenido)
        except Exception as e:
            # Manejo de errores si no se puede abrir el archivo
            print("Error al abrir el archivo:", e)
    

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

# Widget de texto para mostrar el contenido del archivo
texto = tk.Text(ventana, width=120, height=80)
texto.pack()

ventana.mainloop()

