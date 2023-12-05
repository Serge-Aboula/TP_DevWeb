# -*- coding: utf-8 -*-

from django.db import models

class Person(models.Model):
    registration_number = models.CharField(max_length=10)
    last_name = models.CharField(max_length = 30)
    first_name = models.CharField(max_length = 30)
    birth_date = models.DateField()
    email = models.EmailField()
    home_phone_number = models.CharField(max_length = 20)
    cellphone_number = models.CharField(max_length = 20)
    # Dans un cas réel, nous ne devrions pas stocker le mot de passe en clair.
    password = models.CharField(max_length=32)
    friends = models.ManyToManyField('self')
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)

class Message(models.Model):
    author = models.ForeignKey('Person', on_delete=models.CASCADE)
    content = models.TextField()
    publication_date = models.DateField()

class Faculty(models.Model):
    name = models.CharField(max_length = 30)
    color = models.CharField(max_length = 6)
    
class Campus(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 60)
    
class Job(models.Model):
    title = models.CharField(max_length = 30)
    
class Cursus(models.Model):
    title = models.CharField(max_length = 30)
    
class Employee(Person):
    office = models.CharField(max_length = 30)
    campus = models.ForeignKey('Campus', on_delete=models.CASCADE)
    job = models.ForeignKey('Job', on_delete=models.CASCADE)

class Student(Person):
    cursus = models.ForeignKey('Cursus', on_delete=models.CASCADE)
    year = models.IntegerField()
