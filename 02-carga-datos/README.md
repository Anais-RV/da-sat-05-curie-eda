# 📂 Carga y Exploración Inicial de Datos

## Leer diferentes formatos

### CSV
```python
import pandas as pd

# Básico
df = pd.read_csv('datos.csv')

# Con opciones
df = pd.read_csv('datos.csv', 
                 sep=';',              # Delimitador
                 encoding='utf-8',     # Codificación
                 na_values=['NA', ''], # Valores nulos
                 parse_dates=['fecha'] # Convertir a datetime
                )
```

### Excel
```python
# Una hoja
df = pd.read_excel('datos.xlsx', sheet_name='Ventas')

# Múltiples hojas
dfs = pd.read_excel('datos.xlsx', sheet_name=None)
```

### JSON
```python
df = pd.read_json('datos.json')
```

## Exploración inicial (The Big Five)

```python
# 1. Primeras filas
df.head(10)

# 2. Información general
df.info()  # Tipos, nulos, memoria

# 3. Dimensiones
print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")

# 4. Estadísticos
df.describe()

# 5. Valores únicos
df.nunique()
```

## Verificar calidad

```python
# Nulos
df.isnull().sum()

# Duplicados
df.duplicated().sum()

# Tipos de datos
df.dtypes

# Valores únicos por columna
for col in df.columns:
    print(f"{col}: {df[col].nunique()} valores únicos")
```

---

**Autoría:** Anaïs Rodríguez Villanueva
