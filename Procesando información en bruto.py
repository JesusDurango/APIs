import requests

def descargar_datos_csv_desde_url(url, archivo_salida):
    try:
        # Realizamos una solicitud GET a la URL
        response = requests.get(url)

        # Verificamos si la solicitud fue exitosa
        if response.status_code == 200:
            # Guardamos la respuesta en un archivo CSV
            with open(archivo_salida, 'wb') as archivo:
                archivo.write(response.content)
            print(f"Los datos han sido descargados correctamente en {archivo_salida}")
        else:
            print(f"Error al descargar los datos. Código de respuesta: {response.status_code}")

    except Exception as e:
        print(f"Ocurrió un error al descargar los datos: {str(e)}")

# Llamamos a la función para descargar los datos y guardarlos en un archivo CSV
url = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"
nombre_archivo = "heart_failure_dataset.csv"
descargar_datos_csv_desde_url(url, nombre_archivo)
