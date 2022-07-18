from django.db import models

class TEmployees(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)

    def __str__(self):
        return self.name+""+self.lastname+""+self.age+""+self.gender+""+self.department+""+self.adress+""+self.tel

class TDepartments(models.Model):
    department = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    wday = models.CharField(max_length=100)

    def __str__(self):
        return self.department+""+self.salary+""+self.wday

# Create your models here.
