from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)
    joining_date=models.DateField(max_length=200)
    gender=models.CharField(max_length=200)
    dob=models.DateField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    employee_image=models.ImageField(upload_to='images',default='images/default.jpg',blank=True)
    address=models.CharField(max_length=200)
    salary=models.CharField(max_length=200)
    about=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.employee_name
