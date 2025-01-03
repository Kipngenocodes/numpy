# NumPy GCD Greatest Common Denominator
# The GCD (Greatest Common Denominator), also known as HCF (Highest Common Factor) is the biggest number
# that is a common factor of both of the numbers.
# Example of GCD in numpy
# Find the GCD of the following two numbers:
# import numpy as np
import numpy as np
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)  # Output: 3

'''To find the Highest Common Factor of all values in an array,
you can use the reduce() method.
The reduce() method will use the ufunc, 
in this case the gcd() function, on each element, and reduce the array by one dimension.
'''
# Example
# Find the GCD for all of the numbers in the following array:
import numpy as np
arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)