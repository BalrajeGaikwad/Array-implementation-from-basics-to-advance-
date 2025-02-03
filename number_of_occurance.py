#Find the number of occurrences of a sequence in a NumPy array

import numpy as np

arr=[[[2, 8, 9, 4],  
    [9, 4, 9, 4], 
    [4, 5, 9, 7], 
    [2, 9, 4, 3]]]

output=repr(arr).count("9, 4")

print(output)