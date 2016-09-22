from django.shortcuts import render
from supra import views as supra
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import models
 
class Login(supra.SupraSession):
    model = models.Empleado
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Login, self).dispatch(request, *args, **kwargs)
    # end def
# end class

class PersonaListView(supra.SupraListView):
	list_display = ['identificacion', 'direccion', 'fecha_nacimiento', 'telefono', 'first_name', 'last_name', 'pk']
	model = models.Persona
	
# end class

class DepartamentoListView(supra.SupraListView):
	model = models.Departamento
	list_display = ['nombre', 'codigo', 'activo', 'pk', ]
	list_filter = list_display

# end class

