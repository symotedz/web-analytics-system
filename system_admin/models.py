from django.db import models

# Create your models here.
class Super_Admin_User(models.Model):
    name = models.CharField(max_length=255)
    Registration_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.BooleanField(default=True, blank=True, null=True)
    End_Date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

class School(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(Super_Admin_User, on_delete=models.CASCADE)
    Registration_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.BooleanField(default=True, null=True, blank=True)
    End_Date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    County = models.CharField(max_length=255,blank=True, null=True)
    location = models.CharField(max_length=255,blank=True, null=True)
    contact = models.CharField(max_length=255,blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    