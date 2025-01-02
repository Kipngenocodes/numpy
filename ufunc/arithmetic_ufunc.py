'''
Arithmetic Conditionally: 
means that we can define conditions where the arithmetic operation should happen.
All of the discussed arithmetic functions take a where parameter in which we can specify that condition.'''

# ufuncs to handle arithmetic operations like add, subtract, multiply, power, quontient and modulus
# reminder, and divide elements in the array.
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
print(np.add(arr, arr2))  # Output: [ 7  9 11 13 15]
print(np.subtract(arr, arr2))  # Output: [-5 -5 -5 -5 -5]
print(np.multiply(arr, arr2))  # Output: [ 6 14 24 36 50]
print(np.divide(arr, arr2))  # Output: [0.16666667 0.28571429 0.375 0.44444444 0.5]
print(np.power(arr, arr2))  # Output: [      1     128    6561 262144 9765625]
print(np.mod(arr, arr2))  # Output: [1 2 3 4 5]
print(np.remainder(arr, arr2))  # Output: [1 2 3 4 5]
print(np.divmod(arr, arr2))  # Output: (array([0, 0, 0, 0, 0]), array([1, 2, 3, 4, 5]))
print(np.floor_divide(arr, arr2))  # Output: [0 0 0 0 0]
