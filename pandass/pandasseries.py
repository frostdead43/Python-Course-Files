import pandas as pd
import numpy as np
#data
numbers = [20,30,40,50]
letters = ['a','b','c','d']
dict = {'a':10, 'b':20, 'c':30,'d':40}
random_numbers = np.random.randint(10,100,6)

pandas_series = pd.Series()
# pandas_series = pd.Series(numbers)
# pandas_series = pd.Series(letters)
# pandas_series = pd.Series(5,[0,1,2,3])
pandas_series = pd.Series(numbers,['a','b','c','d'])
# pandas_series = pd.Series(dict)
# pandas_series = pd.Series(random_numbers)

pandas_series = pd.Series([20,30,40,50],['a','b','c','d'])
# result = pandas_series[-2:]
# result = pandas_series[['a','b','c','d']]

result = pandas_series.ndim
result = pandas_series.dtype

print(pandas_series)
print(result)