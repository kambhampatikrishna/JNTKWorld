from django.contrib import admin
from . import models

class Branches(admin.ModelAdmin):
     list_display=['branchname','regulation','semester','subname','pdf','unit','teachername','clgname','views']
class videourls(admin.ModelAdmin):
    list_display=['TopicName','Topicpdf','Topicurl','subname','clgname','views']
# Register your models here.
admin.site.register(models.videourls,videourls)
admin.site.register(models.Branches,Branches)

