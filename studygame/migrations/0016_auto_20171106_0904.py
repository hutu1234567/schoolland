# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-06 01:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studygame', '0015_auto_20171103_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='vocabulary',
            name='can_know',
            field=models.BooleanField(default=False, verbose_name='能认识'),
        ),
        migrations.AddField(
            model_name='vocabulary',
            name='can_use',
            field=models.BooleanField(default=False, verbose_name='会使用'),
        ),
        migrations.AddField(
            model_name='vocabulary',
            name='can_write',
            field=models.BooleanField(default=False, verbose_name='会拼写'),
        ),
        migrations.AddField(
            model_name='vocabulary',
            name='passed',
            field=models.BooleanField(default=False, verbose_name='已通关'),
        ),
    ]
