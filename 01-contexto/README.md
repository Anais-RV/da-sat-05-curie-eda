# 🛠️ Contexto: Herramientas Avanzadas para EDA

Instala y configura librerías especializadas para análisis exploratorio profesional.

## Librerías esenciales (ya las tienes)

```bash
pip install numpy pandas matplotlib seaborn scipy
```

## Herramientas avanzadas de EDA

### 1. pandas-profiling (ydata-profiling)

Genera reportes HTML automáticos con EDA completo.

```bash
pip install ydata-profiling
```

**Uso:**
```python
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('datos.csv')
profile = ProfileReport(df, title="Reporte EDA")
profile.to_file("reporte.html")
```

**Incluye:**
- Resumen de variables
- Valores nulos y duplicados
- Correlaciones
- Distribuciones
- Alertas de calidad

### 2. missingno

Visualiza patrones de valores nulos.

```bash
pip install missingno
```

**Uso:**
```python
import missingno as msno

# Matriz de nulos
msno.matrix(df)
plt.show()

# Heatmap de correlación de nulos
msno.heatmap(df)
plt.show()

# Barras de completitud
msno.bar(df)
plt.show()
```

### 3. sweetviz

EDA visual comparativo (ideal para comparar train/test).

```bash
pip install sweetviz
```

**Uso:**
```python
import sweetviz as sv

report = sv.analyze(df)
report.show_html("sweetviz_report.html")
```

### 4. dtale

Interfaz interactiva tipo Excel para explorar datos.

```bash
pip install dtale
```

**Uso:**
```python
import dtale

dtale.show(df)
# Abre interfaz web interactiva
```

## Configuración recomendada

### pandas: Mostrar más filas/columnas

```python
import pandas as pd

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.float_format', '{:.2f}'.format)
```

### matplotlib/seaborn: Estilo profesional

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Estilo
sns.set_style("whitegrid")
sns.set_palette("husl")

# Tamaño por defecto
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 11

# DPI alta resolución
plt.rcParams['figure.dpi'] = 100
```

## Template de inicio para EDA

Crea un archivo `eda_template.py`:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Configuración
sns.set_style("whitegrid")
pd.set_option('display.max_columns', None)
plt.rcParams['figure.figsize'] = (12, 6)

# Cargar datos
df = pd.read_csv('datos.csv')

# Exploración rápida
print("="*60)
print("INFORMACIÓN GENERAL")
print("="*60)
print(f"Dimensiones: {df.shape}")
print(f"\nPrimeras filas:")
print(df.head())
print(f"\nTipos de datos:")
print(df.dtypes)
print(f"\nValores nulos:")
print(df.isnull().sum())
print(f"\nEstadísticos:")
print(df.describe())

# Análisis univariado rápido
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    plt.figure()
    sns.histplot(df[col], kde=True)
    plt.title(f'Distribución: {col}')
    plt.show()
```

## Checklist de instalación

- [ ] NumPy instalado
- [ ] pandas instalado
- [ ] matplotlib instalado
- [ ] seaborn instalado
- [ ] scipy instalado
- [ ] ydata-profiling instalado
- [ ] missingno instalado
- [ ] sweetviz instalado (opcional)
- [ ] dtale instalado (opcional)

## Verificar instalación

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ydata_profiling import ProfileReport
import missingno as msno

print("✅ Todas las librerías cargadas correctamente")
```

---

**Autoría:** Anaïs Rodríguez Villanueva  
**Siguiente:** Carga y exploración inicial de datos.
