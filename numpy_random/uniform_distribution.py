# used to describe probability where events have equal chances of occuring. like generation of random numbers.
# It has three parameters:
#low - lower bound - default 0 .0.
# high - upper bound - default 1.0.
# size - The shape of the returned array.
# Create a 2x3 uniform distribution sample:
import numpy as np

# Define the parameters
low = 0.0
high = 1.0
size = (2, 3)

# Generate the 2x3 uniform distribution sample
sample = np.random.uniform(low, high, size)

print(sample)

# visualization of uniform distribution
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random

sns.histplot(random.uniform(low, high, size=1000), kde=False, color='blue')
plt.title('Uniform Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()