from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    birth = models.DateField()
    note = models.TextField()

class Medication(models.Model):
    name = models.ForeignKey(Drug.name)
    data_start = models.DateField()
    data_end = models.DateField()

class Drug(models.Model):
    name = models.CharField(max_length=50)

class Procedure(models.Model):

class Procedure_name(models.Model):
    name = models.CharField(max_length=50)

class Procedure_type(models.Model):
    name = models.ForeignKey(Procedure_name.name)
    prime_cost = models.IntegerField()
    cost = models.IntegerField()

