"""
EJERCICIO 1: Web Scraping Básico
=================================
Objetivo: Extraer tabla de Wikipedia con BeautifulSoup

Duración: 45 minutos
Nivel: Básico-Intermedio
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

print("="*60)
print("EJERCICIO 1: Web Scraping con Beautiful Soup")
print("="*60)

# =============================================================================
# PASO 1: DESCARGAR LA PÁGINA
# =============================================================================

url = 'https://es.wikipedia.org/wiki/Anexo:Capitales_de_Estado'

print(f"\n🌐 Descargando página...")
print(f"URL: {url}")

try:
    # Headers para simular un navegador
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/124.0.0.0 Safari/537.36'
        )
    }
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Lanza excepción si hay error
    
    print(f"✅ Página descargada exitosamente")
    print(f"   Tamaño: {len(response.text)} caracteres")
    
    # =============================================================================
    # PASO 2: PARSEAR HTML
    # =============================================================================
    
    print(f"\n🔍 Parseando HTML...")
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"✅ HTML parseado correctamente")
    
    # =============================================================================
    # PASO 3: ENCONTRAR LA TABLA
    # =============================================================================
    
    print(f"\n📊 Buscando tablas...")
    
    # Wikipedia puede usar clases distintas segun la pagina/version.
    # Intentamos primero clases comunes y, si no, usamos la primera tabla util.
    tablas = soup.find_all('table', class_=['wikitable', 'sortable'])
    if not tablas:
        tablas = soup.find_all('table')

    print(f"✅ Se encontraron {len(tablas)} tablas candidatas")

    if not tablas:
        raise ValueError("No se encontraron tablas en la pagina")

    # Seleccionar la primera tabla candidata
    tabla = tablas[0]
    print(f"   Tabla seleccionada: {tabla.get('class')}")
    
    # =============================================================================
    # PASO 4: EXTRAER CABECERAS
    # =============================================================================
    
    print(f"\n📋 Extrayendo cabeceras...")
    
    cabeceras = []

    # La primera fila puede venir vacia o con iconos de ordenacion.
    # Buscamos la primera fila que tenga 4 columnas de texto legibles.
    for fila in tabla.find_all('tr'):
        posibles = [c.get_text(' ', strip=True).split('[')[0].strip() for c in fila.find_all(['td', 'th'])]
        if len(posibles) == 4 and all(posibles):
            cabeceras = posibles
            break

    if not cabeceras:
        cabeceras = ['Entidad', 'Capital', 'Continente', 'Habitantes']
    
    print(f"✅ Cabeceras encontradas:")
    for i, cab in enumerate(cabeceras, 1):
        print(f"   {i}. {cab}")
    
    # =============================================================================
    # PASO 5: EXTRAER DATOS
    # =============================================================================
    
    print(f"\n💾 Extrayendo filas de datos...")
    
    filas_datos = []
    filas = tabla.find_all('tr')
    
    for i, fila in enumerate(filas, 1):
        celdas = fila.find_all(['td', 'th'])
        
        if len(celdas) == 4:
            fila_datos = []
            for celda in celdas:
                texto = celda.get_text(' ', strip=True)
                # Limpiar referencias de Wikipedia [1], [2], etc.
                texto = texto.split('[')[0].strip()
                fila_datos.append(texto)

            # Evitar meter la fila de cabeceras como dato
            if fila_datos != cabeceras:
                filas_datos.append(fila_datos)
        
        # Progreso cada 50 filas
        if i % 50 == 0:
            print(f"   Procesadas {i} filas...")
    
    print(f"✅ Total filas extraídas: {len(filas_datos)}")
    
    # =============================================================================
    # PASO 6: CREAR DATAFRAME
    # =============================================================================
    
    print(f"\n📊 Creando DataFrame...")
    
    df = pd.DataFrame(filas_datos, columns=cabeceras)
    
    print(f"✅ DataFrame creado:")
    print(f"   Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas")
    
    # =============================================================================
    # PASO 7: EXPLORAR DATOS
    # =============================================================================
    
    print(f"\n" + "="*60)
    print("EXPLORACIÓN DE DATOS EXTRAÍDOS")
    print("="*60)
    
    print(f"\n🔍 Primeras 10 filas:")
    print(df.head(10))
    
    print(f"\n📊 Información del DataFrame:")
    print(df.info())
    
    print(f"\n🌍 Países únicos extraídos: {df.iloc[:, 0].nunique()}")
    
    # =============================================================================
    # PASO 8: GUARDAR RESULTADOS
    # =============================================================================
    
    print(f"\n💾 Guardando resultados...")
    
    # Guardar CSV
    df.to_csv('capitales_paises.csv', index=False, encoding='utf-8')
    print(f"✅ CSV guardado: capitales_paises.csv")
    
    # Guardar Excel (opcional si openpyxl está disponible)
    try:
        df.to_excel('capitales_paises.xlsx', index=False)
        print(f"✅ Excel guardado: capitales_paises.xlsx")
    except ImportError:
        print("⚠️ No se pudo guardar Excel: falta 'openpyxl' en el entorno")
        print("   Instala con: pip install openpyxl")
    
    # Guardar HTML
    df.head(50).to_html('capitales_top50.html', index=False)
    print(f"✅ HTML guardado: capitales_top50.html (primeras 50)")
    
    print(f"\n✅ ¡Ejercicio completado exitosamente!")

except requests.RequestException as e:
    print(f"\n❌ Error de conexión: {e}")
    print("   Verifica tu conexión a internet")

except Exception as e:
    print(f"\n❌ Error inesperado: {e}")
    print("   La estructura de la página puede haber cambiado")

# =============================================================================
# DESAFÍO EXTRA
# =============================================================================

print(f"\n" + "="*60)
print("🎯 DESAFÍO EXTRA")
print("="*60)
print("""
1. Extrae datos de otra tabla de Wikipedia (ej: países por área)
2. Limpia los datos numéricos (quitar comas, convertir a int/float)
3. Crea un análisis comparativo entre 2 tablas diferentes
4. Genera un reporte HTML con los hallazgos más interesantes

Pistas:
- Usa .replace(',', '') para limpiar números
- Usa pd.to_numeric() para convertir a numérico
- Usa pd.merge() para combinar DataFrames
""")

print(f"\n✅ Fin del ejercicio")
