# Student Marks Analyzer
import numpy as np

def is_pass(nums):
    is_student_pass = True

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
    [1, 12, 45, 78, 23, 56],
    [2, 91, 34, 67, 89, 10],
    [3, 43, 76, 21, 54, 88],
    [4, 65, 19, 92, 37, 41],
    [5, 28, 83, 49, 71, 15],
    [6, 57, 32, 86, 24, 69],
    [7, 11, 64, 38, 95, 47],
    [8, 79, 26, 53, 18, 84],
    [9, 35, 72, 14, 61, 97],
    [10, 48, 90, 31, 66, 22]])


total_marks = np.sum(students_marks[:,1:],axis = 0)
average_marks = total_marks // students_marks.shape[0]
