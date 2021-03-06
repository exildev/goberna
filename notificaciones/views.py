#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from django.core import serializers
from connections import HOST, WEB_PORT, IO_PORT
from datetime import datetime, timedelta, date
from django.core.serializers.json import DjangoJSONEncoder
from exile_ui.admin import admin_site
from goberna.settings import EXILE_UI
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from actividades import models as actividades
from django.contrib.auth.decorators import login_required
from personal import models as personal

import croniter
import urllib2
import json


def verify(request, session_id):
    session = Session.objects.get(session_key=session_id)
    uid = session.get_decoded().get('_auth_user_id')
    usertypes = [personal.Empleado, User, ]
    for tipo in usertypes:
        user = tipo.objects.filter(pk=uid).first()
        if user:
            print "http://%s:%d/?data=" % (HOST, WEB_PORT) + session_id
            socket_id = urllib2.urlopen(
                "http://%s:%d/?data=" % (HOST, WEB_PORT) + session_id).read()
            response = {'socket_id': socket_id,
                        'type': tipo.__name__, 'webuser': user.username}
            return HttpResponse(json.dumps(response))
        # end if
    # end if
    return HttpResponse(uid)
# end def

def test_email(request, reporte):
    reporte = reportes.Reporte.objects.all()[0]
    return render(request, 'notificaciones/email.html', reporte.__dict__)
# edn def

@login_required(login_url="/dashboard/login/")
def schedule(request):

    menu_list = admin_site.get_app_list(request)
    tipos = actividades.TipoActividad.objects.all()
    piscinas = usuarios.Piscina.objects.all()
    piscineros = usuarios.Piscinero.objects.all()
    clientes = usuarios.Cliente.objects.all()
    obj = {
        'menu_list': menu_list,
        'user': request.user,
        'funcname': 'Calendario',
        'model': 'Actividades',
        'tipos': tipos,
        'piscinas': piscinas,
        'piscineros': piscineros,
        'clientes': clientes,
        'data': dict(request.GET.iterlists())
    }
    extra_context = dict(dict(obj).items() + EXILE_UI['media'].items())
    return render(request, 'notificaciones/schedule.html', extra_context)
# edn def

def calendar(request):

    start = request.GET.get('start', False)
    end = request.GET.get('end', False)
    novedad_select = request.GET.get('novedad_select', '0')
    print "este es", start
    return 1
    dates = []
    now = datetime.now()

    if start and isinstance(start, unicode) and start.isdigit():
        start = datetime.fromtimestamp(int(start))
    else:
        try:
            print start
            parts = start.split('-')
            start = datetime(int(parts[0]), int(parts[1]) + 1, int(parts[2]))
        except Exception as e:
            print e
        # end try
    # end if
    if end and isinstance(end, unicode) and end.isdigit():
        end = datetime.fromtimestamp(int(end))
    else:
        try:
            parts = end.split('-')
            end = datetime(int(parts[0]), int(parts[1]) + 1, int(parts[2]))
        except Exception as e:
            print e
        # end try
    # end if
    key = request.GET.get('key', False)
    
    if start and end:
        if novedad_select == '0' or novedad_select == '1':
            #dates = dates + activities(request, start, end, now)
            pass
        # end if
    # end if
    #return HttpResponse(json.dumps(dates, cls=DjangoJSONEncoder), content_type="application/json")
# end def

def seguimientos(request, start, end, now):
    dates = []
    iseguimientos = gestion_cartera.InicioSeguimiento.objects.filter(fecha_proxima__gte=start, fecha_proxima__lte=end)
    seguimientos  = gestion_cartera.Seguimiento.objects.filter(fecha_proxima__gte=start, fecha_proxima__lte=end)

    cliente = request.GET.get('cliente', '0')
    if cliente != '0':
        seguimientos = seguimientos.filter(cliente=int(cliente))
    # end if

    for seguimiento in seguimientos:
        if seguimiento.fecha_proxima:
            dates.append({
                'pk': seguimiento.id,
                'color': 'green',
                'title': "%s, %s" % (seguimiento.comentario, str(seguimiento.inicio.cliente)),
                'now': now.strftime("%Y-%m-%d %I:%M%p"),
                'start': seguimiento.fecha_proxima.strftime("%Y-%m-%d %I:%M%p"),
                "_send_to_": ['Gerente', 'Asistente'],
                "urli": reverse('admin:%s_%s_change' % (seguimiento._meta.app_label,  seguimiento._meta.model_name),  args=[seguimiento.pk]),
                'type': 'Seguimiento'
            })
        # end if        
    # end for
    for seguimiento in iseguimientos:
        if seguimiento.fecha_proxima:
            dates.append({
                'pk': seguimiento.id,
                'color': 'green',
                'title': "%s, %s" % (seguimiento.comentario, str(seguimiento.cliente)),
                'now': now.strftime("%Y-%m-%d %I:%M%p"),
                'start': seguimiento.fecha_proxima.strftime("%Y-%m-%d %I:%M%p"),
                "urli": reverse('admin:%s_%s_change' % (seguimiento._meta.app_label,  seguimiento._meta.model_name),  args=[seguimiento.pk]),
                "_send_to_": ['Gerente', 'Asistente'],
                'type': 'InicioSeguimiento'
            })
        # end if
    return dates
# end def

def cumpleanios(request, start, end, now):
    usuari = [usuarios.Asistente, usuarios.Gerente, usuarios.Piscinero]
    dates = []
    for users in usuari:
        userlist = users.objects.all()
        for user in userlist:
            str_cron = "0 7 %s %s *" % (user.fecha_nacimiento.day, user.fecha_nacimiento.month)
            print str_cron
            cron = croniter.croniter(str_cron, datetime.combine(start, datetime.min.time()))
            nextdate = start
            while nextdate <= end:
                nextdate = cron.get_next(datetime)
                print nextdate
                if nextdate >= now:
                    color = 'pink'
                else:
                    color = 'gray'
                # end if
                dates.append({
                    'pk': user.pk,
                    'color': color,
                    'cron': str_cron,
                    'title': "Hoy cumple %s %s" % (user.first_name, user.last_name),
                    'now': now.strftime("%Y-%m-%d %I:%M%p"),
                    'start': nextdate.strftime("%Y-%m-%d"),
                    'urli': reverse('admin:%s_%s_change' % (user._meta.app_label,  user._meta.model_name),  args=[user.pk]),
                    "_send_to_": ['Gerente'],
                    'type': 'Cumple'
                })
            # end while
        # end if
    # end for
    return dates
# end def


def activities(request, start, end, now):
    emplado = personal.Empleado.objects.filter(pk = request.user.pk)

    acts = models.Actividad.objects.all()

    if emplado and emplado.cargo:
        acts = acts.filter(Q(departamentos__pk=emplado.cargo.departamento.pk) | Q(personas__pk=emplado.pk))
    # end if

    dates = []
    for act in acts:
        if datetime.combine(act.fecha_de_ejecucion, datetime.min.time()) >= now:
            color = act.tipo_de_actividad.color
        else:
            color = 'gray'
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

def error(request):
    return "error"
# end def

def connections(request):
    return HttpResponse("%s:%s" % (HOST, IO_PORT))
# end def
