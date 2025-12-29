from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
class Department(models.Model):
    name = models.CharField(max_length=50)

class Employee(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


#Select Related:

class Department(models.Model):
    name = models.CharField(max_length=50)

class Employee(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
# Prefetch Related:

class Author(models.Model):
    name = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)

# class Departments(models.Model):
#     name = models.CharField(max_length = 50)
    
#     def __str__(self):
#         return self.name
    
# class Employees(models.Model):
#     name = models.CharField(max_length = 50)
#     age = models.IntegerField()
#     salary = models.DecimalField(max_digits=10,decimal_places= 2)
#     department = models.ForeignKey(
#         Departments,
#         on_delete= models.CASCADE,
#         related_name='employees'
#     )
    
#     def __str__(self):
#         return self.name

class Student_ser(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    course = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

#Signals :
class Student_Signals(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name
    