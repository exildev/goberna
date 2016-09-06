from django import forms
from goberna.middleware import get_current_user
import models
from ciudadanos import models as ciudadanos


class RegisterProSForm(forms.ModelForm):

    class Meta:
        model = models.RegistroProS
        exclude = ('ciudadano', 'tramitado')
    # end class

    def save(self, commit=False):
        pro = super(RegisterProSForm, self).save(commit)
        ciudadano = ciudadanos.Ciudadano.objects.filter(pk=get_current_user().pk).first()
        pro.ciudadano = ciudadano
        pro.save()
    # end def
# end class



class RegisterProNForm(forms.ModelForm):

    class Meta:
        model = models.RegistroProN
        exclude = ('ciudadano', 'tramitado')
    # end class

    def save(self, commit=False):
        pro = super(RegisterProNForm, self).save(commit)
        ciudadano = ciudadanos.Ciudadano.objects.filter(pk=get_current_user().pk).first()
        pro.ciudadano = ciudadano
        pro.save()
    # end def
# end class



class TarjetaProForm(forms.ModelForm):

    class Meta:
        model = models.TarjetaPro
        exclude = ('ciudadano', 'tramitado')
    # end class

    def save(self, commit=False):
        pro = super(TarjetaProForm, self).save(commit)
        ciudadano = ciudadanos.Ciudadano.objects.filter(pk=get_current_user().pk).first()
        pro.ciudadano = ciudadano
        pro.save()
    # end def
# end class



class PasaporteForm(forms.ModelForm):

    class Meta:
        model = models.Pasaporte
        exclude = ('ciudadano', 'tramitado')
    # end class

    def save(self, commit=False):
        pro = super(PasaporteForm, self).save(commit)
        print "User", get_current_user()
        ciudadano = ciudadanos.Ciudadano.objects.filter(pk=get_current_user().pk).first()
        pro.ciudadano = ciudadano
        pro.save()
    # end def
# end class
