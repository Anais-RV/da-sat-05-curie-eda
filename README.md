# 🔬 Curie: Análisis Exploratorio de Datos (EDA) Completo

**Proyecto 5 - Módulo 2: Análisis con Python**

---

**Marie Curie exploró lo invisible: la radiactividad, esa energía oculta en la materia. El análisis exploratorio avanzado es así: bucear en profundidades, detectar señales débiles, intuir relaciones que no saltan a la vista. Requiere rigor, paciencia y esa valentía científica que Marie encarnó. Aquí los datos revelan sus secretos más íntimos.**

---

Este satélite integra todo lo aprendido en un **Análisis Exploratorio de Datos (EDA)** completo y profesional. Aplicarás Python, estadística, visualización y pensamiento analítico para entender datasets del mundo real.

## 🎯 Objetivos del proyecto

Al completar este satélite, serás capaz de:

- Realizar un EDA completo de inicio a fin siguiendo metodología profesional
- Cargar, explorar y limpiar datos de múltiples fuentes (CSV, Excel, JSON)
- Identificar y manejar valores nulos, duplicados y outliers
- Analizar variables individualmente (univariado) y en conjunto (bivariado/multivariado)
- Crear visualizaciones avanzadas que comuniquen insights
- Formular y validar hipótesis sobre los datos
- Documentar hallazgos de forma clara y accionable

## 📚 Contenidos

| Carpeta | Tema | Descripción |
|---------|------|-------------|
| **00-bienvenida** | Orientación | Qué es EDA y por qué es fundamental |
| **01-contexto** | Herramientas | pandas, pandas-profiling, missingno, sweetviz |
| **02-carga-datos** | Ingesta | Leer CSV/Excel/JSON, encoding, tipos de datos |
| **03-limpieza** | Preparación | Valores nulos, duplicados, outliers, transformaciones |
| **04-analisis-univariado** | Individual | Distribución, estadísticos, patrones de cada variable |
| **05-analisis-bivariado** | Relaciones | Correlaciones, crosstabs, scatter plots, segmentación |
| **06-visualizacion-avanzada** | Storytelling | Dashboards, pairplots, heatmaps, visualización narrativa |
| **07-practica-guiada** | Aplicación | EDA completo de dataset de e-commerce |
| **08-bitacora** | Reflexión | Tu diario de descubrimientos |

## 🛠️ Herramientas principales

### Librerías esenciales

```python
import pandas as pd                # Manipulación de datos
import numpy as np                 # Operaciones numéricas
import matplotlib.pyplot as plt    # Visualización base
import seaborn as sns              # Visualización estadística
from scipy import stats            # Estadística avanzada
```

### Herramientas auxiliares

```python
import pandas_profiling            # Reporte automático de EDA
import missingno as msno           # Visualización de valores nulos
import sweetviz as sv              # EDA visual automatizado
```

## 📊 Dataset del proyecto

Usaremos un dataset de e-commerce típico de proyecto real.

### Opción recomendada (Kaggle)

- **Dataset:** Brazilian E-Commerce Public Dataset by Olist
- **Enlace:** https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Tablas principales que puedes analizar:

- **Clientes:** ubicación y perfil de compra
- **Órdenes:** fechas, estado y ciclo de compra
- **Items/Productos:** categorías, precio y flete
- **Pagos:** método y valor pagado
- **Reseñas:** satisfacción del cliente

### Opción alternativa (si no puedes descargar Kaggle)

En la carpeta de práctica guiada tienes una versión simulada para hacer el flujo EDA completo sin bloquearte.

**Objetivo:** Entender patrones de compra, segmentar clientes y encontrar oportunidades de negocio.

## 🎓 Prerrequisitos

- **Atlas:** Análisis exploratorio con Google Sheets
- **Kepler:** Python básico (variables, listas, funciones)
- **Galileo:** SQL y bases de datos
- **Newton:** Estadística descriptiva e inferencial

Este proyecto **integra todo**. Es el momento de aplicar lo aprendido.

## 🚀 Metodología EDA

El EDA profesional sigue una estructura:

### 1. Definir objetivo
¿Qué quieres entender? ¿Qué preguntas responder?

### 2. Cargar y explorar
Primeras filas, dimensiones, tipos de datos, valores únicos

### 3. Limpiar
Nulos, duplicados, outliers, inconsistencias

### 4. Analizar
- **Univariado:** Variable por variable
- **Bivariado:** Relaciones entre pares
- **Multivariado:** Patrones complejos

### 5. Visualizar
Gráficos que comunican hallazgos

### 6. Documentar
Insights, hipótesis, recomendaciones

## 💡 ¿Qué es EDA?

**EDA (Exploratory Data Analysis)** es el proceso de investigar datos para:
- Descubrir patrones ocultos
- Detectar anomalías
- Validar supuestos
- Formular hipótesis

