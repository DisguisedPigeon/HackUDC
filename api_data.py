from datetime import datetime, timedelta
from typing import Optional
from pandas.core.api import DataFrame
import requests
import pandas as pd

def get_power_kWh_by_hour(fecha:str, location:str="PCB") -> Optional[pd.DataFrame]:
    url:str = "https://api.esios.ree.es/archives/70/download_json?date=" + fecha
    response = requests.get(url)

    if response.status_code == 200:
        data = pd.DataFrame.from_dict(response.json()["PVPC"])

        data: DataFrame | None = data.get(["Dia", "Hora", location])
        if data == None:
            return None
        data[location] = data[location].map(lambda x: float(x.replace(',', '.')))
        data["kWh"] = data[location] / 1000
        data.drop(location)
        
        return data
    else:
        print("Error al obtener los datos:", response.status_code)
        return None

if __name__ == "__main__":
    print(get_power_kWh_by_hour(str((datetime.today() - timedelta(days=1)).date())))
