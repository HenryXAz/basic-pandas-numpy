import numpy as np

m = np.array([[1, -1, 2], [3,2,0]])
print(m)
print("")

m1 = np.array([[1], [2], [3]])
print(m1)
print(np.transpose(m1))


# Ax=B
print('Ax=B')
A = np.array([[2, 1, -2], [3,0,1], [1,1,-1]])

print(A)
print("")

B = np.array([[-3], [5], [-2]])
print(B)
print("")

x = np.linalg.solve(A, B)
print("x value")
print(x)
print(np.allclose(np.dot(A, x), B))

