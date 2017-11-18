from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Game)
admin.site.register(models.Lobby)
admin.site.register(models.Message)
