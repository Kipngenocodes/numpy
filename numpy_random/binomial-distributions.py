'''
            Binomial Distribution
Binomial Distribution is a Discrete Distribution.

It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.

It has three parameters:
    n - number of trials.
    p - probability of occurrence of each trial (e.g., for toss of a coin 0.5 each).
    size - The shape of the returned array.
'''

from numpy import random
from matplotlib import pyplot as plt
import seaborn as sns

# Generate binomial random samples
x = random.binomial(n=10, p=0.5, size=10)
print(x)

# Visualization of binomial distribution
sns.histplot(random.binomial(n=10, p=0.5, size=1000), bins=10, kde=False, color='blue')

# Add labels and title
plt.title("Binomial Distribution Visualization")
plt.xlabel("Number of Successes")
plt.ylabel("Frequency")

# Show the plot
plt.show()
