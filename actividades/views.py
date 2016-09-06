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


class TipoActividadFormView(supra.SupraFormView):
    model = models.TipoActividad
    form_class = forms.TipoActividadForm

# end class


class TipoActividadListView(supra.SupraListView):
    model = models.TipoActividad
    list_display = ('nombre', )
    serarch_fields = list_display
# end class


class ActividadFormView(supra.SupraFormView):
    model = models.Actividad
    form_class = forms.ActividadForm

# end class


class ActividadListView(supra.SupraListView):
    model = models.Actividad
    list_display = ('nombre', 'descripacion', 'cliente',
                    'tipo_de_actividad', 'fecha_de_ejecucion', 'fecha_de_notificacion')
    serarch_fields = list_display
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

    operario = personal.Personal.objects.filter(pk = request.user.pk)

    acts = models.Actividad.objects.all()
    tipo_selected = request.GET.get('tipo_selected', '0')
    equipo =  request.GET.get('equipo', '0')
    turno = request.GET.get('turno', '0')

    if operario:
        acts = acts.filter(turno=operario.turno)
    # end if

    if tipo_selected != '0':
        acts = acts.filter(tipo_de_actividad=int(tipo_selected))
    # end if

    if equipo != '0':
        acts = acts.filter(equipo=int(equipo))
    # end if

    if turno != '0':
        acts = acts.filter(equipo__turno=int(turno))
    # end if


    dates = []
    for act in acts:

        if act.repetir_cada == 'no':
            dates.append({
                'pk': act.id,
                'color': act.tipo_de_actividad.color,
                'title': "%s, %s" % (act.nombre, str(act.equipo)),
                'now': now.strftime("%Y-%m-%d %I:%M%p"),
                'start': act.fecha_de_ejecucion.strftime("%Y-%m-%d"),
                "urli": reverse('admin:%s_%s_change' % (act._meta.app_label,  act._meta.model_name),  args=[act.pk]),
                'equipo': {
                    'nombre': act.equipo.nombre,
                    'descripcion': act.equipo.descripcion,
                    'turno': act.equipo.turno.nombre,
                    'unidad': {
                        'nombre': act.equipo.unidad.nombre,
                        'planta': {
                            'nombre': act.equipo.unidad.planta.nombre,
                            'ciudad': act.equipo.unidad.planta.ciudad.nombre,
                        }
                    }
                },
                'type': 'Actividad'
            })
        else:
            str_cron = get_cron(act)
            if datetime.combine(act.fecha_de_ejecucion, datetime.min.time()) > start:
                fecha_init = act.fecha_de_ejecucion
            else:
                fecha_init = start
            # end if
            fecha_init = start
            cron = croniter.croniter(str_cron, datetime.combine(fecha_init, datetime.min.time()))
            nextdate = fecha_init
            print 'end', end, type(end)
            while nextdate <= end:
                nextdate = cron.get_next(datetime)
                if nextdate >= now:
                    color = act.tipo_de_actividad.color
                else:
                    color = 'gray'
                # end if
                form = formulario.Formulario.objects.filter(equipo = act.equipo).first()
                if form:
                    form = form.pk
                # end if
                dates.append({
                    'pk': act.id,
                    'color': color,
                    'cron': str_cron,
                    'title': "%s, %s" % (act.nombre, unicode(act.equipo)),
                    'now': now.strftime("%Y-%m-%d %I:%M%p"),
                    'start': nextdate.strftime("%Y-%m-%d"),
                    "urli": reverse('admin:%s_%s_change' % (act._meta.app_label,  act._meta.model_name),  args=[act.pk]),
                    'equipo': {
                        'nombre': act.equipo.nombre,
                        'descripcion': act.equipo.descripcion,
                        'turno': act.equipo.turno.nombre,
                        'unidad': {
                            'nombre': act.equipo.unidad.nombre,
                            'planta': {
                                'nombre': act.equipo.unidad.planta.nombre,
                                'ciudad': act.equipo.unidad.planta.ciudad.nombre,
                            }
                        },
                        'formulario': form
                    },
                    'type': 'Actividad'
                })
            # end while
        # end if
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
