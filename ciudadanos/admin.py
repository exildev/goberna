from django.contrib import admin
from exile_ui.admin import admin_site, ExStacked, ExTabular, DateRangeEX
from sorl.thumbnail.admin import AdminImageMixin
import forms
import models
# Register your models here.


class CiudadanoAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'identificacion',
                    'telefono', 'fijo', 'fecha_nacimiento', 'avatar')
    search_fields = ('username', 'email', 'first_name',
                     'last_name', 'identificacion', 'telefono')
    list_filter = (('fecha_nacimiento', DateRangeEX),)
    form = forms.CiudadanoForm

    class Media:
        js = ("ciudadanos/js/validation.js",)
    # end class
# end class

admin_site.register(models.Departamento)
admin_site.register(models.Municipio)
admin_site.register(models.Ciudadano, CiudadanoAdmin)
