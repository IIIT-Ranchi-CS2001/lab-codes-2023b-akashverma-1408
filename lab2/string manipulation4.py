name = input("Enter the student name: ")
roll_num = input("Enter the roll number: ")
marks = float(input("Enter the mathematics marks out of 100: "))

if marks >= 90:
    grade_point = 10
    remark = "Outstanding"
elif 80 <= marks < 90:
    grade_point = 9
    remark = "Very Good"
elif 70 <= marks < 80:
    grade_point = 8
    remark = "Good"
elif 60 <= marks < 70:
    grade_point = 7
    remark = "Average"
elif 50 <= marks < 60:
    grade_point = 6
    remark = "Pass"
else:
    grade_point = 0
    remark = "Fail"

print("Name:", name)
print("Roll Number:", roll_num)
print("Marks:", marks)
print("Grade Point:", grade_point)
print("Remark:", remark)

