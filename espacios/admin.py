from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Departamentos)
admin.site.register(Zonas)
admin.site.register(Ubicaciones)
admin.site.register(Elementos)

admin.site.register(llaves)
