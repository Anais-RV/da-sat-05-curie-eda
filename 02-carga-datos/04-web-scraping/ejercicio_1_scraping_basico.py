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

url = 'https://es.wikipedia.org/wiki/Anexo:Capitales_de_pa%C3%ADses'

print(f"\n🌐 Descargando página...")
print(f"URL: {url}")

try:
    # Headers para simular un navegador
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
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
    
    # Buscar todas las tablas de clase 'wikitable'
    tablas = soup.find_all('table', class_='wikitable')
    print(f"✅ Se encontraron {len(tablas)} tablas")
    
    # Seleccionar la primera tabla
    tabla = tablas[0]
    print(f"   Tabla seleccionada: {tabla.get('class')}")
    
    # =============================================================================
    # PASO 4: EXTRAER CABECERAS
    # =============================================================================
    
    print(f"\n📋 Extrayendo cabeceras...")
    
    cabeceras = []
    primera_fila = tabla.find('tr')
    for th in primera_fila.find_all('th'):
        cabeceras.append(th.text.strip())
    
    print(f"✅ Cabeceras encontradas:")
    for i, cab in enumerate(cabeceras, 1):
        print(f"   {i}. {cab}")
    
    # =============================================================================
    # PASO 5: EXTRAER DATOS
    # =============================================================================
    
    print(f"\n💾 Extrayendo filas de datos...")
    
    filas_datos = []
    filas = tabla.find_all('tr')[1:]  # Saltar cabecera
    
    for i, fila in enumerate(filas, 1):
        celdas = fila.find_all(['td', 'th'])
        
        if len(celdas) > 0:
            fila_datos = []
            for celda in celdas:
                texto = celda.text.strip()
                # Limpiar referencias de Wikipedia [1], [2], etc.
                texto = texto.split('[')[0]
                fila_datos.append(texto)
            
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
    
    # Guardar Excel
    df.to_excel('capitales_paises.xlsx', index=False)
    print(f"✅ Excel guardado: capitales_paises.xlsx")
    
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
