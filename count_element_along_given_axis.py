#Count the number of elements along a given axis

"""
In Python, numpy.size() function count the number of elements along a given axis.
"""

import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
print("array")

print(np.size(arr))


print(np.size(arr, 0))

print(np.size(arr, 1))