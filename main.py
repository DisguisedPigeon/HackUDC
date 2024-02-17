import tkinter as tk
from tkinter import filedialog
from parser import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import Calendar
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import api_data

fig = None
plot1 = None
canvas = None

def display_tabla_md(texto: tk.Text) -> None:
    archivo = filedialog.askopenfilename(filetypes=[("Facturas de luz", "*.csv"), ("Todos los archivos", "*.*")])
    # Verificar si se seleccionó un archivo
    if archivo:
        # Si se seleccionó un archivo, intenta abrirlo
        try:
            contenido = ret_md(archivo)
            # Limpiar el widget de texto
            texto.delete('1.0', tk.END)
            # Insertar el contenido del archivo en el widget de texto
            texto.insert(tk.END, contenido)
            #print(contenido)
        except Exception as e:
            # Manejo de errores si no se puede abrir el archivo
            print("Error al abrir el archivo:", e)

def display_otro(texto: tk.Text):
    texto.delete('1.0', tk.END)
    texto.insert(tk.END, "gulpon")


def abrir_seleccionador(widgets):
    display_tabla_md(widgets["tabla_md"])
    display_otro(widgets["otro"])
    

def plot_graph(pcb):

    global fig, plot1, canvas
       
    if canvas is not None:
        canvas.get_tk_widget().destroy()
    
    fig = Figure(figsize=(5, 5), dpi=100)
    plot1 = fig.add_subplot(111)

    # Agregar nombres a los ejes
    plot1.set_xlabel('Hora del Día')
    plot1.set_ylabel('Precio')

    # plotting the graph
    plot1.clear()
    plot1.bar(range(len(pcb)), pcb)
    
    canvas = FigureCanvasTkAgg(fig, master = frame_izquierda) 
    canvas.draw() 
    canvas.get_tk_widget().pack()


def get_power_graph(fecha):
    array_precios = np.zeros(24)

    data = api_data.get_power_kWh_by_hour(fecha)

    if data == None:
        print("Error al obtener los datos")
        return

    for i, key in enumerate(data):
        hora = key.hour
        pcb = data[key]

        array_precios[i] = pcb
        # respuesta = str(key.day) + "/" + str(key.month) + "/" + str(key.year) + " " + str(hora) + ":00" + ": " + str(pcb) + "\n"
    plot_graph(array_precios)


def grad_date():
    date.config(text = "El día: " + cal.get_date() + " el precio de la electricidad en kWh era el siguiente: ")
    get_power_graph(cal.get_date())

# Configuración de la ventana principal
    


ventana = tk.Tk()
ventana.title("Ana Rosa Quintana")
ventana.geometry("1800x1000")  # Tamaño de la ventana (ancho x alto)

# Crear un frame principal
frame_principal = tk.Frame(ventana)
frame_principal.pack(fill="both", expand=True)

# Crear un frame para el texto a la izquierda
frame_izquierda = tk.Frame(frame_principal, bg="lightblue", width=200)
frame_izquierda.pack(side="left", fill="y")


# Crear un frame para otro widget a la derecha
frame_derecha = tk.Frame(frame_principal, bg="lightgreen")
frame_derecha.pack(side="right", fill="both", expand=True)

# Color de fondo para la ventana
ventana.configure(bg="#f0f0f0")

frame_top_derecha = tk.Frame(frame_derecha, bg="lightgreen") 

# Título para la ventana
titulo = tk.Label(frame_top_derecha, text="Seleccione su factura", font=("Helvetica", 32), bg="#a9b1d9")
titulo.pack(pady=20)

# Etiqueta para mostrar el archivo seleccionado
#etiqueta = tk.Label(frame_top_derecha, text="Indica tu consumo de luz en kW y la hora", font=("Helvetica", 24), bg="#f0f0f0")
#etiqueta.pack(pady=10)



# Add Calendar
cal = Calendar(frame_izquierda, selectmode = 'day',
               year = 2024, month = 2,
               day = 16, date_pattern='y-mm-dd')

cal.pack(side= tk.TOP,pady = 20)

button_frame = tk.Frame(frame_izquierda)
button_frame.pack(side=tk.TOP)

# Add Buttons
button_get_data = tk.Button(frame_izquierda, text="Get Data", command=grad_date)
button_get_data.pack(in_=button_frame, side=tk.LEFT, pady=10)

button_get_graph = tk.Button(frame_izquierda, text="Get Graph", command=grad_date)
button_get_graph.pack(in_=button_frame, side=tk.LEFT, pady=10)
button_frame.pack(side=tk.TOP)

date = tk.Label(frame_izquierda, text = "")
date.pack(pady = 20)

# Widgets de display de data
widgets: dict[str, tk.Widget] = {}

# Botón para abrir el seleccionador de archivos
boton = tk.Button(frame_top_derecha, text="Seleccionar Archivo", command=lambda: abrir_seleccionador(widgets), width=40, height=5)
boton.pack(pady=1)

frame_top_derecha.pack()

frame_bot_derecha = tk.Frame(frame_derecha)

# Texto mostrando archivo
widgets["tabla_md"] = tk.Text(frame_bot_derecha, width=120, height=80)
widgets["otro"] = tk.Text(frame_bot_derecha, width=120, height=80)



for i, key in enumerate(widgets):
    if i%2 == 0:
        widgets[key].grid(row= i // 2, column=0)
    else:
        widgets[key].grid(row= i // 2, column=1)


frame_bot_derecha.pack(side="bottom", fill="both", expand=True)



def update():       # Para gestionar Ctrl-c
    ventana.after(50, update)
ventana.after(50, update)

ventana.mainloop()

