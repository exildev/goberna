from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Personal(User):
	nombre = models.CharField(max_length=45)
#end class
