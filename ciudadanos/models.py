#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class

class Municipio(models.Model):
    nombre = models.CharField(max_length=200)
    departamento = models.ForeignKey(Departamento)
    
    def __unicode__(self):
        return u"%s" % (self.nombre)
    # end def
# end class


class Ciudadano(User):
    identificacion = models.CharField(max_length=200, unique=True)
    direccion = models.CharField(max_length=120, verbose_name="Dirección")
    telefono = models.CharField(
        max_length=15, verbose_name="Teléfono", blank=True, null=True)
    fijo = models.CharField(
        max_length=15, verbose_name="Fijo", blank=True, null=True)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    imagen = models.ImageField(upload_to="avatar", null=True, blank=True)
    municipio = models.ForeignKey(Municipio)

    class Meta:
        verbose_name = "Ciudadano"
        verbose_name_plural = "Ciudadanos"
    # end class

    def avatar(self):
        if self.imagen:
            imagen = self.imagen
        else:
            imagen = 'account.svg'
        # end if
        return '<img class="image-cicle" src="/media/%s" />' % (imagen)
    # end def

    avatar.allow_tags = True

    def __unicode__(self):
        return u"%s %s - %s" % (self.first_name, self.last_name, self.identificacion)
    # end def
# end class
