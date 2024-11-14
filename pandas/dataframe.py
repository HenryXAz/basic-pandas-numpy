import pandas as pd
import numpy as np

data = {"NOMBRE": ['Maria', 'Jose', 'David', 'Ivan'], "CARRERA": ['Auditoria', 'Informatica', 'Derecho', 'Idiomas'],
        "correo": ['maria@gmail.com', 'jose@gmail.com', 'david@gmail.com', 'ivan@gmail.com']}

estudiantes = pd.DataFrame(data)

print(estudiantes)

df = pd.DataFrame([['Maria', 27], ['David', 34], ['Ana', 18], ['Jose', 17]],
                  columns=['NOMBRE', 'EDAD']
                  )

print("DF")
print(df)

df_array = pd.DataFrame(np.random.randn(4,3), columns=['a', 'b', 'c'])

print("df array")
print(df_array)
