from django.contrib import admin

from sundayfunday import models

admin.site.register(models.User)
admin.site.register(models.Event)
admin.site.register(models.Preference)
admin.site.register(models.Comment)
admin.site.register(models.Grade)
admin.site.register(models.Friend)
