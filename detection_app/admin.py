from django.contrib import admin
from . import models


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'secret_key')


class AnimalImageAdmin(admin.ModelAdmin):
    list_display = ('label', 'image', 'upload_date', 'uploaded_by')


admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.AnimalImage, AnimalImageAdmin)
