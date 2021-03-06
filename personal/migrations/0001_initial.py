# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-06 23:35
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('activo', models.BooleanField(default=True)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=3)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jefes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='personal.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('identificacion', models.CharField(max_length=45)),
                ('direccion', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('telefono', models.CharField(max_length=10)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatar')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='personal.Persona')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
            bases=('personal.persona',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='cargo',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Departamento'),
        ),
        migrations.AddField(
            model_name='jefes',
            name='empleado',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='personal.Empleado'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='cargo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personal.Cargo'),
        ),
    ]
