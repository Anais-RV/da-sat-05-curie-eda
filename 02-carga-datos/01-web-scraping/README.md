# 🕸️ Web Scraping para Análisis de Datos

> **Nivel 3: Extracción de datos web**  
> Duración presencial: 2.5 horas  
> Trabajo autónomo: 3 horas  
> Objetivo: Extraer datos estructurados de páginas web

---

## 🧭 Ruta de sesión (numeración de clase)

Para evitar confusiones, en esta sesión usamos esta numeración fija:

1. **Contexto y casos de uso** (por qué scraping)
2. **Setup técnico** (requests, BeautifulSoup, parser)
3. **Flujo base de scraping** (descargar, parsear, buscar, extraer)
4. **Extracción y limpieza** (texto, atributos, normalización)
5. **Ética y límites** (robots.txt, términos, ritmo de requests)
6. **Práctica guiada**
    - **6.1** Básico: Wikipedia
    - **6.2** Paginación: múltiples páginas
    - **6.3** Mini-proyecto: scraping + EDA

> Nota: Los `PASO 1..5` dentro de los snippets son pasos de código, no el orden global de la clase.

---

## ¿Por qué Web Scraping?

Muchos datos valiosos están en páginas web, no en archivos descargables:
- Precios de productos en e-commerce
- Resultados deportivos
- Datos financieros
- Listados inmobiliarios  
- Noticias y artículos
- Datos públicos gubernamentales

**Web scraping** = Extraer automáticamente datos de páginas web.

---

## Herramientas necesarias

```bash
# Instalar librerías
pip install requests beautifulsoup4 lxml
```

### ¿Qué hace cada una?

| Librería | Función |
|----------|---------|
| `requests` | Descarga el HTML de la página |
| `beautifulsoup4` | Parsea y navega el HTML |
| `lxml` | Parser rápido para HTML/XML |

---

## Anatomía de un web scraping

```python
import requests
from bs4 import BeautifulSoup

# PASO 1: Descargar la página
url = 'https://ejemplo.com/datos'
response = requests.get(url)
html = response.text

# PASO 2: Parsear el HTML
soup = BeautifulSoup(html, 'html.parser')

# PASO 3: Encontrar elementos
elemento = soup.find('table', class_='datos')

# PASO 4: Extraer datos
datos = elemento.text

# PASO 5: Estructurar en DataFrame
df = pd.DataFrame(datos)
```

---

## Navegación del DOM con BeautifulSoup

### Recordatorio: El DOM es un árbol

```html
<body>
  └── <div class="contenedor">
      ├── <h1>Título</h1>
      └── <table id="ventas">
          ├── <tr>
          │   ├── <th>Producto</th>
          │   └── <th>Precio</th>
          └── <tr>
              ├── <td>Laptop</td>
              └── <td>1000</td>
```

### Métodos de búsqueda

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')

# 1. Buscar UN elemento (el primero que encuentre)
titulo = soup.find('h1')
tabla = soup.find('table', id='ventas')
div = soup.find('div', class_='contenedor')

# 2. Buscar TODOS los elementos
filas = soup.find_all('tr')
enlaces = soup.find_all('a')
parrafos = soup.find_all('p', class_='texto')

# 3. Buscar por atributo
elemento = soup.find(attrs={'data-id': '123'})

# 4. Buscar por texto contenido
elemento = soup.find(string='Buscar esto')
```

---

## Selectores CSS (avanzado)

```python
# select() usa selectores CSS (como en CSS)
tabla = soup.select_one('table.datos')  # Un elemento
filas = soup.select('table tr')         # Todos los elementos

# Ejemplos de selectores:
soup.select('.clase')           # Por clase
soup.select('#id')              # Por ID
soup.select('div p')            # p dentro de div
soup.select('div > p')          # p hijo directo de div
soup.select('tr:nth-child(2)')  # Segunda fila
```

---

## Extraer información de elementos

```python
# Obtener texto
elemento.text        # Todo el texto
elemento.get_text()  # Alternativa

# Obtener atributos
enlace = soup.find('a')
url = enlace['href']           # Atributo href
titulo = enlace.get('title')   # Método get (más seguro)

