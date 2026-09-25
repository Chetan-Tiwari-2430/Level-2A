import pandas as pd

data = pd.read_csv("Student.csv")
# Find count, mean, max, min.

result = data.groupby("Gender").agg(
    Count = ("Marks","count"),
    Mean = ("Marks","mean"),
    Minimum = ("Marks","min"),
    Maximum = ("Marks","max")
).astype(int)
print(result)