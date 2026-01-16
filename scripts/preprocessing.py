# Script de preprocesamiento y limpieza de datos
# Aquí puedes agregar funciones para limpiar y transformar los datos generados

import pandas as pd

def cargar_datos(path):
    return pd.read_csv(path)

# Ejemplo de función de limpieza
# def limpiar_datos(df):
#     # Aplica transformaciones y limpieza
#     return df

if __name__ == "__main__":
    df = cargar_datos("data/data_sample.csv")
    print(df.head())
