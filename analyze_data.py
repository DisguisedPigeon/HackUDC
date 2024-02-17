import pandas as pd
import requests
import numpy as np
from datetime import datetime

tipo = None
dfAPI = None

foo1 = "resources/consumptions.csv"
foo2  = "resources/electrodatos.csv"

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
    response = requests.get(url)
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

def mayor_consumo(df):
    print("me voy a pegar un tiro")

df = leer_csv(foo1)
mayor_consumo(df)

