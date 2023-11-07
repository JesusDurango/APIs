import pandas as pd

def procesar_datos(dataframe):
    # Verificar valores faltantes
    if dataframe.isnull().values.any():
        dataframe.dropna(inplace=True)

    # Verificar filas duplicadas
    if dataframe.duplicated().any():
        dataframe.drop_duplicates(inplace=True)

    # Verificación y eliminación de valores atípicos
    numeric_columns = ['age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets', 'serum_sodium', 'time']

    for column in numeric_columns:
        Q1 = dataframe[column].quantile(0.25)
        Q3 = dataframe[column].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        dataframe = dataframe[(dataframe[column] >= lower_bound) & (dataframe[column] <= upper_bound)]

    # Crear columna que categorice por edades
    def categorizar_edades(edad):
        if edad <= 12:
            return "Niño"
        elif edad <= 19:
            return "Adolescente"
        elif edad <= 39:
            return "Jóvenes adulto"
        elif edad <= 59:
            return "Adulto"
        else:
            return "Adulto mayor"

    dataframe['categoria_edad'] = dataframe['age'].apply(categorizar_edades)

    return dataframe

# Cargar el archivo CSV original
archivo_csv = "heart_failure_dataset.csv"
df = pd.read_csv(archivo_csv)

# Llamar a la función para procesar los datos
df_procesado = procesar_datos(df)

# Guardar el DataFrame procesado en un archivo CSV
df_procesado.to_csv("heart_failure_dataset_processed.csv", index=False)
print("Los datos procesados han sido guardados en 'heart_failure_dataset_processed.csv'")
