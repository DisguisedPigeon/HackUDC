import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Dividir Espacio en Tkinter")

# Crear un frame principal
frame_principal = tk.Frame(ventana)
frame_principal.pack(fill="both", expand=True)

# Crear un frame para el texto a la izquierda
frame_izquierda = tk.Frame(frame_principal, bg="lightblue", width=200)
frame_izquierda.pack(side="left", fill="y")

# Agregar un texto dentro del frame de la izquierda
texto_izquierda = tk.Label(frame_izquierda, text="Texto a la Izquierda", font=("Arial", 12))
texto_izquierda.pack(padx=10, pady=10)

# Crear un frame para otro widget a la derecha
frame_derecha = tk.Frame(frame_principal, bg="lightgreen")
frame_derecha.pack(side="right", fill="both", expand=True)

# Agregar otro widget dentro del frame de la derecha (por ejemplo, un canvas)
# Aquí agregamos solo un label como ejemplo
widget_derecha = tk.Label(frame_derecha, text="Widget a la Derecha", font=("Arial", 12))
widget_derecha.pack(padx=10, pady=10)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
