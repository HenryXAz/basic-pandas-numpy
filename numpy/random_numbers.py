import numpy as np

m = np.random.randint(10, size=(3,3))

print(m)

choice_number = np.random.choice([1,2,3,4,5,6], size=(2,3))

# random choice
print('random choice')
print(choice_number)

# choice probably
n = np.random.choice([2,4,8,10], p=[0.3, 0.5, 0.1, 0.1], size=[50])

print("choice probably")
print(n)

