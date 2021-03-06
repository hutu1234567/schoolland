# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-03 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studygame', '0013_auto_20171103_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='vocabulary',
            name='book',
            field=models.CharField(blank=True, choices=[('pep3-1', '人教版三年级上'), ('pep3-2', '人教版三年级下'), ('pep4-1', '人教版四年级上'), ('pep4-2', '人教版四年级下'), ('pep5-1', '人教版五年级上'), ('pep5-2', '人教版五年级下'), ('pep6-1', '人教版六年级上'), ('pep6-2', '人教版六年级下'), ('pep7-1', '人教版七年级上'), ('pep7-2', '人教版七年级下'), ('pep8-1', '人教版八年级上'), ('pep8-2', '人教版八年级下'), ('pep9-1', '人教版九年级上'), ('pep9-2', '人教版九年级下')], max_length=20, null=True, verbose_name='教材'),
        ),
    ]
