'''
What is a Set
A set in mathematics is a collection of unique elements.
Sets are used for operations involving frequent intersection, union and difference operations.Create Sets in NumPy
We can use NumPy's unique() method to find unique elements from any array. E.g. create a set array,
but remember that the set arrays should only be 1-D arrays.
'''
# Example of creating a set array:
import numpy as np
arr = np.array([1, 1, 2, 3, 4, 4, 1])
x = np.unique(arr)
print(x)

# Find the unique values of two arrays
# To find only the values that are present in both arrays, use the intersect1d() method.
# Example
# Find the common values between two arrays:
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print(newarr)

# Finding Union
# To find the unique values of two arrays, use the union1d() method.
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)
print(newarr)

# finding difference
# To find only the values in the first set that is not present in the seconds set,
# use the setdiff1d() method.
# Example
# Find the difference of the set1 from set2:
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.setdiff1d(arr1, arr2, assume_unique=True)
print(newarr)


# Finding Symmetric Difference
# To find only the values that are NOT present in BOTH sets, use the setxor1d() method.
# Example
# Find the symmetric difference of the set1 and set2:
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.setxor1d(arr1, arr2, assume_unique=True)
print(newarr)