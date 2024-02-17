#!/bin/python3
from datetime import datetime
from typing import Dict
import pandas as pd

TEST_DIRECTORY = "./resources/consumptions.csv"


def parse_data(data: str = TEST_DIRECTORY) -> pd.DataFrame:
    df = pd.read_csv(data, sep=";")
    
    df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')
    df['Hora'] = df["Hora"].map(lambda x: 0 if int(x) == 24 else x)
    df['Hora'] = pd.to_timedelta(df["Hora"], unit='h'))

    df['Fecha'] = df['Fecha'] + df['Hora']

    df['Consumo_KWh'] = df['Consumo_KWh'].str.replace(',', '.').astype(float)

    df = df.drop(columns="Hora")

    return df

def print_data(data: str = TEST_DIRECTORY) -> None:
    val = pd.read_csv(data, sep=";").to_markdown() 
    if val == None:
        val = "Failed to parse"
    print(val)

def ret_md(data: str = TEST_DIRECTORY) -> str:
    val = pd.read_csv(data, sep=";").to_markdown() 
    if val == None:
        val = "Failed to parse"
    return val

def main():
    print(parse_data())
    
if __name__ == '__main__':
    main()
