import pandas as pd

numeros = pd.Series([1,2,3,4,5,6,7,8])

print("sum all values")
print(numeros.sum())

print("max value")
print(numeros.max())

serie = pd.Series({
    "Matematicas": 8,
    "Economia": 6,
    "Programacion": 10,
    "Fisica": 8,
})

print("filter by value")
print(serie[serie > 6])

print("sort by value")
print(serie.sort_values())

print("sort by index")
print(serie.sort_index())

print("")

data_list = ['Messi', 'Cristiano Ronaldo', 'Benzema']
indexes = ['Inter Miami', 'AlNassr', 'Altihad']

futbol = pd.Series(index=indexes, data=data_list)

print("data list")
print(futbol)





