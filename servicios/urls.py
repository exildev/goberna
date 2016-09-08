from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^registro/pro/si/$', views.RegistroProSSupra.as_view(), name="registropros"),
    url(r'^registro/pro/no/$', views.RegistroProNSupra.as_view(), name="registropron"),
    url(r'^registro/tarjeta/pro/$', views.TarjetaSupra.as_view(), name="tarjetapro"),
    url(r'^registro/pasaporte/$', views.PasaporteSupra.as_view(), name="pasaporte"),
    url(r'^list/pro/si/$', views.RegistroProSList.as_view(), name="registroproslist"),
    url(r'^list/pro/no/$', views.RegistroProNList.as_view(), name="registropronlist"),
    url(r'^list/tarjeta/pro/$', views.TarjetaProList.as_view(), name="tarjetaprolist"),
    url(r'^list/pasaporte/$', views.PasaporteList.as_view(), name="pasaportelist"),
    url(r'^list/$', views.serviciosList, name="serviciosList"),
]
