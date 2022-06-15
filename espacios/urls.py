from django.urls import path
from django.views import View
from django.views.generic import RedirectView

 

from . import views

urlpatterns = [

############  Gestion ##############
    path ('Departamento_nuevo/', views.Departamento_nuevo, name='Departamento_nuevo'), # nuevo departamento
    path ('Departamentos_list/', views.Departamentos_list.as_view(), name='Departamentos_list'), # Departamentos_list
    path ('Departamento/<int:pk>', views.Departamento_edit, name='Departamentos_edit'), # zonas_list

    path ('zona_nueva/', views.zona_nueva, name='zona_nueva'), # zona_nueva
    path ('zonas_list/', views.zonas_list.as_view(), name='zonas_list'), # zonas_list
    path ('zonas_edit/<int:pk>', views.zonas_edit, name='zonas_edit'), # zonas_list

    path ('ubicacion_nueva/', views.ubicacion_nueva, name='ubicacion_nueva'), # zona_nueva
    path ('ubicacion_list/', views.ubicacion_list.as_view(), name='ubicacion_list'), # zonas_list
    path ('ubicacion_edit/<int:pk>', views.ubicacion_edit , name='ubicacion_edit'), # zonas_list

    path ('elemento_nuevo/', views.elemento_nuevo, name='elemento_nuevo'), # elemento_nuevo
    path ('elemento_list/', views.Elemento_list.as_view(), name='elemento_list'), # elemento_list
    path ('elemento_edit/<int:pk>', views.elemento_edit , name='elemento_edit'), # elemento_list

    path ('llave_nueva/', views.llave_nueva, name='llave_nueva'), # llave_nueva
    path ('llave_list/', views.llave_list.as_view(), name='llave_list'), # llave_list
    path ('llave_edit/<int:pk>', views.llave_edit , name='llave_edit'), # llave_list



############  Usuarios ##############

    path ('zonas_user_list/', views.Zonas_user_list.as_view(), name='zonas_listado'), # zonas_list
    path ('zona_user/<int:pk>', views.ubicacion_user_list.as_view(), name='zonas_listado'), # zonas_list
    path ('ubicacion_user_list/<int:pk>', views.ubicacion_user_list.as_view(), name='Hab_user'), # Habitaciones y salas
    path ('ubicacion_user/<int:pk>', views.ubicacion_user.as_view(), name='Hab_user'), # Habitaciones y salas

    path ('zona_select/', views.zona_select, name='zona_select'), # zona_select
    path ('ubicaciones_select/', views.ubicaciones_select, name='ubicaciones_select'), # ubicaciones_select

    path ('habitaciones_buscar/', views.habitaciones_buscar, name='habitaciones_buscar'), # buscar_Habitaciones
    path ('habitaciones_encontrar/', views.habitaciones_encontrar, name='habitaciones_encontrar'), # buscar_Habitaciones

    
      path ('ubicacion_menu/<int:pk>', views.ubicacion_menu, name='ubicacion_menu'), # ubicacion_menu
  
    
    
    
    path ('pruebas/', views.pruebas, name='Hab_user'), # Habitaciones y salas





]  
