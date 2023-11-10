from datetime import datetime
import csv 

from web_super_admin.models import *

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        self.overall_grade = sum(grades) / len(grades)

    def get_overall_grade(self):
        return self.overall_grade


def read_data(filename):
    students = []
    with open(filename, "r") as f:
        for line in f:
            name, *grades = line.strip().split(",")
            grades = [float(grade) for grade in grades]
            students.append(Student(name, grades))

    return students

def analyze_data(students):
    student_grades = []
    class_grades = []

    for student in students:
        student_grades.append(student.get_overall_grade())
    student_average_grade = sum(student_grades) / len(student_grades)

    for class_ in students:
        class_grades.append(class_.get_average_grade())
    class_average_grade = sum(class_grades) / len(class_grades)

    return student_average_grade, class_average_grade

def main():
    filename = "data.csv"
    students = read_data(filename)

    student_average_grade, class_average_grade = analyze_data(students)

    print("Student average grade:", student_average_grade)
    print("Class average grade:", class_average_grade)

if __name__ == "__main__":
    main()
