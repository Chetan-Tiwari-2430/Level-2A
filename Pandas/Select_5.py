# Select Only the Name and the Marks Column
import pandas as pd

data = pd.read_csv("Student.csv")
print("Only Name And Marks: \n",
data[["Name","Marks"]].to_string(index = False)
)