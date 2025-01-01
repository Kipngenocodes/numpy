'''
Exponential Distribution
Exponential distribution is used for describing time till next event e.g. failure/success etc.
It has two parameters:
scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
size - The shape of the returned array.'''

# Draw out a sample for exponential distribution with 2.0 scale with 2x3 size:
from numpy import random
x = random.exponential(scale=2.0, size=(2, 3))
# output: array([[0.67368363, 0.18693622, 0.92853123],
#                [0.15515515, 0.5131736 , 0.06719315]])

print(x)

# visualization of exponential distribution
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random

sns.histplot(random.exponential(scale=2.0, size=1000), kde=False, color='blue')
plt.title('Exponential Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()