**No es:**
- Solo hacer gráficos bonitos
- Aplicar modelos sin entender los datos
- Ignorar el contexto de negocio

**Es:**
- Hacer preguntas inteligentes
- Combinar estadística + visualización + intuición
- Iterar hasta entender profundamente los datos

## 🎯 Preguntas que responderás

En el proyecto de e-commerce:

### Clientes
- ¿Cuál es el perfil típico del cliente?
- ¿Qué segmentos existen (edad, género, ubicación)?
- ¿Cuánto gastan en promedio?

### Productos
- ¿Qué categorías venden más?
- ¿Hay relación entre precio y cantidad vendida?
- ¿Qué productos tienen mayor margen?

### Comportamiento
- ¿Qué días/horas hay más ventas?
- ¿Cuál es la tasa de conversión?
- ¿Por qué abandonan el carrito?

### Oportunidades
- ¿Dónde enfocar marketing?
- ¿Qué productos promover juntos (cross-selling)?
- ¿Qué clientes están en riesgo de abandono?

## 📖 Metodología de trabajo

1. **Lee el concepto** en cada carpeta
2. **Ejecuta los ejemplos** paso a paso
3. **Experimenta** modificando código
4. **Aplica al proyecto** de e-commerce
5. **Documenta** hallazgos en la bitácora

## 🔍 Flujo típico de EDA

```python
# 1. Cargar
df = pd.read_csv('ruta/a/tu/dataset.csv')

# 2. Explorar
df.head()
df.info()
df.describe()

# 3. Limpiar
df.dropna()
df.drop_duplicates()

# 4. Analizar
df['columna'].value_counts()
df.groupby('categoria')['precio'].mean()

# 5. Visualizar
sns.histplot(df['precio'])
plt.show()

# 6. Iterar
# Vuelve al paso 4 con nuevas preguntas
```

## 🎯 Competencias que desarrollarás

### Técnicas
- Dominio de pandas para manipulación de datos
- Estadística aplicada en contexto real
- Visualización efectiva con matplotlib/seaborn
- Automatización de reportes con pandas-profiling

### Analíticas
- Formular preguntas relevantes
- Detectar patrones y anomalías
- Validar hipótesis con datos
- Priorizar hallazgos según impacto

### Comunicación
- Storytelling con datos
- Visualizaciones que persuaden
- Documentación clara de insights
- Recomendaciones accionables

## 🔗 Conexiones con otros satélites

- **← Atlas:** Exploraste datos en Google Sheets (ahora con Python)
- **← Kepler:** Usarás funciones, loops, listas
- **← Galileo:** Entiendes relaciones entre tablas
- **← Newton:** Aplicarás estadística descriptiva e inferencial
- **→ Faraday (Reporting):** Comunicarás hallazgos con dashboards
- **→ Darwin (Clustering):** Segmentarás clientes con ML
- **→ Turing (Clasificación):** Predecirás comportamiento

## 📅 Duración estimada

**3-4 semanas** (5-7 horas/semana)

- Semana 1: Carga, limpieza, análisis univariado
- Semana 2: Análisis bivariado y multivariado
- Semana 3: Visualización avanzada
- Semana 4: Proyecto completo y documentación

## 📌 Consejos para el éxito

✅ **Haz preguntas constantemente:** "¿Por qué este valor es tan alto?"  
✅ **Visualiza antes de calcular:** Los gráficos revelan lo invisible  
✅ **Documenta todo:** Tu yo futuro te lo agradecerá  
✅ **Itera:** EDA no es lineal, es un proceso cíclico  
✅ **Conecta con el negocio:** Los insights sin acción no sirven  

❌ **No asumas sin validar:** Verifica tus hipótesis con datos  
❌ **No ignores outliers:** Pueden ser errores o hallazgos importantes  
❌ **No te quedes en lo superficial:** Profundiza en patrones interesantes  

## 🌟 ¿Qué hace un buen EDA?

### Malo 😕
- Lista de gráficos sin interpretación
- Estadísticos sin contexto
- Ignorar valores nulos y outliers
- No formular hipótesis

### Bueno 😊
- Gráficos + interpretación
- Estadísticos contextualizados
- Manejo explícito de datos problemáticos
- Hipótesis validadas

### Excelente 🌟
- Historia cohesiva con datos
- Insights accionables
- Segmentación inteligente
- Recomendaciones priorizadas
- Código reproducible

## 🎬 ¿Listo para explorar?

El EDA es donde los datos cuentan su historia. Tu trabajo es escuchar atentamente, hacer las preguntas correctas y comunicar lo que descubres.

**"Los datos son como personas: habla con ellos lo suficiente y te contarán sus secretos."**

Comienza por **00-bienvenida/** para entender la filosofía del EDA exploratorio.

---

**Autoría:** Anaïs Rodríguez Villanueva  
**Bootcamp:** Data Analyst - Módulo 2  
**Proyecto:** 5 de 10
