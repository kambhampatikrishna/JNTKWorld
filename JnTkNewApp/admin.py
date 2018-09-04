from django.contrib import admin
from . import models

class UserProfile(admin.ModelAdmin):
    list_display=['College_Name','user']
admin.site.register(models.UserProfile,UserProfile)