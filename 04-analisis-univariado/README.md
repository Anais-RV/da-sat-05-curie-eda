# 📊 Análisis Univariado

Analiza cada variable individualmente.

## Variables numéricas

```python
# Estadísticos
df['precio'].describe()

# Distribución
sns.histplot(df['precio'], kde=True)
plt.title('Distribución de Precio')
plt.show()

# Boxplot (detectar outliers)
sns.boxplot(x=df['precio'])
plt.show()

# Percentiles
df['precio'].quantile([0.25, 0.5, 0.75, 0.95])
```

## Variables categóricas

```python
# Frecuencias
df['categoria'].value_counts()

# Proporciones
df['categoria'].value_counts(normalize=True)

# Gráfico de barras
df['categoria'].value_counts().plot(kind='bar')
plt.title('Distribución de Categorías')
plt.show()
```

## Normalidad

```python
from scipy.stats import shapiro, probplot

# Test de Shapiro-Wilk
stat, p_value = shapiro(df['precio'])
print(f"P-value: {p_value:.4f}")
if p_value > 0.05:
    print("Los datos parecen normales")

# Q-Q plot
probplot(df['precio'], dist="norm", plot=plt)
plt.show()
```

---

**Autoría:** Anaïs Rodríguez Villanueva
