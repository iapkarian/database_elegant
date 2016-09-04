from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    birth = models.DateField()
    note = models.TextField(blank=True)

class Drug(models.Model):
    name = models.CharField(max_length=50)

class Medication(models.Model):
    drug = models.ForeignKey(Drug)
    data_start = models.DateField()
    data_end = models.DateField()
    client = models.ForeignKey(Client)

class Procedure_name(models.Model):
    name = models.CharField(max_length=50)

class Procedure_type(models.Model):
    procedure_name = models.ForeignKey(Procedure_name)
    prime_cost = models.IntegerField()
    cost = models.IntegerField()
    consumable = models.IntegerField()

class Procedure(models.Model):
    client = models.ForeignKey(Client)
    procedure = models.ForeignKey(Procedure_type)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
