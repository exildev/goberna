#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from django.core.urlresolvers import reverse
from exile_ui.admin import admin_site
from supra import views as supra
from personal import models as personal
import models
import forms
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta, date
import croniter
import urllib2
import json
from goberna.settings import EXILE_UI
from django.db.models import Q


class TipoActividadFormView(supra.SupraFormView):
    model = models.TipoActividad
    form_class = forms.TipoActividadForm
# end class

class TipoActividadListView(supra.SupraListView):
    model = models.TipoActividad
    list_display = ('nombre', 'pk')
    serarch_fields = list_display
# end class

class LugarListView(supra.SupraListView):
    model = models.Lugar
    list_display = ('nombre', 'pk')
    serarch_fields = list_display
# end class

class ActividadFormView(supra.SupraFormView):
    model = models.Actividad
    form_class = forms.ActividadForm
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ActividadFormView, self).dispatch(request, *args, **kwargs)
    # end def
# end class

class ActividadFormEditView(supra.SupraFormView):
    model = models.Actividad
    form_class = forms.ActividadFormEdit
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ActividadFormEditView, self).dispatch(request, *args, **kwargs)
    # end def
# end class


class ActividadListView(supra.SupraListView):
    model = models.Actividad
    list_display = ('nombre', 'descripacion', 'cliente', 'tipo_de_actividad', 'fecha_de_ejecucion', 'fecha_de_notificacion')
    serarch_fields = list_display
# end class

class ActividadDetailView(supra.SupraDetailView):
    model = models.Actividad
    fields = ('nombre', 'tipo_de_actividad', 'fecha_de_ejecucion', 'departamentos', 'personas', 'lugar')
# end class

@login_required(login_url="/dashboard/login/")
def schedule(request):

    menu_list = admin_site.get_app_list(request)

    obj = {
        'menu_list': menu_list,
        'user': request.user,
        'funcname': 'Calendario',
        'model': 'Actividades',
        'data': dict(request.GET.iterlists())
    }
    extra_context = dict(dict(obj).items() + EXILE_UI['media'].items())
    return render(request, 'schedule.html', extra_context)
# edn def

def calendar(request):
    start = request.GET.get('start', False)
    end = request.GET.get('end', False)
    novedad_select = request.GET.get('novedad_select', '0')

    dates = []
    now = datetime.now()

    if start and isinstance(start, unicode) and start.isdigit():
        start = datetime.fromtimestamp(int(start))
    else:
        try:
            print start
            parts = start.split('-')
            start = datetime(int(parts[0]), int(parts[1]) + 0, int(parts[2]))
        except Exception as e:
            print e
        # end try
    # end if
    if end and isinstance(end, unicode) and end.isdigit():
        end = datetime.fromtimestamp(int(end))
    else:
        try:
            parts = end.split('-')
            end = datetime(int(parts[0]), int(parts[1]) + 0, int(parts[2]))
        except Exception as e:
            print e
        # end try
    # end if
    key = request.GET.get('key', False)
    if start and end:
        if novedad_select == '0' or novedad_select == '1':
            dates = dates + activities(request, start, end, now)
        # end if
    # end if
    return HttpResponse(json.dumps(dates, cls=DjangoJSONEncoder), content_type="application/json")
# end def



def activities(request, start, end, now):

    emplado = personal.Empleado.objects.filter(pk = request.user.pk)

    acts = models.Actividad.objects.all().order_by('fecha_de_ejecucion')

    if emplado and emplado.cargo:
        acts = acts.filter(Q(departamentos__pk=emplado.cargo.departamento.pk) | Q(personas__pk=emplado.pk))
    # end if

    dates = []
    for act in acts:
        if datetime.combine(act.fecha_de_ejecucion, datetime.min.time()) >= now:
            color = act.tipo_de_actividad.color
        else:
            color = '#757575'
        # end if
        dates.append({
            'pk': act.id,
            'color': color,
            'title': "%s" % (act.nombre, ),
            'now': now.strftime("%Y-%m-%d %I:%M%p"),
            'start': act.fecha_de_ejecucion.strftime("%Y-%m-%d"),
            "urli": reverse('admin:%s_%s_change' % (act._meta.app_label,  act._meta.model_name),  args=[act.pk]),
            "lugar": act.lugar.nombre,
            'type': 'Actividad'
        })
    # end for
    return dates
# end def

def get_cron(instance):
    cron = ""
    if "dias[" in instance.repetir_cada:  # dias de la semana
        cron = "0 7 * * %s" % (instance.repetir_cada.replace(
            "dias[", "").replace("]", ""), )
    elif "mes[" in instance.repetir_cada:  # dias del mes
        cron = "0 7 %s * *" % (instance.repetir_cada.replace(
            "mes[", "").replace("]", ""), )
    else:
        if int(instance.repetir_cada) <= 0:
            instance.repetir_cada = '1'
            instance.save()
        # end if
        if instance.unidad_de_repeticion == 3:  # intervalo mensual
            cron = "0 7 %s */%s *" % ('%(dia)s', instance.repetir_cada, )
        elif instance.unidad_de_repeticion == 4:  # intervalo anual
            cron = "0 7 %s %s/%d *" % ('%(dia)s', '%(mes)s', int(instance.repetir_cada) * 12, )
        # end if
    return cron % {
        'dia': instance.fecha_de_ejecucion.day,
        'mes': instance.fecha_de_ejecucion.month,
        'dia_semana': instance.fecha_de_ejecucion.weekday()
    }
# end def
