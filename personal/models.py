from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Persona(User):
    identificacion = models.CharField(max_length=45)
    direccion = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    telefono = models.CharField(max_length=10)
    imagen = models.ImageField(upload_to="avatar", null=True, blank=True)
# end class


class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=3)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s' % (self.nombre)
    # end def
# end class


class Cargo(models.Model):
    nombre = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento)
    activo = models.BooleanField(default=True)
    descripcion = models.TextField()

    def __unicode__(self):
        return u'%s' % (self.nombre, )
    # end def
# end class


class Empleado(Persona):
    cargo = models.ForeignKey(Cargo, null=True, blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
    # end def

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
    # end class

# end class


class Jefes(models.Model):
    empleado = models.OneToOneField(Empleado, unique=True)
    departamento = models.OneToOneField(Departamento, unique=True)

    def __unicode__(self):
        return u'%s es jefe del departamento %s ' % (str(self.empleado), str(self.departamento), )
    # end def
# end class
