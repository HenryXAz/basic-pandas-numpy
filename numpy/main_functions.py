import numpy as np

matrix = np.arange(20).reshape(4,5)

# rows and columns of matrix
print(matrix.shape)

# dimensions of matrix
print(matrix.ndim)

# total elements
print(matrix.size)

# matrix with zeros
m = np.zeros((3,4))

print(m)

# matrix by interval value
n = np.linspace(99, 88, 25)
print(n)