# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-31 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studygame', '0003_auto_20171031_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='count',
            field=models.IntegerField(max_length=20, null=True, verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=20, verbose_name='名称'),
        ),
    ]
