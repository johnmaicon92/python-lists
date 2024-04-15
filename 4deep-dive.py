"""
4. Deep Dive into Python Lists
Objective:
The aim of this assignment is to integrate various list operations and methods to solve a complex problem.

Problem Statement:
You're organizing a school event, and you have lists containing student names, their grades, and the activities they're interested in.

Task 1: Given the lists:

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
Filter out students who have grades below 80. Print the name, grade and activity. Expected Outcome "Jane", 78, "Art"

Task 2: For the remaining students, add students name in a new list named students_approved. Expected Outcome: students_approved = ["John", "Doe", "Smith"]

Task 3: Print the list students_approved
"""

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

list_of_dicts = [{'student' : 'John', 'grade' : 85, 'activity' : 'Football'}, {'student' : 'Doe', 'grade' : 90, 'activity' : 'Music'}, {'student' : 'Jane', 'grade' : 78, 'activity' : 'Art'}, {'student' : 'Smith', 'grade' : 88, 'activity' : 'Dance'}]
target_key = 'grade'
filtered_list = list(filter(lambda x: x[target_key] < 80, list_of_dicts))
print(filtered_list)

list_of_dicts = [{'student' : 'John', 'grade' : 85, 'activity' : 'Football'}, {'student' : 'Doe', 'grade' : 90, 'activity' : 'Music'}, {'student' : 'Jane', 'grade' : 78, 'activity' : 'Art'}, {'student' : 'Smith', 'grade' : 88, 'activity' : 'Dance'}]
target_key = 'grade'
approved_list = list(filter(lambda x: x[target_key] > 80, list_of_dicts))
print(approved_list)
