from solucion import descargar_datos, limpiar_y_preparar_datos

if __name__ == "__main__":
    # Aquí puedes usar las funciones como se describe en el script original.
    url_datos = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'
    archivo_txt = 'respuesta.txt'

    # Llama a la función para descargar y guardar los datos
    descargar_datos(url_datos, archivo_txt)

    # Cargar los datos desde el archivo CSV descargado
    archivo_csv = 'respuesta.txt'
    dataframe = pd.read_csv(archivo_csv)

    # Llamar a la función de limpieza y preparación de datos
    limpiar_y_preparar_datos(dataframe)