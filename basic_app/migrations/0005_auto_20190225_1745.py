# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-02-25 09:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0004_auto_20190225_0914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class_model_model1',
            old_name='LicenseLevel',
            new_name='licenselevel',
        ),
        migrations.RenameField(
            model_name='class_model_model1',
            old_name='MgtIP',
            new_name='mgtIP',
        ),
        migrations.RenameField(
            model_name='class_model_model1',
            old_name='SystemID',
            new_name='systemID',
        ),
    ]
