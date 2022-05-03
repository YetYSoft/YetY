#from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from django.views import View
from piscinas import views


urlpatterns = [
    path ('', views.piscinas_start, name='piscinas_start'),
    path ('piscina_grande/', views.piscina_grande, name='piscina_grande_form'),
    path ('piscinas/piscina_pequeña/', views.piscinas_start, name='piscinas_start'),
    path ('piscinas/spa/', views.piscinas_start, name='piscinas_start'),
    path ('piscinas/jacuzzy/', views.piscinas_start, name='piscinas_start'),


]
 