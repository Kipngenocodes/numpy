''' 
Multinomial distribution is a generalization of binomial distribution.
It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.
It has three parameters:
n - number of possible outcomes (e.g. 6 for dice roll).
pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
size - The shape of the returned array.
'''
# Draw out a sample for dice roll.
from numpy import random

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x)


# visualization of multinomial distribution
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# n = number of possible outcomes (e.g. 6 for dice roll).
# pvals = list of probabilities of outcomes (e.g. [1/6, 1
# size = The shape of the returned array.
n = 6
pvals = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
size = (10, 10)
x = random.multinomial(n, pvals, size)

# print(x)
# Create a DataFrame from the array
df = pd.DataFrame(x, columns=['one', 'two', 'three', 'four', 'five', 'six'])
# Plot the DataFrame using seaborn's countplot function
sns.countplot(data=df, palette='viridis')
plt.title('Multinomial Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
# The countplot shows the frequency of each outcome in the sample.\n",
# "The x-axis represents the possible outcomes, and the y-axis represents the frequency of each outcome in the sample.\n",
# The plot shows that each outcome has a frequency of 10, which is the size of the sample. This is consistent with the equal probabilities assigned to each outcom
# sample. This is consistent with the equal probabilities assigned to each outcome in the multinomial distribution.
# in the multinomial distribution.
# The multinomial distribution is a generalization of the binomial distribution, and it can be used
# to model scenarios with multiple possible outcomes. In this example, we used the multinomial
# distribution to simulate a dice roll with six possible outcomes. The countplot provides a visual
# representation of the frequency of each outcome in the sample, showing that each outcome has an
# equal frequency of 10. This is consistent with the equal probabilities assigned to each outcome
# in the multinomial distribution.
# The multinomial distribution is a powerful tool for modeling complex scenarios with multiple
# possible outcomes. It can be used in a variety of applications, including statistics, machine
# learning, and data science. By using the multinomial distribution, you can model scenarios with
# multiple possible outcomes and analyze the frequency of each outcome in the sample.
# Conclusion
# In this example, we used the multinomial distribution to simulate a dice roll with six possible
# outcomes. We generated a sample of outcomes using the random.multinomial function and created a
# DataFrame from the array. We then used seaborn's countplot function to visualize the frequency of 
# each outcome in the sample. The countplot showed that each outcome had an equal frequency of 10,  
# which is consistent with the equal probabilities assigned to each outcome in the multinomial distribution.
# The multinomial distribution is a powerful tool for modeling complex scenarios with multiple possible outcomes. It can
# be used in a variety of applications, including statistics, machine learning, and data science. By using the multinomial
# distribution, you can model scenarios with multiple possible outcomes and analyze the frequency of each outcome in th
# sample.
# References
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.multinomial.html
