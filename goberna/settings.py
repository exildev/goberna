#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Django settings for goberna project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1m60qc#1cqw+v++*mgt@k76rh(^e(42_dar&#=w1=b$c7u&!uw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mariobarrios@exile.com.co'
EMAIL_HOST_PASSWORD = 'rrljhuvayivgzmms'
ALLOWED_HOSTS = []

EXILE_UI = {
    'site_title': 'Rondax',
    'site_header': 'Rondax',
    'index_title': 'Software para las rondas operativos',
    'media': {
        'logo': {
            'dashboard': '/media/piscix_logo/Icono-f-t.png',
            'page': '/media/piscix_logo/Icono-200px.png',
            'login': '/media/piscix_logo/Icono-s-t.png'
        },
        'icons': {
            'actividades': {
                'icon': 'directions_walk',
                'groups': [
                    'Actividades',
                    'Configuración'
                ],
                'models': {
                    'Actividad': {'icon': 'event', 'group': 'Actividades'},
                    'TipoActividad': {'icon': 'settings', 'group': 'Configuración'},
                    'Lugar': {'icon': 'settings', 'group': 'Configuración'},
                },
                'menu-extra': [
                    {'name': 'Calendario', 'url': '/actividades/schedule/', 'icon': 'event', 'group': 'Actividades'}
                ]
            },
<<<<<<< HEAD
            'personal': {
                'icon': 'directions_walk',
                'groups': [
                    'Empleados'
                ],
                'models': {
                    'Empleado': {'icon': 'event', 'group': 'Empleados'},
                    'Departamento': {'icon': 'event', 'group': 'Empleados'},
                    'Cargo': {'icon': 'event', 'group': 'Empleados'},
                    'Jefes': {'icon': 'event', 'group': 'Empleados'},
                }

            },
            'question': {
                'icon': 'directions_walk',
                'groups': [
                    'Preguntas'
                ],
                'models': {
                    'Pregunta': {'icon': 'event', 'group': 'Empleados'}
                }

=======
            'ciudadanos': {
                'icon': 'people',
                'groups': [
                    'Personas',
                    'Municipio'
                ],
                'models': {
                    'Ciudadano': {'icon': 'person', 'group': 'Personas'},
                    'Departamento': {'icon': 'map','group': 'Personas' },
                    'Municipio': {'icon': 'terrain', 'group': 'Municipio'}
                }
            },
            'servicios': {
                'icon': 'accessibility',
                'groups': [
                    'Registro',
                    'Pasaporte'
                ],
                'models': {
                    'RegistroProS': {'icon': 'chrome_reader_mode', 'group': 'Registro'},
                    'RegistroProN': {'icon': 'chrome_reader_mode', 'group': 'Registro'},
                    'TarjetaPro': {'icon': 'account_box', 'group': 'Registro'},
                    'Pasaporte': {'icon': 'airplanemode_active', 'group': 'Registro'},
                }
>>>>>>> 26ac87668838a80b92745facdf2cc4fbab049017
            },
            'auth': {
                'icon': 'security',
                'groups': [
                    'Seguridad',
                ],
                'models': {
                    'Group': {'icon': 'people', 'group': 'Seguridad'},
                    'User': {'icon': 'person', 'group': 'Seguridad'}
                }
            },
            'logout': {
                'icon': 'exit_to_app',
            }
        }
    }
}

MENU_ORDER = [
    {
<<<<<<< HEAD
        'name': 'personal',
        'models': [
            'Empleado',
            'Departamento',
            'Cargo',
            'Jefes'
        ],
        'menu-extra': [
            'Calendario'
        ]
    },
    {
        'name':'actividades',
=======
        'name': 'actividades',
>>>>>>> 26ac87668838a80b92745facdf2cc4fbab049017
        'models': [
            'Actividad',
            'TipoActividad',
            'Lugar'
        ],
        'menu-extra': [
            'Calendario'
        ]
    },
    {
<<<<<<< HEAD
        'name': 'question',
        'models': [
            'Pregunta'
=======
        'name':'ciudadanos',
        'models': [
            'Ciudadano',
            'Departamento',
            'Municipio'
        ]
    },
    {
        'name': 'servicios',
        'models': [
            'RegistroProS',
            'RegistroProN',
            'TarjetaPro',
            'Pasporte'
>>>>>>> 26ac87668838a80b92745facdf2cc4fbab049017
        ]
    },
    {
        'name': 'auth',
        'models': [
            'Group',
            'User'
        ]
    },
    {
        'name': 'logout'
    }
]


# Application definition

INSTALLED_APPS = [
    'exile_ui',
    'notificaciones',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nested_admin',
    'fullcalendar',
    'supra',
    'personal',
    'ciudadanos',
    'actividades',
<<<<<<< HEAD
    'question',
=======
    'servicios'
>>>>>>> 26ac87668838a80b92745facdf2cc4fbab049017
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'notificaciones.triggers.Middleware'
]

ROOT_URLCONF = 'goberna.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'goberna.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        # Or path to database file if using sqlite3.
        'NAME': 'alcaldia',
        # The following settings are not used with sqlite3:
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
