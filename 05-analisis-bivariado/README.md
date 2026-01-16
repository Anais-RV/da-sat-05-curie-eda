# 🔗 Análisis Bivariado

Relaciones entre dos variables.

## Numérica vs Numérica

```python
# Correlación
correlation = df['precio'].corr(df['cantidad'])
print(f"Correlación: {correlation:.2f}")

# Scatter plot
sns.scatterplot(x='precio', y='cantidad', data=df)
plt.title(f'Correlación: {correlation:.2f}')
plt.show()

# Regresión
sns.regplot(x='precio', y='cantidad', data=df)
plt.show()
```

## Categórica vs Numérica

```python
# Boxplot
sns.boxplot(x='categoria', y='precio', data=df)
plt.title('Precio por Categoría')
plt.show()

# Estadísticos por grupo
df.groupby('categoria')['precio'].agg(['mean', 'median', 'std'])

# Prueba estadística (ANOVA)
from scipy.stats import f_oneway
grupos = [df[df['categoria'] == cat]['precio'] for cat in df['categoria'].unique()]
f_stat, p_value = f_oneway(*grupos)
print(f"P-value: {p_value:.4f}")
```

## Categórica vs Categórica

```python
# Tabla cruzada
pd.crosstab(df['categoria'], df['region'])

# Con proporciones
pd.crosstab(df['categoria'], df['region'], normalize='all')

# Heatmap
crosstab = pd.crosstab(df['categoria'], df['region'])
sns.heatmap(crosstab, annot=True, fmt='d', cmap='YlGnBu')
plt.show()
```

## Matriz de correlación

```python
# Solo numéricas
corr = df.select_dtypes(include=[np.number]).corr()

# Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=1, fmt='.2f')
plt.title('Matriz de Correlación')
plt.show()
```

---

**Autoría:** Anaïs Rodríguez Villanueva
