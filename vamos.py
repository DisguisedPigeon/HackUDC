import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport

df = pd.read_csv("./resources/electrodatos.csv")

df.info()

df['Fecha'] = df['Fecha'].apply(lambda x: pd.Timestamp(x))
df['datetime'] = pd.to_datetime(df['datetime'])

df['Código universal de punto de suministro'] = df['Código universal de punto de suministro'].astype(str)

df.info()

# Set the figure size
plt.figure(figsize=(10, 6))
sns.lineplot(data=df,
             x='datetime',
             y='Consumo',
             hue='Código universal de punto de suministro'
            )

plt.tight_layout() #Ajuste del padding
plt.show() #Mostrar imagen

sns.lineplot(data=df[df['Código universal de punto de suministro'] == '6'],
             x='datetime',
             y='Consumo',
             hue='Código universal de punto de suministro')

sns.lineplot(
    data=df[(df['datetime'] > '2023-05-01') & (df['datetime'] < '2023-05-08')],
    x='datetime',
    y='Consumo',
    hue='Código universal de punto de suministro',
    alpha=0.5
  )

df[df['Código universal de punto de suministro'] == '6'].tail()

df['Fecha'].max()

profile = ProfileReport(df, title="Report Contadores Luz")