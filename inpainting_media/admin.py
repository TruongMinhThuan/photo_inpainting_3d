from django.contrib import admin
from .models import MediaModel

# Register your models here.

@admin.register(MediaModel)
class MediaAdmin(admin.ModelAdmin):
    list_display = ("title","media_file")