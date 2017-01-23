# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('elegant', '0003_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0 \xd0\xbf\xd1\x80\xd0\xbe\xd1\x86\xd0\xb5\xd0\xb4\xd1\x83\xd1\x80\xd0\xb8')),
                ('duration', models.CharField(max_length=15, verbose_name=b'\xd0\xa2\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb0\xd0\xbbi\xd1\x81\xd1\x82\xd1\x8c')),
                ('price', models.CharField(max_length=15, verbose_name=b'\xd0\xa6i\xd0\xbd\xd0\xb0')),
            ],
            options={
                'verbose_name_plural': '\u0426i\u043d\u0438',
            },
        ),
        migrations.CreateModel(
            name='Price_category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_category', models.IntegerField(verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xbf\xd0\xbe\xd1\x80\xd1\x8f\xd0\xb4\xd0\xba\xd1\x83: ')),
                ('category', models.CharField(max_length=20, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80i\xd1\x8f')),
            ],
            options={
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0456\u0457 \u043f\u0440\u043e\u0446\u0435\u0434\u0443\u0440',
            },
        ),
        migrations.AddField(
            model_name='client',
            name='allergy',
            field=models.TextField(max_length=500, null=True, verbose_name=b'\xd0\x90\xd0\xbb\xd0\xb5\xd1\x80\xd0\xb3i\xd1\x8f', blank=True),
        ),
        migrations.AddField(
            model_name='client',
            name='complaint',
            field=models.TextField(max_length=500, null=True, verbose_name=b'\xd0\xa1\xd0\xba\xd0\xb0\xd1\x80\xd0\xb3\xd0\xb8', blank=True),
        ),
        migrations.AddField(
            model_name='client',
            name='diagnosis',
            field=models.TextField(max_length=500, null=True, verbose_name=b'\xd0\x94i\xd0\xb0\xd0\xb3\xd0\xbd\xd0\xbe\xd0\xb7', blank=True),
        ),
        migrations.AddField(
            model_name='client',
            name='recommendation',
            field=models.TextField(verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xba\xd0\xbe\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb4\xd0\xb0\xd1\x86\xd1\x96\xd1\x97', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='birth',
            field=models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbd\xd0\xb0\xd1\x80\xd0\xbe\xd0\xb4\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'\xd0\x9f\xd1\x80\xd1\x96\xd0\xb7\xd0\xb2\xd0\xb8\xd1\x89\xd0\xb5'),
        ),
        migrations.AlterField(
            model_name='client',
            name='note',
            field=models.TextField(max_length=500, null=True, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xbci\xd1\x82\xd0\xba\xd0\xb8', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.IntegerField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='data_end',
            field=models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbai\xd0\xbd\xd1\x86\xd1\x8f \xd0\xbf\xd1\x80\xd0\xb8\xd0\xb9\xd0\xbe\xd0\xbc\xd1\x83'),
        ),
        migrations.AlterField(
            model_name='medication',
            name='data_start',
            field=models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd0\xbe\xd1\x87\xd0\xb0\xd1\x82\xd0\xba\xd1\x83 \xd0\xbf\xd1\x80\xd0\xb8\xd0\xb9\xd0\xbe\xd0\xbc\xd1\x83'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xbe\xd0\xb7\xd0\xbc\xd1\x96\xd1\x89\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text_news',
            field=models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81', blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='title_news',
            field=models.CharField(max_length=50, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='time_end',
            field=models.DateTimeField(verbose_name=b'\xd0\xa7\xd0\xb0\xd1\x81 \xd0\xbai\xd0\xbd\xd1\x86\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='time_start',
            field=models.DateTimeField(verbose_name=b'\xd0\xa7\xd0\xb0\xd1\x81 \xd0\xbf\xd0\xbe\xd1\x87\xd0\xb0\xd1\x82\xd0\xba\xd1\x83'),
        ),
        migrations.AlterField(
            model_name='procedure_name',
            name='description',
            field=models.CharField(max_length=500, null=True, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81 \xd0\xbf\xd1\x80\xd0\xbe\xd1\x86\xd0\xb5\xd0\xb4\xd1\x83\xd1\x80\xd0\xb8', blank=True),
        ),
        migrations.AlterField(
            model_name='procedure_name',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0 \xd0\xbf\xd1\x80\xd0\xbe\xd1\x86\xd0\xb5\xd0\xb4\xd1\x83\xd1\x80\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='procedure_type',
            name='cost',
            field=models.IntegerField(verbose_name=b'\xd0\x92\xd0\xb0\xd1\x80\xd1\x82i\xd1\x81\xd1\x82\xd1\x8c \xd0\xb4\xd0\xbb\xd1\x8f '),
        ),
        migrations.AlterField(
            model_name='procedure_type',
            name='prime_cost',
            field=models.IntegerField(verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xb1i\xd0\xb2\xd0\xb0\xd1\x80\xd1\x82i\xd1\x81\xd1\x82\xd1\x8c'),
        ),
        migrations.AddField(
            model_name='price',
            name='category',
            field=models.ForeignKey(to='elegant.Price_category'),
        ),
    ]
