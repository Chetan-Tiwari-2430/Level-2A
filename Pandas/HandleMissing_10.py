import pandas as pd
import numpy as np

information = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Vikas"],
    "Age": [20, 22, 22, 21, 49],
    "Salary": [25000, np.nan, 30000, 28000, np.nan]
}
data = pd.DataFrame(information)
result = data

result["Salary"] = data["Salary"].fillna(data["Salary"].mean()).astype(int)
print(result)
