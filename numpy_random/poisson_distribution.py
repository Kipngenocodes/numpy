'''
Poisson Distribution is a Discrete Distribution.

It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?

It has two parameters:

lam - rate or known number of occurrences e.g. 2 for above problem.

size - The shape of the returned array.
'''
import numpy as np
from numpy import random
from matplotlib import pyplot as plt
import seaborn as sns

# Generate poisson random samples
lam = 2
x = random.poisson(lam, size=10)
print(x)

# visualization of poisson distribution
sns.histplot(random.poisson(lam, size=1000), kde=False, color='blue')
plt.title('Poisson Distribution')
plt.xlabel('Number of Occurrences')
plt.ylabel('Frequency')
plt.show()
