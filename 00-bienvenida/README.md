# 👋 Bienvenida a Curie: El Arte del EDA

**Anaïs Rodríguez Villanueva**

## ¿Qué aprenderás aquí?

Este proyecto te convierte en un **explorador de datos profesional**. No solo aprenderás herramientas, sino la **metodología completa** para investigar cualquier dataset.

## ¿Qué es EDA?

**EDA (Exploratory Data Analysis)** fue popularizado por John Tukey en 1977. Su filosofía:

> **"Los datos deben ser torturados hasta que confiesen."**

Significa: Explora sin prejuicios hasta entender profundamente.

### EDA no es...

❌ **Solo estadísticos:** Media, mediana, std no son suficientes  
❌ **Solo gráficos:** Visualizar sin interpretar no sirve  
❌ **Un paso único:** Es iterativo, vuelves atrás constantemente  
❌ **Automatizable 100%:** Requiere intuición humana  

### EDA es...

✅ **Detective work:** Buscar pistas, seguir rastros  
✅ **Arte + ciencia:** Combina rigor estadístico con intuición  
✅ **Conversación con datos:** Haces preguntas, los datos responden  
✅ **Fundamental:** 80% del trabajo de un analista es EDA  

## ¿Por qué es tan importante?

### 1. Evita errores costosos

**Caso real:** Una empresa implementó un modelo de predicción sin EDA. Resultado: El modelo predecía valores negativos (imposibles en su contexto). Un EDA habría detectado distribuciones anómalas.

### 2. Descubre oportunidades ocultas

**Caso real:** EDA reveló que clientes de cierta región compraban 3x más los viernes. Acción: Promociones geo-localizadas los viernes → +40% ventas.

### 3. Valida supuestos

**Caso real:** Equipo asumía que "más tiempo en web = más compras". EDA mostró lo contrario: Mucho tiempo = confusión. Acción: Simplificar navegación.

## Fases del EDA

### Fase 1: Pregunta inicial
"Quiero entender por qué las ventas bajaron en Q3"

### Fase 2: Carga y exploración superficial
```python
df = pd.read_csv('ventas.csv')
df.head()
df.info()
df.describe()
```

**Primeras observaciones:**
- 10,000 registros, 15 columnas
- Hay valores nulos en 'descuento' (20%)
- 'precio' tiene valores negativos (error)

### Fase 3: Limpieza
```python
# Nulos
df['descuento'].fillna(0, inplace=True)

# Outliers
df = df[df['precio'] > 0]

# Duplicados
df.drop_duplicates(inplace=True)
```

### Fase 4: Análisis univariado
Variable por variable:
```python
# Distribución de precios
sns.histplot(df['precio'])
# → Descubrimiento: Mayoría cuesta $10-50
```

### Fase 5: Análisis bivariado
Relaciones entre pares:
```python
# Precio vs Cantidad
sns.scatterplot(x='precio', y='cantidad', data=df)
# → Descubrimiento: Correlación negativa fuerte
```

### Fase 6: Insights y acción
"Las ventas bajaron porque subimos precios 15% en Q3. Clientes son sensibles al precio. Recomendación: Promociones estratégicas."

## Mentalidad del explorador

### Haz preguntas obsesivamente

- ¿Por qué este valor es tan alto?
- ¿Qué pasó en esta fecha con pico de ventas?
- ¿Por qué esta categoría tiene tantos nulos?
- ¿Estos dos grupos son realmente diferentes?

### Sé escéptico

- ¿Este patrón es real o casualidad?
- ¿Hay suficientes datos para esta conclusión?
- ¿Estoy sesgando la interpretación?

### Visualiza TODO

Antes de calcular la media, **mira la distribución**. Un outlier puede distorsionar todo.

**Ejemplo:**

```python
# ❌ Malo: Solo calcular
print(f"Media: {df['salario'].mean()}")  # $75,000

# ✅ Bueno: Visualizar primero
sns.boxplot(df['salario'])
plt.show()
# → Descubres que hay un CEO con $2M (outlier extremo)
# → Mediana es más representativa: $45,000
```

### Itera sin miedo

