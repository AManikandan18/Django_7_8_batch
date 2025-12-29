from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Student,Department,Employee,Author,Book,Student_ser,Student_Signals
from .serializers import StudentSerializer

from rest_framework.viewsets import ModelViewSet
# from rest_framework import viewsets

# Create your views here.

def home(request):
    return HttpResponse("Welcome to Django")

#Insert:
# Student.objects.create(name = "Arul Prakash",age = 23)

# data = Student.objects.all() #QuerySet
# print("Object Format : ",data)


#Select all objects:
# Student.objects.all()

#Where :
# select * from Student where age = 23;

# Student.objects.filter(age=23)

#Get Single Record(Limit):
# SELECT * FROM Student WHERE id = 1 LIMIT 1;

# Student.objects.get(id=1)

#Update :
# UPDATE employee SET age = 30 WHERE id = 1;

# std = Student.objects.get(id=1)
# std.age = 30
# std.save()

#Delete :
# delete from student where id = 1 ;

# std = Student.objects.get(id=1)
# std.delete()

#QuerySet:
# data = Student.objects.all()
# print("Object Format : ",data)

#Department table value:
# it = Department.objects.create(name="IT")
# hr = Department.objects.create(name="HR")
# finance = Department.objects.create(name="Finance")
# sales = Department.objects.create(name="Sales")


#Employee table value:
# Employee.objects.create(name="Mani", department=it)
# Employee.objects.create(name="Arun", department=it)
# Employee.objects.create(name="Ravi", department=it)

# Employee.objects.create(name="Kumar", department=hr)
# Employee.objects.create(name="Suresh", department=hr)

# Employee.objects.create(name="Anitha", department=finance)
# Employee.objects.create(name="Divya", department=finance)

# Employee.objects.create(name="Vijay", department=sales)
# Employee.objects.create(name="Ajith", department=sales)
# Employee.objects.create(name="Surya", department=sales)

# employees = Employee.objects.all()
# for e in employees:
#     print(e.department.name)
    
    
# employees = Employee.objects.select_related('department')
# for e in employees:
#     print(e.department.name)
    
    
# Prefetch Related:
# a1 = Author.objects.create(name="Author One")
# a2 = Author.objects.create(name="Author Two")
# a3 = Author.objects.create(name="Author Three")
# a4 = Author.objects.create(name="Author Four")
# a5 = Author.objects.create(name="Author Five")


# b1 = Book.objects.create(title="Python Basics")
# b2 = Book.objects.create(title="Django Guide")
# b3 = Book.objects.create(title="REST API Design")
# b4 = Book.objects.create(title="Web Development")
# b5 = Book.objects.create(title="Backend Mastery")


    
# books = Book.objects.all() #1 query for books (select * from book;)
# for b in books:
#     print(b.authors.all()) #N queries for each book’s authors
    
    # SELECT * FROM author WHERE book_id = 1;
    # SELECT * FROM author WHERE book_id = 2;
    # SELECT * FROM author WHERE book_id = 3;
    
    
# books = Book.objects.prefetch_related('authors')
# for b in books:
#     print(b.authors.all())
    
#    1. SELECT * FROM book;
#    2. SELECT * FROM author 
#       INNER JOIN book_authors
#       WHERE book_id IN (1, 2, 3);

# ✔ Only 2 queries
# ✔ No DB hit inside loop


class StudentViewSet(ModelViewSet):
    queryset = Student_ser.objects.all() #For Read All Data(Display)
    serializer_class = StudentSerializer

# Student_ser.objects.create(name = 'kavin',age = 23,course = 'Java')


# Signals Value Inserted:
# Student_Signals.objects.create(name = "Arul",age = 22)