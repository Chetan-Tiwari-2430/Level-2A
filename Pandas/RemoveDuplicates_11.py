import pandas as pd

data = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul", "Amit", "Sneha", "Priya", "Vikas"],
    "Age": [20, 21, 22, 20, 23, 21, 24],
    "Marks": [85, 90, 78, 85, 88, 90, 92]
})

result = data
# Remove Duplicates inn the Data Frame
# data[data.duplicated()]
data.drop_duplicates(inplace = True)
print(data)

