'''Question1: Student Grades Processing
You need to write a Python program to process student grades. The program should perform the following functions:

Use a dictionary to store the information and grades of 10 students. Each student should have a name, surname, and grades (Midterm, Final, and Oral grades).
'''

students = {
    'Aysima Coskun':  [90, 85, 75],
    'Suheyb Coskun':  [35, 60, 50],
    'Guluzar Coskun': [68, 88, 78],
    'Derya Seker': [65, 87,86],
    'Gamze Yilmaz': [78, 88, 78],
    'Ahmet Furkan': [88, 66, 56],
    'Elif SEN': [78, 58, 88],
    'Ender Yilmaz': [77, 88, 67],
    'Dilan Demir': [99, 88, 77],
    'Duygu Seker': [69, 88, 78]
}

#1-Calculate the average grade for each student and add it to the dictionary.

def calculate_average(grades):
    return sum(grades) / len(grades)

names = students.keys()

for name in names:
    #I assigned both the grades and the average to variables for later use.
    
    student_grades = students[name]
    average = int(calculate_average(student_grades))
    students[name] = {'average': average, 'grades': student_grades}
print(students)

#2-Find and print the student with the highest average grade.

highest_average_grade = 0
student_with_highest_average_grade = ""

for name in students:
    average = students[name]['average']
    if average > highest_average_grade:
        highest_average_grade = average
        student_with_highest_average_grade = name
print("Student with the highest average grade: {}".format(student_with_highest_average_grade))



#3-Separate each student's name and surname and store them in a separate tuple, then add them to a list.


list_of_tuple_names = []
for name in students:
    name_list = tuple(name.split())
    list_of_tuple_names.append(name_list)
print(list_of_tuple_names)
    

#4-Sort the names in alphabetical order and print the sorted list.

print(sorted(names))
    
#5-Store the students with an average grade below 70 in a set.

set_of_students = set([])
for name in students:
    if students[name]['average'] < 70 :
        set_of_students.add(name)
    
print(set_of_students)