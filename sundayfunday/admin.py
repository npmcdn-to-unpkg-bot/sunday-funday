from django.contrib import admin

from sundayfunday import models

admin.site.register(models.User)
admin.site.register(models.Event)

