# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 19:15:15 2026

@author: muham
"""

print("STUDENT GRADE CALCULATOR")

name = input("Enter student name: ")

maths = int(input("Enter Mathematics mark: "))
physics = int(input("Enter Physics mark: "))
chemistry = int(input("Enter Chemistry mark: "))
english = int(input("Enter English mark: "))
computer = int(input("Enter Computer Science mark: "))

if (maths < 0 or maths > 100 or
    physics < 0 or physics > 100 or
    chemistry < 0 or chemistry > 100 or
    english < 0 or english > 100 or
    computer < 0 or computer > 100):

    print("Invalid marks! Enter marks between 0 and 100.")

else:
    total = maths + physics + chemistry + english + computer

    percentage = total / 5

    if maths < 40 or physics < 40 or chemistry < 40 or english < 40 or computer < 40:
        result = "FAIL"
        grade = "F"

    elif percentage >= 90:
        grade = "A"
        result = "PASS"

    elif percentage >= 80:
        grade = "B"
        result = "PASS"

    elif percentage >= 70:
        grade = "C"
        result = "PASS"

    elif percentage >= 60:
        grade = "D"
        result = "PASS"

    elif percentage >= 50:
        grade = "E"
        result = "PASS"

    else:
        grade = "F"
        result = "FAIL"

    print("\n------ STUDENT REPORT ------")

    print("Student Name:", name)
    print("Total Marks:", total, "/ 500")
    print("Percentage:", percentage, "%")
    print("Grade:", grade)
    print("Result:", result)