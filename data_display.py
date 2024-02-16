import tkinter as tk
from PIL import ImageTk, Image


def scroll_y(*args):
    text.yview(*args)



root = tk.Tk()

# Creamos un Text widget
text = tk.Text(root)
text.pack(side="left", fill="both", expand=True)

# Creamos una Scrollbar (barra de desplazamiento) vertical
scrollbar = tk.Scrollbar(root, command=scroll_y)
scrollbar.pack(side="right", fill="y")

# Configuramos la relación entre el Text widget y la barra de desplazamiento
text.config(yscrollcommand=scrollbar.set)

# Insertamos contenido en el Text widget para que sea lo suficientemente largo para requerir desplazamiento
for i in range(100):
    text.insert("end", f"This is line {i}\n")


root.mainloop()
