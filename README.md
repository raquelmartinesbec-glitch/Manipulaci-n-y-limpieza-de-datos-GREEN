# 🌿 Proyecto de Análisis y Limpieza de Datos - GreenMart Dataset

Este repositorio contiene un flujo de trabajo completo para el análisis, manipulación y limpieza de datos basado en el dataset de GreenMart, una cadena de retail especializada en productos ecológicos.

## 📋 Descripción del Proyecto

El proyecto se centra en el análisis de patrones de compra de clientes y productos de GreenMart, implementando técnicas de limpieza de datos, análisis exploratorio y generación de datasets ficticios para preservar la confidencialidad de la información real.

### 🔒 Confidencialidad, Privacidad y Anonimización de Datos

**IMPORTANTE**: Este repositorio implementa **anonimización completa** y NO contiene datos reales de clientes o transacciones. Los datos sintéticos se han generado porque **los datos reales de GreenMart no pueden ser compartidos** por razones de confidencialidad empresarial y cumplimiento de normativas de privacidad:

- ✅ **Los datos reales están protegidos** y no pueden salir del entorno empresarial
- ✅ Se utilizan exclusivamente **datos ficticios completamente anonimizados** como alternativa
- ✅ Los datos ficticios **replican la estructura** del dataset real sin comprometer información sensible
- ✅ **Eliminación total** de nombres, direcciones, información financiera o datos personales reales
- ✅ **Códigos anónimos** reemplazan cualquier identificador personal
- ✅ El generador de datos sintéticos utiliza **identificadores no trazables**

## 🎯 Origen y Generación de Datos

### 📊 ¿De dónde provienen los datos?
**CONTEXTO IMPORTANTE**: Los datos reales de GreenMart no pueden ser compartidos por políticas de confidencialidad empresarial y normativas de privacidad. Por esta razón, los datos utilizados en este proyecto son **100% sintéticos** y se generan usando:

- **🎲 Algoritmos matemáticos**: Distribuciones estadísticas controladas
- **🎭 Librería Faker**: Generación de datos ficticios realistas pero no reales
- **🔢 NumPy Random**: Números aleatorios con semillas controladas
- **📅 Fechas sintéticas**: Rangos temporales ficticios de los últimos 2 años
- **💰 Valores económicos**: Precios y cantidades dentro de rangos lógicos

### 🔄 Proceso de Generación:
1. **Protección de datos reales**: Los datos originales permanecen en el entorno empresarial
2. **Definición de estructura**: Columnas y tipos de datos esperados (sin datos reales)
3. **Generación algorítmica**: Creación de registros sintéticos que replican patrones
4. **Aplicación de reglas**: Lógica de negocio para datos coherentes pero inventados
5. **Anonimización**: Códigos y IDs no trazables
6. **Exportación**: Archivo CSV listo para procesamiento académico/educativo

### 📁 Flujo de Archivos:
```
Datos Reales GreenMart (PROTEGIDOS/NO COMPARTIDOS) 
           ↓ 
    Estructura Replicada
           ↓
Algoritmos Sintéticos → data_generator.py → greenmart_customers_products.csv → preprocessing.py → greenmart_dataset_limpio.csv
```

## 🗂️ Estructura del Proyecto

