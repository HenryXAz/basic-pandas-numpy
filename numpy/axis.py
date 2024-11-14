import numpy as np

m = np.array([[0,1,2], [4,2,3]])

print(m)
print("")

# axis 0 (columns)
print("axis 0 (columns")
print(np.sum(m, axis=0))

# axis 1 (rows)
print("axis 1 (rows)")
print(np.sum(m, axis=1))