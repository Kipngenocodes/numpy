# creating a ufunction to execute a multipication in simple function

import numpy as np

def mymultipication(x, y):
    return x * y

my_multiplication = np.frompyfunc(mymultipication, 2, 1)
print(my_multiplication([1, 2, 3, 4], [5, 6, 7, 8]))

# creating a ufunction to execute a division in simple function
def mydivision(x, y):
    return x / y

my_division = np.frompyfunc(mydivision, 2, 1)
print(my_division([1, 2, 3, 4], [5, 6, 7, 8]))
