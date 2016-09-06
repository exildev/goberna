from __future__ import unicode_literals

from django.db import models
from personal import models as personal

# Create your models here.


class Pregunta(models.Model):
    email = models.EmailField()
    departamento = models.ForeignKey(personal.Departamento)
    pregunta = models.CharField(max_length=2000)
    respuesta = models.CharField(max_length=2000, blank=True, null=True)
    state = models.BooleanField(default=False)

    def __unicode__(self):
        return self.email
    # end def

    class Meta:
        verbose_name = "Pregusta"
        verbose_name_plural = "Preguntas"
    # end class
# end class
