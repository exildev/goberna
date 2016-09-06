#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from exile_ui.widgets import DatePickerWidget
import models
from django.contrib.auth.models import User
from exile_ui.widgets import AdminImageWidget
from django.contrib.auth.models import Permission, Group


class CiudadanoForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CiudadanoForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"
        self.fields['fecha_nacimiento'].widget = DatePickerWidget(
            attrs={'class': 'date'},
            format="%m/%d/%Y")
        self.fields['fecha_nacimiento'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y')
        self.fields['telefono'].widget = forms.NumberInput()
        self.fields['identificacion'].widget = forms.NumberInput()
    # end def

    class Meta:
        model = models.Ciudadano
        fields = ['username', 'password1', 'password2', 'email', 'first_name',
                  'last_name', 'identificacion', 'fijo', 'telefono', 'fecha_nacimiento', 'municipio', 'direccion', 'imagen']
    # end class

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen', False)
        if imagen:
            if hasattr(imagen, '_size') and imagen._size > 1 * 1024 * 1024:
                raise forms.ValidationError(
                    "El tamaño de la imagen no puede ser superior a 1 mega")
            # end if
            return imagen
        # end if
    # end def

    def save(self, commit=True):
        usuario = super(CiudadanoForm, self).save(commit)
        usuario.is_staff = True
        grupo, created = Group.objects.get_or_create(name="Ciudadanos")
        """
        if created:
            add = Permission.objects.filter(name="Can add reporte").first()
            change = Permission.objects.filter(
                name="Can change reporte").first()
            fotos = Permission.objects.filter(
                name__icontains="Foto de reporte")
            grupo.permissions.add(add, change)
            for f in fotos:
                grupo.permissions.add(f)
            # end for
            grupo.save()
        usuario.save()
        usuario.groups.add(grupo)
        """
        return usuario
    # end def
# end class
