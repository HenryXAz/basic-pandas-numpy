import pandas as pd

df = pd.read_csv('ModalidadVirtual.csv')


print(df)

print("specific value")
print(df['carrera'][1])


df_filter = df['edad'] > 23
df_filtered = df[df_filter]
print(df_filtered)


print("head")
print(df.head(10))

print("tail")
print(df.tail(10))

