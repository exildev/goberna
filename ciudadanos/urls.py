from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^login/$', views.LoginSupra.as_view(), name="login"),
    url(r'^logout/$', views.logoutCiudadano, name="login"),
    url(r'^registro/$', views.RegistroSupra.as_view(), name="login"),
]
