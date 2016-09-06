from django.conf.urls import url
import views


# Gestion de preguntas
urlpatterns = [
    url(r'^add/$', views.PreguntaView.as_view(), name='add_motorizado')
]