# Atributos comunes
img = soup.find('img')
src = img['src']
alt = img['alt']
```

---

## Ejemplo completo: Extraer tabla

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Descargar página
url = 'https://es.wikipedia.org/wiki/Anexo:Capitales_de_Estado'
headers = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/124.0.0.0 Safari/537.36'
    )
}
response = requests.get(url, headers=headers, timeout=20)
response.raise_for_status()
html = response.text

# 2. Parsear HTML
soup = BeautifulSoup(html, 'html.parser')

# 3. Encontrar la tabla (Wikipedia puede usar 'wikitable' o 'sortable')
tabla = soup.find('table', class_=['wikitable', 'sortable'])
if tabla is None:
    tabla = soup.find('table')

# 4. Extraer cabeceras
cabeceras = []
for th in tabla.find('tr').find_all('th'):
    cabeceras.append(th.text.strip())

# 5. Extraer filas de datos
filas_datos = []
for fila in tabla.find_all('tr')[1:]:  # Saltar primera fila (cabeceras)
    celdas = fila.find_all(['td', 'th'])
    fila_datos = [celda.text.strip() for celda in celdas]
    filas_datos.append(fila_datos)

# 6. Crear DataFrame
df = pd.DataFrame(filas_datos, columns=cabeceras)
print(df.head())
```

---

## Limpieza de datos extraídos

Los datos web suelen venir "sucios":

```python
# Texto con espacios y saltos de línea
texto = elemento.text
texto_limpio = texto.strip()         # Quitar espacios
texto_limpio = texto.replace('\n', '') # Quitar saltos de línea

# Múltiples espacios
texto = '  Hola    mundo  '
texto_limpio = ' '.join(texto.split())  # 'Hola mundo'

# Símbolos molestos
precio = '$1,234.56'
precio_num = precio.replace('$', '').replace(',', '')
precio_float = float(precio_num)  # 1234.56
```

---

## Headers y User-Agent

Algunas webs bloquean scrapers. Solución: añadir headers:

```python
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

response = requests.get(url, headers=headers)
```

---

## Ética del Web Scraping

### ✅ Buenas prácticas:

1. **Revisa el archivo robots.txt** → `https://ejemplo.com/robots.txt`
2. **Lee los términos de servicio** → Algunos sitios prohíben scraping
3. **No sobrecargues el servidor** → Añade pausas entre requests
4. **Respeta la propiedad intelectual** → Datos públicos ≠ libre uso comercial

```python
import time

# Añadir pausa entre requests
for url in urls:
    response = requests.get(url)
    # Procesar...
    time.sleep(2)  # Esperar 2 segundos
```

### ❌ Evita:

- Scrapear datos personales sin consentimiento
- Usar datos scrapeados para fines ilegales
- Hacer miles de requests por segundo
- Ignorar avisos legales del sitio

---

## 🎯 Bloque práctico 6.1: Scraping básico (45 min)

**Ver archivo:** `ejercicio_1_scraping_basico.py`

**Versión guiada en notebook:** `ejercicio_1_scraping_basico.ipynb`

Extraerás datos de una tabla de Wikipedia usando BeautifulSoup.

---

## 🎯 Bloque práctico 6.2: Múltiples páginas (45 min)

**Ver archivo:** `ejercicio_2_paginacion.py`

**Versión guiada en notebook:** `ejercicio_2_paginacion.ipynb`

Aprenderás a extraer datos de múltiples páginas (paginación).

---

## 🎯 Bloque práctico 6.3: Proyecto real (60 min)

**Ver archivo:** `ejercicio_3_proyecto_real.py`

**Versión guiada en notebook:** `ejercicio_3_proyecto_real.ipynb`

Proyecto completo: extraer datos, limpiar, analizar y visualizar.

---

## Debugging: ¿Qué hacer si falla?

### 1. Ver el HTML descargado

```python
print(response.text[:1000])  # Primeros 1000 caracteres
```

### 2. Verificar que encontró el elemento

