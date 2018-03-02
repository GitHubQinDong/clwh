# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-06 05:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cl_goods', '0007_auto_20180204_1048'),
        ('cl_user', '0004_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cl_goods.GoodInfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cl_user.User')),
            ],
        ),
    ]
