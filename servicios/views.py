from django.shortcuts import render
from supra import views as supra
import models
import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
supra.SupraConf.ACCECC_CONTROL["allow"] = True

class RegistroProSSupra(supra.SupraFormView):
    model = models.RegistroProS
    template_name = "servicios/registropros.html"
    form_class = forms.RegisterProSForm

    @method_decorator(login_required(login_url="/ciudadanos/login/"))
    def dispatch(self, request, *args, **kwargs):
        return super(RegistroProSSupra, self).dispatch(request, *args, **kwargs)
    # end def
# end class

class RegistroProNSupra(supra.SupraFormView):
    model = models.RegistroProN
    template_name = "servicios/registropros.html"
    form_class = forms.RegisterProNForm

    @method_decorator(login_required(login_url="/ciudadanos/login/"))
    def dispatch(self, request, *args, **kwargs):
        return super(RegistroProNSupra, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class TarjetaSupra(supra.SupraFormView):
    model = models.TarjetaPro
    template_name = "servicios/tarjetapro.html"
    form_class = forms.TarjetaProForm

    @method_decorator(login_required(login_url="/ciudadanos/login/"))
    def dispatch(self, request, *args, **kwargs):
        return super(TarjetaSupra, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class PasaporteSupra(supra.SupraFormView):
    model = models.Pasaporte
    template_name = "servicios/pasaporte.html"
    form_class = forms.PasaporteForm

    @method_decorator(login_required(login_url="/ciudadanos/login/"))
    def dispatch(self, request, *args, **kwargs):
        return super(PasaporteSupra, self).dispatch(request, *args, **kwargs)
    # end def
# end class
