# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-07 00:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='pregunta',
            field=models.TextField(max_length=2000),
        ),
    ]