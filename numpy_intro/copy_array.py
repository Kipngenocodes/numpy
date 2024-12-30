import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

'''The copy owns the data and any changes made to the copy will not affect original array,
and any changes made to the original array will not affect the copy.
'''