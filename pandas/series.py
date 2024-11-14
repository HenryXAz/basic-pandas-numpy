import pandas as pd

colores = pd.Series(['rojo', 'azul', 'amarillo', 'verde', 'morado'])

materias = pd.Series({
    "Matematicas" : 60,
    "Fisica": 100,
    "Quimica": 78,
})

print(colores)

print(materias)

print("numero de colores", colores.size)
print("index", colores.index)
print("type", colores.dtype)
print("select specific values of serie")
print(colores[2:4])

numeros = pd.Series([1,2,3,4,5,6])

print("numbers multiplied by 2")
print(numeros * 2)














