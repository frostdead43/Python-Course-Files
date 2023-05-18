import numpy as np

# result = np.array([1,3,5,7,9])
# result = np.arange(1,10,3)
# result = np.zeros(10)
# result = np.ones(10)
# result = np.linspace(0,100,5)
# result = np.random.randint(0,10)
# result = np.random.rand(3)

np_array = np.arange(50)
result = np_array.reshape(5,10)
print(result)
