# -*- coding: utf-8 -*-

from django.db import models


class Person(models.Model):
    registration_number = models.CharField(max_length=10)
    last_name = models.CharField(max_length = 30)
    first_name = models.CharField(max_length = 30)
    birth_date = models.DateField()
    email = models.EmailField()
    home_phone_number = models.CharField(max_length = 20)
    cell_phone_number = models.CharField(max_length = 20)
    # Dans un cas réel, nous ne devrions pas stocker le mot de passe en clair.
    password = models.CharField(max_length=32)
    
    