# Find the most frequent value in a NumPy array

#  bincount() method of NumPy to get the count of occurrences of each element in the array.

#argmax() method to get the value having a maximum number of occurrences(frequency).
import numpy as np

arr=([1,2,3,4,5,1,2,1,1,1])
print("original array ")
print(arr)

print("Most Frequent value in above arrayy")
print(np.bincount(arr).argmax())