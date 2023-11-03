from datasets import load_dataset
import numpy as np


#Cargar el dataset

dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

#Convertir data a un DataFrame
df = pd.DataFrame(data)

#Acceder a la lista de edades y convertirla a un arreglo Numpy
edades = data["age"]
edades_np = np.array(edades)

#Calcular el promedio de edades
promedio_edad = np.mean(edades_np)

print("El promedio es:", promedio_edad, "años.")

# Filtrar las filas en funcion de "is_dead"
perecidos = df[df["is_dead"] == 1]
no_perecidos = df[df["is_dead"] == 0]

# Calcular el promedio de edades para cada dataset
promedio_edad_perecidos = perecidos["age"].mean()
promedio_edad_no_perecidos = no_perecidos["age"].mean()

print("Promedio de edades de las personas que perecieron:", promedio_edad_perecidos)
print("Promedio de edades de las personas que no perecieron:", promedio_edad_no_perecidos)