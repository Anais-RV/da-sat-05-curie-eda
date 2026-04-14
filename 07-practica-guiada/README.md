# 🎯 Práctica Guiada: EDA Completo de E-commerce

## Ruta recomendada de trabajo

1. Ejecuta primero el notebook guiado: `eda_curie_guiado.ipynb`
2. Después adapta el flujo a tu dataset (Kaggle o simulado)
3. Cierra con 3 insights accionables y exportación de resultados

## Dónde colocar el dataset (ruta única)

Para que todo el grupo trabaje igual, usa esta ruta:

- `07-practica-guiada/data/olist/`

Guía de archivos esperados en:

- `07-practica-guiada/data/README.md`

## Opción A (recomendada): Dataset de Kaggle

Si quieres trabajar con un caso más realista, usa:

- Brazilian E-Commerce Public Dataset by Olist
- https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Sugerencia de arranque:

```python
import pandas as pd

clientes = pd.read_csv('olist_customers_dataset.csv')
ordenes = pd.read_csv('olist_orders_dataset.csv')
items = pd.read_csv('olist_order_items_dataset.csv')
pagos = pd.read_csv('olist_order_payments_dataset.csv')
productos = pd.read_csv('olist_products_dataset.csv')

df = items.merge(ordenes, on='order_id', how='left') \
          .merge(pagos.groupby('order_id', as_index=False)['payment_value'].sum(), on='order_id', how='left') \
          .merge(productos[['product_id', 'product_category_name']], on='product_id', how='left')

df.head()
```

## Opción B: Dataset simulado (rápido para practicar)

```python
import pandas as pd
import numpy as np

np.random.seed(42)
n = 500

df = pd.DataFrame({
    'cliente_id': range(1, n+1),
    'edad': np.random.randint(18, 70, n),
    'genero': np.random.choice(['M', 'F'], n),
    'region': np.random.choice(['Norte', 'Sur', 'Este', 'Oeste'], n),
    'categoria': np.random.choice(['Electrónica', 'Ropa', 'Hogar'], n),
    'precio': np.random.normal(100, 50, n),
    'cantidad': np.random.randint(1, 10, n),
    'descuento': np.random.choice([0, 5, 10, 15, 20], n),
})

df['precio'] = np.maximum(df['precio'], 10)  # No negativos
df['total'] = df['precio'] * df['cantidad'] * (1 - df['descuento']/100)
```

## EDA completo

```python
# 1. Exploración inicial
print(df.head())
print(df.info())
print(df.describe())

# 2. Limpieza (si hubiera nulos/duplicados)
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

# 3. Análisis univariado
sns.histplot(df['edad'], kde=True)
plt.title('Distribución de Edad')
plt.show()

df['categoria'].value_counts().plot(kind='bar')
plt.title('Productos por Categoría')
plt.show()

# 4. Análisis bivariado
corr = df[['precio', 'cantidad', 'total']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

sns.boxplot(x='categoria', y='total', data=df)
plt.title('Ventas por Categoría')
plt.show()

# 5. Segmentación
print("\nVentas promedio por región:")
print(df.groupby('region')['total'].mean().sort_values(ascending=False))

# 6. Insights
print("\n=== INSIGHTS ===")
print(f"Cliente promedio: {df['edad'].mean():.0f} años")
print(f"Ticket promedio: ${df['total'].mean():.2f}")
print(f"Categoría top: {df['categoria'].value_counts().index[0]}")
print(f"Región con más ventas: {df.groupby('region')['total'].sum().idxmax()}")
```

---

**Autoría:** Anaïs Rodríguez Villanueva
