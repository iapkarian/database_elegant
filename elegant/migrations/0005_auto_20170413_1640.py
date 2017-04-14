# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 13:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elegant', '0004_auto_20170122_0237'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='News_section',
        #     fields=[
        #         ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('name', models.CharField(max_length=20, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0')),
        #     ],
        #     options={
        #         'verbose_name_plural': '\u041d\u043e\u0432\u0438\u043d\u0438(\u0440\u043e\u0437\u0434i\u043b\u0438)',
        #     },
        # ),
        migrations.AddField(
            model_name='price',
            name='currency',
            field=models.CharField(blank=True, choices=[(b'\xd0\xb3\xd1\x80\xd0\xbd', b'UAH'), (b'$', b'USD'), (b'\xe2\x82\xac', b'EUR')], max_length=5, null=True, verbose_name=b'\xd0\x92\xd0\xb0\xd0\xbb\xd1\x8e\xd1\x82\xd0\xb0'),
        ),
        migrations.AddField(
            model_name='news',
            name='section',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='elegant.News_section'),
            preserve_default=False,
        ),
    ]
