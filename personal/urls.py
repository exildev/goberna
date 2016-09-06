from django.conf.urls import url
import views

urlpatterns = [
    url(r'^login/', views.Login.as_view()),
]
