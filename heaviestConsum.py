#!/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys 

TEST_DIRECTORY = "./resources/electrodatos.csv"
#Load data
df = pd.read_csv(TEST_DIRECTORY)
#Create column extracting the year and month
df['year'] = pd.to_datetime(df['datetime']).dt.year
df['month'] = pd.to_datetime(df['datetime']).dt.month
print('Heaviest consume days of the August month in 2022 (first 10): ')
print(df[df['year']==2022][df['month']==8][["Fecha", "Consumo"]].groupby('Fecha').sum().sort_values('Consumo', ascending=False).head(10))
print('Heaviest consume days of the year 2022 (first 10): ')
print(df[df['year']==2022][["Fecha", "Consumo"]].groupby('Fecha').sum().sort_values('Consumo', ascending=False).head(10))