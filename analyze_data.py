import pandas as pd
import requests as rq
import numpy as np

file1 = "resources/consumptions.csv"
file2 = "resources/electrodatos.csv"

def identificar_formato(archivo):
    global tipo
    with open(archivo, 'r') as f:
        primera_linea = f.readline()
        if "CUPS;Fecha;Hora;Consumo_KWh;Metodo_obtencion" in primera_linea:
            tipo = True
        else:
            tipo = False

        return tipo

def get_API(fecha):
    global dfAPI
    url = "https://api.esios.ree.es/archives/70/download_json?date=" + fecha
    response = rq.get(url)
    array_precios = np.zeros(24)

    dfAPI = []
    i = 0
    if response.status_code == 200:
        data = response.json()
        data = data["PVPC"]
        for line in data:
            hora = line['Hora']
            pcb = line['PCB']

            array_precios[i] = float(pcb.replace(",","."))
            dfAPI.append((hora,pcb))

            i = i + 1
    else:
        print("Error al obtener los datos:", response.status_code)

def leer_csv(archivo):
    formato = identificar_formato(archivo)
    if formato:
        df = pd.read_csv(archivo,sep=';')
    else:
        df = pd.read_csv(archivo)
    return df

if __name__ == "__main__":
    df = leer_csv(file1)
