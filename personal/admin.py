from django.contrib import admin
import nested_admin
import forms
import models
from exile_ui.admin import admin_site, ExStacked, ExTabular
from question import models as question
from question import forms as form_question
# Register your models here.

"""
Requerimiento R013
"""


class PrengustasDepartamento(ExTabular):
    model = question.Pregunta
    extra = 0
    form = form_question.QuestionFormAdmin

    def get_queryset(self, request):
        print 'llego a el query'
        qs = super(PrengustasDepartamento, self).get_queryset(request)
        return qs
    # end def
# end class


class DepartamentoAdmin(nested_admin.NestedModelAdmin):
    list_display = ('nombre',)
    search_fields = list_display
    inlines = [PrengustasDepartamento]


class EmpleadoAdmin(nested_admin.NestedModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',
                    'direccion', 'telefono', 'fecha_nacimiento')
    search_fields = list_display

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = forms.EmpleadoEditForm
        # end if
        return super(EmpleadoAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def


admin_site.register(models.Empleado, EmpleadoAdmin)
admin_site.register(models.Departamento, DepartamentoAdmin)
admin_site.register(models.Cargo)
admin_site.register(models.Jefes)
