# Student Marks Analyzer
import numpy as np

def is_pass(nums):
    #is_pass_student = np.array([])
    rows = nums.shape[0]
    pass_list = np.zeros(rows)
    for i in range(rows):
        arr = nums[i,1:]
        is_passed = np.where(arr >= 35,True,False)
        if False in is_passed:
            pass_list[i] = 0
        else:
            pass_list[i] = 1

    return int(sum(pass_list))
        
        

names = {
    1: "Aarav",
    2: "Vihaan",
    3: "Aditya",
    4: "Rohan",
    5: "Kabir",
    6: "Arjun",
    7: "Ishaan",
    8: "Reyansh",
    9: "Vivaan",
    10: "Kunal"
}

students_marks = np.array([
    [1, 62, 45, 78, 94, 56],
    [2, 91, 44, 67, 89, 50],
    [3, 43, 76, 21, 54, 88],
    [4, 65, 19, 92, 37, 41],
    [5, 28, 83, 49, 71, 15],
    [6, 57, 72, 86, 84, 69],
    [7, 51, 64, 78, 95, 47],
    [8, 79, 78, 53, 68, 84],
    [9, 35, 72, 14, 61, 97],
    [10, 48, 90, 31, 66, 22]])


total_marks = np.sum(students_marks[:,1:],axis = 0)
average_marks = total_marks // students_marks.shape[0]
total_passed_students = is_pass(students_marks)
print("Total Passes Student: ",total_passed_students)