'''
A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).
It has two parameter:
a - shape parameter.
size - The shape of the returned array.
'''
# Draw out a sample for pareto distribution with shape of 2 with size 2x3:
from numpy import random
import numpy as np
# Define the parameters of the pareto distribution
a = 2
size = (2, 3)
# Draw out a sample for pareto distribution with shape of 2 with size 2x3
pareto_sample = random.pareto(a, size=size)
print(pareto_sample)

# Visualization of pareto distribution
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random

# Generate a sample from the pareto distribution
sample = random.pareto(a=2, size=1000)
# Plot the histogram of the sample
sns.histplot(sample, kde=True)
plt.title('Pareto Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()


