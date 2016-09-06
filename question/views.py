from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from . import models as models
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic.edit import FormView
from django.views.generic import CreateView
import forms
# Create your views here.


class PreguntaView(CreateView):
    model = models.Pregunta
    template_name = 'question/addpregunta.html'
    fields = ['email', 'departamento', 'pregunta']
    success_url = '/preguntas/add/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(PreguntaView, self).form_valid(form)
# end class
