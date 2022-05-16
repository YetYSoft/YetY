from django.urls import path
from django.views.generic import TemplateView

from django.views import View
from . import views
from django.views.generic import RedirectView

#from partes.views import partes, DetalleParte, parte_nuevo, parte_editar, EditarTrab,Marcar_Terminado

from resumen.views import *

urlpatterns = [
   
   
   
   
    path ('', views.ver_resumen, name='resumen'), #va a class view.OtListView

]
