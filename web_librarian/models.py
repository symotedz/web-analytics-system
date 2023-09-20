from django.db import models
from web_super_admin.models import *

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)

class Books_render(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    book_name = models.ForeignKey(Books, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    return_day = models.DateField()
    



