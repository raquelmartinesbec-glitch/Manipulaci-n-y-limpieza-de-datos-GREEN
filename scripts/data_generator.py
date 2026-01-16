# Script para generar datos ficticios basados en la estructura de los datos reales
# Actualiza la variable 'columns' con los nombres y tipos de tus columnas reales

import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

# Estructura basada en el dataset real de Greenmart
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
                row[col] = fake.name()
            elif col == "city":
                row[col] = fake.city()
            elif col == "product_name":
                products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones", "Tablet", "Phone"]
                row[col] = np.random.choice(products)
            elif col == "category":
                categories = ["Electronics", "Accessories", "Computing", "Audio", "Mobile"]
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

data = [generate_row() for _ in range(N)]
df = pd.DataFrame(data)
df.to_csv("data/greenmart_customers_products.csv", index=False)
print("Datos ficticios generados en data/greenmart_customers_products.csv")
