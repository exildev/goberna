from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^tipoactividad/list/$', views.TipoActividadListView.as_view(), ),
    url(r'^tipoactividad/form/$', views.TipoActividadFormView.as_view(), ),
    url(r'^tipoactividad/form/(?P<pk>\d+)$',
        views.TipoActividadFormView.as_view(), ),
    url(r'^actividad/list/$', views.ActividadListView.as_view(), ),
    url(r'^actividad/form/$', views.ActividadFormView.as_view(), ),
    url(r'^actividad/form/(?P<pk>\d+)/$', views.ActividadFormView.as_view(), ),
	url(r'^calendar/$', views.calendar),
	url(r'^schedule/$', views.schedule),
]
