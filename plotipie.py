#!/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

TEST_DIRECTORY = "./resources/consumptions.csv"


def ploti_pie(yiar, data: str = TEST_DIRECTORY):
    if yiar == None:
        print("Usage: plotipie.py year")
        print("Exiting with code -1")
        sys.exit(-1)
    #Load data
    df = pd.read_csv(data, sep=";")
    #Create datetime column
    df['Fecha'] = df['Fecha'].apply(lambda x: pd.Timestamp(x))
    df['datetime'] = df['Fecha'].astype(str) + ' ' + df['Hora'].astype(str).replace("24", "00") + ':00:00'
    df['datetime'] = pd.to_datetime(df['datetime'])
    #Replace in consumo "," for "."
    df["Consumo_KWh"] = df['Consumo_KWh'].map(lambda x : float(x.replace(",", ".")))
    #Create column extracting the year
    df['year'] = pd.to_datetime(df['datetime']).dt.year
    #Create column 
    user_year = int(yiar)
    df['month'] = pd.to_datetime(df[df['year']==user_year]['datetime']).dt.month
    #All consume months of the user 
    months_year = df[df['year']==user_year]['month'].unique()
    months_dict = { 1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 
                   7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 
                   12: 'December'}
    #Keys array
    a1 = months_dict.keys()
    #Cast float array to int array
    a2 = months_year.astype(np.int32)
    #Extract same values from two arrays (only consume months)
    months_dict_filtered = np.intersect1d(list(a1),list(a2))
    #Consumes for month
    values = list(df['Consumo_KWh'].groupby(df['month']).sum())
    plt.pie(values, labels=[months_dict[key] for key in list(months_dict_filtered)], autopct=lambda p : '{:,.2f}'.format(p * sum(values)/100))

    plt.savefig('ploti.png')