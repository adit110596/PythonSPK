# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-26 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0002_auto_20180726_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kecerdasan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sistematika_berfikir', models.IntegerField(blank=True, max_length=5, null=True)),
                ('konsentrasi', models.IntegerField(blank=True, max_length=5, null=True)),
                ('logika_praktis', models.IntegerField(blank=True, max_length=5, null=True)),
                ('imajinasi_kreatif', models.IntegerField(blank=True, max_length=5, null=True)),
                ('antisipasi', models.IntegerField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'kecerdasan',
                'ordering': ['id'],
            },
        ),
    ]
