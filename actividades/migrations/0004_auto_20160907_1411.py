# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-07 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0003_auto_20160907_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='departamentos',
            field=models.ManyToManyField(blank=True, to='personal.Departamento'),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='personas',
            field=models.ManyToManyField(blank=True, to='personal.Persona'),
        ),
    ]
