import pandas as pd

data = pd.read_csv("Student.csv")
# Display students scoring above 75.
print("Student who Score Above than 75 marks is: \n",
data[data["Marks"] >= 75]
)