# Add bonus 5 marks to all of the students
import numpy as np
marks = np.array([20,30,40,5,78,90,98,95])
updated_marks = np.where(marks <= 95,marks + 5,marks)
print("Updated Marks",updated_marks)