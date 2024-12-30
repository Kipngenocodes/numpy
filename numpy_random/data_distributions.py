# Data Distribution is a list of all possible values, and how often each value occurs.
# Random Distribution is a set of random values that follow a certain probability density function.
# Probability Density Function is a function that describes the likelihood of a random variable to take on a given value.

from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.4, 0.2], size=(100))

print(x)



# Random Permutations: A permutation refers to an arrangement of elements. e.g. [3, 5, 7] is a permutation of [5, 3, 7], but not of [5, 3, 7, 9].
# The NumPy Random module provides two methods for this: shuffle() and permutation().

from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)

# Generate a random permutation of elements of an array
arr1 = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr1))