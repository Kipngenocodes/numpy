'''
ufuncs stands for "Universal Functions" and they are NumPy functions that operate on the ndarray object.
ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.
They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.
ufuncs also take additional arguments, like:
where boolean array or condition defining where the operations should take place.
dtype defining the return type of elements.
out output array where the return value should be copied.'''

# With ufunc, we can use the add() function:
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
x = np.add(arr, arr2)
print(x)