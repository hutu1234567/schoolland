# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-03 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studygame', '0009_accomplishedtask_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accomplishedtask',
            name='desc',
            field=models.CharField(max_length=100, verbose_name='描述'),
        ),
    ]
