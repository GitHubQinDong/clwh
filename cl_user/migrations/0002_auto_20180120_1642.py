# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-20 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uemil',
            field=models.EmailField(default='', max_length=30),
        ),
    ]
