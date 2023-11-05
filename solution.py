from datasets import load_dataset
import numpy as np
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

# URL de los datos
url_datos = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv' 

# Nombre del archivo CSV en el que se guardarán los datos
archivo_csv = 'datos.csv'

# Llama a la función para descargar y guardar los datos
descargar_datos(url_datos, archivo_csv)