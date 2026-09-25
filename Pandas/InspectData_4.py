import pandas as pd


data = pd.read_csv("Student.csv")
print("Head of the Data Frame: \n",data.head())
print("Tail of the Data Frame: \n",data.tail())
print("Shape of the Data Fame: \t",data.shape)
print("Information of the Data Frame: \n",data.info)
