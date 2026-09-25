import pandas as pd
import numpy as np

data = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
                   111, 112, 113, 114, 115],
    
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Vikas",
             "Neha", "Arjun", "Pooja", "Rohan", "Anjali",
             "Karan", "Simran", "Aditya", "Meena", "Varun"],
    
    "Department": ["IT", "CSE", "ECE", "IT", "ME",
                   "CSE", "IT", "ECE", "CSE", "ME",
                   "IT", "CSE", "ECE", "IT", "ME"],
    
    "Age": [20, 21, 20, 19, 22,
            21, 20, 23, 21, 22,
            22, 20, 21, 22, 23],
    
    "Marks": [85, 92, 78, 88, 73,
              95, 67, 81, 90, 74,
              86,73, 79, 91, 72],
    
    "Attendance": [90, 95, 82, 88, 75,
                   96, 98, 85, 92, 78,
                   89, 94, 80, 91, 76],
    
    "City": ["Bhopal", "Indore", "Delhi", "Bhopal", "Mumbai",
             "Delhi", "Indore", "Bhopal", "Mumbai", "Delhi",
             "Bhopal", "Indore", "Mumbai", "Delhi", "Bhopal"]
})

# Calculate The Marks By Department
result = data.groupby("Department")["Marks"].mean().astype(int)
print("Marks By the Departments: \n",
result
)
