# Sum of the Row And the Columns
import numpy as np
a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("Column Sum: \t",np.sum(a,axis = 0))
print("Rows Sum: \t",np.sum(a,axis = 1))