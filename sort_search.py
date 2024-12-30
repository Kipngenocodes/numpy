import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = np.searchsorted(arr, 3, side='right')

print(x)