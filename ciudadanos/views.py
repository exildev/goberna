from django.shortcuts import render, HttpResponseRedirect
from supra import views as supra
import forms
import models

# Create your views here.
supra.SupraConf.ACCECC_CONTROL["allow"] = True


class LoginSupra(supra.SupraSession):
    model = models.Ciudadano
    template_name = "ciudadanos/login.html"

    def form_valid(self, form):
        instance = form.save()
        for inline in self.validated_inilines:
            inline.instance = instance
            inline.save()
        # end for
        return HttpResponseRedirect('/')
    # end def

    def form_invalid(self, form):
        errors = dict(form.errors)
        print errors
        for i in self.invalided_inilines:
			errors['inlines'] = list(i.errors)
		# end for
        return render(self.request, self.template_name, {"form": form})
    # end def
# end class


class RegistroSupra(supra.SupraFormView):
    model = models.Ciudadano
    form_class = forms.CiudadanoForm
    template_name = "ciudadanos/registro.html"
# end class
