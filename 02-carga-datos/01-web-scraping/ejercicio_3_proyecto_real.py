"""
EJERCICIO 3: Mini proyecto de scraping + EDA
============================================
Objetivo: extraer datos, limpiarlos y sacar insights basicos

Duracion: 60 minutos
Nivel: Intermedio-Avanzado
"""

import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
MAX_PAGINAS = 5

print("=" * 70)
print("EJERCICIO 3: Proyecto completo de scraping y analisis")
print("=" * 70)

registros = []

for pagina in range(1, MAX_PAGINAS + 1):
    url = BASE_URL.format(pagina)
    print(f"\nDescargando pagina {pagina}/{MAX_PAGINAS}")

    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
    except requests.RequestException as err:
        print(f"Error en pagina {pagina}: {err}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    libros = soup.select("article.product_pod")

    for libro in libros:
        titulo = libro.h3.a.get("title", "").strip()
        precio_raw = libro.select_one("p.price_color").get_text(strip=True)
        rating_raw = libro.select_one("p.star-rating").get("class", [])
        stock = libro.select_one("p.instock.availability").get_text(" ", strip=True)

        rating = "Sin rating"
        if len(rating_raw) > 1:
            rating = rating_raw[1]

        registros.append(
            {
                "pagina": pagina,
                "titulo": titulo,
                "precio_raw": precio_raw,
                "rating": rating,
                "stock": stock,
            }
        )

    time.sleep(1)

if not registros:
    print("No se pudieron extraer datos. Revisa conexion o selectores.")
    raise SystemExit(1)

df = pd.DataFrame(registros)

# Limpieza basica para dejar columnas analizables
rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
df["precio"] = (
    df["precio_raw"]
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .astype(float)
)
df["rating_num"] = df["rating"].map(rating_map)
df["en_stock"] = df["stock"].str.contains("In stock", case=False, na=False)

print("\nDimensiones del dataset:", df.shape)
print("\nPrimeras filas:")
print(df.head())

print("\nPrecio promedio por rating:")
print(df.groupby("rating")["precio"].mean().sort_values(ascending=False))

print("\nDistribucion de ratings:")
print(df["rating"].value_counts())

print("\nPorcentaje en stock:")
print(round(df["en_stock"].mean() * 100, 2), "%")

df.to_csv("proyecto_scraping_libros.csv", index=False, encoding="utf-8")
print("\nArchivo generado: proyecto_scraping_libros.csv")
print("Fin del ejercicio 3")
