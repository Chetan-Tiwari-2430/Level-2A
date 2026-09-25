import pandas as pd
import numpy as np

data = pd.read_csv("Student.csv")
def grade(data):
    temp = np.array(data["Marks"])
    grades = np.empty(len(temp),dtype="U2")
    j = 0
    for i in temp:
        if i >= 90 and i <= 100:
            grades[j] = "A+"
        elif i >= 80 and i < 90:
            grades[j] = "A"
        elif i >= 65 and i < 80:
            grades[j] = "B"
        elif i >= 55 and i < 65:
            grades[j] = "C"
        elif i >= 33 and i < 55:
            grades[j] = "D"
        else:
            grades[j] = "F"
        
        j += 1
    data["Grade"] = grades
    


grade(data)
print(data)