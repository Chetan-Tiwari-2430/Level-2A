# Multiple Two Compatible Matrices
import numpy as np 
a = np.array([
    [1,2,3,9],
    [4,5,6,9],
    [7,8,9,9]
])

b = np.array([
    [6,7],
    [8,9],
    [10,11],
    [12,13]
])
# check the Matrix Is Compatible or Not 

if a.shape[1] == b.shape[0]:
    print("Multiplied Matrixes: \n",np.matmul(a,b))
else:
    print("The Matrices is not Compatible")