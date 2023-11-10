from datetime import datetime 
import csv 
import io

from web_super_admin.models import *

class Class:
    def __init__(self, name, students):
        self.name = name
        self.students = students

    def get_average_grade(self):
        average_grade = 0
        for student in self.students:
            average_grade += student.get_overall_grade()
        return average_grade / len(self.students)