```
Proyecto_Analisis_GREEN/
├── 📓 notebooks/                    # Jupyter Notebooks para análisis exploratorio
│   ├── 01_analisis_inicial.ipynb   # Análisis exploratorio y generación de datos
│   └── Limpieza_de_dataset_Green.ipynb  # Proceso detallado de limpieza de datos
├── 🐍 scripts/                     # Scripts de procesamiento y generación
│   ├── data_generator.py           # Generador de datos ficticios
│   └── preprocessing.py            # Script de limpieza sin funciones (estructura lineal)
├── 📊 data/                        # Datasets ficticios generados
│   ├── greenmart_customers_products.csv (generado localmente)
│   └── greenmart_dataset_limpio.csv (resultado del preprocesamiento)
├── 📋 reports/                     # Informes y documentación
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

### 2. Generar Datos Sintéticos (ORIGEN DE LOS DATOS)
```bash
# PASO 1: Ejecutar el generador de datos sintéticos
python scripts/data_generator.py
```
**🔍 ¿De dónde vienen los datos?**
- 🚫 **Datos reales protegidos**: Los datos originales de GreenMart no pueden ser compartidos
- ✅ **100% sintéticos**: Generados por algoritmos usando la librería `Faker`
- ✅ **Sin fuente real**: No provienen de ningún dataset real o base de datos
- ✅ **Completamente ficticios**: Creados matemáticamente para simular patrones
- ✅ **Guardados en**: `data/greenmart_customers_products.csv`

### 3. Ejecutar Limpieza de Datos
```bash
# PASO 2: Procesar y limpiar datos sintéticos
python scripts/preprocessing.py
```
**📊 Flujo de datos:**
- 📥 **Entrada**: `data/greenmart_customers_products.csv` (datos sintéticos)
- 🧹 **Procesamiento**: Limpieza, normalización y anonimización
- 📤 **Salida**: `data/greenmart_dataset_limpio.csv` (datos procesados)

### 4. Análisis Exploratorio
```bash
# PASO 3: Análisis interactivo
jupyter notebook notebooks/01_analisis_inicial.ipynb
```

## 📊 Estructura del Dataset Anónimo

El dataset generado contiene las siguientes columnas **completamente anonimizadas**:

| Columna | Tipo | Descripción | Estado de Anonimización |
|---------|------|-------------|-------------------------|
| `customer_name` | string | ID de cliente anonimizado (CUSTOMER_XXXXXX) | 🚫 Eliminado en limpieza |
| `age` | integer | Rango de edad ficticio | 🚫 Eliminado en limpieza |
| `city` | string | Código de ciudad anónimo (CITY_XXXX) | 🚫 Eliminado en limpieza |
| `purchase_date` | date | Fecha de compra ficticia | ✅ Transformado a variables temporales |
| `purchase_quantity` | integer | Cantidad de productos (normalizado) | ✅ Normalizado |
| `price_per_unit` | float | Precio por unidad (normalizado) | ✅ Normalizado |
| `total_spent` | float | Total gastado (normalizado) | ✅ Normalizado |
| `product_name` | string | Código de producto anónimo (PROD_ECO001) | ✅ Codificado numéricamente |
| `category` | string | Código de categoría anónimo (CAT_A) | ✅ Codificado numéricamente |

## 🧹 Proceso de Limpieza de Datos

El pipeline de limpieza sigue una **estructura secuencial sin funciones**, implementando los siguientes pasos:

### 1. **Exploración Inicial**
- Visualización de primeras filas con `df.head()`
- Información de tipos de datos con `df.info()`
- Estadísticas descriptivas con `df.describe()`
- Listado de columnas disponibles

### 2. **Identificación de Valores Faltantes**
- Análisis con `df.isnull().sum()`
- Identificación de patrones de datos ausentes

### 3. **Eliminación de Datos Sensibles**
- **Anonimización completa**: Eliminación de toda información personal identificable
- Columnas removidas por privacidad: `customer_name`, `age`, `city`
- **Cumplimiento GDPR**: Sin datos que permitan identificar individuos

### 4. **Manejo de Duplicados**
- Conteo con `df.duplicated().sum()`
- Eliminación con `df.drop_duplicates()`

### 5. **Normalización de Fechas**
- Conversión a formato datetime con `pd.to_datetime()`
- Extracción de características temporales:
  - `year`: Año de la compra
  - `month`: Mes de la compra
  - `day`: Día de la compra
  - `weekday`: Día de la semana (0=Lunes)
- Eliminación de la columna fecha original

### 6. **Estandarización Numérica**
- Aplicación de `StandardScaler` (media=0, desviación=1)
- Variables normalizadas: `purchase_quantity`, `price_per_unit`, `total_spent`

### 7. **Codificación Categórica**
- Aplicación de `LabelEncoder` para convertir categorías en números únicos
- Variables codificadas: `product_name`, `category`

### 8. **Guardado del Dataset Limpio**
- Exportación como `greenmart_dataset_limpio.csv`

## 🔍 Características del Análisis

- **Anonimización Total**: Eliminación completa de datos personales identificables
- **Estructura Lineal**: Código secuencial sin funciones para facilitar comprensión y modificación
- **Análisis Exploratorio**: Estadísticas descriptivas, distribuciones y patrones
- **Calidad de Datos**: Identificación de inconsistencias y valores atípicos
- **Transformaciones**: Normalización y codificación de variables
- **Reproducibilidad**: Pipeline claro y documentado paso a paso
- **Cumplimiento de Privacidad**: Sin información trazable a individuos reales

## 🛡️ Consideraciones de Seguridad

- Los datos ficticios se generan usando librerías como `Faker` para crear información realista pero no real
- No se almacenan credenciales ni información sensible en el repositorio
- El `.gitignore` está configurado para excluir archivos de configuración locales
- El dataset limpio se genera localmente y no se incluye en el control de versiones

## 🤝 Contribuciones

Este proyecto está diseñado para fines educativos y de análisis. Las contribuciones son bienvenidas siguiendo las mejores prácticas de desarrollo colaborativo.

## 📄 Licencia

Proyecto desarrollado con fines académicos y de aprendizaje en manipulación y limpieza de datos.

---

*⚠️ Recordatorio: Este repositorio contiene únicamente datos ficticios. Cualquier similitud con personas o transacciones reales es pura coincidencia.*
