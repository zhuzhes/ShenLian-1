# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-02-25 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class_Model_Model1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MgtIP', models.CharField(max_length=60)),
                ('SystemID', models.CharField(max_length=60)),
                ('LicenseLevel', models.CharField(max_length=60)),
            ],
        ),
    ]
