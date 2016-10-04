#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from exile_ui.admin import admin_site, ExStacked, ExTabular, DateRangeEX, DateRangeEX
import models
import forms

class TipoActividadAdmin(admin.ModelAdmin):
    form = forms.TipoActividadForm
    list_display = ('nombre', )
    serarch_fields = list_display
# end class

class ActividadAdmin(admin.ModelAdmin):
    form = forms.ActividadForm
    list_display = ('nombre', 'lugar', 'objeto', 'tipo_de_actividad', 'fecha_de_ejecucion',)
    serarch_fields = ('nombre',)
    list_filter = ('tipo_de_actividad', ('fecha_de_ejecucion', DateRangeEX), )
# end class

admin_site.register(models.TipoActividad, TipoActividadAdmin)
admin_site.register(models.Actividad, ActividadAdmin)
admin_site.register(models.Lugar)
