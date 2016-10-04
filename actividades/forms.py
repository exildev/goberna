#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms

import models
from exile_ui.widgets import DatePickerWidget, MapWidget
import widgets


class TipoActividadForm(forms.ModelForm):
    color = forms.CharField(widget=forms.TextInput(attrs={'type': 'color'}))

    class Meta:
        model = models.TipoActividad
        exclude = ()
    # end class
# end class


class ActividadForm(forms.ModelForm):

    class Meta:
        model = models.Actividad
        exclude = ()
        
    # end class

# end class

class ActividadFormEdit(forms.ModelForm):

    class Meta:
        model = models.Actividad
        fields = ['fecha_de_ejecucion']
        widgets = {
            "fecha_de_ejecucion": DatePickerWidget(attrs={'class': 'date'}, format="%m/%d/%Y")
        }
    # end class

# end class
