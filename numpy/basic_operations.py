import numpy as np

m1 = np.array([2,4,56,1,24,18,100,15])


# sort matrix
print('sort')
print(np.sort(m1))

m2 = np.array([2,3])

# potentiate
print("potentiate")
print(np.power(m2, 2))
print(m2**3)

# conditions
print('conditions')
print(np.array(m1 >= 4))

# max min value
print('max min value')
print(np.max(m1), np.min(m1))

# concatenate
print('concatenate')
print(np.concatenate([m1,m2]))