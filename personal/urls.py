from django.conf.urls import url
import views

urlpatterns = [
    url(r'^login/', views.Login.as_view()),
    url(r'^departamento/list/$', views.DepartamentoListView.as_view(), ),
    url(r'^persona/list/$', views.PersonaListView.as_view(), ),
]
