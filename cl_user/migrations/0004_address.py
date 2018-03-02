# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-27 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cl_user', '0003_user_usex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('reciver', models.CharField(help_text='收件人', max_length=20)),
                ('sheng', models.CharField(default='', max_length=8)),
                ('shi', models.CharField(default='', max_length=16)),
                ('qu', models.CharField(default='', max_length=16)),
                ('detialaddr', models.CharField(default='', max_length=100)),
                ('rphone', models.CharField(default='', max_length=11)),
                ('yzbm', models.CharField(default='150001', max_length=6)),
                ('mrdz', models.BooleanField(default='0', max_length=1)),
                ('scbz', models.BooleanField(default='0', max_length=1)),
            ],
        ),
    ]
