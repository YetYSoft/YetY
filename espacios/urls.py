from django.urls import path
from django.views import View
from django.views.generic import RedirectView



from . import views

urlpatterns = [

############  Gestion ##############
    path ('Departamento_nuevo/', views.Departamento_nuevo, name='Departamento_nuevo'), # nuevo departamento
    path ('Departamentos_list/', views.Departamentos_list.as_view(), name='Departamentos_list'), # Departamentos_list
    path ('Departamento/<int:pk>', views.Departamento_edit, name='Departamentos_edit'), # Plantas_o_zonas_list

    path ('Planta_o_zona_nueva/', views.Planta_o_zona_nueva, name='Planta_o_zona_nueva'), # Planta_o_zona_nueva
    path ('Plantas_o_zonas_list/', views.Plantas_o_zonas_list.as_view(), name='Plantas_o_zonas_list'), # Plantas_o_zonas_list
    path ('Plantas_o_zonas_edit/<int:pk>', views.Plantas_o_zonas_edit, name='Plantas_o_zonas_edit'), # Plantas_o_zonas_list

    path ('Hab_cuarto_sala_nueva/', views.Hab_cuarto_sala_nueva, name='Hab_cuarto_sala_nueva'), # Planta_o_zona_nueva
    path ('Hab_cuarto_sala_list/', views.Hab_cuarto_sala_list.as_view(), name='Hab_cuarto_sala_list'), # Plantas_o_zonas_list
    path ('Hab_cuarto_sala_edit/<int:pk>', views.Hab_cuarto_sala_edit , name='Hab_cuarto_sala_edit'), # Plantas_o_zonas_list

    path ('puerta_nueva/', views.puerta_nueva, name='puerta_nueva'), # puerta_nueva
    path ('puerta_list/', views.puerta_list.as_view(), name='puerta_list'), # puerta_list
    path ('puerta_edit/<int:pk>', views.puerta_edit , name='puerta_edit'), # puerta_list











############  Usuarios ##############

    path ('zonas_listado/', views.Zonas_listado.as_view(), name='zonas_listado'), # Plantas_o_zonas_list
    path ('zona_user/<int:pk>', views.Habs_listado.as_view(), name='zonas_listado'), # Plantas_o_zonas_list
    path ('Hab_user/<int:pk>', views.Hab_user.as_view(), name='Hab_user'), # Habitaciones y salas





]  
