# How to Remove rows in Numpy array that contains non-numeric values?

import numpy as np

arr=np.array([[10.5,22.5,3.8],
              [41,np.nan,np.nan]])

print("Given array")
print(arr)


print("Remove all rows containing NaN values ")
cleaned_array=arr[~np.isnan (arr).any (axis=1)]
print(cleaned_array)