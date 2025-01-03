'''Trigonometric Functions
NumPy provides the ufuncs sin(), cos() and tan() 
that take values in radians and produce the corresponding sin, cos and tan values.
'''
# Example
# Find sine value of pi/2:
import numpy as np
x = np.sin(np.pi/2)
print(x)  # Output: 1.0

# Example
# Find sine values for all of the values in arr:
import numpy as np
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)  # Output: [1.         0.8660254  0.70710678 0.58778525]

'''
By default all of the trigonometric functions take radians
as parameters but we can convert radians to degrees and vice versa as well in NumPy.
Note: radians values are pi/180 * degree_values.'''
# Example
# Convert all of the values in following array arr to degrees:
import numpy as np
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])    
x = np.degrees(arr)
print(x)  # Output: [ 90. 180. 270. 360.]


# Radians to Degrees
# Example
# Convert all of the values in following array arr to radians:
import numpy as np
arr = np.array([90, 180, 270, 360])
x = np.radians(arr)
print(x)  # Output: [1.57079633 3.14159265 4.71238898 6.28318531]

# Finding Angles
# Example
# Find the angle of 1.0:
import numpy as np
x = np.arcsin(1.0)
print(x)  # Output: 1.5707963267948966

'''
Angles of Each Value in Arrays
Example
Find the angle for all of the sine values in the array
'''
import numpy as np
arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x)  # Output: [1.57079633 -1.57079633 0.10016742]

# Hypotenues
# Example
# Find the hypotenues for 4 and 3:
import numpy as np
base = 3
perpendicular = 4
x = np.hypot(base, perpendicular)
print(x)  # Output: 5.0
# NumPy provides the hypot() function that takes the base and perpendicular values 
# and produces hypotenues based on pythagoras theorem.
# The hypotenues is the value of the 3rd side of the right-angled triangle.