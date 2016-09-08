#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ciudadanos import models as ciudadanos
# Create your models here.


class RegistroProS(models.Model):
    ciudadano = models.ForeignKey(ciudadanos.Ciudadano)
    diploma = models.FileField("Copia del diploma", upload_to='diploma')
    acta = models.FileField("Copia del acta de grado", upload_to='acta')
    cedula = models.FileField("Copia ampliada (150) de la cedula de ciudadania", upload_to='cedula')
    resolucion = models.FileField("resolucion de nombramiento del servicio social obligatorio", upload_to='resolucion')
    rural = models.FileField("Acta posesion del rural", upload_to='rural')
    certificado = models.FileField("Certificado de culiminacion del año rural", upload_to='certificado')
    tramitado = models.BooleanField(default=False)
    fecha = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Registro Profecional"
        verbose_name_plural = "Registros Profecionales"
    # end class

    def __unicode__(self):
        return u"Registro Profecional %s %s"%(self.ciudadano.first_name, self.ciudadano
        )
# end class


class RegistroProN(models.Model):
    ciudadano = models.ForeignKey(ciudadanos.Ciudadano)
    diploma = models.FileField("Copia del diploma", upload_to='diploma')
    acta = models.FileField("Copia del acta de grado", upload_to='acta')
    cedula = models.FileField("Copia ampliada (150) de la cedula de ciudadania", upload_to='cedula')
    tramitado = models.BooleanField(default=False)
    fecha = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Registro Profecionale(que no hacen rural)"
        verbose_name_plural = "Registros Profecionales(que no hacen rural)"
    # end class

    def __unicode__(self):
        return u"Registro Profecionale(que no hacen rural) de %s %s"%(self.ciudadano.first_name, self.ciudadano
        )
# end class


class TarjetaPro(models.Model):
    ciudadano = models.ForeignKey(ciudadanos.Ciudadano)
    registro = models.FileField("Registro profesional", upload_to='registro')
    cedula = models.FileField("Copia ampliada (150) de la cedula de ciudadania", upload_to='cedula')
    sellos = models.FileField("Copia de los sellos del diploma", upload_to='sellos')
    tramitado = models.BooleanField(default=False)
    fecha = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Tarjeta Profesional"
        verbose_name_plural = "Tarjetas Profecionales"
    # end class

    def __unicode__(self):
        return u"Registro Tarjeta profecional de %s %s" % (self.ciudadano.first_name, self.ciudadano.last_name)
    # end def
# end class


class Pasaporte(models.Model):
    ciudadano = models.ForeignKey(ciudadanos.Ciudadano)
    cedula = models.FileField("Copia ampliada (150) de la cedula de ciudadania", upload_to='cedula')
    foto = models.ImageField(upload_to="foto")
    tramitado = models.BooleanField(default=False)
    fecha = models.DateField(auto_now=True)

    def __unicode__(self):
        return u"Registro de pasaporte de %s %s"%(self.ciudadano.first_name, self.ciudadano.last_name)
    # end def
# end class
