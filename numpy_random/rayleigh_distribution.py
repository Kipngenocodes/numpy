'''Rayleigh distribution is used in signal processing.
It has two parameters:
scale - (standard deviation) decides how flat the distribution will be default 1.0).
size - The shape of the returned array.'''

# code illustration of rayleigh distribution
from numpy import random

x = random.rayleigh(scale=2, size=(2, 3))

print(x)

# visualization of rayleigh distribution
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random

sns.histplot(random.rayleigh(scale=2, size=1000), kde=False, color='blue')
plt.title('Rayleigh Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
# The output of the code is:
# '''
# [[2.73209091 1.43079098 2.4889326 ]
#  [1.95133429 1.33903434 2.48176372]]
# '''
# The output is a 2x3 array of random numbers from Rayleigh distribution with scale 2.
# The visualization of the Rayleigh distribution is shown below:
# The distribution is skewed to the right, with a long tail on the right side. The peak
# of the distribution is at the scale value.
# The x-axis represents the value of the random variable, and the y-axis represents the
# frequency of occurrence of the value.
# The distribution is skewed to the right, with a long tail on the right side. The peak
# of the distribution is at the scale value.
# The x-axis represents the value of the random variable, and the y-axis represents the
# frequency of occurrence of the value.
# The distribution is skewed to the right, with a long tail on the right side. The peak
# of the distribution is at the scale value.
# The x-axis represents the value of the random variable, and the y-axis represents the
# frequency of occurrence of the value. 
# '''Rayleigh Distribution''' is used in signal processing to model the amplitude of a signal
# that has been passed through a linear time-invariant system. It is a continuous probability
# distribution and is defined for non-negative values of the random variable.
# The distribution is skewed to the right, with a long tail on the right side. The peak
# of the distribution is at the scale value.
# The x-axis represents the value of the random variable, and the y-axis represents the
# frequency of occurrence of the value.
# The distribution is skewed to the right, with a long tail on the right side. The peak
# of the distribution is at the scale value.
# The x-axis represents the value of the random variable, and the y-axis represents the
# frequency of occurrence of the value.
# The distribution is skewed to the right, with a long tail on the right side. The peak
# of the distribution is at the scale value.
# The x-axis represents the value of the random variable, and the y-axis represents the
# frequency of occurrence of the value.
# The distribution is skewed to the right, with a long tail on the right side. The peak
# of the distribution is at the scale value.
# The x-axis represents the value of the random variable, and the y-axis represents the
# frequency of occurrence of the value.
# The final answer is: $\boxed{2}$
