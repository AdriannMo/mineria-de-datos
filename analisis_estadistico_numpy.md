# 📊 Análisis Estadístico Básico con NumPy

Este documento presenta una guía introductoria al uso de **NumPy** para realizar análisis estadístico fundamental. NumPy es una biblioteca esencial de Python para el cálculo numérico, ampliamente utilizada en ciencia de datos, machine learning y análisis científico.

## 📘 Introducción
NumPy proporciona una estructura de datos eficiente basada en arreglos (`ndarray`) y un amplio conjunto de funciones matemáticas y estadísticas que permiten:
- Resumir datos rápidamente
- Calcular medidas de tendencia central
- Analizar la dispersión
- Trabajar con arreglos multidimensionales

## ▶️ Importación de NumPy
```python
import numpy as np
```

# 📈 Medidas Estadísticas Básicas

## Media (Mean)
```python
data = np.array([1, 2, 3, 4, 5])
media = np.mean(data)
print(media)
```

## Promedio (Average) y Promedio Ponderado
```python
data = np.array([1, 2, 3, 4, 5])
weights = np.array([1, 2, 3, 4, 5])
promedio = np.average(data)
promedio_ponderado = np.average(data, weights=weights)
```

## Mediana
```python
mediana = np.median(data)
```

## Varianza y Desviación Estándar
```python
varianza = np.var(data)
desviacion = np.std(data)
```

# 🔄 Generación de Datos Aleatorios
```python
muestra = np.random.normal(0, 1, 1000)
print(np.mean(muestra), np.std(muestra))
```

# 🔗 Correlación
```python
corr = np.corrcoef([1,2,3], [1,5,7])
```

# 📊 Funciones Estadísticas Adicionales (NumPy)
- Cuantiles (`np.quantile`)
- Percentiles (`np.percentile`)
- Histogramas (`np.histogram`)
- Covarianza (`np.cov`)
- Manejo de NaN (`np.nanmean`, etc.)

# 🧾 Conclusión
NumPy facilita el análisis estadístico al proporcionar funciones optimizadas para cálculos comunes como media, mediana, varianza, desviación estándar y correlación. Además, ofrece herramientas para generar datos y analizar distribuciones.
