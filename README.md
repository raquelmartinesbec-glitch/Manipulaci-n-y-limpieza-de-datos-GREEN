# 🌿 Proyecto de Análisis y Limpieza de Datos - GreenMart Dataset

Este repositorio contiene un flujo de trabajo completo para el análisis, manipulación y limpieza de datos basado en el dataset de GreenMart, una cadena de retail especializada en productos ecológicos.

## 📋 Descripción del Proyecto

El proyecto se centra en el análisis de patrones de compra de clientes y productos de GreenMart, implementando técnicas de limpieza de datos, análisis exploratorio y generación de datasets ficticios para preservar la confidencialidad de la información real.

### 🔒 Confidencialidad y Privacidad de Datos

**IMPORTANTE**: Este repositorio NO contiene datos reales de clientes o transacciones. Por motivos de seguridad y cumplimiento de normativas de privacidad:

- ✅ Se utilizan exclusivamente **datos ficticios** generados sintéticamente
- ✅ Los datos ficticios **replican la estructura** del dataset real sin comprometer información sensible
- ✅ No se incluyen nombres, direcciones, información financiera o datos personales reales
- ✅ El generador de datos sintéticos permite recrear escenarios de análisis sin riesgos de privacidad

## 🗂️ Estructura del Proyecto

```
Proyecto_Analisis_GREEN/
├── 📓 notebooks/                    # Jupyter Notebooks para análisis exploratorio
│   ├── 01_analisis_inicial.ipynb   # Análisis exploratorio y generación de datos
│   └── Limpieza_de_dataset_Greenmart.ipynb  # Proceso original de limpieza
├── 🐍 scripts/                     # Scripts de procesamiento y generación
│   ├── data_generator.py           # Generador de datos ficticios
│   └── preprocessing.py            # Funciones de limpieza y preprocesamiento
├── 📊 data/                        # Datasets ficticios generados
│   └── greenmart_customers_products.csv (generado localmente)
├── 📋 reports/                     # Informes y documentación
│   └── Informe_GreenMart_Dataset.pdf
├── 🔧 .gitignore                   # Configuración de archivos ignorados
├── 📝 README.md                    # Este archivo
└── 📦 requirements.txt             # Dependencias del proyecto
```

## 🚀 Instalación y Uso

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### 1. Configuración del Entorno
```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd Proyecto_Analisis_GREEN

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Generar Datos Ficticios
```bash
# Ejecutar el generador de datos
python scripts/data_generator.py
```

### 3. Análisis Exploratorio
```bash
# Abrir Jupyter Notebook
jupyter notebook notebooks/01_analisis_inicial.ipynb
```

## 📊 Estructura del Dataset Ficticio

El dataset generado contiene las siguientes columnas:

| Columna | Tipo | Descripción |
|---------|------|-------------|
| `customer_name` | string | Nombre ficticio del cliente |
| `age` | integer | Edad del cliente (18-80 años) |
| `city` | string | Ciudad ficticia |
| `purchase_date` | date | Fecha de compra (últimos 2 años) |
| `purchase_quantity` | integer | Cantidad de productos comprados |
| `price_per_unit` | float | Precio por unidad del producto |
| `total_spent` | float | Total gastado en la compra |
| `product_name` | string | Nombre del producto |
| `category` | string | Categoría del producto |

## 🧹 Proceso de Limpieza de Datos

El pipeline de limpieza incluye:

1. **Identificación de valores faltantes**: Análisis de patrones de datos ausentes
2. **Eliminación de columnas no utilizables**: Columnas con >60% de valores faltantes
3. **Normalización de fechas**: Conversión a formato estándar y extracción de características temporales
4. **Estandarización numérica**: Aplicación de StandardScaler para variables numéricas
5. **Codificación categórica**: LabelEncoder para variables categóricas
6. **Eliminación de duplicados**: Identificación y remoción de registros duplicados

## 🔍 Características del Análisis

- **Análisis Exploratorio**: Estadísticas descriptivas, distribuciones y patrones
- **Calidad de Datos**: Identificación de inconsistencias y valores atípicos
- **Visualizaciones**: Gráficos para entender patrones de compra y comportamiento
- **Simulación de Problemas**: Recreación de escenarios de datos sucios para práctica

## 🛡️ Consideraciones de Seguridad

- Los datos ficticios se generan usando librerías como `Faker` para crear información realista pero no real
- No se almacenan credenciales ni información sensible en el repositorio
- El `.gitignore` está configurado para excluir archivos de configuración locales
- El informe original se incluye como excepción para documentación del proyecto

## 🤝 Contribuciones

Este proyecto está diseñado para fines educativos y de análisis. Las contribuciones son bienvenidas siguiendo las mejores prácticas de desarrollo colaborativo.

## 📄 Licencia

Proyecto desarrollado con fines académicos y de aprendizaje en manipulación y limpieza de datos.

---

*⚠️ Recordatorio: Este repositorio contiene únicamente datos ficticios. Cualquier similitud con personas o transacciones reales es pura coincidencia.*
