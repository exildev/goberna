#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from personal import models as personal

class TipoActividad(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Tipo de reunión"
        verbose_name_plural = "Tipo de reuniones"
    # end class

    def __unicode__(self):
        return u'%s' % self.nombre
    # end def
# end class

class Lugar(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return u'%s' % self.nombre
    # end def
# end class

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    lugar = models.ForeignKey(Lugar, null=True)
    objeto = models.TextField("Objeto de la reunión", max_length=400)
    tipo_de_actividad = models.ForeignKey(TipoActividad, verbose_name="Tipo de reunion")
    fecha_de_ejecucion = models.DateField()
    #repetir_cada = models.CharField(max_length=100, default=0)
    #unidad_de_repeticion = models.IntegerField(choices=((3, "Mes(es)", ), (4, "Año(s)", ), ), null=True, blank=True, default=3)
    departamentos = models.ManyToManyField(personal.Departamento, blank=True, )
    personas = models.ManyToManyField(personal.Persona, blank=True, )

    class Meta:
        verbose_name = "Reunión"
        verbose_name_plural = "Reuniones"
    # end class

    def __unicode__(self):
        return u'%s' % self.nombre
    # end def
# end class
