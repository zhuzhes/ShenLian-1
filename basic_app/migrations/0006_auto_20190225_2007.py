# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-02-25 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0005_auto_20190225_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='class_model_model1',
            name='architecture_name',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='class_model_model1',
            name='board_name',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='class_model_model1',
            name='cpu',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='class_model_model1',
            name='cpu_frequency',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='class_model_model1',
            name='free_memory',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='class_model_model1',
            name='total_memory',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='class_model_model1',
            name='uptime',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='class_model_model1',
            name='version',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]