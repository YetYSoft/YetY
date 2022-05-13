#from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from django.views import View
from . import views
from django.views.generic import RedirectView

#from partes.views import partes, DetalleParte, parte_nuevo, parte_editar, EditarTrab,Marcar_Terminado

from partes.views import *

urlpatterns = [

   
   


    
    #path  ("", views.index, name='index'),  #va a pag de Inicio
    path ('partes/', views.partes.as_view(), name='Listapartes'), #va a class view.OtListView
    path ('<int:pk>', views.DetalleParte, name='Detalle_Parte'),
    path ('Marcar_Terminado/<int:num_ot>', views.Marcar_Terminado, name='Marcar_Terminado'),

    path ('edit/<int:num_ot>', views.parte_editar, name='Editar_Parte'),
    path ('nuevo/', views.parte_nuevo, name='Nuevo_Parte'), # nuevo parte sin listado de partes

    # Nuevo parte-----------------------------------------------------
    path ('nuevo_form/' , views.nuevo_form, name='Partenuev'), # Abre el formulario
    path ('listaPor/' , views.nuevo_lista_partes, name='nuevo_lista_partes'), #Envia el dato del form


    # Formularios para listados y busquedas-----------------------------------
    path ('ubicacion_list_form/' , views.ubicacion_list_form, name='ubicacion_list_form'), #- Abre el formulario
    path ('elemento_list_form/' , views.elemento_list_form, name='elemento_list_form'), # Abre el formulario

    path ('ubicacion_lista_partes/' , views.ubicacion_lista_partes, name='ubicacion_lista_partes'),
    path ('elemento_lista_partes/' , views.elemento_lista_partes, name='elemento_lista_partes'),



    # Listados de partes------------------------------------------------------
    path ('pendientes/', views.partes_pendientes.as_view(), name='Partes_Pendientes'),
    path ('ubicacion/<str:ubicaci>' , views.PartesPorUbicacion, name='PartesPorUbicacion'),#-
    path ('elemento/<str:element>' , views.PartesPorElemento, name='PartesPorElemento'),


    # Trabajos ------------------------------------------------------
    path ('trabajo/<int:num_tra>/<int:numero_ot>' , views.EditarTrab , name='edit_trabajo'),
    path ('trabajo/nuevo/<int:numero_ot>' , views.NuevoTrab , name='add_trabajo'),
    path ('trabajo/ver/<int:numero_ot>' , views.ListaTrabParte.as_view() , name='ver_trabajos'),
    path ('trabajo/listado' , views.ListaTrab.as_view() , name='lista_trabajo'),
   
   
   
   # Buscar partes
    path ('buscar_partes/' , views.buscar_parte , name='buscar_parte'),
    path ('encontrar_partes/' , views.encontrar_parte , name='encontrar_parte'),


 
]
