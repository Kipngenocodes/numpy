# NumPy provides functions to perform log at the base 2, e and 10.
# All of the log functions will place -inf or inf in the elements if the log can not be computed.
# Log at Base 2
# Use the log2() function to perform log at the base 2.
# Example
# Find log at base 2 of all elements of following array:
import numpy as np

arr = np.arange(1, 10)

print(np.log2(arr))

# Log at Base 10
# Use the log10() function to perform log at the base 10.
# Example
# Find log at base 10 of all elements of following array:
import numpy as np

arr = np.arange(1, 10)

print(np.log10(arr))

# Natural Log, or Log at Base e
# Use the log() function to perform log at the base e.
# Example
import numpy as np

arr = np.arange(1, 10)

print(np.log(arr))

'''
Log at Any Base
NumPy does not provide any function to take log at any base,
so we can use thefrompyfunc() function along with 
inbuilt function math.log() with two input parameters and one output parameter:'''

import numpy as np
from math import log
from numpy import frompyfunc
# Define a function to take log at any base
log_at_base = frompyfunc(lambda x, b: log(x) / log(b), 2, 1)
arr = np.arange(1, 10)
print(log_at_base(8, 2))  # Output: 3.0
