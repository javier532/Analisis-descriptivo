#andres felipe / Javier bautista
"""archivo de parcial

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bFeBN_dlbwAvSQvMV1CuQWwwKNYSc64r

este archivo lo que hace es mostrar diferente tipos de acta y de su idioma la forma que esta hecha , si existe fisico o pdf y mas cosas
"""

import pandas as pd
import glob
import numpy as np
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

all_files = glob.glob("/content/drive/MyDrive/Esquema_de_Publicaci_n_de_Informaci_n_20240911.csv")

file_list = []
for f in all_files:
    data = pd.read_csv(f,skiprows=4)
    data['source_file'] = f # nueva columna conteniendo el nombre del fichero leido
    file_list.append(data)
df = pd.concat(file_list)


# leer un archivo CSV desde Google Drive, procesarlo y almacenar los datos en un DataFrame de pandas

df.shape
#filas columnas

df.head()
#muestra primera 5 filas

df=df.rename(columns={'ACTAS DE CONCILIACION - INFORMES AL MINISTERIO		': 'ESPAÑOL	','ACTAS DE SUCESION':'sucesion','ACTAS DE VISITAS':'visitas','ACTAS SERIALES INUTILIZADOS	':'inutilizados','CERTIFICADOS DE CANCELACION DE GRAVAMENES O LI...	':'cancelacion','CERTIFICADOS DE RETENCION':'retencion'})
df.head()

#renombrar columnas

df=df.replace(to_replace=r'.\(.+\)$', value='', regex=True)
df.head(1)
#reemplazar

df.fecha=df.ESPAÑOL.replace(regex={'':'',r'\.+xls':''})
df.head(1)

# Verificar los nombres de las columnas
print(df.columns)

if 'SEMESTRAL' in df.columns:
    df['SEMESTRAL'] = df['SEMESTRAL'].astype('string')

if 'ARCHIVO NOTARIAL' in df.columns:
    df['ARCHIVO NOTARIAL'] = df['ARCHIVO NOTARIAL'].astype('string')

# Si 'fecha' ya es datetime, no necesitas convertirlo de nuevo
# Solo asegúrate de que esté en el formato correcto
df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')  # Solo si es necesario

# Mostrar información del DataFrame
df.info()

estaciones_con_nan=df[df.isnull().any(axis=1)]['ESPAÑOL'].unique()
df.drop(df[df['ESPAÑOL'].isin(estaciones_con_nan)].index, inplace=True)
df.isna().sum()

df.filter(regex='^temp_*', axis=1).sample(5)

result = df.groupby('ACTAS DE CONCILIACION - INFORMES AL MINISTERIO').mean()
    print(result)

try:
    result = df.sort_values(by='ACTAS DE CONCILIACION - INFORMES AL MINISTERIO', ascending=False)[['ACTAS DE SUCESION', 'ACTAS DE VISITAS']].head()
    print(result)
except KeyError as e:
    print(f"KeyError: {e}. Asegúrate de que los nombres de las columnas sean correctos.")

if not frequencies.empty:
    import matplotlib.pyplot as plt

    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    frequencies.plot(kind='bar', color='skyblue')
    plt.title('ESPAÑOL')
    plt.xlabel('ACTAS DE CONCILIACION - INFORMES AL MINISTERIO')
    plt.ylabel('SEMESTRAL')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y')

    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()
else:
    print("No hay datos para graficar.")
