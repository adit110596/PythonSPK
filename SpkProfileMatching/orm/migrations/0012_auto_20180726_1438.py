# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-26 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0011_sikapkerja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='karyawan',
            name='nama',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
