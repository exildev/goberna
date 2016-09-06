# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-06 19:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ciudadanos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='ciudadano',
            options={'verbose_name': 'Ciudadano', 'verbose_name_plural': 'Ciudadanos'},
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='identificacion',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='municipio',
            name='departamento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ciudadanos.Departamento'),
            preserve_default=False,
        ),
    ]
