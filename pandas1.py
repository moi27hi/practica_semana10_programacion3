import pandas as pd 

archivo = pd.read_csv("movies.csv")
print(archivo)


# primeros cinco valores o la cantidad que especifique. 

print(archivo.head())

# ultimos 5 valores o la cantidad que especifique.
print(archivo.tail())

print(archivo.columns)

# Para imprimir datos de una columna.
print(archivo['release_date'])

# Para filtrar
#rango = archivo[(archivo['popularity'] >= 80  & (archivo['popularity']) <= 500)]
#print(rango)

print('\n ***Analisis estadistico***\n')

print(f"Media: {archivo['popularity'].mean()}")
print(f"Mediana: {archivo['popularity'].median()}")
print(f"Varianza: {archivo['popularity'].var()}")
print(f"Desviacion estandar: {archivo['popularity'].std()}")
print(f"Popularidad mas alta: {archivo['popularity'].min()}")
print(f"Popularidad mas baja: {archivo['popularity'].max()}")