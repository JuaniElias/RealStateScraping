from django.contrib import admin

# Register your models here.

from .models import Barrio,Propiedad,Filtro

admin.site.register(Barrio)
admin.site.register(Propiedad)
admin.site.register(Filtro)
