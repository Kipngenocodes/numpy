import numpy as np
import os as p

arr = np.array([1, 2, 3, 4, 5])

p = np.array([1, 2, 3, 4, 5, 6, 7, 8], ndmin=7)

print(arr)
print(np.__version__)
print(type(arr))

print(p)
print(p.ndim)
