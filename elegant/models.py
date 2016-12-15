from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField('Прізвище', max_length=100)
    phone = models.IntegerField('Телефон')
    birth = models.DateField('Дата народження', )
    note = models.TextField('Рекомендації', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клієнт'
        verbose_name_plural = 'Клієнти'


class Drug(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Лiки'
        verbose_name_plural = 'Лiки'


class Medication(models.Model):
    drug = models.ForeignKey(Drug)
    data_start = models.DateField('Дата початку прийому')
    data_end = models.DateField('Дата кiнця прийому')
    client = models.ForeignKey(Client)

    def __str__(self):
        return self.drug

    class Meta:
        verbose_name = 'Прийом ліків'
        verbose_name_plural = 'Прийом ліків'


class Procedure_name(models.Model):
    name = models.CharField('Назва процедури', max_length=50)
    # photo = models.ImageField('Фото', )
    description = models.CharField('Опис процедури', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Назва процедури'
        verbose_name_plural = 'Перелiк процедур'


class Procedure_type(models.Model):
    procedure_name = models.ForeignKey(Procedure_name)
    prime_cost = models.IntegerField('Собiвартiсть')
    cost = models.IntegerField('Вартiсть для ')
    consumable = models.IntegerField('')

    def __str__(self):
        return str(self.procedure_name)

    class Meta:
        verbose_name = 'Вид процедури'
        verbose_name_plural = 'Процедури (фiнанси)'

class Procedure(models.Model):
    client = models.ForeignKey(Client)
    procedure = models.ForeignKey(Procedure_type)
    time_start = models.DateTimeField('Час початку')
    time_end = models.DateTimeField('Час кiнця')

    def __str__(self):
        return self.client.name

    class Meta:
        verbose_name = 'Процедура'
        verbose_name_plural = 'Процедури (календар клієнтiв)'
