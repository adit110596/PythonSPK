# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-26 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0004_masakerja'),
    ]

    operations = [
        migrations.AddField(
            model_name='masakerja',
            name='lima_delapanthn',
            field=models.IntegerField(blank=True, max_length=5, null=True),
        ),
    ]
