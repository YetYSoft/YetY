from django.urls import path
from django.views.generic import TemplateView

from django.views import View
from . import views

urlpatterns = [

 # Pantalla cabecera
 path  ("", views.start, name='index'),  #va a pag de Inicio,
 path('start/', views.start),



]