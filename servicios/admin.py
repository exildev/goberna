from django.contrib import admin
from exile_ui.admin import admin_site, ExStacked, ExTabular, DateRangeEX
import models
# Register your models here.


class ProSAdmin(admin.ModelAdmin):
    list_display = ('ciudadano', 'diploma', 'acta', 'cedula', 'resolucion', 'rural', 'certificado', 'fecha', 'tramitado')
    search_fields = ('ciudadano__first_name', 'ciudadano__last_name', 'ciudadano__indentificacion')
    list_editable = ('tramitado',)
# end class


class ProNAdmin(admin.ModelAdmin):
    list_display = ('ciudadano', 'diploma', 'acta', 'cedula', 'fecha', 'tramitado')
    search_fields = ('ciudadano__first_name', 'ciudadano__last_name', 'ciudadano__indentificacion')
    list_editable = ('tramitado',)
# end class


class TarjetaAdmin(admin.ModelAdmin):
    list_display = ('ciudadano', 'registro', 'cedula', 'sellos', 'fecha', 'tramitado')
    search_fields = ('ciudadano__first_name', 'ciudadano__last_name', 'ciudadano__indentificacion')
    list_editable = ('tramitado',)
# end class


class Pasaporte(admin.ModelAdmin):
    list_display = ('ciudadano', 'cedula', 'foto', 'fecha', 'tramitado')
    search_fields = ('ciudadano__first_name', 'ciudadano__last_name', 'ciudadano__indentificacion')
    list_editable = ('tramitado',)
# end class


admin_site.register(models.RegistroProS, ProSAdmin)
admin_site.register(models.RegistroProN, ProNAdmin)
admin_site.register(models.TarjetaPro, TarjetaAdmin)
admin_site.register(models.Pasaporte, Pasaporte)
