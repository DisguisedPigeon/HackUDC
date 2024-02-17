import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from parser import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import Calendar
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import api_data
import sys

TEST_DIRECTORY = "./resources/consumptions.csv"

fig = None
plot1 = None
canvas = None
canvasPie = None

scroll_y = None
frame = None
frame2 = None
table = None
widgets = {}

def ploti_pie(yiar, data: str = TEST_DIRECTORY):
    global canvasPie,frame2
    if frame2 is not None:
        frame2.destroy()
    if canvasPie is not None:
        canvasPie.get_tk_widget().destroy()
    if yiar == None:
        print("Usage: plotipie.py year")
        print("Exiting with code -1")
        sys.exit(-1)
    #Load data
    df = pd.read_csv(data, sep=";")
    #Create datetime column
    df['Fecha'] = df['Fecha'].apply(lambda x: pd.Timestamp(x))
    df['datetime'] = df['Fecha'].astype(str) + ' ' + df['Hora'].astype(str).replace("24", "00") + ':00:00'
    df['datetime'] = pd.to_datetime(df['datetime'])
    #Replace in consumo "," for "."
    df["Consumo_KWh"] = df['Consumo_KWh'].map(lambda x : float(x.replace(",", ".")))
    #Create column extracting the year
    df['year'] = pd.to_datetime(df['datetime']).dt.year
    #Create column 
    user_year = int(yiar)
    df['month'] = pd.to_datetime(df[df['year']==user_year]['datetime']).dt.month
    #All consume months of the user 
    months_year = df[df['year']==user_year]['month'].unique()
    months_dict = { 1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 
                   7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 
                   12: 'December'}
    #Keys array
    a1 = months_dict.keys()
    #Cast float array to int array
    a2 = months_year.astype(np.int32)
    #Extract same values from two arrays (only consume months)
    months_dict_filtered = np.intersect1d(list(a1),list(a2))
    #Consumes for month
    values = list(df['Consumo_KWh'].groupby(df['month']).sum())
    
    frame2 = tk.Frame(frame_derecha)
    frame2.pack(side="bottom", fill="both", expand=True)

    fig = Figure(figsize=(6.5, 5), dpi=100)
    plot2 = fig.add_subplot(111)

    # plotting the graph
    plot2.clear()
    plot2.pie(values, labels=[months_dict[key] for key in list(months_dict_filtered)], autopct=lambda p : '{:,.2f}'.format(p * sum(values)/100))
    plot2.set_title("Consumo total (KWh) en cada mes para el año: " + str(yiar))

    canvasPie = FigureCanvasTkAgg(fig, master = frame2) 
    canvasPie.draw() 
    canvasPie.get_tk_widget().pack_propagate(0)
    canvasPie.get_tk_widget().pack(fill= "both",expand=0)

def ploted(archivo):
    if widgets.get("ploti_pie", "Not Found") != "Not Found":
        widgets["ploti_pie"].destroy()
    inp = widgets["input_year"].get(1.0, "end-1c")
    ploti_pie(str(inp), archivo)

def display_tabla_md() -> None:
    archivo = filedialog.askopenfilename(filetypes=[("Facturas de luz", "*.csv"), ("Todos los archivos", "*.*")])
    # Verificar si se seleccionó un archivo
    if archivo:
        # Si se seleccionó un archivo, intenta abrirlo
        try:
            widgets["tabla_md"] = tk.Text(frame_bot_derecha, height=15)
            contenido = ret_md(archivo)
            # Limpiar el widget de texto
            widgets["tabla_md"].delete('1.0', tk.END)
            # Insertar el contenido del archivo en el widget de texto
            widgets["tabla_md"].insert(tk.END, contenido)
            #Seleccionar el año:
            widgets["input_label"] = tk.Label(frame_bot_derecha, text = "Selecciona el año")
            widgets["input_year"] = tk.Text(frame_bot_derecha, height=1)
            widgets["btn"] = tk.Button(frame_bot_derecha, 
                        text = "Search",  
                        command = lambda: ploted(archivo)) 
            #TODO: ponerle título a la gráfica
            for i, key in enumerate(widgets):
                widgets[key].grid(row= i, column=0)
            frame_bot_derecha.pack(side="bottom", fill="both", expand=True)

        except Exception as e:
            # Manejo de errores si no se puede abrir el archivo
            print("Error al abrir el archivo:", e)

def abrir_seleccionador():
    display_tabla_md()
    
