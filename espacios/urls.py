from django.urls import path
from django.views import View
from django.views.generic import RedirectView



from . import views

urlpatterns = [

    path ('nuevo_departamento/', views.nuevo_departamento, name='Nuevo_departamento'), # nuevo departamento
    path ('Departamentos_list/', views.Departamentos_list.as_view(), name='Departamentos_list'), # nuevo departamento


]