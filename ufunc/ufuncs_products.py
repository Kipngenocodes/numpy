'''
Products
To find the product of the elements in an array, use the prod() function.   
The prod() function multiplies the elements of an array.
'''
# Example
# Find the product of the elements of the following array:
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = np.prod(arr)
print(x)

# Find the product of the elements of two arrays:
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2])
print(x)

# products over an axis in numpy
# If you specify axis=1, NumPy will return the product of each array.
# Example
# Perform product in the following array over 1st axis:
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
newarr = np.prod(arr, axis=1)
print(newarr)


# Cummulatve product in numpy
# Cummulative product means taking the product partially.   
# Example
# Find the cumulative product of the following array:
import numpy as np
arr = np.array([1, 2, 3, 4])
newarr = np.cumprod(arr)
print(newarr)