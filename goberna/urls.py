"""goberna URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from exile_ui.admin import admin_site
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView
from ciudadanos import views
import settings


urlpatterns = [
    url(r'^$', views.Menu.as_view()),
    url(r'^dashboard/', admin_site.urls),
    url(r'^actividades/', include('actividades.urls')),
    url(r'^preguntas/', include('question.urls', namespace='pregunta')),
    url(r'^nested_admin/', include('nested_admin.urls')),
    url(r'^notificaciones/', include('notificaciones.urls')),
    url(r'^personal/', include('personal.urls')),
    url(r'^ciudadanos/', include('ciudadanos.urls')),
    url(r'^servicios/', include('servicios.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
