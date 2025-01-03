# summations in numpy using ufunc
import numpy as np

# Create a numpy array
arr = np.array([1, 2, 3, 4, 5])
arr1 = np.array([6, 7, 8, 9, 10])

# Calculate the summation of the array
sum_arr = np.sum(arr)

print("Sum of the array:", sum_arr)

# Addition is done between two arguments whereas summation happens over n elements.
# Add the values in arr1 to the values in arr2:
# Example of addition in the numpy array
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2)

print(newarr)

# Summation over an axis in numpy
# If you specify axis=1, NumPy will sum the numbers in each array.
# Example
# Perform summation in the following array over 1st axis:
import numpy as np
arr = np.array([[10, 20, 30], [40, 50, 60]])
newarr = np.sum(arr, axis=1)
print(newarr)

# Cummulative summation in numpy
# Cummulative sum means partially adding the elements in array.
# Example of cummulative summation in numpy array
import numpy as np
arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)
print(newarr) 

