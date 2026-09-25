import pandas as pd

data = pd.read_csv("Student.csv")
print("Sort The Student Data on the basis of Their MArks Highest To Lowest: \n",
data.sort_values("Marks",ascending = False)
)