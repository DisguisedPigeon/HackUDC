import tkinter as tk

def mouse_entra(event):
    boton.config(bg="blue", fg="white")
    ventana.config(cursor="hand2")

def mouse_sale(event):
    boton.config(bg="SystemButtonFace", fg="black")
    ventana.config(cursor="")

def imprimir_mensaje():
    etiqueta.config(text="¡Botón pulsado!")

ventana = tk.Tk()
ventana.title("Botón con Efecto Hover")

# Crear el botón
boton = tk.Button(ventana, text="Haz clic aquí", command=imprimir_mensaje)
boton.pack(pady=20)

# Enlazar eventos de mouse al botón
boton.bind("<Enter>", mouse_entra)
boton.bind("<Leave>", mouse_sale)

# Etiqueta para mostrar el mensaje cuando se hace clic en el botón
etiqueta = tk.Label(ventana, text="")
etiqueta.pack()

ventana.mainloop()
