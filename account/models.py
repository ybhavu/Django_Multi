from django.db import models
from django.contrib.auth.models import AbstractUser,User
#from django.contrib.auth.models import AbstractUser

#from django.utils.html import escape, make_safe

# Create your models here.
class User(AbstractUser):
	is_admin = models.BooleanField(default=False)
	is_patient = models.BooleanField(default=False)
	is_doctor = models.BooleanField(default=False)
