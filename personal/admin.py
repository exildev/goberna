from django.contrib import admin

from exile_ui.admin import admin_site
import models
admin_site.register(models.Personal)