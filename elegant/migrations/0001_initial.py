# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('birth', models.DateField()),
                ('note', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_start', models.DateField()),
                ('data_end', models.DateField()),
                ('client', models.ForeignKey(to='elegant.Client')),
                ('drug', models.ForeignKey(to='elegant.Drug')),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_start', models.DateTimeField()),
                ('time_end', models.DateTimeField()),
                ('client', models.ForeignKey(to='elegant.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Procedure_name',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Procedure_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prime_cost', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('consumable', models.IntegerField()),
                ('procedure_name', models.ForeignKey(to='elegant.Procedure_name')),
            ],
        ),
        migrations.AddField(
            model_name='procedure',
            name='procedure',
            field=models.ForeignKey(to='elegant.Procedure_type'),
        ),
    ]
