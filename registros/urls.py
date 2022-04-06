#from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from django.views import View
from . import views

urlpatterns = [


path ('Temp_Clima/Listado/', views.Temp_Clima.as_view(), name='ListaTempHabs'), #va a class view.OtListView
path ('Temp_Clima/<int:num_Temp_Clima>', views.Temp_Clima_editar, name='Editar_Registro'),
path ('Temp_Clima/nuevo', views.Temp_Clima_nuevo, name='Nuevo_Registro'),


path ('Temp_Minibar/Listado/', views.Temp_Clima.as_view(), name='ListaTempMinibar'), #va a class view.OtListView


path ('pedidos/Listado/', views.Pedidos_list.as_view(), name='ListaPedidos'), #va a class view.OtListView
path ('pedidos/<int:num_Pedido>', views.Pedido_editar, name='Editar_Registro'),
path ('pedidos/nuevo/', views.Pedido_nuevo, name='Nuevo_pedido'),





]
