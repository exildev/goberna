from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^login/movil/$', views.LoginMovil.as_view(), name="loginmovil"),
    url(r'^logout/$', views.logoutCiudadano, name="logout"),
    url(r'^registro/$', views.RegistroSupra.as_view(), name="registro"),
    url(r'^login/$', views.LoginSu.as_view(), name="login"),

]
