import numpy as np
import matplotlib.pyplot as plt

# Parameters for the normal distribution
mean = 0  # Mean (mu) of the distribution
std_dev = 1  # Standard deviation (sigma) of the distribution
num_samples = 1000  # Number of samples to generate

# Generate random numbers from a normal distribution
samples = np.random.normal(mean, std_dev, num_samples)

# Plot the histogram of the samples
plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')

# Plot the probability density function (PDF) of the normal distribution
x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
pdf = (1/(std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean)/std_dev)**2)
plt.plot(x, pdf, 'r', linewidth=2)

# Add labels and title
plt.title('Normal Distribution (Gaussian Distribution)')
plt.xlabel('Value')
plt.ylabel('Probability Density')

# Show the plot
plt.show()