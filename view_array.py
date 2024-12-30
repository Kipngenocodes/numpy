import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

'''
The view does not own the data and any changes made to the view will affect the original array,
and any changes made to the original array will affect the view.
The original array SHOULD be affected by the changes made to the view.
The view SHOULD be affected by the changes made to the original array.'''