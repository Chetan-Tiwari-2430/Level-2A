import numpy as np
students_marks = np.random.randint(1,100,size= (30,5))
shape = students_marks.shape
sum = sum(students_marks)
avg = sum // shape[0]
print("Total Marks: ",sum)
print("Average Marks: ",avg)