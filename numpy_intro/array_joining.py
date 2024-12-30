import numpy as np

# Creating two arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Joining arrays using concatenate
joined_array = np.concatenate((array1, array2))
print("Concatenated array:", joined_array)

# Joining arrays along a new axis using stack
stacked_array = np.stack((array1, array2), axis=0)
print("Stacked array along new axis:\n", stacked_array)

# Joining arrays along rows using vstack
vstacked_array = np.vstack((array1, array2))
print("Vertically stacked array:\n", vstacked_array)

# Joining arrays along columns using hstack
hstacked_array = np.hstack((array1, array2))
print("Horizontally stacked array:", hstacked_array)