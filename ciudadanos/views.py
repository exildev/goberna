from django.shortcuts import render
from supra import views as supra
import forms
import models

# Create your views here.
supra.SupraConf.ACCECC_CONTROL["allow"] = True


class LoginSupra(supra.SupraSession):
    model = models.Ciudadano
    template_name = "ciudadanos/login.html"
# end class


class RegistroSupra(supra.SupraFormView):
    model = models.Ciudadano
    form_class = forms.CiudadanoForm
    template_name = "ciudadanos/registro.html"
# end class
