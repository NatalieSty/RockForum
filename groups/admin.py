from django.contrib import admin
from . import models

# Register your models here.

# tabular inline class
# allow us to use admin interface with ability to edit model on the same page as the parent model (group)
class GroupMemberInline(admin.TabularInline):
	model = models.GroupMember

#dont need to register group member because its inline here

admin.site.register(models.Group)


