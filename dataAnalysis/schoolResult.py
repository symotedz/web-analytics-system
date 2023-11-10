from datetime import datetime 
import csv 
import io 

from web_super_admin.models import *

class School:
    def __init__(self, name, classes):
        self.name = name
        self.classes = classes

    def get_average_grade(self):
        average_grade = 0
        for class_ in self.classes:
            average_grade += class_.get_average_grade()
        return average_grade / len(self.classes)