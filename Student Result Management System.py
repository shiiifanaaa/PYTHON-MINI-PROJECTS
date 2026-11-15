print("====== STUDENT RESULT MANAGEMENT SYSTEM ======")

name = input("Enter student name: ")
roll = input("Enter roll number: ")

maths = float(input("Enter Mathematics marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))
english = float(input("Enter English marks: "))
computer = float(input("Enter Computer Science marks: "))

if (maths < 0 or maths > 100 or
    physics < 0 or physics > 100 or
    chemistry < 0 or chemistry > 100 or
    english < 0 or english > 100 or
    computer < 0 or computer > 100):

    print("Invalid marks! Enter marks between 0 and 100.")

else:
    total = maths + physics + chemistry + english + computer

    percentage = total / 5

    average = total / 5

    if (maths < 40 or physics < 40 or
        chemistry < 40 or english < 40 or computer < 40):

        grade = "F"
        result = "FAIL"

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

    print("\n====== STUDENT REPORT ======")

    print("Student Name:", name)
    print("Roll Number:", roll)
    print("Total Marks:", total, "/ 500")
    print("Percentage:", percentage, "%")
    print("Average:", average)
    print("Grade:", grade)
    print("Result:", result)

print("====== END OF REPORT ======")
