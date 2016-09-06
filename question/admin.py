from django.contrib import admin
from django.contrib import admin
import nested_admin
import forms
import models
from exile_ui.admin import admin_site


class QuestionAdmin(nested_admin.NestedModelAdmin):
    list_display = ('email', 'pregunta')
    search_fields = list_display

    def get_queryset(self, request):
        print request.user.id
        return models.Pregunta.objects.filter(state=False, departamento__jefes__empleado__id=request.user.id)
    # end def

# Register your models here.
admin_site.register(models.Pregunta, QuestionAdmin)
