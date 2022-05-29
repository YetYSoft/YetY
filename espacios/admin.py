from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Departamentos)
admin.site.register(Planta_o_zonas)
admin.site.register(Habs_cuartos_salas)
admin.site.register(Puertas)

admin.site.register(llaves)
