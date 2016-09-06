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
        widgets = {
            "fecha_de_ejecucion": DatePickerWidget(attrs={'class': 'date'}, format="%m/%d/%Y"),
            "repetir_cada": widgets.IntervalWidget()
        }
    # end class

    def __init__(self, *args, **kwargs):
        super(ActividadForm, self).__init__(*args, **kwargs)
        self.fields['fecha_de_ejecucion'].input_formats = (
            '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y')
        self.fields['unidad_de_repeticion'].widgets = widgets.RepeatWidget(
            choices=self.fields['unidad_de_repeticion'].choices)
    # end def
# end class
