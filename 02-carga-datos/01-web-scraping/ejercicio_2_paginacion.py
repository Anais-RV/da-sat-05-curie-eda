"""
EJERCICIO 2: Scraping con Paginacion
====================================
Objetivo: recorrer varias paginas y consolidar los resultados

Duracion: 45 minutos
Nivel: Intermedio
"""

import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
MAX_PAGINAS = 3

print("=" * 60)
print("EJERCICIO 2: Scraping de multiples paginas")
print("=" * 60)

registros = []

for pagina in range(1, MAX_PAGINAS + 1):
    url = BASE_URL.format(pagina)
    print(f"\nProcesando pagina {pagina}: {url}")

    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
    except requests.RequestException as err:
        print(f"No se pudo descargar la pagina {pagina}: {err}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    libros = soup.select("article.product_pod")

    for libro in libros:
        titulo = libro.h3.a.get("title", "").strip()
        precio = libro.select_one("p.price_color").get_text(strip=True)
        stock = libro.select_one("p.instock.availability").get_text(" ", strip=True)

        registros.append(
            {
                "pagina": pagina,
                "titulo": titulo,
                "precio_raw": precio,
                "stock": stock,
            }
        )

    print(f"   Libros extraidos en esta pagina: {len(libros)}")
    time.sleep(1)

if not registros:
    print("\nNo se extrajeron registros.")
else:
    df = pd.DataFrame(registros)
    df["precio"] = (
        df["precio_raw"]
        .str.replace("£", "", regex=False)
        .str.replace("Â", "", regex=False)
        .astype(float)
    )

    print("\nVista previa:")
    print(df.head())

    print("\nResumen:")
    print(df["precio"].describe())

    df.to_csv("libros_paginacion.csv", index=False, encoding="utf-8")
    print("\nCSV generado: libros_paginacion.csv")

print("\nFin del ejercicio 2")
