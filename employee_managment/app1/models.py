from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length = 100, null = False)
    location = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length = 100, null=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    First_name = models.CharField(max_length = 100, null= False)
    Last_name = models.CharField(max_length = 100)
    Dept = models.ForeignKey(Department, on_delete = models.CASCADE)
    Salary = models.IntegerField()
    role = models.ForeignKey(Role, on_delete = models.CASCADE)
    phone = models.IntegerField()
    Hire_date = models.DateField()


    def __str__(self):
        return "%s %s %s" %(self.First_name, self.Last_name, self.phone)
