# How to check whether specified values are present in NumPy array?

"""
we use the “in” operator. “in” operator is used to check whether certain element and values are present in a given sequence and hence return Boolean values ‘True” and “False“.
"""

import numpy as np
array=np.array([[2,3,0],[4,1,6]])

print("given array")
print(array)

print(2 in array)
print(3 in array)
print(0 in array)
print(4 in array)
print( 1 in array)
print(6 in array)