"""ot URL Configuration ..........

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django import views
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView,View
from cabecera.views import *

urlpatterns = [
    path("", include('cabecera.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cabecera/', include('cabecera.urls')),
    path('aguas/', include('aguas.urls')),
    path('partes/', include('partes.urls')),
    path('piscinas/', include('piscinas.urls')),
    path('registros/', include('registros.urls')),
<<<<<<< HEAD
   
=======
    path('rondas/', include('rondas.urls')),

>>>>>>> f2e7bc42ef7b2b4c9efe4c14b64b36cc58305cd6

    #path  ("/", views.start, name='index'),  #va a pag de Inicio
   
   
   
    #path('/', RedirectView.as_view(url='/cabecera/start/', permanent=True)),

    #path('', include('partes.urls')),

    #path('', include('rondas.urls')),

    # path('', include('registros.urls')),
    #path  ("", views.index, name='index'),  #va a pag de Inicio
    #path('', RedirectView.as_view(url='/cabecera/start/', permanent=True))
]



#Add URL maps to redirect the base URL to our application
<<<<<<< HEAD
from django.views.generic import RedirectView
urlpatterns += [
    #path('', RedirectView.as_view(url='partes/', permanent=True)),

    # path('', RedirectView.as_view(url='start/', permanent=True)),
   
]
=======
#
#urlpatterns += [
   # path('', RedirectView.as_view(url='/partes/', permanent=True)),
#    path('', RedirectView.as_view(url='/start/', permanent=True)),
#]
>>>>>>> f2e7bc42ef7b2b4c9efe4c14b64b36cc58305cd6
