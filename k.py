import tkinter as tk
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

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gráfico de Matplotlib en Tkinter")

# Crear un botón para graficar
boton_graficar = tk.Button(ventana, text="Graficar", command=graficar)
boton_graficar.pack()

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
