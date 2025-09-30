# Ejercicio. 
import numpy as np
import pandas as pd 

# Cargando el archivo csv. 

df = pd.read_csv('vehiculos_electricos.csv')



# Ver los primeros registros. 
print('***Informacion sobre vehiculos electricos***\n')
print(df.head())

print("****Resumen del dataset***\n")
print(df.describe())


print("*** Identificando los tipos de datos***\n")
print(df.dtypes)

print ("*** Mostrando los primeros 5 registros***\n")
print(df.head())   # Primeros 5


print("*** Mostrando los ultimos registros ***\n")
print(df.tail())   # Últimos 5



# Ordenar por una columna (ejemplo: "Edad" o "Precio")

print("***Ordenando los datos\n***")
print(df.sort_values("Model Year", ascending=False))



columna = df["Model Year"]

print("Media:", columna.mean())
print("Mediana:", columna.median())
print("Desviación estándar:", columna.std())




# a. Describe brevemente de qué trata el dataset utilizado
# Se trata de un Dataset sobre la poblacion de autos electricos

# b. ¿Qué información permite ver el resumen estadístico?
# El tipo de vehiculos, año, rango electrico (el tiempo de uso por cada carga, etc.)

# c. ¿Qué cambios o tendencias se detectan en la información del dataset?
# Se nota un incremento en modelos recientes (2020–2025) y más autos con mayores rangos eléctricos.




