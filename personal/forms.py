#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm
from django import forms
from exile_ui.widgets import DatePickerWidget
from django_select2.forms import (
    HeavySelect2MultipleWidget, HeavySelect2Widget, ModelSelect2TagWidget,
    ModelSelect2Widget, Select2Widget
)
import models


class EmpleadoForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(EmpleadoForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"
        self.fields['email'].label = "Correo Electrtónico"
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellidos"
        self.fields['fecha_nacimiento'].widget = DatePickerWidget(
            attrs={'class': 'date'},
            format="%m/%d/%Y")
        self.fields['telefono'].widget = forms.NumberInput()
    # end def

    class Meta:
        model = models.Empleado
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'cargo',
                  'last_name', 'identificacion', 'direccion', 'telefono', 'fecha_nacimiento', 'imagen']
    # end class

    def save(self, commit=True):
        empleado = super(EmpleadoForm, self).save(commit)
        empleado.is_staff = True
        empleado.is_superuser =True
        empleado.save()
        return empleado
    # end def
# end class


class EmpleadoEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmpleadoEditForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Correo Electrtónico"
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellidos"
        self.fields['fecha_nacimiento'].widget = DatePickerWidget(
            attrs={'class': 'date'},
            format="%m/%d/%Y")
        self.fields['telefono'].widget = forms.NumberInput()
    # end def

    class Meta:
        model = models.Empleado
        exclude = ('password1', 'password2',)
        fields = ('username', 'email', 'first_name', 'cargo',
                  'last_name', 'identificacion', 'direccion', 'telefono', 'fecha_nacimiento', 'imagen',)

    # end class

    def save(self, commit=True):
        empleado = super(EmpleadoEditForm, self).save(commit)
        empleado.is_staff = True
        empleado.is_superuser = True
        empleado.save()
        return empleado
    # end def
# end class
