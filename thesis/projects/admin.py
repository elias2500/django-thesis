from django.contrib import admin
from projects.models import UserProfileInfo, Project, User

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Project)