#!/bin/python3
from datetime import datetime
from typing import Dict
import pandas as pd
import matplotlib.pyplot as plt

TEST_DIRECTORY = "./resources/electrodatos.csv"

#def make_autopct(values):


def parse_data(data: str = TEST_DIRECTORY) -> Dict[str, Dict[int, str | int | float | datetime]]:
    df = pd.read_csv(data)
    df['month'] = pd.to_datetime(df['datetime']).dt.month
    #TODO: mapear nombres de los meses a su correspondiente número
    months = ['Enero', 'febrero', 'marzo', 'abril', '', 'agosto']
    values = df[df['month']== 8]['Consumo'].groupby(df['month']).sum()
    plt.pie(values, labels=months, autopct='{v}'.format(v=float(values)))
    plt.show()

parse_data()