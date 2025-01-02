'''Chi Square distribution is used as a basis to verify the hypothesis.
It has two parameters:
df - (degree of freedom).
size - The shape of the returned array.'''

# Draw out a sample for chi squared distribution with degree of freedom 2 with size 2x3:
from numpy import random
import numpy as np
# Define the parameters of the chi squared distribution
df = 2
size = (2, 3)
# Draw out a sample for chi squared distribution with degree of freedom 2 with size 2x
# 3
x = random.chisquare(df, size)
print(x)

# Visualization of chi squared distribution
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random

# Generate a sample from the chi squared distribution
x = random.chisquare(df=2, size=1000)
# Plot the histogram of the sample
sns.histplot(x, kde=True)
plt.title('Chi Squared Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
