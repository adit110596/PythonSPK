# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-27 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0027_auto_20180726_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='karyawan',
            name='kecerdasan',
        ),
        migrations.RemoveField(
            model_name='karyawan',
            name='masakerja',
        ),
        migrations.RemoveField(
            model_name='karyawan',
            name='pendidikanterakhir',
        ),
        migrations.RemoveField(
            model_name='karyawan',
            name='prilaku',
        ),
        migrations.RemoveField(
            model_name='karyawan',
            name='sikapkerja',
        ),
        migrations.AddField(
            model_name='kecerdasan',
            name='karyawan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kecerdasans', to='orm.Karyawan'),
        ),
        migrations.AddField(
            model_name='masakerja',
            name='karyawan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='masakerjas', to='orm.Karyawan'),
        ),
        migrations.AddField(
            model_name='pendidikanterakhir',
            name='karyawan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pendidikanterkahirs', to='orm.Karyawan'),
        ),
        migrations.AddField(
            model_name='prilaku',
            name='karyawan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prilakus', to='orm.Karyawan'),
        ),
        migrations.AddField(
            model_name='sikapkerja',
            name='karyawan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sikapkerjas', to='orm.Karyawan'),
        ),
    ]
