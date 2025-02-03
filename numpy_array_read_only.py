#How to make a NumPy array read-only?

"""
Let’s discuss how to make NumPy array immutable i.e that can not be rewritten or can’t be changed. This can be done by setting a writable flag of the NumPy array to false.

Syntax:

array.flags.writable=False

"""

import numpy as np
a=np.zeros(11)
print("Print array before reading")
print(a)

a[1]=2
print("print after changing the second element")
print(a)

a.setflags(write=False)
print("After applying read only function")
a[1]=7