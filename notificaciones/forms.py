#!/usr/bin/env python
# -*- coding: utf-8 -*-
import triggers
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from connections import HOST, IO_PORT
from django.core.signals import request_finished, got_request_exception
import os
from datetime import datetime
from goberna.settings import BASE_DIR

from actividades import models as actividades
from personal import models as personal


class DefaultTrigger(triggers.Trigger):
    exlude = []
    def get_url(self, instance):
        return reverse('admin:%s_%s_change' % (instance._meta.app_label,  instance._meta.model_name),  args=[instance.pk])
    # end def

    def get_exclude(self, instance):
        return self.exlude
    # end def

    def save(self, instance):
        super(DefaultTrigger, self).create(instance)
        data = self.get_data(instance)
        send_to = []
        for type_ in self.types:
            send_to.append(type_.__name__)
        # end for
        url = self.get_url(instance)

        obj = {
            "data": data,
            "url": url,
            "html": self.message % data,
            "_send_to_": send_to,
            "exclude": self.get_exclude(instance)
        }
        print obj
        if self.has_plugin('ioplugin'):
            self.emit_by('save', obj, 'ioplugin')
        # end if

        if self.has_plugin('smtpplugin'):
            emails = []
            for type_ in self.types:
                users = type_.objects.all()
                for user in users:
                    if user.email != '' and not user.email in emails:
                        emails.append(user.email)
                    # end if
                # end for
            # end for
            obj['data']['emails'] = emails
            self.emit_by('create', obj, 'smtpplugin')
        # end if
    # end def
# end class


class ResendTrigger(triggers.Trigger):

    def get_url(self, instance):
        return reverse('admin:%s_%s_change' % (instance._meta.app_label,  instance._meta.model_name),  args=[instance.pk])
    # end def

    def update(self, instance):
        super(ResendTrigger, self).update(instance)
        data = self.get_data(instance)
        send_to = []
        for type_ in self.types:
            send_to.append(type_.__name__)
        # end for

        obj = {
            "data": data,
            "url": self.get_url(instance),
            "html": self.message % data,
            "_send_to_": send_to
        }

        if self.has_plugin('smtpplugin') and hasattr(instance, 'resend') and instance.resend:
            emails = []
            for type_ in self.types:
                users = type_.objects.all()
                for user in users:
                    if user.email != '' and not user.email in emails:
                        emails.append(user.email)
                    # end if
                # end for
            # end for
            obj['data']['emails'] = emails
            self.emit_by('create', obj, 'smtpplugin')
        # end if
    # end def
# end class


class UserTrigger(triggers.Trigger):

    def get_type(self, instance):
        return self.type
    # end  def

    def get_url(self, instance):
        return reverse('admin:%s_%s_change' % (instance._meta.app_label,  instance._meta.model_name),  args=[instance.pk])
    # end def

    def save(self, instance):
        super(UserTrigger, self).save(instance)
        data = self.get_data(instance)
        url = self.get_url(instance)
        obj = {
            "data": data,
            "url": url,
            "html": self.message % data,
            "webuser": self.get_webuser(instance)
        }

        if self.has_plugin('ioplugin'):
            obj["_send_to_"] = self.get_type(instance).__name__
            self.emit_by('user', obj, 'ioplugin')
        # end if

        with open(os.path.join(BASE_DIR, 'io_plugin.log'), 'a+') as log:
            log.write("%s sended to: %s\n" % (datetime.now(), obj, ))
            log.close()
        # end with

        if self.has_plugin('smtpplugin'):
            emails = []
            for type_ in self.types:
                users = type_.objects.all()
                for user in users:
                    if user.email != '' and not user.email in emails:
                        emails.append(user.email)
                    # end if
                # end for
            # end for
            obj['data']['emails'] = emails
            self.emit_by('save', obj, 'smtpplugin')
        # end if
    # end def
# end class


class CronTrigger(triggers.Trigger):

    def get_url(self, instance):
        return reverse('admin:%s_%s_change' % (instance._meta.app_label,  instance._meta.model_name),  args=[instance.pk])
    # end def

    def save(self, instance):
        super(CronTrigger, self).save(instance)
        data = self.get_data(instance)
        send_to = []
        for type_ in self.types:
            send_to.append(type_.__name__)
        # end for
        url = self.get_url(instance)
        obj = {
            "data": data,
            "url": url,
            "cron": self.get_cron(instance),
            "html": self.message % data,
            "class": self.__class__.__name__,
            "owner": str(instance.pk),
            "_send_to_": send_to
        }
        if self.has_plugin('ioplugin'):
            self.emit_by('cron', obj, 'ioplugin')
        # end if
    # end def
# end class



class ActividadTrigger(CronTrigger):
    model = actividades.Actividad
    types = [User]
    message = u"Hoy debe cumplirse la actividad %(nombre)s"

    def get_cron(self, instance):
        cron = ""
        if "dias[" in instance.repetir_cada:  # diario
            cron = "0 0 12 * * %s" % (
                instance.repetir_cada.replace("dias[", "").replace("]", ""), )
        # end if
        if "mes[" in instance.repetir_cada:  # diario
            cron = "0 0 12 %s * *" % (
                instance.repetir_cada.replace("mes[", "").replace("]", ""), )
        # end if
        if instance.unidad_de_repeticion == 3:  # mensual
            cron = "0 0 7 %%(dia)s */%s *" % (instance.repetir_cada, )
        # end if
        if instance.unidad_de_repeticion == 4:  # anual
            cron = "0 0 7 %s %s/%s *" % ('%(dia)s', '%(mes)s', int(instance.repetir_cada) * 12, )
        # end if
        return cron % {
            'dia': instance.fecha_de_ejecucion.day,
            'mes': instance.fecha_de_ejecucion.month,
            'dia_semana': instance.fecha_de_ejecucion.weekday()
        }
    # end def

    def get_data(self, instance):
        data = {
            "nombre": instance.nombre,
            "fecha_de_ejecucion": instance.fecha_de_ejecucion.strftime("%Y-%m-%d %I:%M%p"),
            "tipo": "Actividad"
        }
        return data
    # end def
# end class

class ActividadCreateTrigger(DefaultTrigger):
    model = actividades.Actividad
    types = [User, personal.Empleado]
    message = u"""Nueva reunion"""

    def get_data(self, instance):
        data = {
            "nombre": instance.nombre,
            "fecha_de_ejecucion": instance.fecha_de_ejecucion.strftime("%Y-%m-%d %I:%M%p"),
            "tipo": "Actividad"
        }
        return data
    # end def
# end class

class DefaultSMTPPlugin(triggers.TriggerSMTPPlugin):
    messages = {
        "save": {
            "headers": {
                "Subject": 'Reporte de prisma service'
            },
            "message_template": "notificaciones/email.html",
            "include": "%(include)s",
            "exclude": "%(exclude)s"
        },
        "create": {
            "headers": {
                "Subject": 'Reporte de prisma service'
            },
            "message_template": "notificaciones/email.html",
            "include": "%(include)s",
            "exclude": "%(exclude)s"
        },
        "update": {
            "headers": {
                "Subject": 'Reporte de prisma service'
            },
            "message_template": "notificaciones/email.html",
            "include": "%(include)s",
            "exclude": "%(exclude)s"
        }
    }
# end class

class DefaultIOPluing(triggers.TriggerIOPlugin):
    username = 'user2'
    password = '123456'
    host = HOST
    port = IO_PORT
# end class

triggers.triggers.register(ActividadCreateTrigger, [DefaultIOPluing, DefaultSMTPPlugin])