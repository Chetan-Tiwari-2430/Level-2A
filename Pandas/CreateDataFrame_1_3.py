import pandas as pd

data = {
    "Name": ["Aarav", "Diya", "Kabir", "Ananya", "Rohan",
             "Ishita", "Arjun", "Meera", "Vivaan", "Saanvi"],
    "Age": [18, 19, 18, 20, 19, 18, 20, 19, 18, 20],
    "Gender": ["Male", "Female", "Male", "Female", "Male",
               "Female", "Male", "Female", "Male", "Female"],
    "Marks": [85, 92, 78, 88, 76, 95, 81, 89, 74, 91]
}

df = pd.DataFrame(data)
df.to_csv("Student.csv",index = False)
print(df)
