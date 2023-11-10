import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Lee los datos procesados
df = pd.read_csv('datos_limpios.csv')

plt.figure(figsize=(10,6))
plt.hist(df['age'], bins=20, color='skyblue')
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.75)
plt.show()


# Obtener los valores para hombres y mujeres
valores_hombres = df[df['sex'] == True][['anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']].sum().values
valores_mujeres = df[df['sex'] == False][['anaemia', 'diabetes', 'smoking', 'DEATH_EVENT']].sum().values

# Convertir los valores booleanos a números enteros
valores_hombres = [int(valor) for valor in valores_hombres]
valores_mujeres = [int(valor) for valor in valores_mujeres]

# Imprimir los valores de las variables
print(valores_hombres)
print(valores_mujeres)

# Configurar el gráfico de barras
etiquetas = ['Anemicos', 'Diabeticos', 'Fumadores', 'Muertos']
x = np.arange(len(etiquetas))
ancho = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
rectsTrue = ax.bar(x - ancho/2, valores_hombres, ancho, label='Hombres', color='blue')
rects2 = ax.bar(x + ancho/2, valores_mujeres, ancho, label='Mujeres', color='red')

# Agregar texto, etiquetas y título
ax.set_xlabel('Categorías')
ax.set_ylabel('Cantidad')
ax.set_title('Histograma Agrupado por Sexo')
ax.set_xticks(x)
ax.set_xticklabels(etiquetas)
ax.legend()

plt.show()

# PARTE 8: Gráficas de torta, distribuciones 2
valores_anémicos = df['anaemia'].value_counts()
valores_diabéticos = df['diabetes'].value_counts()
valores_fumadores = df['smoking'].value_counts()
valores_muertos = df['DEATH_EVENT'].value_counts()

print("Valor de la anaemia: ", valores_anémicos)
print("Valor de la diabetes: ", valores_diabéticos)
print("Valor del fumar: ", valores_fumadores)
print("Valor de las muertes: ", valores_muertos)


anemicos = 'Si','No'
diabeticos =  'Si','No'
fumadores =  'Si','No'
muertos =  'Si','No'

# Configuración de colores
colores = [ '#FF69B4', '#87CEEB']

# Crear las gráficas de torta
fig, axs = plt.subplots(1, 4, figsize=(15, 5))
axs[0].pie(valores_anémicos, labels=anemicos, autopct='%1.1f%%', startangle=90, colors=colores)
axs[1].pie(valores_diabéticos, labels=diabeticos, autopct='%1.1f%%', startangle=90, colors=colores)
axs[2].pie(valores_fumadores, labels=fumadores, autopct='%1.1f%%', startangle=90, colors=colores)
axs[3].pie(valores_muertos, labels=muertos, autopct='%1.1f%%', startangle=90, colors=colores)

# Ajustar los títulos de las gráficas
axs[0].set_title('Anémicos')
axs[1].set_title('Diabéticos')
axs[2].set_title('Fumadores')
axs[3].set_title('Muertos')

# Mostrar la gráfica
plt.show()