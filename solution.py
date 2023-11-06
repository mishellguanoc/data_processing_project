import numpy as np
import pandas as pd
import requests
import os

def descargar_datos(url, nombre_archivo):
     # Realizar una solicitud GET para descargar los datos
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Escribir el contenido de la respuesta en un archivo CSV
        with open(nombre_archivo, 'wb') as archivo:
            archivo.write(response.content)
        print(f'Los datos se han descargado y guardado como {nombre_archivo}')
    else:
        print(f'Error al descargar los datos. Código de estado: {response.status_code}')


def limpiar_y_preparar_datos(dataframe):
    # Verificar que no existan valores faltantes
    if dataframe.isnull().values.any():
        dataframe.dropna(inplace=True)
        print("Valores faltantes eliminados.")
    # Verificar que no existan filas repetidas
    if dataframe.duplicated().any():
        dataframe.drop_duplicates(inplace=True)
        print("Filas duplicadas eliminadas.")
    # Verificar si existen valores atipicos y eliminarlos
    Q1 = dataframe['age'].quantile(0.25)
    Q3 = dataframe['age'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    dataframe = dataframe[(dataframe['age'] >= lower_bound) & (dataframe['age'] <= upper_bound)]
    print("Valores atípicos en la columna 'age' eliminados.")
    # Crear una columna que categorice por edades
    dataframe['edad_categorizada'] = pd.cut(
        dataframe['age'],
        bins=[0, 12, 19, 39, 59, np.inf],
        labels=['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
    )

    # Guardar el resultado como csv
    dataframe.to_csv('datos_limpios.csv', index=False)
    print("Datos limpios guardados como 'datos_limpios.csv'.")

