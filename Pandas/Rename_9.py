import pandas as pd


data = pd.read_csv("Student.csv")
result = data.rename(columns = {"Marks" : "Number"})
print(result)