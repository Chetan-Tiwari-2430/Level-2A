# Multiply two compatible matrices.
import numpy as np
mat1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

mat2 = np.array([
    [10,11],
    [12,13],
    [14,15]
    
])

shape1 = mat1.shape
shape2 = mat2.shape
if shape1[1] == shape2[0]:
    print("Multiplication of two Matrix is: \n",np.matmul(mat1,mat2))
else:
    print("It is not Comparable")
