import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr) # Output: array([1, 2, 3, 4, 5])

print(arr + 2) # Output: array([3, 4, 5, 6, 7])

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2) # Output: array([5, 7, 9])

# built-in functionality for mean, sum, etc
arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr)) # Output: 15
print(np.mean(arr)) # Output: 3.0

multi_dim_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(multi_dim_arr)