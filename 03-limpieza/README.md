# 🧹 Limpieza de Datos

## Valores nulos

```python
# Detectar
df.isnull().sum()

# Eliminar filas
df.dropna(inplace=True)

# Eliminar columnas con > 50% nulos
df.dropna(thresh=len(df)*0.5, axis=1, inplace=True)

# Imputar con media
df['columna'].fillna(df['columna'].mean(), inplace=True)

# Imputar con mediana
df['columna'].fillna(df['columna'].median(), inplace=True)

# Forward fill
df.fillna(method='ffill', inplace=True)
```

## Duplicados

```python
# Detectar
df.duplicated().sum()

# Eliminar
df.drop_duplicates(inplace=True)

# Basándose en columnas específicas
df.drop_duplicates(subset=['id'], keep='first', inplace=True)
```

## Outliers

```python
# IQR method
Q1 = df['columna'].quantile(0.25)
Q3 = df['columna'].quantile(0.75)
IQR = Q3 - Q1
filtro = (df['columna'] >= Q1 - 1.5*IQR) & (df['columna'] <= Q3 + 1.5*IQR)
df_limpio = df[filtro]

# Z-score
from scipy import stats
z_scores = np.abs(stats.zscore(df['columna']))
df_limpio = df[z_scores < 3]
```

## Tipos de datos

```python
# Convertir a numérico
df['columna'] = pd.to_numeric(df['columna'], errors='coerce')

# Convertir a datetime
df['fecha'] = pd.to_datetime(df['fecha'])

# Convertir a categórico
df['categoria'] = df['categoria'].astype('category')
```

---

**Autoría:** Anaïs Rodríguez Villanueva
