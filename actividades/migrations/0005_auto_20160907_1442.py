# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-07 14:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0004_auto_20160907_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividad',
            name='repetir_cada',
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='unidad_de_repeticion',
        ),
    ]