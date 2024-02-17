from datetime import datetime, timedelta
from typing import Optional
from pandas.core.api import DataFrame
import requests
import pandas as np

def get_power_kWh_by_hour(fecha:str, location:str="PCB") -> Optional[np.DataFrame]:
    url:str = "https://api.esios.ree.es/archives/70/download_json?date=" + fecha
    response = requests.get(url)

    if response.status_code == 200:
        data = np.DataFrame.from_dict(response.json()["PVPC"])
        data = data.get(["Dia", "Hora", location])
        data[location] = data[location].map(lambda x: float(x.replace(',', '.')))
        data[location] = data[location] / 1000
        
        return data
    else:
        print("Error al obtener los datos:", response.status_code)
        return None

def get_price(consumption:DataFrame) -> DataFrame:
    pass

if __name__ == "__main__":
    print(get_power_kWh_by_hour(str((datetime.today() - timedelta(days=1)).date())))
