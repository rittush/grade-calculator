# -*- coding: utf-8 -*-
"""
Enter student name: Priya
Enter marks (0-100): 85

RESULT FOR PRIYA:
Marks: 85/100
Grade: B
Message: Very Good! Keep it up! 👍
"""
import sys
def grade(marks):
    if marks > 90 and marks <= 100:
        return "A+", "Outstanding!"
    elif marks > 80 and marks <= 90:
        return "A", "Excellent!"
    elif marks > 65 and marks <= 80:
        return "B+", "Good!"
    elif marks > 50 and marks <= 65:
        return "B", "Satisfactory!"
    else:
        return "C", "You failed in Examination"
name = input("Enter Your name ")
marks = int(input("enter your marks [0-100] "))
if marks > 100 or marks < 0:
    print("Marks cannot be more than 100 or less than 0")
    sys.exit()
print(f"Result for {name}")
grade, message = grade(marks)
print(f"Grade: {grade}")
print(message)
        