EDA no es lineal:
1. Exploras edad → Descubres patrón en jóvenes
2. Vuelves a filtrar jóvenes → Analizas su comportamiento
3. Comparas con adultos → Validas diferencias
4. Segmentas por edad → Nuevas preguntas surgen

## Herramientas del EDA

### pandas: Tu navaja suiza

```python
df.head()                 # Primeras filas
df.info()                 # Tipos de datos, nulos
df.describe()             # Estadísticos
df['col'].value_counts()  # Frecuencias
df.groupby('A')['B'].mean()  # Agregaciones
```

### Visualización: Tus ojos

```python
sns.histplot()    # Distribuciones
sns.boxplot()     # Outliers
sns.scatterplot() # Relaciones
sns.heatmap()     # Correlaciones
sns.pairplot()    # Múltiples variables
```

### Automatización: Primeras impresiones

```python
import pandas_profiling
profile = df.profile_report()
profile.to_file("reporte.html")
```

**Ventaja:** Reporte completo en segundos  
**Desventaja:** No reemplaza el análisis manual profundo

## Diferencias clave

### EDA vs Análisis confirmatorio

| EDA | Confirmatorio |
|-----|---------------|
| Explorar sin hipótesis previa | Validar hipótesis específica |
| Generar preguntas | Responder pregunta definida |
| Flexible, iterativo | Estructurado, lineal |
| Muchas visualizaciones | Pocas, específicas |

**Ambos son necesarios.** EDA primero, luego confirmas con estadística inferencial.

### EDA vs Data Cleaning

| EDA | Limpieza |
|-----|----------|
| Entender patrones | Corregir errores |
| "¿Por qué hay nulos?" | "Eliminar/imputar nulos" |
| Exploración | Preparación |

**Están conectados.** Limpias → Exploras → Descubres más problemas → Limpias más.

## Tu primer EDA (5 minutos)

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Cargar
df = pd.read_csv('datos.csv')

# 2. Explorar rápido
print(df.head())
print(df.info())
print(df.describe())

# 3. Visualizar variable clave
sns.histplot(df['precio'])
plt.title('Distribución de Precios')
plt.show()

# 4. Primera pregunta
print("¿Qué rango de precios domina?")
print(f"50% están entre ${df['precio'].quantile(0.25)} y ${df['precio'].quantile(0.75)}")
```

## Errores comunes a evitar

### 1. No explorar antes de limpiar

```python
# ❌ Malo
df.dropna(inplace=True)  # Eliminas sin saber por qué hay nulos

# ✅ Bueno
print(df.isnull().sum())  # Cuántos nulos hay
msno.matrix(df)           # Patrón de nulos
# → Decides: ¿eliminar, imputar, o dejar?
```

### 2. Confiar ciegamente en correlación

```python
# Correlación 0.9 entre helados y ahogamientos
# → NO significa causalidad
# → Ambos suben en verano (variable oculta)
```

### 3. Ignorar el contexto

**Dato:** Ventas subieron 200% en enero  
**Sin contexto:** ¡Éxito!  
**Con contexto:** Enero anterior hubo huelga, ventas fueron 0. El 200% no es real crecimiento.

### 4. Analizar sin objetivo

EDA sin pregunta de negocio es turismo de datos. Define:
- ¿Qué problema resolver?
- ¿Qué decisión tomar con los insights?

## Estructura de este proyecto

```
00-bienvenida/       ← Estás aquí
01-contexto/         → Herramientas técnicas
02-carga-datos/      → Leer CSV, Excel, JSON
03-limpieza/         → Nulos, duplicados, outliers
04-univariado/       → Variable por variable
05-bivariado/        → Relaciones entre pares
06-visualizacion/    → Gráficos avanzados
07-practica/         → EDA completo de e-commerce
08-bitacora/         → Tu diario de descubrimientos
```

## Mentalidad final

> **"EDA es el arte de hacer preguntas inteligentes y dejar que los datos te sorprendan con sus respuestas."**

No es solo código. Es curiosidad disciplinada.

**Estás listo para convertirte en detective de datos.**

---

**Siguiente:** Ve a `01-contexto/` para configurar herramientas avanzadas de EDA.
