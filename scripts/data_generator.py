# =========================================================================
# GENERADOR DE DATOS SINTÉTICOS - GREENMART
# =========================================================================
# MOTIVO: Los datos reales NO PUEDEN ser compartidos por confidencialidad
# SOLUCIÓN: Generación de dataset completamente ficticio para análisis
# ORIGEN REAL: Datos confidenciales de GreenMart (NO incluidos)
# ORIGEN SINTÉTICO: Algoritmos que replican estructura sin datos reales
# DESTINO: data/greenmart_customers_products.csv
# PRIVACIDAD: 100% protegida - sin información real comprometida
# =========================================================================

# Script para generar datos ficticios basados en la estructura de los datos reales
# Actualiza la variable 'columns' con los nombres y tipos de tus columnas reales

import pandas as pd
import numpy as np
from faker import Faker
import os

fake = Faker()

# Estructura de datos sintética que replica el dataset real de GreenMart
# (Los datos reales no pueden ser compartidos por políticas de privacidad)
columns = [
    ("customer_name", "str"),
    ("age", "int"),
    ("city", "str"),
    ("purchase_date", "date"),
    ("purchase_quantity", "int"),
    ("price_per_unit", "float"),
    ("total_spent", "float"),
    ("product_name", "str"),
    ("category", "str")
]

N = 100  # Número de filas ficticias

def generate_row():
    row = {}
    for col, tipo in columns:
        if tipo == "int":
            if col == "age":
                row[col] = np.random.randint(18, 80)
            elif col == "purchase_quantity":
                row[col] = np.random.randint(1, 10)
            else:
                row[col] = np.random.randint(1, 1000)
        elif tipo == "str":
            if col == "customer_name":
                row[col] = f"CUSTOMER_{np.random.randint(100000, 999999)}"
            elif col == "city":
                row[col] = f"CITY_{np.random.randint(1000, 9999)}"
            elif col == "product_name":
                products = ["PROD_ECO001", "PROD_ECO002", "PROD_ECO003", "PROD_ECO004", "PROD_ECO005", "PROD_ECO006", "PROD_ECO007"]
                row[col] = np.random.choice(products)
            elif col == "category":
                categories = ["CAT_A", "CAT_B", "CAT_C", "CAT_D", "CAT_E"]
                row[col] = np.random.choice(categories)
            else:
                row[col] = fake.word()
        elif tipo == "date":
            row[col] = fake.date_between(start_date="-2y", end_date="today")
        elif tipo == "float":
            if col == "price_per_unit":
                row[col] = round(np.random.uniform(10, 500), 2)
            elif col == "total_spent":
                # Calcular basado en quantity y price (con algo de variación)
                quantity = np.random.randint(1, 10)
                price = round(np.random.uniform(10, 500), 2)
                row[col] = round(quantity * price * np.random.uniform(0.9, 1.1), 2)
            else:
                row[col] = round(np.random.uniform(100, 10000), 2)
        else:
            row[col] = None
    return row

# Generar datos sintéticos
print("📋 Generando datos sintéticos anónimos...")
data = [generate_row() for _ in range(N)]
df = pd.DataFrame(data)

# Crear directorio si no existe
os.makedirs("data", exist_ok=True)

# Guardar dataset sintético
output_path = "data/greenmart_customers_products.csv"
df.to_csv(output_path, index=False)

print("\n" + "="*60)
print("🎉 DATASET SINTÉTICO GENERADO EXITOSAMENTE")
print("="*60)
print("🔒 MOTIVO: Los datos reales de GreenMart no pueden ser compartidos")
print("🎩 SOLUCIÓN: Dataset sintético que replica estructura y patrones")
print(f"📁 Archivo creado: {os.path.abspath(output_path)}")
print(f"📏 Registros generados: {len(df):,}")
print(f"📊 Columnas: {len(df.columns)}")
print(f"🔒 Nivel de anonimización: 100% (sin datos reales)")
print(f"🎩 Método: Algoritmos sintéticos con Faker")
print("\n📢 Próximo paso: Ejecutar preprocessing.py para limpiar datos")
print("="*60)
