'''
Zipf distributions are used to sample data based on zipf's law.
Zipf's Law: In a collection, the nth common term is 1/n times of the most common term. 
E.g. the 5th most common word in English occurs nearly 1/5 times as often as the most common word.
It has two parameters:
a - distribution parameter.
size - The shape of the returned array.'''

# Draw out a sample for zipf distribution with distribution parameter 2 with size 2x3:
from numpy import random

x = random.zipf(a=2, size=(2, 3))

print(x)

# draw an illustration of the zipf distribution:
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
# Create a figure and a set of subplots
fig, ax = plt.subplots(1, 1)
a = 2.
x = np.arange(1, 5)
# Probability mass function at x of the given RV.
pmf = stats.zipf.pmf(x, a)
# Plot the PMF
sns.heatmap(pmf.reshape(1, -1), ax=ax, cmap='Blues',
            cbar=False, annot=True)
ax.set_yticks([])
ax.set_title('Zipf Distribution')
plt.show()

  