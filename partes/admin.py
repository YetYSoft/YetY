from django.contrib import admin

# Register your models here.

from .models import *



admin.site.register(Ot_Parte)
admin.site.register(Ot_Trabajos)
admin.site.register(Ot_Ubicaciones)
admin.site.register(Ot_Elementos)
admin.site.register(Ot_Pedidos)
admin.site.register(Ot_Etiquetas)
admin.site.register(Parte)
admin.site.register(Trabajos)
admin.site.register(Pedido)
admin.site.register(Prioridad)
admin.site.register(Estados)