```python
elemento = soup.find('table')
if elemento is None:
    print("⚠️ No se encontró la tabla")
else:
    print("✅ Tabla encontrada")
```

### 3. Inspeccionar en el navegador

1. Abre la página en Chrome/Firefox
2. Click derecho → Inspeccionar
3. Busca el elemento que quieres extraer
4. Copia el selector CSS o la clase

### 4. Probar selectores

```python
# Probar diferentes métodos
tabla = soup.find('table', class_='datos')
tabla = soup.find('table', id='ventas')
tabla = soup.select_one('table.datos')
```

---

## Limitaciones del web scraping simple

### No funciona bien con:

1. **JavaScript dinámico** → Páginas que cargan contenido con JS
   - **Solución:** Selenium (lo verás más adelante)
   
2. **APIs protegidas** → Requieren autenticación
   - **Solución:** Usar la API oficial

3. **CAPTCHAs** → Protecciones anti-bots
   - **Solución:** No hay solución simple (¡y está bien!)

4. **Contenido que cambia rápido** → Estructura HTML inestable
   - **Solución:** Hacer el scraper más robusto con try/except

---

## Alternativa: APIs oficiales

Antes de hacer scraping, **verifica si existe una API oficial**:

```python
# En vez de scrapear una web de clima...
import requests

# ...usa su API:
api_key = 'tu_api_key'
url = f'https://api.openweathermap.org/data/2.5/weather?q=Madrid&appid={api_key}'
response = requests.get(url)
datos = response.json()  # Datos estructurados directamente
```

**APIs son mejores que scraping:**
- Datos estructurados (JSON)
- Más rápidas
- Legales y éticas
- No se rompen si cambia el diseño web

---

## 📚 Recursos para trabajo autónomo (3 horas)

### Videos:
1. **"Web Scraping with Python - Beautiful Soup"** - Corey Schafer [1h]
2. **"Real Python Web Scraping Tutorial"** - Real Python [45 min]

### Lectura:
1. **Beautiful Soup Documentation** - [crummy.com/software/BeautifulSoup/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
2. **Real Python - Web Scraping Guide** - [realpython.com/beautiful-soup-web-scraper-python/](https://realpython.com/beautiful-soup-web-scraper-python/)

### Práctica:
1. Scrapea 3 páginas de Wikipedia diferentes
2. Extrae datos de un sitio de noticias
3. Crea un dataset desde web de productos

---

## ✅ Checklist de competencias

Al terminar esta sesión, deberías poder:

- [ ] Descargar HTML de una página con `requests`
- [ ] Parsear HTML con BeautifulSoup
- [ ] Navegar el DOM con `find()` y `find_all()`
- [ ] Extraer texto y atributos de elementos
- [ ] Limpiar datos extraídos
- [ ] Estructurar datos en DataFrame
- [ ] Manejar errores comunes (elemento no encontrado)
- [ ] Aplicar buenas prácticas éticas
- [ ] Distinguir cuándo usar scraping vs APIs

---

## 🔜 Próximos pasos

En **Satélite 6 (Faraday - Reporting)** aprenderás:
- CSS para **personalizar dashboards**
- HTML/CSS integrado en **Streamlit y Dash**
- Reportes HTML profesionales automáticos

---

## 💡 Tips profesionales

### Tip 1: Guarda el HTML localmente

```python
# Mientras desarrollas, guarda el HTML
html = response.text
with open('pagina.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Luego trabaja con el archivo local
with open('pagina.html', 'r', encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')
```

### Tip 2: Usa try/except

```python
try:
    tabla = soup.find('table')
    datos = tabla.find_all('tr')
except AttributeError:
    print("⚠️ No se encontró la tabla")
    datos = []
```

### Tip 3: Verifica antes de extraer

```python
elemento = soup.find('div', class_='datos')
if elemento:
    texto = elemento.text
else:
    texto = "No disponible"
```

---

**Autoría:** Anaïs Rodríguez Villanueva  
**Satélite 5 - Curie: EDA Completo**  
**Bootcamp Data Analyst - 600h**

🎯 **Siguiente:** CSS para dashboards en Satélite 6
