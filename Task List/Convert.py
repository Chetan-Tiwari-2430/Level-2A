import numpy

nums_1d = numpy.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
nums_2d = nums_1d.reshape((6,4))
print("1D Original Array: ",nums_1d)
print("2D Reshaped Array: \n",nums_2d)