#from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from django.views import View
from . import views

urlpatterns = [
    path ('aguas/', views.aguas_start, name='aguas_start'),
   


]
