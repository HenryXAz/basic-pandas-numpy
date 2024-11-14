import pandas as pd

df = pd.read_csv('ModalidadVirtual.csv')

print(df.iloc[1,2])
print(df.iloc[1,:4])

print(df.loc[1, 'carrera'])

print("sort values")
print(df.sort_values('carrera'))

print(df.sort_values("edad"))