import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Lee los datos procesados
df = pd.read_csv('datos_limpios.csv')

# Eliminar la columna 'categoria_edad' del DataFrame
df = df.drop('edad_categoria', axis=1)

# Graficar la distribución de clases
plt.figure(figsize=(6, 4))
df['DEATH_EVENT'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Distribución de Clases')
plt.xlabel('Clases')
plt.ylabel('Frecuencia')
plt.xticks([0, 1], ['Vive', 'Muere'])
plt.show()

# Definir X y y
X = df.drop('DEATH_EVENT', axis=1)
y = df['DEATH_EVENT']

# Realizar la partición del conjunto de datos de forma estratificada
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Ajustar el modelo de árbol de decisión
clf = DecisionTreeClassifier(max_depth=5, min_samples_split=2, random_state=42)
clf.fit(X_train, y_train)

# Realizar predicciones en el conjunto de pruebas y calcular la precisión
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión en el conjunto de pruebas: {accuracy}")
