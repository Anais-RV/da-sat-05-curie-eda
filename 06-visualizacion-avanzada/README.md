# 🎨 Visualización Avanzada

## Pairplot: Múltiples relaciones

```python
# Ver todas las combinaciones
sns.pairplot(df[['precio', 'cantidad', 'descuento']])
plt.show()

# Coloreado por categoría
sns.pairplot(df, hue='categoria')
plt.show()
```

## Subplots: Múltiples gráficos

```python
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Gráfico 1
axes[0, 0].hist(df['precio'], bins=30)
axes[0, 0].set_title('Distribución de Precios')

# Gráfico 2
axes[0, 1].scatter(df['precio'], df['cantidad'])
axes[0, 1].set_title('Precio vs Cantidad')

# Gráfico 3
df['categoria'].value_counts().plot(kind='bar', ax=axes[1, 0])
axes[1, 0].set_title('Productos por Categoría')

# Gráfico 4
sns.boxplot(x='categoria', y='precio', data=df, ax=axes[1, 1])
axes[1, 1].set_title('Precios por Categoría')

plt.tight_layout()
plt.show()
```

## Violin plot

```python
sns.violinplot(x='categoria', y='precio', data=df)
plt.title('Distribución de Precios por Categoría')
plt.show()
```

## Facet Grid: Subgráficos por categoría

```python
g = sns.FacetGrid(df, col='categoria', height=4)
g.map(sns.histplot, 'precio')
plt.show()
```

---

**Autoría:** Anaïs Rodríguez Villanueva
