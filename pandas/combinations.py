import pandas as pd

df1 = pd.DataFrame({
    "NOMBRE": ['Jose', 'Max'],
    "CARRERA": ['Economía', 'Arquitectura'],
    "EDAD": [23,26],
}).set_index("NOMBRE")

df2 = pd.DataFrame({
    "NOMBRE": ['Aurora', 'Maria'],
    "CARRERA": ['Medicina', 'Informática'],
    "EDAD": [22, 28],
}).set_index("NOMBRE")

df3 = pd.concat([df1, df2])

print("concat by rows")
print(df3)


df4 = pd.DataFrame({
    "AUTOS": ['Nissan', 'Ford', 'Audi'],
    "COLOR": ['blanco', 'azul', 'rojo'],
}).set_index("AUTOS")

df5 = pd.DataFrame({
    'AUTOS': ['Toyota', 'Ford', 'Audi'],
    'MODELO': ['2018', '2020', '2022'],
}).set_index('AUTOS')

df6 = pd.concat([df4, df5], axis=1)

print('concat by columns')
print(df6)


combination = pd.merge(df4, df5, on="AUTOS", how="right")

print("Merge")
print(combination)

print("chart")
print("")
