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




admin_site.register(models.TipoActividad, TipoActividadAdmin)
admin_site.register(models.Actividad)
admin_site.register(models.Lugar)
