import requests
import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np


# Definir la fecha inicial
fecha_actual = datetime.strptime("2023-01-01", "%Y-%m-%d")

media_horas = {
    "00-01": 0,
    "01-02": 0,
    "02-03": 0,
    "03-04": 0,
    "04-05": 0,
    "05-06": 0,
    "06-07": 0,
    "07-08": 0,
    "08-09": 0,
    "09-10": 0,
    "10-11": 0,
    "11-12": 0,
    "12-13": 0,
    "13-14": 0,
    "14-15": 0,
    "15-16": 0,
    "16-17": 0,
    "17-18": 0,
    "18-19": 0,
    "19-20": 0,
    "20-21": 0,
    "21-22": 0,
    "22-23": 0,
    "23-24": 0,
}

# URL del endpoint proporcionado
url = "https://api.esios.ree.es/archives/70/download_json?date=" + fecha_actual.strftime("%Y-%m-%d")
# Envía la solicitud GET al endpoint
response = requests.get(url)

# Verifica si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Si la solicitud fue exitosa, carga los datos JSON
    data = response.json()
    data = data["PVPC"]
    for line in data:
        # Accede a los valores específicos dentro del objeto JSON
        dia = line['Dia']
        hora = line['Hora']
        pcb = line['PCB']
        #cym = line['CYM']
        #cof2td = line['COF2TD']
        # y así sucesivamente para los demás campos
        # Imprime algunos de los valores obtenidos
        print("\nInformación específica:")
        print("Hora:", hora)
        print("Precio PCB:", pcb)
        media_horas[hora] += float(pcb.replace(",","."))
        
        #print("Precio CYM:", cym)
        #print("Cof2td:", cof2td)
        # y así sucesivamente para los demás campos
else:
    # Si la solicitud falló, imprime el mensaje de error
    print("Error al obtener los datos:", response.status_code)

i = 0

media_horas_array = np.zeros(len(media_horas))
for x in media_horas:
    media_horas_array[i] = media_horas[x]/num_dias
    i = i + 1
    
plt.style.use('_mpl-gallery')

plt.bar([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],media_horas_array)

plt.tight_layout() #Ajuste del padding
plt.show() #Mostrar imagen
# Obtener graficos que ayuden a visualizar en que horas del día esta más cara la electricidad