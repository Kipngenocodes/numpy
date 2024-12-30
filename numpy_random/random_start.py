import numpy as np

# Generate a random number between 0 and 1
random_number = np.random.rand(30)

print("Random number:", random_number)

# Generate a random number between 1 and 100
random_number1 = np.random.randint(1, 100)
print("Random number between 1 and 100:", random_number1)


# Generate a random number between 1 and 100 with size 5
random_number2 = np.random.randint(1, 100, size=(5,6))
print("Random number between 1 and 100 with size 5:", random_number2)

# Generate a random number from array using choice
random_number3 = np.random.choice([1049, 2, 364, 4, 500])
print("Random number from array:", random_number3)

