import numpy as np

# Create a sample array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Create a boolean index list
boolean_index_list = array > 5

# Use the boolean index list to filter the array
filtered_array = array[boolean_index_list]

print("Original array:", array)
print("Boolean index list:", boolean_index_list)
print("Filtered array:", filtered_array)