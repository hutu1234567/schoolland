# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-31 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studygame', '0004_auto_20171031_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='编号')),
                ('name', models.CharField(max_length=20, verbose_name='名称')),
                ('subject', models.CharField(choices=[('001', '语文'), ('002', '英语'), ('003', '数学')], max_length=4, verbose_name='科目')),
                ('describe', models.CharField(max_length=100, verbose_name='描述')),
                ('reward', models.IntegerField(max_length=2, verbose_name='赏金')),
            ],
            options={
                'verbose_name': '任务',
                'verbose_name_plural': '任务',
            },
        ),
        migrations.AlterField(
            model_name='vocabulary',
            name='subject',
            field=models.CharField(choices=[('001', '语文'), ('002', '英语'), ('003', '数学')], max_length=4, verbose_name='科目'),
        ),
    ]
