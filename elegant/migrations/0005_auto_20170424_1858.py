# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-04-24 15:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elegant', '0004_auto_20170122_0237'),
    ]

    operations = [
        migrations.CreateModel(
            name='News_section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Назва')),
            ],
            options={
                'verbose_name_plural': 'Новини(роздiли)',
            },
        ),
        migrations.AddField(
            model_name='price',
            name='currency',
            field=models.CharField(blank=True, choices=[('грн', 'UAH'), ('$', 'USD'), ('€', 'EUR')], max_length=5, null=True, verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='client',
            name='allergy',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Алергiя'),
        ),
        migrations.AlterField(
            model_name='client',
            name='birth',
            field=models.DateField(verbose_name='Дата народження'),
        ),
        migrations.AlterField(
            model_name='client',
            name='complaint',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Скарги'),
        ),
        migrations.AlterField(
            model_name='client',
            name='diagnosis',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Дiагноз'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Прізвище'),
        ),
        migrations.AlterField(
            model_name='client',
            name='note',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Примiтки'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.IntegerField(verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='client',
            name='recommendation',
            field=models.TextField(blank=True, verbose_name='Рекомендації'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='data_end',
            field=models.DateField(verbose_name='Дата кiнця прийому'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='data_start',
            field=models.DateField(verbose_name='Дата початку прийому'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата розміщення'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text_news',
            field=models.TextField(blank=True, verbose_name='Опис'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_news',
            field=models.CharField(max_length=50, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='price',
            name='duration',
            field=models.PositiveIntegerField(max_length=15, verbose_name='Тривалiсть'),
        ),
        migrations.AlterField(
            model_name='price',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Назва процедури'),
        ),
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.PositiveIntegerField(max_length=15, verbose_name='Цiна'),
        ),
        migrations.AlterField(
            model_name='price_category',
            name='category',
            field=models.CharField(max_length=20, verbose_name='Категорiя'),
        ),
        migrations.AlterField(
            model_name='price_category',
            name='num_category',
            field=models.IntegerField(verbose_name='Номер порядку: '),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='time_end',
            field=models.DateTimeField(verbose_name='Час кiнця'),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='time_start',
            field=models.DateTimeField(verbose_name='Час початку'),
        ),
        migrations.AlterField(
            model_name='procedure_name',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Опис процедури'),
        ),
        migrations.AlterField(
            model_name='procedure_name',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Назва процедури'),
        ),
        migrations.AlterField(
            model_name='procedure_type',
            name='cost',
            field=models.IntegerField(verbose_name='Вартiсть для '),
        ),
        migrations.AlterField(
            model_name='procedure_type',
            name='prime_cost',
            field=models.IntegerField(verbose_name='Собiвартiсть'),
        ),
        migrations.AddField(
            model_name='news',
            name='section',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='elegant.News_section'),
            preserve_default=False,
        ),
    ]
