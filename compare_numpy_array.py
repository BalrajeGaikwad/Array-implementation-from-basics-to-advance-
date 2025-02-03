#How to compare two NumPy arrays? 

"""
Here we will be focusing on the comparison done using NumPy on arrays. 
Comparing two NumPy arrays determines whether they are equivalent by checking if every element at each corresponding index is the same. 

Method 1: We generally use the == operator to compare two NumPy arrays to generate a new array object. Call ndarray.all() 
with the new array object as ndarray to return True if the two NumPy arrays are equivalent. 
"""

import numpy as np

arr1=np.array([[1,2],[3,4]])
arr2=np.array([[1,2],[3,4]])

comparsion=arr1==arr2
equal_array=comparsion.all()

print(equal_array)


"""
Method 2: We can also use greater than, less than and equal to operators to compare
"""

a=np.array([[111,333,444]])
b=np.array([[111,222,333]])

print("Array 4 :-",a)
print("Array 5 :-",b)

print("a>b")
print(np.greater(a,b))

print("a>=b")
print(np.greater_equal(a,b))

print("a<b")
print(np.less(a,b))

print("a<=b")
print(np.less_equal(a,b))



"""
Method 3: Using array_equal() 

"""

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 2], [3, 4]])


# Comparing the arrays
if np.array_equal(arr1, arr2):
	print("Equal")
else:
	print("Not Equal")
