from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^registro/pro/si/$', views.RegistroProSSupra.as_view(), name="registropros"),
    url(r'^registro/pro/no/$', views.RegistroProNSupra.as_view(), name="registropron"),
    url(r'^registro/tarjeta/pro/$', views.TarjetaSupra.as_view(), name="tarjetapro"),
    url(r'^registro/pasaporte/$', views.PasaporteSupra.as_view(), name="pasaporte"),
]
