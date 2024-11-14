import numpy as np

m = np.array([[1,2,3], [4,5,6], [7,8,9]])

print(m)
print("")
print(np.min(m))


# max min by axis
print("max by axis")
print(np.amax(m, 0))
print(np.amax(m,1))

# range by axis
print("range by axis")
print(np.ptp(m, 0))
print(np.ptp(m,1))

# percentile
print("pecentile")
print(np.percentile(m, 50))

# median
print("median")
print(np.median(m))


# mean
print("mean")
print(np.mean(m))

n = np.array([1,2,3,4,5,6])
print(n)

# average
print('average')
print(np.average(n))

# std
print("std")
print(np.std(n))





