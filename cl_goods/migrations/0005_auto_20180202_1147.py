# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-02 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_goods', '0004_typeinfo_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodinfo',
            name='gprice',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]