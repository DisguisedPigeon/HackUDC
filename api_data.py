from datetime import datetime, timedelta
from typing import Optional
import requests

def get_power_kWh_by_hour(fecha:str, location:str="PCB")-> Optional[dict[datetime, float]]:
    url:str = "https://api.esios.ree.es/archives/70/download_json?date=" + fecha
    response = requests.get(url)

    if response.status_code == 200:
        data: list[dict[str, str]] = response.json()["PVPC"]

        prices_per_kWh: dict[datetime, float] = {}
        for line in data:
            timestamp: datetime = datetime(
                    day=int(line["Dia"][0:2]),
                    month=int(line["Dia"][3:5]),
                    year=int(line["Dia"][6:]),
                    hour=int(line["Hora"][0:2]),
                    )
            prices_per_kWh[timestamp] = float(line[location].replace(",", "."))
        return prices_per_kWh
    else:
        print("Error al obtener los datos:", response.status_code)
        return None
        
if __name__ == "__main__":
    print(get_power_kWh_by_hour(str((datetime.today() - timedelta(days=1)).date())))
