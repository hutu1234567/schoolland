# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-03 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studygame', '0012_auto_20171103_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='subject',
            field=models.CharField(choices=[('001', '语文'), ('002', '英语'), ('003', '数学'), ('301', '美术'), ('302', '音乐'), ('301', '体育'), ('601', '记忆'), ('602', '劳动')], max_length=4, verbose_name='科目'),
        ),
        migrations.AlterField(
            model_name='task',
            name='url',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='vocabulary',
            name='subject',
            field=models.CharField(choices=[('001', '语文'), ('002', '英语'), ('003', '数学'), ('301', '美术'), ('302', '音乐'), ('301', '体育'), ('601', '记忆'), ('602', '劳动')], max_length=4, verbose_name='科目'),
        ),
    ]
