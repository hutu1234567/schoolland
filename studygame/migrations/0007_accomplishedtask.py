# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-02 06:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studygame', '0006_auto_20171102_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccomplishedTask',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('completion_date', models.CharField(max_length=8, verbose_name='完成日期')),
                ('actual_reward', models.IntegerField(verbose_name='赏金')),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studygame.Task')),
            ],
        ),
    ]
