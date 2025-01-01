import numpy as np

# logistic distribution is used to describe growth.
# It has three parameters:
# loc  - mean, where the peak is. Default 0.
# scale - standard deviation, the flatness of distribution. Default 1
# size - The shape of the returned array.
# Draw 2x3 samples from a logistic distribution with mean at 1 and stddev 2.0:

samples = np.random.logistic(loc=1, scale=2.0, size=(2, 3))
print(samples)

# Visualization of Logistic Distribution
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(random.logistic(loc=1, scale=2.0, size=1000), kde=False, color='blue')
plt.title('Logistic Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

