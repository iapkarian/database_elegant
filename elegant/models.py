# -*- coding: utf-8 -*-

import datetime

from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField('Прізвище', max_length=100)
    phone = models.IntegerField('Телефон')
    birth = models.DateField('Дата народження', )
    recommendation = models.TextField('Рекомендації', blank=True)
    diagnosis = models.TextField('Дiагноз', max_length=100, blank=True, null=True)
    complaint = models.TextField('Скарги', max_length=500, blank=True, null=True)
    allergy = models.TextField('Алергiя', max_length=200, blank=True, null=True)
    note = models.TextField('Примiтки', max_length=500, blank=True, null=True)

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
    description = models.TextField('Опис процедури', max_length=500, blank=True, null=True)

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


class News_section(models.Model):
    name = models.CharField('Назва', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Новини(роздiли)'


class News(models.Model):
    section = models.ForeignKey(News_section)
    title_news = models.CharField('Назва', max_length=50)
    text_news = models.TextField('Опис', blank=True)
    image_news = models.ImageField(upload_to='uploads/', null=True, blank=True)
    created = models.DateTimeField('Дата розміщення', default=datetime.datetime.now)

    def __str__(self):
        return self.title_news

    class Meta:
        verbose_name_plural = 'Новини'

    def get_absolute_url(self):
        return "/news/%i/" % self.id

class Price_category(models.Model):
    num_category = models.IntegerField('Номер порядку: ')
    category = models.CharField('Категорiя', max_length=20)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Категорії процедур'


class Price(models.Model):
    category = models.ForeignKey(Price_category)
    name = models.CharField('Назва процедури', max_length=40)
    duration = models.PositiveIntegerField('Тривалiсть', max_length=15)
    price = models.PositiveIntegerField('Цiна', max_length=15)
    CURRENCY_CHOICES = (
        ('грн', 'UAH',),
        ('$', 'USD', ),
        ('€', 'EUR',),
    )
    currency = models.CharField('Валюта', max_length=5, choices=CURRENCY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Цiни'



