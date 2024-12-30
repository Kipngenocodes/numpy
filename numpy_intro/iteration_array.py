import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# for x in np.nditer(arr[:, ::2]):
#   print(x)


arry1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arry2 = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
for x, y in np.nditer([arry1, arry2]):
  print(x, y)


for idx, x in np.ndenumerate(arry1):
  print(idx, x)