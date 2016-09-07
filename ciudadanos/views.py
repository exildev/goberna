from django.shortcuts import render, HttpResponseRedirect
from supra import views as supra
import forms
import models
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


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
        nex = self.request.GET.get('next', False)
        if nex:
            return HttpResponseRedirect(nex)
        return HttpResponseRedirect('/')
    # end def

    def login(self, request, cleaned_data):
		user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
		if user is not None:
			exist_obj = self.model.objects.filter(pk = user.pk).count()
			if exist_obj and user.is_active:
				login(request, user)
				return user
			#end if
		#end if
		return HttpResponseRedirect('/ciudadanos/login/')
	#end def


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


class Menu(TemplateView):
    template_name = "ciudadanos/menu.html"

    @method_decorator(login_required(login_url="/ciudadanos/login/"))
    def dispatch(self, request, *args, **kwargs):
        return super(Menu, self).dispatch(request, *args, **kwargs)
    # end def
# end class


def logoutCiudadano(request):
    logout(request)
    return HttpResponseRedirect('/')
# end def
