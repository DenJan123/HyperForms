from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.FormRecord)
admin.site.register(models.FormModel)
admin.site.register(models.FormField)
admin.site.register(models.FormData)
admin.site.register(models.Participant)
