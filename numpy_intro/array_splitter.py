import numpy as np

# Create an array
array = np.arange(10)
print("Original array:")
print(array)

# Split the array into 3 parts
split_array = np.array_split(array, 3)
print("\nSplit array into 3 parts:")
for part in split_array:
    print(part)

# Split the array at specific indices
split_array_indices = np.split(array, [3, 6])
print("\nSplit array at indices 3 and 6:")
for part in split_array_indices:
    print(part)