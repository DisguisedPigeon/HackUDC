#!/bin/python3
from datetime import datetime
from typing import Dict
import pandas as pd

TEST_DIRECTORY = "./resources/consumptions.csv"


def parse_data(data: str = TEST_DIRECTORY) -> Dict[str, Dict[int, str | int | float | datetime]]:
    ret_dict = pd.read_csv(data, sep=";").to_dict()
    dates: Dict[int, str] = ret_dict["Fecha"]
    hours: Dict[int, str] = ret_dict["Hora"]

    for index in dates:
        ret_dict["Fecha"][index] = datetime(
                int(dates[index][6:]),      #Año
                int(dates[index][3:5]),     #Mes
                int(dates[index][0:2]),     #Dia
                int(hours[index]) if int(hours[index]) != 24 else 0 #Hora (0-23)
                )
    ret_dict.pop("Hora")

    consumo = ret_dict["Consumo_KWh"]
    for index in consumo:
        ret_dict["Consumo_KWh"][index] = float(consumo[index].replace(",", "."))

    return ret_dict

def print_data(data: str = TEST_DIRECTORY) -> None:
    val = pd.read_csv(data, sep=";").to_markdown() 
    if val == None:
        val = "Failed to parse"
    print(val)

