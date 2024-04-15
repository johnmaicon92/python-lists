'''
Objective:
The aim of this assignment is to practice advanced list operations and transformations.

Problem Statement:
You've been given a list of numerical grades from a class exam. You need to process and analyze these grades.

Task 1: Given the list of grades:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
Sort the grades in descending order and display the sorted list.

Task 2: Calculate the average grade and display it.

Task 3: Replace any grade below 80 with the value Failed.
'''

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse = True)

print(grades)



sorted_grades = [95, 93, 90, 89, 88, 85, 80, 78, 76, 72]
def average(sorted_grades):
    return sum(sorted_grades) / len(sorted_grades)
average = average(sorted_grades)
print(average)



sorted_grades = [95, 93, 90, 89, 88, 85, 80, 78, 76, 72]
sorted_grades = ["failed" if x < 80 else x for x in sorted_grades]
print(sorted_grades)