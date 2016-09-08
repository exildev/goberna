from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^tipoactividad/list/$', views.TipoActividadListView.as_view(), ),
    url(r'^lugar/list/$', views.LugarListView.as_view(), ),
    url(r'^tipoactividad/form/$', views.TipoActividadFormView.as_view(), ),
    url(r'^tipoactividad/form/(?P<pk>\d+)/$', views.TipoActividadFormView.as_view(), ),
    url(r'^actividad/list/$', views.ActividadListView.as_view(), ),
    url(r'^actividad/(?P<pk>\d+)/$', views.ActividadDetailView.as_view(), ),
    url(r'^actividad/form/$', views.ActividadFormView.as_view(), ),
    url(r'^actividad/form/(?P<pk>\d+)/$', views.ActividadFormEditView.as_view(), ),
	url(r'^calendar/$', views.calendar),
	url(r'^schedule/$', views.schedule),
]
