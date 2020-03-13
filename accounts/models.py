from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):
## user model
	def __str__(self):
		#username comes with modes.User
		return "@{}".format(self.username)