def plot_graph(pcb):
    global fig, plot1, canvas

    if canvas is not None:
        canvas.get_tk_widget().destroy()
    
    fig = Figure(figsize=(6.5, 5), dpi=100)
    plot1 = fig.add_subplot(111)

    # Agregar nombres a los ejes
    plot1.set_xlabel('Hora del Día')
    plot1.set_ylabel('Precio')

    # plotting the graph
    x_values = range(24)

    # plotting the graph
    plot1.clear()
    plot1.bar(x_values, pcb)

    # Establecer las etiquetas del eje x para que muestren todos los valores de 0 a 23
    plot1.set_xticks(x_values)

    canvas = FigureCanvasTkAgg(fig, master = frame_izquierda) 
    canvas.draw() 
    canvas.get_tk_widget().pack()
def plot_data(data):   
    global table,scroll_y
    
    frame = tk.Frame(frame_izquierda)
    frame.pack(fill=tk.BOTH, expand=True)

    table = ttk.Treeview(frame, columns=("Hora", "PCB"), show="headings")
    table.heading("Hora", text="Hora")
    table.heading("PCB", text="PCB")

    for hora, pcb in data:
        table.insert("", "end", values=(hora, pcb))

    scroll_y = tk.Scrollbar(frame, orient="vertical", command=table.yview)
    table.configure(yscrollcommand=scroll_y.set)

    table.pack(side="left", fill="both", expand=True)
    scroll_y.pack(side="right", fill="y")
    
def get_power(fecha, graph):
    array_precios = np.zeros(24)

    data = api_data.get_power_kWh_by_hour(fecha)
    global frame,table,scroll_y,fig, plot1, canvas

    if frame is not None:
        frame.destroy()
    if table is not None:
        table.destroy()
    if scroll_y is not None: 
        scroll_y.destroy()
    if canvas is not None:
        canvas.get_tk_widget().destroy()

    data = api_data.get_power_kWh_by_hour(fecha)
    if data is None or data.empty:
        print("Error al obtener los datos")
        return

    hora = data['Hora']
    pcb = data['PCB']

    respuesta = []
    respuesta.append((hora,pcb))

    if graph:
        plot_graph(data["PCB"])
    else:
        plot_data(respuesta)

def grad_graph():
    date.config(text = "El día:  " + cal.get_date() + " el precio de la electricidad en kWh era el siguiente: ")
    get_power(cal.get_date(),True)
def grad_data():
    date.config(text = "El día:  " + cal.get_date() + " el precio de la electricidad en kWh era el siguiente: ")
    get_power(cal.get_date(),False)

# Configuración de la ventana principal
    


ventana = tk.Tk()
ventana.title("Ana Rosa Quintana")
ventana.geometry("1800x1000")

# Crear un frame principal
frame_principal = tk.Frame(ventana)
frame_principal.pack(fill="both", expand=True)

# Crear un frame para el texto a la izquierda
frame_izquierda = tk.Frame(frame_principal, bg="lightblue")#, width=200)
frame_izquierda.pack(side="left", fill="y")


# Crear un frame para otro widget a la derecha
frame_derecha = tk.Frame(frame_principal, bg="lightgreen")
frame_derecha.pack(side="right", fill="both", expand=True)


#frame2.grid_propagate(0)

# Color de fondo para la ventana
ventana.configure(bg="#f0f0f0")

frame_top_derecha = tk.Frame(frame_derecha, bg="lightgreen") 

# Título para la ventana
titulo_d = tk.Label(frame_top_derecha, text="Seleccione su factura", font=("Helvetica", 32), bg="#a9b1d9")
titulo_d.pack(pady=20)

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
button_get_data = tk.Button(frame_izquierda, text="Get Data", command=grad_data)
button_get_data.pack(in_=button_frame, side=tk.LEFT, pady=10)

button_get_graph = tk.Button(frame_izquierda, text="Get Graph", command=grad_graph)
button_get_graph.pack(in_=button_frame, side=tk.LEFT, pady=10)

date = tk.Label(frame_izquierda, text = "Compare con los precios de mercado")
date.pack(pady = 20)

# Widgets de display de data
widgets: dict[str, tk.Widget] = {}

# Botón para abrir el seleccionador de archivos
boton = tk.Button(frame_top_derecha, text="Seleccionar Archivo", command=lambda: abrir_seleccionador())#, width=40, height=5)
boton.pack(pady=1)

frame_top_derecha.pack()

frame_bot_derecha = tk.Frame(frame_derecha)

def update():       # Para gestionar Ctrl-c
    ventana.after(50, update)
ventana.after(50, update)
#while True:
#    ventana.update_idletasks
ventana.mainloop()

