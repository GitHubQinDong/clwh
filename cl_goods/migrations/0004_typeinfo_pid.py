# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-02 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_goods', '0003_auto_20180202_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeinfo',
            name='pid',
            field=models.IntegerField(default=0),
        ),
    ]