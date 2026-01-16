# Script de preprocesamiento y limpieza de datos
# Estructura sin funciones siguiendo el mismo flujo del notebook de limpieza
# CONTEXTO: Procesamiento de datos sintéticos generados porque los datos
#           reales de GreenMart no pueden ser compartidos por confidencialidad
# ENFOQUE EN ANONIMIZACIÓN: Todos los datos sensibles son eliminados o codificados

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Verificar y cargar dataset
import os

dataset_path = "data/greenmart_customers_products.csv"

# Verificar si el dataset existe
if not os.path.exists(dataset_path):
    print("❌ ERROR: No se encontró el archivo de datos")
    print("📍 Ubicación esperada:", os.path.abspath(dataset_path))
    print("🔧 SOLUCIÓN: Ejecuta primero el generador de datos:")
    print("   python scripts/data_generator.py")
    print("="*50)
    exit(1)

print("✅ Cargando dataset desde:", os.path.abspath(dataset_path))
print("� CONTEXTO: Los datos reales de GreenMart no pueden ser compartidos")
print("�📊 FUENTE DE DATOS: Datos sintéticos generados por data_generator.py")
print("🔒 TIPO: Completamente anónimos y ficticios")
print("="*50)

# Cargar dataset
df = pd.read_csv(dataset_path)

# Exploración inicial del dataset
print("Primeras filas del dataset:")
print(df.head())
print("\nInformación del dataset:")
print(df.info())
print("\nEstadísticas descriptivas:")
print(df.describe())
print("\nColumnas del dataset:")
print(list(df.columns))

# Identificación de valores faltantes
print("\nValores faltantes por columna:")
print(df.isnull().sum())

# Eliminar columnas con información sensible o identificable
# Estas columnas contienen información personal que debe ser removida por privacidad
cols_to_drop = ["customer_name", "age", "city"]
df = df.drop(columns=[col for col in cols_to_drop if col in df.columns], errors="ignore")
print(f"Columnas sensibles eliminadas: {cols_to_drop}")

# Verificar y eliminar duplicados
print(f"\nDuplicados encontrados: {df.duplicated().sum()}")
df = df.drop_duplicates()

# Normalizar fechas (purchase_date)
if "purchase_date" in df.columns:
    df["purchase_date"] = pd.to_datetime(df["purchase_date"], errors="coerce")
    df["year"] = df["purchase_date"].dt.year
    df["month"] = df["purchase_date"].dt.month
    df["day"] = df["purchase_date"].dt.day
    df["weekday"] = df["purchase_date"].dt.weekday  # 0 = Lunes
    
    # Eliminar la columna fecha original
    df = df.drop(columns=["purchase_date"])

# Normalizar valores numéricos con StandardScaler
num_cols = [col for col in ["purchase_quantity", "price_per_unit", "total_spent"] if col in df.columns]

if num_cols:
    scaler = StandardScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])

# Codificar variables categóricas con LabelEncoder para anonimización completa
# Esto convierte texto a números, eliminando cualquier referencia identificable
cols_to_encode = [col for col in ["product_name", "category"] if col in df.columns]
le = LabelEncoder()
for col in cols_to_encode:
    df[col] = le.fit_transform(df[col])
    print(f"Columna '{col}' codificada para anonimización")

# Guardar el dataset limpio y anonimizado
df.to_csv("data/greenmart_dataset_limpio.csv", index=False)

print("\n" + "="*60)
print("PROCESO DE LIMPIEZA Y ANONIMIZACIÓN COMPLETADO")
print("="*60)
print("✅ Dataset guardado como 'greenmart_dataset_limpio.csv'")
print(f"✅ Forma final del dataset: {df.shape}")
print("✅ Todos los datos sensibles han sido eliminados o codificados")
print("✅ No hay información personal identificable en el dataset final")
print("="*60)
