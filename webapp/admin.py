from django.contrib import admin
from .models import Place


# Register your models here.
class Placeadmin(admin.ModelAdmin):
    list_display = ['name',]
admin.site.register(Place,Placeadmin)
