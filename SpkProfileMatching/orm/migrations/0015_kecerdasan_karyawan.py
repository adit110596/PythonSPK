# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-26 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0014_auto_20180726_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='kecerdasan',
            name='karyawan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kecerdasans', to='orm.Karyawan'),
        ),
    ]
