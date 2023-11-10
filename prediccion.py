import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


df = pd.read_csv('datos_limpios.csv')

# Eliminar las columnas especificadas para X y definir la columna 'age' como vector y
X = df.drop(['DEATH_EVENT', 'age', 'edad_categorizada'], axis=1)
y = df['age']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Ajustar el modelo de regresión lineal
regresion_lineal = LinearRegression()
regresion_lineal.fit(X_train, y_train)

# Realizar predicciones
y_pred = regresion_lineal.predict(X_test)

# Comparar las predicciones con las edades reales
resultados = pd.DataFrame({'Real': y_test, 'Predicción': y_pred})
print(resultados)

# Calcular el error cuadrático medio
mse = mean_squared_error(y_test, y_pred)
print(f"Error cuadrático medio: {mse}")