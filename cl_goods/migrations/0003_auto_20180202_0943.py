# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-02 01:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cl_goods', '0002_auto_20180202_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodinfo',
            name='gtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cl_goods.TypeInfo'),
        ),
    ]
